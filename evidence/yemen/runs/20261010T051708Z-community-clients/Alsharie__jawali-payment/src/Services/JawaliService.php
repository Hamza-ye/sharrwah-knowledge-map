<?php

namespace Alsharie\Jawali\Services;

use Alsharie\Jawali\Exceptions\JawaliApiException;
use Alsharie\Jawali\Responses\JawaliEcommerceCashoutResponse;
use Alsharie\Jawali\Responses\JawaliEcommerceInquiryResponse;
use Alsharie\Jawali\Responses\JawaliLoginResponse;
use Alsharie\Jawali\Responses\JawaliWalletAuthResponse;
use Illuminate\Http\Client\Response;
use Illuminate\Support\Facades\Http;
use Illuminate\Support\Facades\Log;
use Illuminate\Support\Str;
use Throwable;

class JawaliService
{
    protected string $baseUrl;
    protected array $authConfig;
    protected int $timeout;
    protected bool $disableSslVerification;
    protected array $retryConfig;
    protected TokenManager $tokenManager;
    protected bool $enableLogging;

    // Hardcoded API specific details
    private const LOGIN_SYSTEM_ENDPOINT = '/oauth/token';
    private const LOGIN_SYSTEM_CLIENT_ID = 'restapp';
    private const LOGIN_SYSTEM_CLIENT_SECRET = 'restapp';
    private const LOGIN_SYSTEM_GRANT_TYPE = 'password';
    private const LOGIN_SYSTEM_SCOPE = 'read';

    private const WALLET_AUTH_ENDPOINT = '/v1/ws/callWS'; // Adjust if different
    private const WALLET_AUTH_SERVICE_NAME = 'PAYWA.WALLETAUTHENTICATION';
    private const WALLET_AUTH_DOMAIN_NAME = 'WalletDomain';

    private const ECOMMERCE_INQUIRY_ENDPOINT = '/v1/ws/callWS'; // Adjust if different
    private const ECOMMERCE_INQUIRY_SERVICE_NAME = 'PAYAG.ECOMMERCEINQUIRY';
    private const ECOMMERCE_INQUIRY_DOMAIN_NAME = 'MerchantDomain';

    private const ECOMMERCE_CASHOUT_ENDPOINT = '/v1/ws/callWS'; // Adjust if different
    private const ECOMMERCE_CASHOUT_SERVICE_NAME = 'PAYAG.ECOMMCASHOUT';
    private const ECOMMERCE_CASHOUT_DOMAIN_NAME = 'MerchantDomain';

    private const COMMON_SIGNON_CLIENT_ID = 'WeCash'; // For PAYWA/PAYAG headers
    private const COMMON_BODY_TYPE = 'Clear';       // For PAYWA/PAYAG headers


    public function __construct(array $config)
    {
        $this->baseUrl = rtrim($config['url']['base'], '/');
        $this->authConfig = $config['auth'];
        $this->timeout = $config['timeout'] ?? 30;
        $this->disableSslVerification = $config['url']['disable_ssl_verification'] ?? false;
        $this->retryConfig = $config['retry'] ?? [
            'enabled' => true,
            'max_attempts' => 2,
            'status_codes' => [400, 401, 403],
        ];
        $this->enableLogging = $config['logging']['enabled'] ?? false;
        $this->tokenManager = new TokenManager();
        
        // Set salt for token encryption using user_id from config
        $salt = $config['auth']['user_id'] ?? $config['auth']['username'] ?? 'default_salt';
        $this->tokenManager->setSalt($salt);
    }

    /**
     * LOGIN TO SYSTEM
     * Uses credentials from config: auth.username, auth.password.
     *
     * @return JawaliLoginResponse
     * @throws JawaliApiException
     */
    public function loginToSystem(): JawaliLoginResponse
    {
        $url = $this->baseUrl . self::LOGIN_SYSTEM_ENDPOINT;

        if (empty($this->authConfig['username']) || empty($this->authConfig['password'])) {
            throw new JawaliApiException("Missing required authentication credentials. Please ensure JAWALI_MERCHANT_USERNAME and JAWALI_MERCHANT_PASSWORD are set in your environment configuration.");
        }

        $payload = [
            'grant_type' => self::LOGIN_SYSTEM_GRANT_TYPE,
            'client_id' => self::LOGIN_SYSTEM_CLIENT_ID,
            'client_secret' => self::LOGIN_SYSTEM_CLIENT_SECRET,
            'scope' => self::LOGIN_SYSTEM_SCOPE,
            'username' => $this->authConfig['username'],
            'password' => $this->authConfig['password'],
        ];

        try {
            $this->logApiRequest('POST', $url, $payload, ['operation' => 'loginToSystem']);

            $request = Http::asForm()
                ->timeout($this->timeout);

            if ($this->disableSslVerification) {
                $request->withoutVerifying();
            }

            $response = $request->post($url, $payload);

            $this->logApiResponse($response, ['operation' => 'loginToSystem']);
            $data = $this->handleRawResponse($response);
            $loginResponse = new JawaliLoginResponse($data);

            if ($loginResponse->isSuccess()) {
                $this->tokenManager->setAuthToken(
                    $loginResponse->getAccessToken(),
                    $loginResponse->getExpiresIn()
                );
            }

            return $loginResponse;
        } catch (JawaliApiException $e) {
            $this->logApiError($e, ['operation' => 'loginToSystem']);
            // Re-throw API exceptions to preserve response data
            throw $e;
        } catch (Throwable $e) {
            // Wrap other exceptions (network, timeout, etc.)
            $wrappedException = new JawaliApiException("Login to System API request failed: " . $e->getMessage(), 0, null, $e);
            $this->logApiError($wrappedException, ['operation' => 'loginToSystem', 'original_error' => $e->getMessage()]);
            throw $wrappedException;
        }
    }

    /**
     * Handle raw HTTP response without wrapping it in a response object.
     *
     * @param Response $response
     * @return array
     * @throws JawaliApiException
     */
    protected function handleRawResponse(Response $response): array
    {
        if (!$response->successful()) {
            $errorMessage = "API request failed with status {$response->status()}.";
            $apiError = $response->json();
            if ($apiError && (isset($apiError['error_description']) || isset($apiError['error']))) {
                $errorMessage .= " Error: " . ($apiError['error_description'] ?? $apiError['error']);
            } elseif ($apiError && isset($apiError['responseStatus']['systemStatusDesc'])) {
                $errorMessage .= " Error: " . $apiError['responseStatus']['systemStatusDesc'];
            }
            throw new JawaliApiException($errorMessage, $response->status(), $response);
        }

        $jsonData = $response->json();

        // Handle cases where response is successful but JSON parsing fails
        if ($jsonData === null && $response->body()) {
            // Try to provide more context about the response
            $body = $response->body();
            $contentType = $response->header('Content-Type');

            throw new JawaliApiException(
                "API returned successful status but invalid JSON response. Content-Type: {$contentType}, Body: " . substr($body, 0, 200),
                $response->status(),
                $response
            );
        }

        return $jsonData ?? [];
    }

    /**
     * PAYWA.WALLETAUTHENTICATION
     * Uses credentials from config: auth.wallet_identifier, auth.wallet_password.
     * Header details (org_id, user_id, external_user) also from config.
     *
     * @param array|null $headerOverrides
     * @return JawaliWalletAuthResponse
     * @throws JawaliApiException
     */
    public function walletAuthentication(?array $headerOverrides = []): JawaliWalletAuthResponse
    {
        // Ensure we have a valid auth token first
        if (!$this->tokenManager->hasAuthToken()) {
            $this->loginToSystem();
        }

        $url = $this->baseUrl . self::WALLET_AUTH_ENDPOINT;

        if (empty($this->authConfig['wallet_identifier']) || empty($this->authConfig['wallet_password'])) {
            throw new JawaliApiException("Missing required wallet credentials for authentication. Please ensure JAWALI_MERCHANT_WALLET (wallet identifier) and JAWALI_MERCHANT_WALLET_PASSWORD are set in your environment configuration.");
        }

        $body = [
            'identifier' => $this->authConfig['wallet_identifier'],
            'password' => $this->authConfig['wallet_password'],
        ];

        $payload = $this->buildStructuredRequestPayload(
            $body,
            self::WALLET_AUTH_SERVICE_NAME,
            self::WALLET_AUTH_DOMAIN_NAME,
            $headerOverrides
        );

        try {
            $this->logApiRequest('POST', $url, $payload, ['operation' => 'walletAuthentication']);

            $request = Http::asJson()
                ->timeout($this->timeout)
                ->acceptJson();

            if ($this->disableSslVerification) {
                $request->withoutVerifying();
            }

            // Add authorization header with the auth token
            if ($this->tokenManager->hasAuthToken()) {
                $request->withToken($this->tokenManager->getAuthToken());
            }

            //log all the request headers
            Log::info('Request Headers', [
                'options' => $request->getOptions(),
                'headers' => $request->getOptions()['headers'] ?? [],
                'payload_size' => strlen(json_encode($payload)),
            ]);


            $response = $request->post($url, $payload);

            $this->logApiResponse($response, ['operation' => 'walletAuthentication']);

            $data = $this->handleStructuredResponse($response);
            $walletAuthResponse = new JawaliWalletAuthResponse($data);

            if ($walletAuthResponse->isSuccess()) {
                $this->tokenManager->setWalletToken($walletAuthResponse->getAccessToken());
            }

            return $walletAuthResponse;
        } catch (JawaliApiException $e) {
            $this->logApiError($e, ['operation' => 'walletAuthentication']);

            // Re-throw API exceptions to preserve response data
            throw $e;
        } catch (Throwable $e) {
            // Wrap other exceptions (network, timeout, etc.)
            throw new JawaliApiException("Wallet Authentication API request failed: " . $e->getMessage(), 0, null, $e);
        }
    }

    /**
     * Handle structured API response with responseBody and responseStatus.
     *
     * @param Response $response
     * @return array
     * @throws JawaliApiException
     */
    protected function handleStructuredResponse(Response $response): array
    {
        $data = $this->handleRawResponse($response);

        if (!array_key_exists('responseBody', $data) || !array_key_exists('responseStatus', $data)) {
            throw new JawaliApiException('Invalid response structure from API: Missing responseBody or responseStatus.', 0, $response);
        }

        if (($data['responseStatus']['systemStatus'] ?? '1') != '0') {
            $desc = $data['responseStatus']['systemStatusDesc'] ?? 'Unknown API error';
            $descNative = $data['responseStatus']['systemStatusDescNative'] ?? '';
            throw new JawaliApiException("API Error: {$desc} ({$descNative})", (int)($data['responseStatus']['systemStatus'] ?? -1), $response);
        }

        return $data;
    }

    /**
     * PAYAG.ECOMMERCEINQUIRY
     *
     * @param string $voucher
     * @param string $receiverMobile
     * @param string $purpose
     * @param array|null $headerOverrides
     * @return JawaliEcommerceInquiryResponse
     * @throws JawaliApiException
     */
    public function ecommerceInquiry(
        string $voucher,
        string $receiverMobile,
        string $purpose = '',
        ?array $headerOverrides = []
    ): JawaliEcommerceInquiryResponse
    {
        // Validate input parameters
        $this->validateEcommerceParams($voucher, $receiverMobile);

        // Ensure we have valid tokens
        $this->ensureValidTokens();

        $url = $this->baseUrl . self::ECOMMERCE_INQUIRY_ENDPOINT;

        if (empty($this->authConfig['wallet_identifier']) || empty($this->authConfig['wallet_password'])) {
            throw new JawaliApiException("Missing required wallet credentials for ecommerce inquiry. Please ensure JAWALI_MERCHANT_WALLET (wallet identifier) and JAWALI_MERCHANT_WALLET_PASSWORD are set in your environment configuration.");
        }

        $bodyParams = [
            'agentWallet' => $this->authConfig['wallet_identifier'],
            'voucher' => $voucher,
            'receiverMobile' => $receiverMobile,
            'password' => $this->authConfig['wallet_password'],
            'accessToken' => $this->tokenManager->getWalletToken(),
            'refId' => $this->generateRefId(),
            'purpose' => $purpose,
        ];

        $payload = $this->buildStructuredRequestPayload(
            $bodyParams,
            self::ECOMMERCE_INQUIRY_SERVICE_NAME,
            self::ECOMMERCE_INQUIRY_DOMAIN_NAME,
            $headerOverrides
        );

        return $this->sendStructuredRequest(
            $url,
            $payload,
            JawaliEcommerceInquiryResponse::class,
            "Ecommerce Inquiry API request failed"
        );
    }

    /**
     * Generate a reference ID for requests.
     *
     * @return string
     */
    protected function generateRefId(): string
    {
        return (string)time();
    }

        /**
     * Ensure we have valid tokens for API requests.
     * Will attempt to refresh tokens if needed.
     * 
     * @return void
     * @throws JawaliApiException
     */
    protected function ensureValidTokens(): void
    {
        // Log token status for debugging
        if ($this->enableLogging) {
            $tokenStatus = $this->tokenManager->getTokenStatus();
            Log::info('Token Status Check', $tokenStatus);
        }

        if (!$this->tokenManager->hasAuthToken()) {
            Log::info('Auth token missing or expired, calling loginToSystem');
            $this->loginToSystem();
        }

        if (!$this->tokenManager->hasWalletToken()) {
            Log::info('Wallet token missing or expired, calling walletAuthentication');
            $this->walletAuthentication();
        }
    }

    /**
     * Get current token status for debugging.
     * 
     * @return array
     */
    public function getTokenStatus(): array
    {
        return $this->tokenManager->getTokenStatus();
    }

    /**
     * Securely clear all stored tokens.
     * Use this when logging out or when security is compromised.
     * 
     * @return void
     */
    public function secureLogout(): void
    {
        $this->tokenManager->secureClearAllTokens();
        
        if ($this->enableLogging) {
            Log::info('Secure logout completed - all tokens cleared and overwritten');
        }
    }

    /**
     * Send a structured request with retry mechanism.
     *
     * @param string $url
     * @param array $payload
     * @param string $responseClass
     * @param string $errorMessage
     * @return mixed
     * @throws JawaliApiException
     */
    protected function sendStructuredRequest(
        string $url,
        array  $payload,
        string $responseClass,
        string $errorMessage
    )
    {
        $maxAttempts = $this->retryConfig['enabled'] ? $this->retryConfig['max_attempts'] : 1;
        $attempt = 0;
        $lastException = null;

        while ($attempt < $maxAttempts) {
            $attempt++;

            try {
                $this->logApiRequest('POST', $url, $payload, ['operation' => 'sendStructuredRequest', 'attempt' => $attempt]);

                $request = Http::asJson()
                    ->timeout($this->timeout);

                if ($this->disableSslVerification) {
                    $request->withoutVerifying();
                }

                // Add authorization header with the auth token
                if ($this->tokenManager->hasAuthToken()) {
                    $request->withToken($this->tokenManager->getAuthToken());
                }

                $response = $request->post($url, $payload);

                $this->logApiResponse($response, ['operation' => 'sendStructuredRequest', 'attempt' => $attempt]);

                // Check for token errors in the response
                $data = $response->json();
                $shouldRetryDueToTokenError = false;
                
                if ($response->successful() && isset($data['responseStatus'])) {
                    $systemStatus = $data['responseStatus']['systemStatus'] ?? '';
                    $systemStatusDesc = $data['responseStatus']['systemStatusDesc'] ?? '';
                    $systemStatusDescNative = $data['responseStatus']['systemStatusDescNative'] ?? '';

                    
                    // Check for token-related error messages
                    $tokenErrorKeywords = ['invalid access token', 'expired', 'unauthorized', 'authentication failed', 'token'];
                    $errorMessage = strtolower($systemStatusDesc . ' ' . $systemStatusDescNative);
                    
                    foreach ($tokenErrorKeywords as $keyword) {
                        if (strpos($errorMessage, $keyword) !== false) {
                            $shouldRetryDueToTokenError = true;
                            break;
                        }
                    }
                }
                
                if ($shouldRetryDueToTokenError && $attempt < $maxAttempts) {
                    // Token issue detected, refresh tokens and retry
                    if ($this->enableLogging) {
                        Log::info('Token error detected, refreshing tokens', [
                            'systemStatus' => $data['responseStatus']['systemStatus'] ?? 'unknown',
                            'systemStatusDesc' => $data['responseStatus']['systemStatusDesc'] ?? 'unknown',
                            'attempt' => $attempt,
                            'maxAttempts' => $maxAttempts
                        ]);
                    }
                    
                    $this->refreshTokens();
                    // Update the access token in the payload
                    $payload['body']['accessToken'] = $this->tokenManager->getWalletToken();
                    $payload['body']['refId'] = $this->generateRefId();
                    continue;
                }

                $data = $this->handleStructuredResponse($response);
                return new $responseClass($data);

            } catch (JawaliApiException $e) {
                $this->logApiError($e, ['operation' => 'sendStructuredRequest', 'attempt' => $attempt]);
                $lastException = $e;

                $shouldRetry = false;
                
                // Check if we should retry based on status code
                if (
                    $attempt < $maxAttempts &&
                    $this->retryConfig['enabled'] &&
                    in_array($e->getApiStatus(), $this->retryConfig['status_codes'])
                ) {
                    $shouldRetry = true;
                }
                
                // Also check for token-related error messages in the exception
                if (!$shouldRetry && $attempt < $maxAttempts && $this->retryConfig['enabled']) {
                    $errorMessage = strtolower($e->getMessage());
                    $tokenErrorKeywords = ['invalid access token', 'expired', 'unauthorized', 'authentication failed', 'token'];
                    
                    foreach ($tokenErrorKeywords as $keyword) {
                        if (strpos($errorMessage, $keyword) !== false) {
                            $shouldRetry = true;
                            break;
                        }
                    }
                }
                
                if ($shouldRetry) {
                    // Refresh tokens and retry
                    if ($this->enableLogging) {
                        Log::info('Token error detected in exception, refreshing tokens', [
                            'apiStatus' => $e->getApiStatus(),
                            'errorMessage' => $e->getMessage(),
                            'attempt' => $attempt,
                            'maxAttempts' => $maxAttempts
                        ]);
                    }
                    
                    $this->refreshTokens();
                    // Update the access token in the payload
                    $payload['body']['accessToken'] = $this->tokenManager->getWalletToken();
                    $payload['body']['refId'] = $this->generateRefId();
                    continue;
                }

                throw $e;
            } catch (Throwable $e) {
                // Wrap other exceptions (network, timeout, etc.)
                throw new JawaliApiException("{$errorMessage}: " . $e->getMessage(), 0, null, $e);
            }
        }

        // If we've exhausted all attempts, throw the last exception
        if ($lastException) {
            throw $lastException;
        }

        throw new JawaliApiException("{$errorMessage}: Maximum retry attempts reached", 0);
    }

    /**
     * Refresh both the auth token and wallet token.
     *
     * @return bool
     */
    protected function refreshTokens(): bool
    {
        try {
            if ($this->enableLogging) {
                Log::info('Starting token refresh process');
            }
            
            $loginResponse = $this->loginToSystem();
            if ($loginResponse->isSuccess()) {
                if ($this->enableLogging) {
                    Log::info('Login successful, proceeding with wallet authentication');
                }
                
                $walletAuthResponse = $this->walletAuthentication();
                $success = $walletAuthResponse->isSuccess();
                
                if ($this->enableLogging) {
                    Log::info('Token refresh completed', [
                        'login_success' => $loginResponse->isSuccess(),
                        'wallet_auth_success' => $success
                    ]);
                }
                
                return $success;
            }
            
            if ($this->enableLogging) {
                Log::warning('Login failed during token refresh');
            }
            
            return false;
        } catch (Throwable $e) {
            if ($this->enableLogging) {
                Log::error('Token refresh failed with exception', [
                    'error' => $e->getMessage(),
                    'exception_class' => get_class($e)
                ]);
            }
            // Silently fail token refresh - the calling method will handle the error
            return false;
        }
    }

    /**
     * PAYAG.ECOMMCASHOUT
     *
     * @param string $voucher
     * @param string $receiverMobile
     * @param string $purpose
     * @param array|null $headerOverrides
     * @return JawaliEcommerceCashoutResponse
     * @throws JawaliApiException
     */
    public function ecommerceCashout(
        string $voucher,
        string $receiverMobile,
        string $purpose = '',
        ?array $headerOverrides = []
    ): JawaliEcommerceCashoutResponse
    {
        // Validate input parameters
        $this->validateEcommerceParams($voucher, $receiverMobile);

        // Ensure we have valid tokens
        $this->ensureValidTokens();

        $url = $this->baseUrl . self::ECOMMERCE_CASHOUT_ENDPOINT;

        if (empty($this->authConfig['wallet_identifier']) || empty($this->authConfig['wallet_password'])) {
            throw new JawaliApiException("Missing required wallet credentials for ecommerce cashout. Please ensure JAWALI_MERCHANT_WALLET (wallet identifier) and JAWALI_MERCHANT_WALLET_PASSWORD are set in your environment configuration.");
        }

        $bodyParams = [
            'agentWallet' => $this->authConfig['wallet_identifier'],
            'voucher' => $voucher,
            'receiverMobile' => $receiverMobile,
            'password' => $this->authConfig['wallet_password'],
            'accessToken' => $this->tokenManager->getWalletToken(),
            'refId' => $this->generateRefId(),
            'purpose' => $purpose,
        ];

        $payload = $this->buildStructuredRequestPayload(
            $bodyParams,
            self::ECOMMERCE_CASHOUT_SERVICE_NAME,
            self::ECOMMERCE_CASHOUT_DOMAIN_NAME,
            $headerOverrides
        );

        return $this->sendStructuredRequest(
            $url,
            $payload,
            JawaliEcommerceCashoutResponse::class,
            "Ecommerce Cashout API request failed"
        );
    }

    protected function buildStructuredRequestPayload(
        array  $bodyData,
        string $serviceName,
        string $domainName,
        ?array $headerOverrides = []
    ): array
    {
        $signonDetailDefaults = [
            'clientID' => self::COMMON_SIGNON_CLIENT_ID,
            'orgID' => $this->authConfig['org_id'] ?? null,
            'userID' => $this->authConfig['user_id'] ?? null,
            'externalUser' => $this->authConfig['external_user'] ?? null,
        ];

        $signonDetail = array_merge(
            $signonDetailDefaults,
            $headerOverrides['signonDetail'] ?? []
        );
        $signonDetail = array_filter($signonDetail, fn($value) => !is_null($value));

        if (empty($signonDetail['orgID']) || empty($signonDetail['userID'])) {
            throw new JawaliApiException("Missing JAWALI_MERCHANT_ORG_ID or JAWALI_MERCHANT_USER_ID in configuration for API header.");
        }

        $payload = [
            'header' => [
                'serviceDetail' => [
                    'corrID' => (string)Str::uuid(),
                    'domainName' => $domainName,
                    'serviceName' => $serviceName,
                ],
                'signonDetail' => $signonDetail,
                'messageContext' => [
                    'clientDate' => now()->format('YmdHis'),
                    'bodyType' => self::COMMON_BODY_TYPE,
                ],
            ],
            'body' => $bodyData,
        ];

        if (isset($headerOverrides['serviceDetail'])) {
            $payload['header']['serviceDetail'] = array_merge($payload['header']['serviceDetail'], $headerOverrides['serviceDetail']);
        }
        if (isset($headerOverrides['messageContext'])) {
            $payload['header']['messageContext'] = array_merge($payload['header']['messageContext'], $headerOverrides['messageContext']);
        }

        return $payload;
    }

    /**
     * Validate ecommerce operation parameters.
     *
     * @param string $voucher
     * @param string $receiverMobile
     * @throws JawaliApiException
     */
    protected function validateEcommerceParams(string $voucher, string $receiverMobile): void
    {
        if (empty(trim($voucher))) {
            throw new JawaliApiException("Voucher number cannot be empty");
        }

        if (empty(trim($receiverMobile))) {
            throw new JawaliApiException("Receiver mobile number cannot be empty");
        }

        // Basic mobile number validation (adjust pattern as needed for Yemen numbers)
        if (!preg_match('/^[0-9+\-\s()]{7,15}$/', $receiverMobile)) {
            throw new JawaliApiException("Invalid mobile number format: {$receiverMobile}");
        }

        // Basic voucher validation (adjust as needed based on your voucher format)
        if (!preg_match('/^[0-9A-Za-z\-_]{3,50}$/', $voucher)) {
            throw new JawaliApiException("Invalid voucher format: {$voucher}");
        }
    }

    /**
     * Log API request information if logging is enabled.
     *
     * @param string $method
     * @param string $url
     * @param array $payload
     * @param array $context
     * @return void
     */
    protected function logApiRequest(string $method, string $url, array $payload = [], array $context = []): void
    {
        if (!$this->enableLogging) {
            return;
        }

        $sanitizedPayload = $this->sanitizeLogData($payload);

        try {
            Log::info('Jawali API Request', [
                'method' => $method,
                'url' => $url,
                'payload' => $sanitizedPayload,
                'context' => $context
            ]);
        } catch (\Throwable $e) {
            // Silently ignore logging errors to prevent them from breaking main functionality
        }
    }

    /**
     * Log API response information if logging is enabled.
     *
     * @param Response $response
     * @param array $context
     * @return void
     */
    protected function logApiResponse(Response $response, array $context = []): void
    {
        if (!$this->enableLogging) {
            return;
        }

        $responseData = $response->json();
        $sanitizedResponse = $this->sanitizeLogData($responseData);

        try {
            Log::info('Jawali API Response', [
                'status' => $response->status(),
                'response' => $sanitizedResponse,
                'context' => $context
            ]);
        } catch (\Throwable $e) {
            // Silently ignore logging errors to prevent them from breaking main functionality
        }
    }

    /**
     * Log API errors if logging is enabled.
     *
     * @param JawaliApiException $exception
     * @param array $context
     * @return void
     */
    protected function logApiError(JawaliApiException $exception, array $context = []): void
    {
        if (!$this->enableLogging) {
            return;
        }

        try {
            Log::error('Jawali API Error', [
                'message' => $exception->getMessage(),
                'status' => $exception->getApiStatus(),
                'error_details' => $exception->getApiErrorDetails(),
                'context' => $context,
            ]);
        } catch (\Throwable $e) {
            // Silently ignore logging errors to prevent them from breaking main functionality
        }
    }

    /**
     * Sanitize log data by removing sensitive information.
     *
     * @param mixed $data
     * @return mixed
     */
    protected function sanitizeLogData($data)
    {
        if (!is_array($data)) {
            return $data;
        }

        $sensitiveKeys = [
            'password', 'access_token', 'refresh_token', 'token',
            'accessToken', 'refreshToken', 'client_secret', 'clientSecret'
        ];

        $sanitized = $data;
        foreach ($sensitiveKeys as $key) {
            if (isset($sanitized[$key])) {
                $sanitized[$key] = '***REDACTED***';
            }
        }

        // Recursively sanitize nested arrays
        foreach ($sanitized as $key => $value) {
            if (is_array($value)) {
                $sanitized[$key] = $this->sanitizeLogData($value);
            }
        }

        return $sanitized;
    }

    // handleResponse method has been replaced by handleRawResponse and handleStructuredResponse methods
}

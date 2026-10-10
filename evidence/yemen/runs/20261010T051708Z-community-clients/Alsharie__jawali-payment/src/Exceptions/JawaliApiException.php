<?php

namespace Alsharie\Jawali\Exceptions;

use Exception;
use Illuminate\Http\Client\Response;

class JawaliApiException extends Exception
{
    protected ?Response $response;
    protected ?array $context;

    public function __construct(
        string $message = "",
        int $code = 0,
        ?Response $response = null,
        ?Exception $previous = null,
        ?array $context = null
    ) {
        parent::__construct($message, $code, $previous);
        $this->response = $response;
        $this->context = $context;
    }

    /**
     * Get the raw response data (standardized name matching successful responses).
     *
     * @return array|null
     */
    public function getData(): ?array
    {
        return $this->response ? $this->response->json() : null;
    }

    /**
     * Get a value from the response body (standardized name matching successful responses).
     *
     * @param string|null $attribute
     * @return mixed
     */
    public function getResponseBody(?string $attribute = null)
    {
        $data = $this->getData();
        
        if (!$data) {
            return null;
        }

        // Handle structured API responses (PAYWA/PAYAG)
        if (isset($data['responseBody'])) {
            if ($attribute && isset($data['responseBody'][$attribute])) {
                return $data['responseBody'][$attribute];
            }
            return $data['responseBody'];
        }

        // Handle simple responses (OAuth)
        if ($attribute && isset($data[$attribute])) {
            return $data[$attribute];
        }
        
        return $data;
    }

    /**
     * Get a value from the response (standardized name matching successful responses).
     *
     * @param string|null $attribute
     * @return mixed
     */
    public function getResponse(?string $attribute = null)
    {
        $data = $this->getData();
        
        if (!$data) {
            return null;
        }

        if ($attribute && isset($data[$attribute])) {
            return $data[$attribute];
        }
        
        return $data;
    }

    /**
     * Get the error message (standardized name matching successful responses).
     *
     * @return string|null
     */
    public function getErrorMessage(): ?string
    {
        $data = $this->getData();
        
        if (!$data) {
            return $this->getMessage();
        }

        // Handle OAuth/Login API errors
        if (isset($data['error_description'])) {
            return $data['error_description'];
        }
        
        if (isset($data['error'])) {
            return $data['error'];
        }

        // Handle structured API errors (PAYWA/PAYAG)
        if (isset($data['responseStatus']['systemStatusDesc'])) {
            return $data['responseStatus']['systemStatusDesc'];
        }

        return $this->getMessage();
    }

    /**
     * Get the HTTP status code from the API response.
     *
     * @return int|null
     */
    public function getApiStatus(): ?int
    {
        return $this->response ? $this->response->status() : null;
    }

    /**
     * Get the raw response body as a string.
     *
     * @return string|null
     */
    public function getResponseBodyRaw(): ?string
    {
        return $this->response ? $this->response->body() : null;
    }

    /**
     * Get the response headers.
     *
     * @return array
     */
    public function getResponseHeaders(): array
    {
        return $this->response ? $this->response->headers() : [];
    }



    /**
     * Get API error details in a structured format.
     *
     * @return array
     */
    public function getApiErrorDetails(): array
    {
        $responseData = $this->getData();
        
        if (!$responseData) {
            return [
                'error' => $this->getMessage(),
                'status' => $this->getApiStatus(),
                'type' => 'network_or_parsing_error'
            ];
        }

        // Handle OAuth/Login API errors
        if (isset($responseData['error']) || isset($responseData['error_description'])) {
            return [
                'error' => $responseData['error'] ?? 'unknown_error',
                'error_description' => $responseData['error_description'] ?? $this->getMessage(),
                'status' => $this->getApiStatus(),
                'type' => 'oauth_error'
            ];
        }

        // Handle structured API errors (PAYWA/PAYAG)
        if (isset($responseData['responseStatus'])) {
            $responseStatus = $responseData['responseStatus'];
            return [
                'error' => $responseStatus['systemStatusDesc'] ?? 'Unknown API error',
                'error_description' => $responseStatus['systemStatusDescNative'] ?? '',
                'system_status' => $responseStatus['systemStatus'] ?? 'unknown',
                'status' => $this->getApiStatus(),
                'type' => 'structured_api_error'
            ];
        }

        return [
            'error' => $this->getMessage(),
            'status' => $this->getApiStatus(),
            'response_data' => $responseData,
            'type' => 'unknown_api_error'
        ];
    }

    /**
     * Get additional context information.
     *
     * @return array|null
     */
    public function getContext(): ?array
    {
        return $this->context;
    }

    /**
     * Check if this is a token-related error.
     *
     * @return bool
     */
    public function isTokenError(): bool
    {
        $status = $this->getApiStatus();
        $errorDetails = $this->getApiErrorDetails();
        
        if (in_array($status, [401, 403])) {
            return true;
        }

        $errorText = strtolower($errorDetails['error'] ?? '');
        return strpos($errorText, 'token') !== false || 
               strpos($errorText, 'unauthorized') !== false || 
               strpos($errorText, 'authentication') !== false;
    }

    /**
     * Check if this error is retryable.
     *
     * @return bool
     */
    public function isRetryable(): bool
    {
        $status = $this->getApiStatus();
        
        // Retry on token errors, rate limits, and server errors
        return in_array($status, [401, 403, 429, 500, 502, 503, 504]) || 
               $this->isTokenError();
    }

    /**
     * Get a user-friendly error message.
     *
     * @return string
     */
    public function getUserFriendlyMessage(): string
    {
        $errorDetails = $this->getApiErrorDetails();
        
        switch ($errorDetails['type']) {
            case 'oauth_error':
                return "Authentication failed: " . ($errorDetails['error_description'] ?? $errorDetails['error']);
            
            case 'structured_api_error':
                $message = $errorDetails['error'];
                if (!empty($errorDetails['error_description'])) {
                    $message .= " - " . $errorDetails['error_description'];
                }
                return $message;
            
            case 'network_or_parsing_error':
                return "Network or connection error: " . $errorDetails['error'];
            
            default:
                return $this->getMessage();
        }
    }
}
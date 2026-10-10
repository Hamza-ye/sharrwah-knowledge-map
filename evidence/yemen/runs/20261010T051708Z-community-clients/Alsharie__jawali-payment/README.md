# Laravel Jawali API Client

![Logo](https://raw.githubusercontent.com/Alsharie/jawali-payment-js/main/img.png)

Jawali Payment is a Laravel package for interacting with the Jawali payment gateway. It provides a simple API to perform operations like ecommerce inquiry and cash out, with automatic token management and structured responses.

---

## Installation

1.  Require the package using Composer:
    ```bash
    composer require alsharie/jawali-payment
    ```
    (Replace `alsharie/jawali-payment` with your actual package name on Packagist if you publish it, or use a local path repository for development).

2.  Publish the configuration file (optional, but recommended):
    ```bash
    php artisan vendor:publish --provider="Alsharie\Jawali\JawaliServiceProvider" --tag="jawali-config"
    ```
    This will create a `config/jawali.php` file.

3.  Add the following environment variables to your `.env` file and configure them:
    ```dotenv
    # JAWALI (Jawali) API Configuration
    JAWALI_BASE_URL=https://82.114.179.89:9493/paygate # Or your actual base URL
    JAWALI_DISABLE_SSL_VERIFICATION=false # Set to true to disable SSL verification

    # Credentials for "LOGIN TO SYSTEM" API
    JAWALI_MERCHANT_USERNAME=your_system_login_username
    JAWALI_MERCHANT_PASSWORD=your_system_login_password

    # Credentials for Wallet Authentication & PAYAG operations
    JAWALI_MERCHANT_WALLET=your_agent_wallet_identifier
    JAWALI_MERCHANT_WALLET_PASSWORD=your_agent_wallet_password

    # Common Header Information for PAYWA/PAYAG APIs
    JAWALI_MERCHANT_ORG_ID=your_organization_id
    JAWALI_MERCHANT_USER_ID=your_user_id
    JAWALI_MERCHANT_EXTERNAL_USER=your_external_user # Optional, if applicable



    # Request settings
    JAWALI_TIMEOUT=30
    JAWALI_RETRY_ENABLED=true
    JAWALI_RETRY_MAX_ATTEMPTS=2

    # Logging settings (optional - for debugging)
    JAWALI_LOGGING_ENABLED=false
    ```

---

## Configuration

The package uses Laravel's configuration system. After publishing the config file, you can find it at `config/jawali.php`. The configuration is structured as follows:

```php
return [
    'auth' => [
        // For "LOGIN TO SYSTEM" API
        'username' => env('JAWALI_MERCHANT_USERNAME'),
        'password' => env('JAWALI_MERCHANT_PASSWORD'),

        // For PAYWA/PAYAG header: signonDetail
        'org_id' => env('JAWALI_MERCHANT_ORG_ID'),
        'user_id' => env('JAWALI_MERCHANT_USER_ID'),
        'external_user' => env('JAWALI_MERCHANT_EXTERNAL_USER'),

        // For PAYWA.WALLETAUTHENTICATION body & PAYAG body
        'wallet_identifier' => env('JAWALI_MERCHANT_WALLET'),
        'wallet_password' => env('JAWALI_MERCHANT_WALLET_PASSWORD'),
    ],

    'url' => [
        'base' => env('JAWALI_BASE_URL', 'https://82.114.179.89:9493/paygate'),
        'disable_ssl_verification' => env('JAWALI_DISABLE_SSL_VERIFICATION', false),
    ],

    'timeout' => env('JAWALI_TIMEOUT', 30),

    'retry' => [
        'enabled' => env('JAWALI_RETRY_ENABLED', true),
        'max_attempts' => env('JAWALI_RETRY_MAX_ATTEMPTS', 2),
        'status_codes' => [400, 401],
    ],
];
```

The `disable_ssl_verification` option is particularly useful when working with development environments or self-signed certificates.

---

## Logging Configuration

The package includes built-in logging capabilities for debugging API requests and responses. To enable logging:

1. **Enable logging** in your `.env` file:
   ```dotenv
   JAWALI_LOGGING_ENABLED=true
   ```

2. **Ensure the logs directory is writable**:
   ```bash
   mkdir -p storage/logs
   chmod 755 storage/logs
   ```

The package will log all API interactions using Laravel's default logging system. Log entries include:
- Request method, URL, and payload (with sensitive data redacted)
- Response status and data
- Error details with context

**Note**: Logging errors are silently ignored to prevent them from breaking the main application functionality.

---

## Features

This package provides the following features:

1. **Structured Response Classes**: Each API response is wrapped in a dedicated response class that provides methods to access the data in a type-safe way.
2. **Automatic Token Management**: The package automatically manages authentication and wallet tokens, refreshing them when needed.
3. **Retry Mechanism**: Failed requests due to token expiration or certain HTTP status codes are automatically retried.
4. **SSL Verification Control**: Option to disable SSL verification for development or when working with self-signed certificates.
5. **Simplified API**: The API is simplified to focus on the essential parameters, with tokens managed automatically.
6. **Enhanced Error Handling**: Comprehensive error information with API response preservation and user-friendly error messages.
7. **Optional Logging**: Built-in request/response logging for debugging purposes.
8. **Input Validation**: Automatic validation of request parameters to prevent common errors.

---

## Usage

You can use the `Jawali` facade or inject the `Alsharie\Jawali\Services\JawaliService` class.

```php
use Alsharie\Jawali\Facades\Jawali;
use Alsharie\Jawali\Exceptions\JawaliApiException;

// Example: Login to System
try {
    $loginResponse = Jawali::loginToSystem();

    if ($loginResponse->isSuccess()) {
        // Access token is automatically stored for future requests
        echo "Login successful! Access token: " . $loginResponse->getAccessToken();
    } else {
        echo "Login failed!";
    }
} catch (JawaliApiException $e) {
    // Handle API error
    // $e->getMessage(), $e->getApiStatus(), $e->getData()
    logger()->error('Jawali Login Error: ' . $e->getMessage(), ['response' => $e->getData()]);
}

// Example: Wallet Authentication
// Optional header overrides if needed for a specific call
$headerOverrides = [
    'signonDetail' => [
        'orgID' => '22000001688', // Example, could be different
        'userID' => 'school.branch.api.test',
        'externalUser' => 'user1',
    ]
];

try {
    $walletAuthResponse = Jawali::walletAuthentication($headerOverrides);

    if ($walletAuthResponse->isSuccess()) {
        // Wallet token is automatically stored for future requests
        echo "Wallet authentication successful!";
    } else {
        echo "Wallet authentication failed!";
    }
} catch (JawaliApiException $e) {
    logger()->error('Jawali Wallet Auth Error: ' . $e->getMessage(), ['response' => $e->getData()]);
}

// Example: Ecommerce Inquiry
// Note: No need to pass tokens - they are managed automatically
try {
    $voucher = '3360714';
    $receiverMobile = '711029220';
    $purpose = 'test bill payment';

    $inquiryResponse = Jawali::ecommerceInquiry($voucher, $receiverMobile, $purpose, $headerOverrides);

    if ($inquiryResponse->isSuccess()) {
        echo "Inquiry successful!";
        echo "Amount: " . $inquiryResponse->getAmount();
        echo "Currency: " . $inquiryResponse->getCurrency();
        echo "State: " . $inquiryResponse->getState();
        echo "Transaction Reference: " . $inquiryResponse->getTransactionRef();

        // Check if the transaction is in PENDING state
        if ($inquiryResponse->getState() === 'PENDING') {
            // Proceed with cashout
        }
    } else {
        echo "Inquiry failed!";
    }
} catch (JawaliApiException $e) {
    logger()->error('Jawali Inquiry Error: ' . $e->getMessage(), ['response' => $e->getData()]);
}

// Example: Ecommerce Cashout
try {
    $voucher = '2383314';
    $receiverMobile = '711029220';
    $purpose = 'test bill payment';

    $cashoutResponse = Jawali::ecommerceCashout($voucher, $receiverMobile, $purpose, $headerOverrides);

    if ($cashoutResponse->isSuccess()) {
        echo "Cashout successful!";
        echo "Amount: " . $cashoutResponse->getAmount();
        echo "Currency: " . $cashoutResponse->getCurrency();
        echo "Transaction Reference: " . $cashoutResponse->getTransactionRef();
    } else {
        echo "Cashout failed!";
    }
} catch (JawaliApiException $e) {
    logger()->error('Jawali Cashout Error: ' . $e->getMessage(), ['response' => $e->getData()]);
}

// Complete End-to-End Example
// This example shows how to perform an inquiry and then a cashout if the conditions are met
function processPayment($voucher, $receiverMobile, $purpose, $expectedAmount, $expectedCurrency)
{
    try {
        // Step 1: Perform an ecommerce inquiry
        $inquiryResponse = Jawali::ecommerceInquiry($voucher, $receiverMobile, $purpose);

        if ($inquiryResponse->isSuccess()) {
            // Step 2: Check if the state is "PENDING" and the amount and currency are correct
            if ($inquiryResponse->getState() === 'PENDING') {
                if ($inquiryResponse->getAmount() == $expectedAmount && 
                    $inquiryResponse->getCurrency() === $expectedCurrency) {

                    // Step 3: Perform cashout
                    $cashoutResponse = Jawali::ecommerceCashout($voucher, $receiverMobile, $purpose);

                    if ($cashoutResponse->isSuccess()) {
                        return [
                            'message' => 'Payment processed successfully',
                            'success' => true,
                            'data' => $cashoutResponse->getData(),
                        ];
                    } else {
                        return [
                            'message' => 'Error during cashout',
                            'success' => false,
                            'data' => $cashoutResponse->getData(),
                        ];
                    }
                } else {
                    return [
                        'message' => 'Amount or currency mismatch',
                        'success' => false,
                        'expected' => [
                            'amount' => $expectedAmount,
                            'currency' => $expectedCurrency,
                        ],
                        'actual' => [
                            'amount' => $inquiryResponse->getAmount(),
                            'currency' => $inquiryResponse->getCurrency(),
                        ],
                    ];
                }
            } else {
                return [
                    'message' => 'Transaction is not in PENDING state',
                    'success' => false,
                    'state' => $inquiryResponse->getState(),
                ];
            }
        } else {
            return [
                'message' => 'Inquiry failed',
                'success' => false,
                'error' => $inquiryResponse->getErrorMessage(),
            ];
        }
    } catch (JawaliApiException $e) {
        return [
            'message' => 'API Exception',
            'success' => false,
            'error' => $e->getMessage(),
            'status' => $e->getApiStatus(),
        ];
    } catch (\Exception $e) {
        return [
            'message' => 'General Exception',
            'success' => false,
            'error' => $e->getMessage(),
        ];
    }
}
```

---

## Enhanced Error Handling

The package now provides comprehensive error handling with detailed API response information and **standardized method names** that match successful responses:

```php
use Alsharie\Jawali\Facades\Jawali;
use Alsharie\Jawali\Exceptions\JawaliApiException;

try {
    $inquiryResponse = Jawali::ecommerceInquiry($voucher, $receiverMobile, $purpose);
    // Handle successful response
} catch (JawaliApiException $e) {
    // Get detailed error information
    $errorDetails = $e->getApiErrorDetails();
    
    // Access specific error information
    $statusCode = $e->getApiStatus();
    $apiResponse = $e->getData();
    $userFriendlyMessage = $e->getUserFriendlyMessage();
    
    // Check error type
    if ($e->isTokenError()) {
        // Handle token-related errors
        logger()->warning('Token error occurred', $errorDetails);
    } elseif ($e->isRetryable()) {
        // Handle retryable errors
        logger()->info('Retryable error occurred', $errorDetails);
    }
    
    // Log the error with context
    logger()->error('Jawali API Error', [
        'error_details' => $errorDetails,
        'voucher' => $voucher,
        'mobile' => $receiverMobile,
    ]);
}
```

### Standardized Method Names

Both successful responses and exceptions now use the same method names for consistency:

| Purpose | Method Name | Available On | Description |
|---------|-------------|--------------|-------------|
| Get raw data | `getData()` | ✅ Success & Exception | Returns the complete response data array |
| Get response body | `getResponseBody($attribute?)` | ✅ Success & Exception | Gets response body or specific attribute |
| Get response value | `getResponse($attribute?)` | ✅ Success & Exception | Gets response data or specific attribute |
| Get error message | `getErrorMessage()` | ✅ Success & Exception | Gets API error message if available |
| Check success | `isSuccess()` | ✅ Success only | Not applicable for exceptions |

**Example - Same methods work for both success and error:**
```php
try {
    $response = Jawali::ecommerceInquiry($voucher, $mobile);
    
    // Success case
    $data = $response->getData();
    $amount = $response->getResponseBody('amount');
    $error = $response->getErrorMessage(); // null if successful
    
} catch (JawaliApiException $e) {
    // Error case - SAME method names!
    $data = $e->getData();
    $errorDetail = $e->getResponseBody('error');
    $error = $e->getErrorMessage();
}
```

**Breaking Change:** Old method names (`getApiResponse()`, `getApiResponseBody()`, `getApiResponseHeaders()`) have been removed. Use the standardized method names instead.

## Debugging and Logging

Enable logging to debug API requests and responses:

```php
// In your .env file
JAWALI_LOGGING_ENABLED=true

```

The package automatically logs:
- API requests (with sensitive data redacted)
- API responses 
- Error details and context
- Token refresh attempts

### Explanation

- **loginToSystem()**  
  This method authenticates with the Jawali system using the credentials from your configuration. The response is an instance of `JawaliLoginResponse` which provides access to the authentication token.

- **walletAuthentication()**  
  After system login, this method authenticates your wallet. The response is an instance of `JawaliWalletAuthResponse` which provides access to the wallet token.

- **ecommerceInquiry()**  
  This method contacts the gateway to verify payment details. The response is an instance of `JawaliEcommerceInquiryResponse` which provides methods like `getAmount()`, `getCurrency()`, and `getState()`.

- **ecommerceCashout()**  
  When the inquiry indicates a pending state with the correct amount and currency, this method is called to complete the cash-out. Its response is wrapped in the `JawaliEcommerceCashoutResponse` class.

- **Response Handling**  
  All response classes extend the base `JawaliResponse` class (except `JawaliLoginResponse`). They provide methods like `isSuccess()`, `getErrorMessage()`, and `getData()` for consistent response handling.

---

## License

This package is open-sourced software licensed under the [MIT license](https://opensource.org/licenses/MIT).

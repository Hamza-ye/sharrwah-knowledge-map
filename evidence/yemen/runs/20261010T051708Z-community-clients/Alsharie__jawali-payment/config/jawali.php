<?php

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
        'wallet_identifier' => env('JAWALI_MERCHANT_WALLET'),   // This is the 'identifier' for WalletAuth and 'agentWallet' for PAYAG
        'wallet_password' => env('JAWALI_MERCHANT_WALLET_PASSWORD'), // Password for WalletAuth and PAYAG calls


    ],

    'url' => [
        'base' => env('JAWALI_BASE_URL', 'https://82.114.179.89:9493/paygate'),
        'disable_ssl_verification' => env('JAWALI_DISABLE_SSL_VERIFICATION', false), // Set to true to disable SSL verification
    ],

    'timeout' => env('JAWALI_TIMEOUT', 30), // HTTP request timeout in seconds

    'retry' => [
        'enabled' => env('JAWALI_RETRY_ENABLED', true), // Enable or disable retry mechanism
        'max_attempts' => env('JAWALI_RETRY_MAX_ATTEMPTS', 2), // Maximum number of retry attempts
        'status_codes' => [400, 401], // HTTP status codes that should trigger a retry
    ],

    'logging' => [
        'enabled' => env('JAWALI_LOGGING_ENABLED', false), // Enable or disable request/response logging
    ],
];

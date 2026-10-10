# Kuraimi Bank E-Pay SDK for Node.js (TypeScript)

A TypeScript Node.js client library for integrating with the Kuraimi Bank E-Pay API.

This SDK helps you (the Supplier) call Kuraimi Bank's APIs for E-Payment and Reversals.



## ❗ Crucial Pre-Integration Step: Supplier's Web API

**Before you can successfully use the E-Payment features facilitated by this SDK (and by Kuraimi Bank's system), your system MUST expose a "Verify Customer details API".**

As per Section 13 of the "Supplier Integration Guide and Technical Specification":

*   **Purpose:** Kuraimi Bank's E-Pay system will call this API (hosted by you, the supplier) to verify customer details registered on your platform.
*   **Your Responsibility:**
    1.  You need to develop and host an HTTP POST endpoint.
    2.  This endpoint will receive customer details (e.g., `SCustID`, `MobileNo`, `Email`, `CustomerZone`) from Kuraimi Bank.
    3.  Your API must validate these details against your customer database.
    4.  Your API must respond in the format specified in the Kuraimi Bank documentation , including a `Code` ("1" for success, others for failure) and the `SCustID` if verified.
    5.  You must provide Kuraimi Bank with:
        *   The URL (Endpoint) for both UAT and Production environments.
        *   Username and Password for Basic Authentication that Kuraimi Bank will use to call your API.
*   **Impact:** If this supplier-hosted API is not implemented, not reachable, or does not function correctly, customer verification will fail, and subsequent E-Payment transactions initiated via Kuraimi Bank's applications (KJ, Mfloos) for your services may not be possible.

**This SDK (`@alsharie/kuraimiepay`) helps you call Kuraimi Bank's APIs. It does NOT implement the API that Kuraimi Bank calls on your system.** Ensure this separate integration requirement is met with Kuraimi Bank.

## Features (of this SDK)

*   Easy-to-use client for E-Payment and Reversal transactions (calling Kuraimi Bank).
*   Strongly typed interfaces for requests and responses.
*   Handles Basic Authentication for calls *to* Kuraimi Bank.
*   Automatic Base64 encoding for `PINPASS`.
*   Configurable for UAT and Production environments.
*   Uses `axios` for HTTP requests.
*   Written in TypeScript, compiled to JavaScript.

## Prerequisites (for using this SDK)

*   **Completion of the "Supplier's Web API" integration (see section above).**
*   Node.js (v14 or higher recommended)
*   TypeScript (v4.5 or higher recommended)
*   API Credentials (Username and Password) for *your supplier account* to call Kuraimi Bank's E-Pay APIs (provided by Kuraimi Bank).
*   UAT and Production Base URLs for Kuraimi Bank's E-Pay APIs. The UAT URL is included based on the document; the Production URL will need to be supplied during client initialization.

## Installation

```bash
npm install @alsharie/kuraimiepay
# or
yarn add @alsharie/kuraimiepay
```

## Usage

### 1. Initialize the Client

```typescript
import KuraimiEPayClient from '@alsharie/kuraimiepay';

const apiClient = new KuraimiEPayClient({
    username: 'YOUR_SUPPLIER_USERNAME', // Provided by Kuraimi Bank
    password: 'YOUR_SUPPLIER_PASSWORD', // Provided by Kuraimi Bank
    environment: 'UAT', // 'UAT' or 'PROD'
    // baseUrl: 'https://your-custom-or-prod-base-url.com' // Optional: if PROD URL is known or to override default
});
```

### 2. Send an E-Payment Transaction

```typescript
async function makePayment() {
    const paymentDetails: SendPaymentPayload = {
        SCustID: 'SCUST98765',
        REFNO: `TS_PAY${Date.now()}`, // Ensure this is unique
        AMOUNT: 150.75,
        MRCHNTNAME: 'My Online Store TS',
        PINPASS: '1234', // Customer's PIN
    };

    try {
        const response: ApiResponse = await apiClient.sendPayment(paymentDetails);
        console.log('Payment Response:', response);

        if (response.CODE === 1 && response.ResultSet?.PH_REF_NO) {
            console.log('Payment successful! Bank Ref:', response.ResultSet.PH_REF_NO);
        } else {
            console.error(`Payment failed: ${response.MESSAGE} (Code: ${response.CODE})`);
        }
    } catch (error) {
        const apiError = error as ApiError;
        console.error('Error during payment:', apiError.data || apiError.message || apiError);
        if (apiError.statusCode) console.error('Status Code:', apiError.statusCode);
    }
}

makePayment();
```

### 3. Reverse an E-Payment Transaction

```typescript
import { ReversePaymentPayload } from '@alsharie/kuraimiepay'; // Import additional types as needed

async function reverseExistingPayment() {
    const reversalDetails: ReversePaymentPayload = {
        SCustID: 'SCUST98765',
        REFNO: 'TS_PAY1678886660000', // The REFNO of the transaction you want to reverse
    };

    try {
        const response: ApiResponse = await apiClient.reversePayment(reversalDetails);
        console.log('Reversal Response:', response);

        if (response.CODE === 1) {
            console.log('Reversal request processed successfully.');
        } else {
            console.error(`Reversal failed: ${response.MESSAGE} (Code: ${response.CODE})`);
        }
    } catch (error) {
        const apiError = error as ApiError;
        console.error('Error during reversal:', apiError.data || apiError.message || apiError);
        if (apiError.statusCode) console.error('Status Code:', apiError.statusCode);
    }
}

reverseExistingPayment();
```

## API Reference (Types)

Key types are exported from the main module:
*   `KuraimiEPayClientOptions`
*   `SendPaymentPayload`
*   `ReversePaymentPayload`
*   `ApiResponse<T = ResultSet | null>`
*   `ApiError`
*   `ResultSet`

Refer to the source code in `src/index.ts` for detailed type definitions.

## Error Handling

The SDK methods return Promises. If an API call fails or a network error occurs, the Promise will be rejected with an `ApiError` object. This object typically includes:
*   `message` (string): A summary of the error.
*   `statusCode` (number, optional): The HTTP status code, if available.
*   `data` (ApiErrorResponseData, optional): The response body from the API, if available (this usually contains `CODE`, `MESSAGE`, `MESSAGEDESC` from Kuraimi Bank).
*   `originalError` (AxiosError | Error, optional): The underlying error object.

Always wrap API calls in `try...catch` blocks.


## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

MIT
---
title: Implementation considerations
description: Learn about implementing a payments app.
source_url:
  html: 'https://shopify.dev/docs/apps/build/payments/considerations'
  md: 'https://shopify.dev/docs/apps/build/payments/considerations.md'
api_name: payments-apps
---

# Implementation considerations

After you've created your payments app and extension, learned about the payments app actions and published your payments app and extension, you must make sure you've implemented the following protocols to be approved as a payments app.

***

## Requirements

* You've created a payments app.

* You've made sure your payments app meets [the requirements](https://shopify.dev/docs/apps/build/payments/requirements).

* Your app has the `write_payment_gateways` and `write_payment_sessions` [access scopes](https://shopify.dev/docs/api/usage/access-scopes#authenticated-access-scopes).

  **Note:**

  These are restricted scopes, and you need to [apply](https://shopify.dev/docs/apps/build/payments/payments-extension-review) for access.

***

## m​TLS configuration

Payments apps need to implement [mTLS](https://en.wikipedia.org/wiki/Mutual_authentication#mTLS) to handle all requests where the app acts as the server and Shopify acts as the client, such as when Shopify initiates sessions with payments apps for `payment`, `refund`, `capture`, and `void` requests. In these cases, Shopify uses its own client certificate. Payments apps need to use the provided [self-signed CA](#shopifys-self-signed-certificate-authority-ca) to validate Shopify's certificate. Using mTLS in these scenarios allows payments apps to verify that the client initiating the request is Shopify and that the traffic between Shopify and the payments app is trusted and secure.

Because mTLS is mutual, the payments app also needs to provide a certificate that Shopify will validate. For this certificate, you need to use a [Trusted CA Signed SSL Certificate](https://shopify.dev/docs/apps/build/security#encrypt-with-tls), and not Shopify’s self-signed CA.

**Note:**

mTLS isn’t used to retrieve the [OAuth access token](https://shopify.dev/docs/apps/build/authentication-authorization). All requests that use Shopify GraphQL mutations are authenticated with an OAuth access token, not mTLS.

***

## Shopify's client certificate

### Current certificate

The following is the current client certificate used by Shopify:

```text
-----BEGIN CERTIFICATE-----
MIIDcjCCAxigAwIBAgITOUWD5NfOXTdSo9M6194RprBBtDAKBggqhkjOPQQDAjB5
MQswCQYDVQQGEwJDQTEQMA4GA1UECBMHT250YXJpbzEPMA0GA1UEBxMGT3R0YXdh
MRAwDgYDVQQKEwdTaG9waWZ5MTUwMwYDVQQDEyxTaG9waWZ5IFBheW1lbnRzIFBs
YXRmb3JtIFByb2R1Y3Rpb24gbVRMUyBDQTAeFw0yNjA0MTMxODUxNTNaFw0yNzA0
MTMxODUxNTJaMIG+MQswCQYDVQQGEwJDQTEQMA4GA1UECBMHT250YXJpbzEPMA0G
A1UEBxMGT3R0YXdhMRAwDgYDVQQKEwdTaG9waWZ5MTwwOgYDVQQLEzNTaG9waWZ5
IFBheW1lbnRzIFBsYXRmb3JtIC0gbVRMUyAtIEV4dGVybmFsIFBhcnRuZXIxPDA6
BgNVBAMTM1BheW1lbnRzIFBhcnRuZXJzIFBsYXRmb3JtIC0gUHJvZHVjdGlvbiBD
ZXJ0aWZpY2F0ZTBZMBMGByqGSM49AgEGCCqGSM49AwEHA0IABBR+y+uge5fE9aIT
OIGHJChMl4CHFicL8AShDizGxCCesOr/UTODqM9EoEIWT2kTTPVLfKhetiPCOngb
a2v7z0qjggE3MIIBMzAOBgNVHQ8BAf8EBAMCA7gwEwYDVR0lBAwwCgYIKwYBBQUH
AwIwDAYDVR0TAQH/BAIwADAdBgNVHQ4EFgQUmuHbhbgkrEprvd4fVq8pUqiIcfow
HwYDVR0jBBgwFoAUCbl6NVk6TjkIHNjvaj37xkKONxgwYwYIKwYBBQUHAQEEVzBV
MFMGCCsGAQUFBzAChkdodHRwOi8vc2hvcGlmeS1wcC1jYS5zdG9yYWdlLmdvb2ds
ZWFwaXMuY29tLzE3YWUzYWNlMzMzYjBjY2IwMjUxL2NhLmNydDBZBgNVHR8EUjBQ
ME6gTKBKhkhodHRwOi8vc2hvcGlmeS1wcC1jYS5zdG9yYWdlLmdvb2dsZWFwaXMu
Y29tLzE3YWUzYWNlMzMzYjBjY2IwMjUxL2NybC5jcmwwCgYIKoZIzj0EAwIDSAAw
RQIgYap0l4PHD/DQ3d1P+Zt7qXPn5d5F/qzPtUjFUI1hQNwCIQD6E5i9ngdE8rm1
JSdwwUn1QssbtJuRyc5rGOK/qf5/tQ==
-----END CERTIFICATE-----
```

***

## Shopify's self-signed Certificate Authority (CA)

Shopify uses a self-signed CA chain. This means you must add this CA chain to your web server trust store in order for it to be recognized when Shopify makes requests to your payment app server.

By adding Shopify's self-signed CA and enforcing mTLS on your web server you are adding a security measure to ensure your web server can distinguish requests originating from Shopify.

### Current CA chain

## Shopifys Payments Platform Root CA

```text
-----BEGIN CERTIFICATE-----
MIICWDCCAf+gAwIBAgITMygdbwhl8kBOTvx27/fTtzHiojAKBggqhkjOPQQDAjB5
MQswCQYDVQQGEwJDQTEQMA4GA1UECBMHT250YXJpbzEPMA0GA1UEBxMGT3R0YXdh
MRAwDgYDVQQKEwdTaG9waWZ5MTUwMwYDVQQDEyxTaG9waWZ5IFBheW1lbnRzIFBs
YXRmb3JtIFByb2R1Y3Rpb24gUm9vdCBDQTAeFw0yNDA2MDUxNzQyMzVaFw0zMjA2
MDMxNzQyMzRaMHkxCzAJBgNVBAYTAkNBMRAwDgYDVQQIEwdPbnRhcmlvMQ8wDQYD
VQQHEwZPdHRhd2ExEDAOBgNVBAoTB1Nob3BpZnkxNTAzBgNVBAMTLFNob3BpZnkg
UGF5bWVudHMgUGxhdGZvcm0gUHJvZHVjdGlvbiBSb290IENBMFkwEwYHKoZIzj0C
AQYIKoZIzj0DAQcDQgAEqr/2xbnpnvGlY5/rRv77k1UEiPfBEyScAASgXpL7r7VN
8FFzbr+yonNDIoYwB3SpYbSazY6YecvdeoGV2Oj1HqNmMGQwDgYDVR0PAQH/BAQD
AgEGMBIGA1UdEwEB/wQIMAYBAf8CAQEwHQYDVR0OBBYEFOIXfkVFo1W7SyL24b/n
HG95w+rSMB8GA1UdIwQYMBaAFOIXfkVFo1W7SyL24b/nHG95w+rSMAoGCCqGSM49
BAMCA0cAMEQCIHBeLk+U8UX8HTboeMwLrlHik+EJNoQeSHcN29ZjW0SpAiBJXU0j
+t5QRiZ5X+dIVZpJuecZFpm7V68SWNke9FkQ0w==
-----END CERTIFICATE-----
```

### Full CA chain

If your web server doesn't support receiving the CA chain within the request sent by Shopify, but instead requires the full CA chain to be stored in your web server's trust store (for example, [Amazon `API Gateway`](https://docs.aws.amazon.com/apigateway/latest/developerguide/rest-api-mutual-tls.html)), then you require both the Intermediate and Root CA:

## Shopifys Payments Platform Intermediate and Root CAs

```text
-----BEGIN CERTIFICATE-----
MIIDHTCCAsOgAwIBAgITKMnwAMsx0R9mCbVn67on3AWuKTAKBggqhkjOPQQDAjB5
MQswCQYDVQQGEwJDQTEQMA4GA1UECBMHT250YXJpbzEPMA0GA1UEBxMGT3R0YXdh
MRAwDgYDVQQKEwdTaG9waWZ5MTUwMwYDVQQDEyxTaG9waWZ5IFBheW1lbnRzIFBs
YXRmb3JtIFByb2R1Y3Rpb24gUm9vdCBDQTAeFw0yNDA2MDUxNzQyNThaFw0yNzA2
MDUxNzQyNTdaMHkxCzAJBgNVBAYTAkNBMRAwDgYDVQQIEwdPbnRhcmlvMQ8wDQYD
VQQHEwZPdHRhd2ExEDAOBgNVBAoTB1Nob3BpZnkxNTAzBgNVBAMTLFNob3BpZnkg
UGF5bWVudHMgUGxhdGZvcm0gUHJvZHVjdGlvbiBtVExTIENBMFkwEwYHKoZIzj0C
AQYIKoZIzj0DAQcDQgAEBs0SxmOg60LgM2qU7UXuHAnUNGLwfxCYAt8XmWKN9nTM
f46A0qnRwkaRH7mHbbpdEGoUfv7v/4en4osORRdLbKOCASgwggEkMA4GA1UdDwEB
/wQEAwIBBjASBgNVHRMBAf8ECDAGAQH/AgEAMB0GA1UdDgQWBBQJuXo1WTpOOQgc
2O9qPfvGQo43GDAfBgNVHSMEGDAWgBTiF35FRaNVu0si9uG/5xxvecPq0jBjBggr
BgEFBQcBAQRXMFUwUwYIKwYBBQUHMAKGR2h0dHA6Ly9zaG9waWZ5LXBwLWNhLnN0
b3JhZ2UuZ29vZ2xlYXBpcy5jb20vNTc2MjU1NzJjZTgyYjRmZDI0MWMvY2EuY3J0
MFkGA1UdHwRSMFAwTqBMoEqGSGh0dHA6Ly9zaG9waWZ5LXBwLWNhLnN0b3JhZ2Uu
Z29vZ2xlYXBpcy5jb20vNTc2MjU1NzJjZTgyYjRmZDI0MWMvY3JsLmNybDAKBggq
hkjOPQQDAgNIADBFAiBuOeNxCQXeIlY9uSsMnW5F3Q3ykq7CB6nSWfVL2t8eCAIh
AOZOg7bU+xUtNMOE/d54TxwDymqI6NZ1lLfCMfEUwF7W
-----END CERTIFICATE-----
-----BEGIN CERTIFICATE-----
MIICWDCCAf+gAwIBAgITMygdbwhl8kBOTvx27/fTtzHiojAKBggqhkjOPQQDAjB5
MQswCQYDVQQGEwJDQTEQMA4GA1UECBMHT250YXJpbzEPMA0GA1UEBxMGT3R0YXdh
MRAwDgYDVQQKEwdTaG9waWZ5MTUwMwYDVQQDEyxTaG9waWZ5IFBheW1lbnRzIFBs
YXRmb3JtIFByb2R1Y3Rpb24gUm9vdCBDQTAeFw0yNDA2MDUxNzQyMzVaFw0zMjA2
MDMxNzQyMzRaMHkxCzAJBgNVBAYTAkNBMRAwDgYDVQQIEwdPbnRhcmlvMQ8wDQYD
VQQHEwZPdHRhd2ExEDAOBgNVBAoTB1Nob3BpZnkxNTAzBgNVBAMTLFNob3BpZnkg
UGF5bWVudHMgUGxhdGZvcm0gUHJvZHVjdGlvbiBSb290IENBMFkwEwYHKoZIzj0C
AQYIKoZIzj0DAQcDQgAEqr/2xbnpnvGlY5/rRv77k1UEiPfBEyScAASgXpL7r7VN
8FFzbr+yonNDIoYwB3SpYbSazY6YecvdeoGV2Oj1HqNmMGQwDgYDVR0PAQH/BAQD
AgEGMBIGA1UdEwEB/wQIMAYBAf8CAQEwHQYDVR0OBBYEFOIXfkVFo1W7SyL24b/n
HG95w+rSMB8GA1UdIwQYMBaAFOIXfkVFo1W7SyL24b/nHG95w+rSMAoGCCqGSM49
BAMCA0cAMEQCIHBeLk+U8UX8HTboeMwLrlHik+EJNoQeSHcN29ZjW0SpAiBJXU0j
+t5QRiZ5X+dIVZpJuecZFpm7V68SWNke9FkQ0w==
-----END CERTIFICATE-----
```

We will continue to send the leaf certificate in any request we make to the web server URL you set in your payment extension config.

***

## Idempotency

Payments Apps APIs support idempotency, which allows Shopify to safely retry requests without accidentally performing the same operation twice. Idempotency is critical in cases where there are network errors to prevent, such as multiple charges for the same payment. Idempotency keys don't expire.

### HTTP requests from Shopify to your payments app

You need to support idempotent requests for the Payments Apps APIs. Regardless of how many requests with the same idempotency key are sent, the result must be the same. The idempotency key attributes are defined on a per-API basis in the [payment request body](https://shopify.dev/docs/apps/build/payments/request-reference).

### Graph​QL requests from your payments app to Shopify

Idempotency is implemented on a per mutation basis for a given `id`. If multiple requests of the same mutation are made, then the mutation will only be performed once during the first request, and the same response will be returned in subsequent requests. For instance, if several requests for [`paymentSessionResolve`](https://shopify.dev/docs/api/payments-apps/latest/mutations/paymentSessionResolve) are made using the same `id`, then the mutation will only be executed once.

Some mutations are mutually exclusive, such as [`paymentSessionResolve`](https://shopify.dev/docs/api/payments-apps/latest/mutations/paymentSessionResolve) and [`paymentSessionReject`](https://shopify.dev/docs/api/payments-apps/latest/mutations/paymentSessionReject), where only one can be processed for a given `id`. If requests for different mutations are submitted using the same `id`, then the first request to be received will be processed, and any subsequent requests with incompatible mutation will fail with a [`user_error`](https://shopify.dev/docs/api/payments-apps/latest/objects/UserError).

***

## Retry policy

### Outbound

Due to the asynchronous nature of Shopify's Payments Apps APIs, you must send a GraphQL request to notify Shopify of the results of any payment or refund requests. A retry policy helps provide data consistency between merchants, Partners, and Shopify. You must implement a retry policy for the [Payments Apps API mutations](https://shopify.dev/docs/api/payments-apps).

If there's a Shopify service disruption (or if 5xx status codes are being returned), then requests must be retried according to the following incremental strategy, up to a total of 18 retries over 24h. During this time, you can provide the customer with the following information:

* Their payment is processed, but Shopify is unreachable.
* They'll receive a notification from Shopify when the order is processed.
* They should contact the merchant directly if the maximum number of recommended retries elapses without acknowledgment.

| Parameter | Description | Value |
| - | - | - |
| **Number of recommended retries** | The maximum number of recommended retries. | 18 |
| **Base delay interval** | The time interval after which the first retry is attempted. | 5 seconds |
| **Exponential backoff factor** | Partners are expected to retry their requests immediately, and then 5 seconds afterwards, and then at increasing time intervals after that, until the request is acknowledged or 24 hours has passed, whichever comes first. | See example |

**Example:**

\[0 seconds, 5 seconds, 10 seconds, 30 seconds, 45 seconds, 1 minute, 2 minutes, 5 minutes, 12 minutes, 38 minutes, 1 hour, 2 hours] + \[4 hours] \* 5

### Inbound

All HTTP requests from Shopify to your payments app endpoints (payment session, refund session, capture session, void session, and balance URLs) are subject to timeouts. If your endpoint doesn't respond in time, Shopify retries the request several times.

***

## Rate limiting

To protect the stability of the platform, payments apps are rate-limited. For more information, refer to [Shopify API rate limits](https://shopify.dev/docs/api/payments-apps#rate-limits).

***

## Next steps

Learn how to [onboard a merchant to your payment app](https://shopify.dev/docs/apps/build/payments/onboard-a-merchant-payments-extension).

***

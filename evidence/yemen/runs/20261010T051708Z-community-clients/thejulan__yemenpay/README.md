# YemenPay JavaScript SDK & Gateway API 💳

The official lightweight JavaScript SDK and UI integration library for **YemenPay** — the unified digital payment gateway for Yemen. Enable your e-commerce store or app to accept payments from popular Yemeni e-wallets including **Jaib**, **Jawaly**, **Kuraimi**, **OneCash**, and **Yemen Wallet**.

---

## ✨ Features

- **Multiple UI Layouts**: Supports floating `modal` popups or embedded `inline` checkout forms directly inside your cart page.
- **22 Color Themes**: Pre-built dark & light themes (`dark-yellow`, `dark-blue`, `light-cyber`, `dark-gold`, etc.) to match any store branding.
- **Anti-Price Tampering**: Server-side product price verification and optional browser DevTools blocking to prevent client-side modifications.
- **Automated Verification (API)**: Automatic backend verification of customer transfers with real-time countdown timers.
- **Responsive & Lightweight**: Zero external framework dependencies. Isolated CSS prevents styling leaks into your website.
- **Multi-Currency Support**: Supports `YER` (Yemeni Rial), `SAR` (Saudi Rial), and `USD`.

---

## 📁 Repository Structure

```
yemenpay/
├── app/                    # Flutter Mobile Application (Merchant & Admin)
│   ├── lib/                # App source code (Dart)
│   └── pubspec.yaml        # Flutter dependencies & assets
├── sdk/                    # The SDK library for the project
│   ├── yemenpay.css        # CSS file for the SDK
│   └── yemenpay.js         # JS file for the SDK
└── README.md
```

---

## 🚀 Integration Guide

### Method 1: HTML Data Attributes (Auto-Initialization)

Add a `<div>` container to your checkout page where you want the payment button or inline widget to appear:

```html
<div 
  id="yemenpay-root"
  data-yemenpay
  data-client-id="YOUR_MERCHANT_CLIENT_ID"
  data-amount="15000"
  data-currency="YER"
  data-theme="dark-yellow"
  data-layout="modal"
  data-button-text="Pay with Digital Wallet"
  data-sticky-modal="true"
></div>

<!-- Include the YemenPay SDK before the </body> tag -->
<script src="/assets/js/yemenpay.js"></script>
```

#### Supported Data Attributes:
| Attribute | Type | Description | Default |
| :--- | :--- | :--- | :--- |
| `data-amount` | `Number` | The payment amount | Required |
| `data-currency` | `String` | Currency code (`YER`, `SAR`, `USD`) | `YER` |
| `data-theme` | `String` | Select one of 22 color themes | `dark-yellow` |
| `data-layout` | `String` | Layout type (`modal` or `inline`) | `modal` |
| `data-button-text` | `String` | Custom CTA button text | `Pay with Wallet` |
| `data-sticky-modal` | `Boolean` | Prevents closing modal when clicking outside | `true` |
| `data-block-devtools`| `Boolean` | Blocks right-click and DevTools shortcuts | `false` |

---

### Method 2: Programmatic JavaScript API

Instantiate `YemenPay` dynamically with event callbacks:

```javascript
const pay = new YemenPay({
  merchantId: 'YOUR_MERCHANT_ID',
  amount: 15000,
  currency: 'YER',
  theme: 'dark-yellow',
  layout: 'modal',
  sticky: true,
  blockDevTools: true,

  // Callbacks
  onOpen: () => {
    console.log('Payment modal opened');
  },
  onClose: () => {
    console.log('Payment modal closed');
  },
  onStepChange: (step) => {
    console.log('Current step:', step);
  },
  onError: (error) => {
    console.error(`Validation Error in [${error.field}]:`, error.message);
  },
  onSuccess: (details) => {
    console.log('Payment verified successfully! Transaction ID:', details.paymentId);
    // Add logic to clear shopping cart or update order status
  },
  onFailed: (details) => {
    console.warn('Payment failed or redirected to manual support:', details.paymentId);
  }
});

// Open payment modal programmatically
pay.open();

// Dynamically update payment amount (e.g. when cart quantity changes)
pay.updateAmount(20000);
```

---

## 📢 Global Event Listeners

If using HTML data attributes for automatic initialization, listen for global events on `document`:

```javascript
// 1. Success Event
document.addEventListener('yemenpay:success', function (event) {
  const details = event.detail;
  console.log('Payment ID:', details.paymentId);
  console.log('Wallet Used:', details.wallet);
});

// 2. Failure Event
document.addEventListener('yemenpay:failed', function (event) {
  console.warn('Payment failed:', event.detail.paymentId);
});

// 3. Update default instance payment amount
window.YemenPay.updateAmount(25000);
```

---

## 🛡 Anti-Tampering & Security

To prevent users from opening browser DevTools and modifying price attributes (`data-amount`), YemenPay provides dual-layer security:

### 1. DevTools Blocker
Blocks right-click and common inspection shortcuts (`F12`, `Ctrl+Shift+I`, `Ctrl+Shift+C`):
- HTML: `data-block-devtools="true"`
- JS: `blockDevTools: true`

### 2. Server-Side Price Crawling
The backend server validates the payment price directly against your server's product URL:
- `productInfo`: Passed as `URL : Quantity` (e.g., `/product/12 : 2`).
- The payment engine crawls the product URL and reads the official price from the HTTP Header `yemenpay-value: 10000` or Meta tag `<meta name="yemenpay-value" content="10000">`.
- **Encrypted Discount Signatures**: Discount codes must include a cryptographic signature generated via `SHA256(discount_rate + merchant_secret)` to prevent invalid discount attempts.

---

## 🧪 Testing & Simulation

Use the following test keywords in the sender field during Step 1 of checkout to simulate payment states:

| Test Keyword | Result |
| :--- | :--- |
| `success` | Instantly completes and verifies the transaction |
| `fail` or `error` | Triggers immediate failure & displays manual WhatsApp support |
| *Any other name* | Runs full 60s countdown simulation with 80% auto-success rate |

---

## 📄 License

Copyright © 2026 YemenPay. All rights reserved.

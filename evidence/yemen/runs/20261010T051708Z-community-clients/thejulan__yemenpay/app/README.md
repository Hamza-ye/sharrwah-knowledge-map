# YemenPay Mobile App 📱

A modern, secure Flutter application for YemenPay merchants and administrators to manage digital wallet transactions, track business analytics, handle real-time verification, and monitor payment gateways across Yemen.

---

## 🚀 Features

- **Merchant Dashboard**: Real-time stats on total sales, successful transactions, automated payouts, and active wallet gateways.
- **Transaction Management**: Search, filter, and inspect detailed digital wallet transactions (Jaib, Jawaly, Kuraimi, OneCash, Yemen Wallet, etc.).
- **System Admin Controls**: Full management for system administrators to view merchant activity, update system versions, and manage access keys.
- **AES-256 Security & Payload Encryption**: End-to-end payload encryption using AES-256-CBC for all sensitive communication.
- **Biometric & OTP Security**: Secure session authentication and quick unlock options.
- **Multi-Language & Theme Support**: Built-in support for Arabic & English (RTL/LTR) with Dark and Light mode themes.
- **Real-Time Push Notifications**: Instant alerts for transaction completions, payouts, and security events.

---

## 🛠 Tech Stack

- **Framework**: [Flutter](https://flutter.dev/) (Dart)
- **State Management**: Provider / Stateful Architecture
- **Encryption**: AES-256-CBC & SHA-256 derivation via `crypto`
- **Networking**: `http` / REST API with custom secure headers (`Merchant-Id`, `Secret-Key`)
- **Icons**: Phosphor Icons (`phosphor_flutter`)

---

## 📋 Prerequisites

Before running the application, make sure you have installed:

- **Flutter SDK**: `>=3.0.0`
- **Dart SDK**: `>=3.0.0`
- **Android Studio / Xcode** (for device simulators)
- **Java Development Kit (JDK)**: `17+`

---

## 💻 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/sama-yemen/yemenpay.git
cd yemenpay/app
```

### 2. Install Dependencies
```bash
flutter pub get
```

### 3. Run the App
To run in debug mode on an attached device or emulator:
```bash
flutter run
```

---

## 📦 Building for Production

### Android (APK / App Bundle)
To build a release APK:
```bash
flutter build apk --release
```

To build an Android App Bundle (AAB):
```bash
flutter build appbundle --release
```

### iOS
```bash
flutter build ios --release
```

---

## 🔒 Security Overview

- **No Hardcoded Keys**: All API secrets are loaded dynamically and stored in encrypted local storage.
- **API Payload Encryption**: Request bodies are encrypted on the client side using AES-256-CBC and decrypted by the backend server.
- **Anti-Tampering Checks**: Package integrity and checksum validation ensure the app binaries cannot be modified.

---

## 📄 License

Copyright © 2026 YemenPay. All rights reserved.

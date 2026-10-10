/**
 * YemenPay — Yemeni Digital Wallet Payment SDK
 * Version: 1.1.0 (2026 Enhanced Edition)
 */

(function () {
  'use strict';

  // 1. Image Links for Digital Wallets
  const WalletLogos = {
    jaib: '/assets/images/wallets/jaib.png',
    jawaly: '/assets/images/wallets/jawaly.png',
    kuraimi: '/assets/images/wallets/kuraimi.png',
    one_cash: '/assets/images/wallets/one-cash.png',
    yemen_wallet: '/assets/images/wallets/yemen-wallet.png',
    mobile_money: '/assets/images/wallets/mobile-money.png'
  };

  const WalletNames = {
    jaib: 'جيب',
    jawaly: 'جوالي',
    kuraimi: 'كريمي',
    one_cash: 'ون كاش',
    yemen_wallet: 'يمن والت',
    mobile_money: 'موبايل موني'
  };

  const CityNames = {
    sanaa: 'صنعاء',
    aden: 'عدن',
    taiz: 'تعز',
    ibb: 'إب',
    hodeidah: 'الحديدة',
    hadhramaut: 'حضرموت',
    dhamar: 'ذمار',
    marib: 'مأرب',
    amran: 'عمران',
    lahj: 'لحج',
    abyan: 'أبين',
    shabwah: 'شبوة',
    al_jawf: 'الجوف',
    al_mahrah: 'المهرة',
    al_mahwit: 'المحويت',
    raymah: 'ريمة',
    hajjah: 'حجة',
    al_bayda: 'البيضاء',
    ad_dali: 'الضالع',
    socotra: 'سقطرى',
    saada: 'صعدة'
  };

  // 2. Definitive list of +20 custom color themes
  const YemenpayThemes = {
    'dark': {
      primary: '#0ea5e9', primaryHover: '#0284c7', bg: '#0f172a', cardBg: 'rgba(30, 41, 59, 0.95)',
      border: 'rgba(51, 65, 85, 0.5)', text: '#f8fafc', textMuted: '#94a3b8', inputBg: '#1e293b'
    },
    'light': {
      primary: '#0ea5e9', primaryHover: '#0284c7', bg: '#f8fafc', cardBg: '#ffffff',
      border: '#e2e8f0', text: '#0f172a', textMuted: '#64748b', inputBg: '#f1f5f9'
    },
    'dark-blue': {
      primary: '#2563eb', primaryHover: '#1d4ed8', bg: '#0b1329', cardBg: '#111b35',
      border: '#1e2d54', text: '#f8fafc', textMuted: '#8ba2d0', inputBg: '#182547'
    },
    'light-blue': {
      primary: '#2563eb', primaryHover: '#1d4ed8', bg: '#f0f4f8', cardBg: '#ffffff',
      border: '#d0dceb', text: '#0f172a', textMuted: '#52667a', inputBg: '#e1ebf5'
    },
    'dark-yellow': {
      primary: '#f59e0b', primaryHover: '#d97706', bg: '#171412', cardBg: '#211d1a',
      border: '#38302b', text: '#fffbeb', textMuted: '#a39285', inputBg: '#2a2521'
    },
    'light-yellow': {
      primary: '#d97706', primaryHover: '#b45309', bg: '#fefcf6', cardBg: '#fffdf9',
      border: '#f3e8c4', text: '#451a03', textMuted: '#78350f', inputBg: '#fef9e7'
    },
    'dark-green': {
      primary: '#10b981', primaryHover: '#059669', bg: '#061a14', cardBg: '#0b2920',
      border: '#153f32', text: '#f0fdf4', textMuted: '#7aa89b', inputBg: '#10352b'
    },
    'light-green': {
      primary: '#059669', primaryHover: '#047857', bg: '#f0fdf4', cardBg: '#ffffff',
      border: '#c6f6d5', text: '#064e3b', textMuted: '#1b805c', inputBg: '#e6fffa'
    },
    'dark-red': {
      primary: '#f43f5e', primaryHover: '#e11d48', bg: '#1c090e', cardBg: '#2a1017',
      border: '#441d27', text: '#fff1f2', textMuted: '#b88c97', inputBg: '#34151e'
    },
    'light-red': {
      primary: '#e11d48', primaryHover: '#be123c', bg: '#fff5f5', cardBg: '#ffffff',
      border: '#fed7d7', text: '#742a2a', textMuted: '#9b2c2c', inputBg: '#fff5f5'
    },
    'dark-purple': {
      primary: '#a855f7', primaryHover: '#9333ea', bg: '#120d1c', cardBg: '#1b1429',
      border: '#2f2249', text: '#faf5ff', textMuted: '#a290c4', inputBg: '#231a35'
    },
    'light-purple': {
      primary: '#9333ea', primaryHover: '#7e22ce', bg: '#faf5ff', cardBg: '#ffffff',
      border: '#e9d5ff', text: '#3b0764', textMuted: '#6b21a8', inputBg: '#f3e8ff'
    },
    'dark-teal': {
      primary: '#14b8a6', primaryHover: '#0d9488', bg: '#081717', cardBg: '#0f2424',
      border: '#1a3c3c', text: '#f0fdfa', textMuted: '#80a8a8', inputBg: '#142f2f'
    },
    'light-teal': {
      primary: '#0d9488', primaryHover: '#0f766e', bg: '#f0fdfa', cardBg: '#ffffff',
      border: '#ccfbf1', text: '#115e59', textMuted: '#134e4a', inputBg: '#e6fffa'
    },
    'dark-orange': {
      primary: '#f97316', primaryHover: '#ea580c', bg: '#1c120c', cardBg: '#271b12',
      border: '#412d1e', text: '#fff7ed', textMuted: '#b89982', inputBg: '#322317'
    },
    'light-orange': {
      primary: '#ea580c', primaryHover: '#ca8a04', bg: '#fff7ed', cardBg: '#ffffff',
      border: '#ffedd5', text: '#7c2d12', textMuted: '#9a3412', inputBg: '#fff7ed'
    },
    'dark-cyber': {
      primary: '#00ff66', primaryHover: '#00cc52', bg: '#000000', cardBg: '#0b0b0b',
      border: '#00ff66', text: '#00ff66', textMuted: '#33cc66', inputBg: '#141414'
    },
    'dark-gold': {
      primary: '#d4af37', primaryHover: '#aa8c2c', bg: '#0d0d0d', cardBg: '#1a1a1a',
      border: '#333333', text: '#f3e5ab', textMuted: '#c5b358', inputBg: '#262626'
    },
    'light-gold': {
      primary: '#aa8c2c', primaryHover: '#8c7324', bg: '#faf7f0', cardBg: '#ffffff',
      border: '#e8e2d0', text: '#5c4d1a', textMuted: '#7c6824', inputBg: '#f3eedc'
    },
    'dark-nord': {
      primary: '#88c0d0', primaryHover: '#81a1c1', bg: '#2e3440', cardBg: '#3b4252',
      border: '#4c566a', text: '#eceff4', textMuted: '#d8dee9', inputBg: '#434c5e'
    },
    'light-nord': {
      primary: '#5e81ac', primaryHover: '#81a1c1', bg: '#eceff4', cardBg: '#ffffff',
      border: '#d8dee9', text: '#2e3440', textMuted: '#4c566a', inputBg: '#e5e9f0'
    },
    'dark-crimson': {
      primary: '#ef4444', primaryHover: '#b91c1c', bg: '#180a0a', cardBg: '#241010',
      border: '#3f1a1a', text: '#fee2e2', textMuted: '#b97a7a', inputBg: '#2e1515'
    }
  };

  // Helper to load CSS dynamically
  function loadStylesheet() {
    const scriptTag = document.querySelector('script[src*="yemenpay.js"]');
    let cssUrl = 'yemenpay.css';
    if (scriptTag) {
      const src = scriptTag.getAttribute('src');
      cssUrl = src.replace('.js', '.css');
    }
    if (!document.querySelector(`link[href="${cssUrl}"]`)) {
      const link = document.createElement('link');
      link.rel = 'stylesheet';
      link.type = 'text/css';
      link.href = cssUrl;
      document.head.appendChild(link);
    }
  }

  // Load Phosphor Icons if not present
  function loadPhosphorIcons() {
    if (!document.querySelector('link[href*="phosphor-icons"]')) {
      const link = document.createElement('link');
      link.rel = 'stylesheet';
      link.type = 'text/css';
      link.href = 'https://cdn.jsdelivr.net/npm/@phosphor-icons/web@2.1.2/src/regular/style.css';
      document.head.appendChild(link);
    }
  }

  // YemenPay Class
  class YemenPay {
    constructor(options = {}) {
      this.initialized = false;
      this.config = {
        merchantId: 'yemenpay',
        clientId: '',
        amount: '0',
        currency: 'YER',
        theme: 'light-blue',
        layout: 'inline', // 'modal' or 'inline'
        buttonText: 'الدفع بإستخدام المحافظ الإلكترونية',
        locationEnabled: false,
        deliveryCities: 'all',
        sticky: false,
        onSuccess: null,
        onFailed: null,
        onError: null,
        onOpen: null,
        onClose: null,
        onStepChange: null,
        container: null,
        blockDevTools: false,
        productInfo: '',
        couponCode: '',
        couponEnc: '',
        arNum: true
      };
      
      this.merchantData = null;
      this.currentStep = 1;
      this.selectedWallet = null;
      this.senderName = '';
      this.senderPhone = '';
      this.selectedCity = '';
      this.addressDetails = '';
      this.paymentId = '';
      this.timerInterval = null;
      
      this.containerDiv = null;
      this.modalElement = null; // Backdrop or the embedded outer wrapper

      // If options are provided, initialize immediately
      if (Object.keys(options).length > 0) {
        this.init(options);
      }
    }

    init(options = {}) {
      if (this.initialized) return;

      // Merge dynamic options
      this.config = { ...this.config, ...options };

      // Detect container (either via options.container or defaulting to ID/selector)
      let container = null;
      if (this.config.container) {
        if (typeof this.config.container === 'string') {
          container = document.querySelector(this.config.container);
        } else if (this.config.container.nodeType) {
          container = this.config.container;
        }
      }
      
      if (!container) {
        container = document.getElementById('yemenpay-root') || document.querySelector('[data-yemenpay]');
      }

      if (container) {
        this.containerDiv = container;
        // Only load data attributes if not explicitly passed in options
        if (!options.merchantId) this.config.merchantId = container.getAttribute('data-merchant-id') || this.config.merchantId;
        if (!options.clientId) this.config.clientId = container.getAttribute('data-client-id') || this.config.clientId;
        if (!options.amount) this.config.amount = container.getAttribute('data-amount') || this.config.amount;
        if (!options.currency) this.config.currency = container.getAttribute('data-currency') || this.config.currency;
        if (!options.theme) this.config.theme = container.getAttribute('data-theme') || this.config.theme;
        if (!options.layout) this.config.layout = container.getAttribute('data-layout') || this.config.layout;
        if (!options.buttonText) this.config.buttonText = container.getAttribute('data-button-text') || this.config.buttonText;
        if (!options.locationEnabled && container.hasAttribute('data-location-enabled')) {
          this.config.locationEnabled = container.getAttribute('data-location-enabled') === 'true';
        }
        if (!options.deliveryCities) this.config.deliveryCities = container.getAttribute('data-delivery-cities') || this.config.deliveryCities;
        if (!options.sticky && container.hasAttribute('data-sticky-modal')) {
          this.config.sticky = container.getAttribute('data-sticky-modal') === 'true';
        }
        if (!options.blockDevTools && container.hasAttribute('data-block-devtools')) {
          this.config.blockDevTools = container.getAttribute('data-block-devtools') === 'true';
        }
        if (!options.productInfo) this.config.productInfo = container.getAttribute('data-product-info') || this.config.productInfo;
        if (!options.couponCode) this.config.couponCode = container.getAttribute('data-coupon-code') || this.config.couponCode;
        if (!options.couponEnc) this.config.couponEnc = container.getAttribute('data-coupon-enc') || this.config.couponEnc;
        if (!options.hasOwnProperty('arNum') && container.hasAttribute('data-ar-num')) {
          this.config.arNum = container.getAttribute('data-ar-num') !== 'false';
        }
      }

      if (this.config.productInfo) {
        this.config.products = [];
        const items = this.config.productInfo.split(',');
        items.forEach(item => {
          const trimmed = item.trim();
          if (trimmed) {
            const parts = trimmed.split(':');
            this.config.products.push({
              productUrl: parts[0].trim(),
              quantity: parseInt(parts[1] || '1', 10)
            });
          }
        });
        
        // Retain backwards compatibility for single product properties
        if (this.config.products.length > 0) {
          this.config.productUrl = this.config.products[0].productUrl;
          this.config.quantity = this.config.products[0].quantity;
        }
      }

      loadStylesheet();
      loadPhosphorIcons();
      
      // Render pay button only if container is available
      if (this.containerDiv) {
        this.renderPayButton();
        this.fetchMerchantDetails().catch(() => {});
      }
      this.setupDevToolsBlocker();
      this.initialized = true;
    }

    open() {
      if (!this.initialized) {
        this.init();
      }
      return this.handleTriggerClick();
    }

    close() {
      return this.cancelWizard();
    }

    setupDevToolsBlocker() {
      if (!this.config.blockDevTools) return;

      // Disable right-click context menu
      document.addEventListener('contextmenu', (e) => {
        e.preventDefault();
      });

      // Disable keyboard shortcuts for inspector/devtools
      document.addEventListener('keydown', (e) => {
        // F12
        if (e.key === 'F12') {
          e.preventDefault();
          return false;
        }
        // Ctrl+Shift+I, Ctrl+Shift+J, Ctrl+Shift+C
        if (e.ctrlKey && e.shiftKey && (e.key === 'I' || e.key === 'J' || e.key === 'C')) {
          e.preventDefault();
          return false;
        }
        // Ctrl+U (view source)
        if (e.ctrlKey && e.key === 'u') {
          e.preventDefault();
          return false;
        }
      });
    }

    updateAmount(amount) {
      this.config.amount = amount;
      if (this.containerDiv) {
        this.containerDiv.setAttribute('data-amount', amount);
      }
      const priceText = document.querySelectorAll('.yemenpay-price-value');
      priceText.forEach(el => {
        el.innerText = this.formatPrice(amount, this.config.currency);
      });
    }

    updateCouponEnc(couponEnc) {
      this.config.couponEnc = couponEnc;
      if (this.containerDiv) {
        this.containerDiv.setAttribute('data-coupon-enc', couponEnc);
      }
    }

    updateCouponCode(couponCode) {
      this.config.couponCode = couponCode;
      if (this.containerDiv) {
        this.containerDiv.setAttribute('data-coupon-code', couponCode);
      }
    }

    formatPrice(amount, currency) {
      let formattedAmount = parseFloat(amount).toLocaleString(this.config.arNum ? 'ar-YE' : 'en-US');
      let currencySymbol = 'ر.ي';
      if (currency === 'SAR') currencySymbol = 'ر.س';
      if (currency === 'USD') currencySymbol = '$';
      return `${formattedAmount} ${currencySymbol}`;
    }

    renderPayButton() {
      if (!this.containerDiv) return;
      this.containerDiv.innerHTML = '';
      
      // Inject theme styles into containerDiv so trigger button has access to custom tooltips
      this.containerDiv.setAttribute('style', this.getThemeStyleString());
      
      const button = document.createElement('button');
      button.className = 'yemenpay-trigger-btn';
      
      const themeColors = YemenpayThemes[this.config.theme] || YemenpayThemes['dark'];
      
      const styleId = 'yemenpay-button-global-styles';
      if (!document.getElementById(styleId)) {
        const style = document.createElement('style');
        style.id = styleId;
        style.textContent = `
          .yemenpay-trigger-btn {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 12px;
            background: linear-gradient(135deg, var(--btn-primary, #0ea5e9) 0%, var(--btn-primary-hover, #0284c7) 50%, var(--btn-primary, #0ea5e9) 100%);
            background-size: 200% auto;
            background-position: right center;
            color: #ffffff;
            border: none;
            padding: 14px 28px;
            border-radius: 14px;
            font-family: 'Noto Kufi Arabic', system-ui, -apple-system, sans-serif;
            font-size: 16px;
            font-weight: 700;
            cursor: pointer;
            transition: background-position 0.4s ease, transform 0.3s ease, box-shadow 0.3s ease;
            box-shadow: 0 4px 15px rgba(14, 165, 233, 0.2);
            direction: rtl;
            width: 100%;
            position: relative;
          }
          .yemenpay-trigger-btn:hover {
            background-position: left center;
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(14, 165, 233, 0.3);
          }
          .yemenpay-trigger-btn:active {
            transform: translateY(0);
          }
          .yemenpay-btn-wallets-pile {
            display: flex;
            align-items: center;
            flex-direction: row-reverse;
          }
          .yemenpay-pile-avatar {
            width: 24px;
            height: 24px;
            border-radius: 50%;
            background: #ffffff;
            border: 1.5px solid #ffffff;
            overflow: visible;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-right: -8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.15);
            transition: transform 0.2s ease;
            position: relative;
          }
          .yemenpay-pile-avatar:hover {
            transform: scale(1.2) translateY(-2px);
            z-index: 10 !important;
          }
          .yemenpay-pile-avatar svg,
          .yemenpay-pile-avatar img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            border-radius: 50%;
          }
        `;
        document.head.appendChild(style);
      }

      button.style.setProperty('--btn-primary', themeColors.primary);
      button.style.setProperty('--btn-primary-hover', themeColors.primaryHover);
      button.innerHTML = `
        <div class="yemenpay-btn-wallets-pile">
          <div class="yemenpay-pile-avatar" data-tooltip="يمن والت" data-tooltip-pos="top" style="z-index: 1;"><img src="${WalletLogos.yemen_wallet}" alt="يمن والت"></div>
          <div class="yemenpay-pile-avatar" data-tooltip="ون كاش" data-tooltip-pos="top" style="z-index: 3;"><img src="${WalletLogos.one_cash}" alt="ون كاش"></div>
          <div class="yemenpay-pile-avatar" data-tooltip="موبايل موني" data-tooltip-pos="top" style="z-index: 2;"><img src="${WalletLogos.mobile_money}" alt="موبايل موني"></div>
          <div class="yemenpay-pile-avatar" data-tooltip="جوالي" data-tooltip-pos="top" style="z-index: 4;"><img src="${WalletLogos.jawaly}" alt="جوالي"></div>
          <div class="yemenpay-pile-avatar" data-tooltip="جيب" data-tooltip-pos="top" style="z-index: 5;"><img src="${WalletLogos.jaib}" alt="جيب"></div>
          <div class="yemenpay-pile-avatar" data-tooltip="كريمي" data-tooltip-pos="top" style="z-index: 6;"><img src="${WalletLogos.kuraimi}" alt="كريمي"></div>
        </div>
        <span>${this.isExpired ? 'بإنتظار تجديد الإشتراك' : this.config.buttonText}</span>
      `;
      if (this.isExpired) {
        button.disabled = true;
        button.style.opacity = '0.6';
        button.style.cursor = 'not-allowed';
      } else {
        button.addEventListener('click', () => this.handleTriggerClick());
      }
      this.containerDiv.appendChild(button);
    }

    async handleTriggerClick() {
      try {
        await this.fetchMerchantDetails();
        
        if (typeof this.config.onOpen === 'function') {
          this.config.onOpen();
        }

        if (this.config.layout === 'inline') {
          // Render inside the merchant div directly (inline layout)
          this.buildInlineHTML();
        } else {
          // Render as full-screen modal (default layout)
          this.buildModalHTML();
          setTimeout(() => {
            this.modalElement.classList.add('yemenpay-open');
          }, 10);
        }
      } catch (err) {
        if (typeof this.config.onError === 'function') {
          this.config.onError({ field: 'network', message: err.message || 'فشل في الاتصال بالخادم.' });
        } else {
          alert('فشل في الاتصال بالخادم. يرجى المحقق من الاتصال بالإنترنت.');
        }
        console.error(err);
      }
    }

    // Fetch merchant details from Flask API using merchantId, with safe default fallback
    fetchMerchantDetails() {
      let url = `https://api.yemenpay.app/api/merchant-details/${encodeURIComponent(this.config.merchantId)}`;
      if (window.location.port === '5000') {
        url = `/api/merchant-details/${encodeURIComponent(this.config.merchantId)}`;
      }

      return fetch(url)
        .then(async res => {
          if (!res.ok) {
            try {
              const errData = await res.json();
              if (errData.error === 'subscription_expired') {
                this.isExpired = true;
                if (this.containerDiv) this.renderPayButton();
                throw new Error('subscription_expired');
              }
            } catch(e) {
                if (e.message === 'subscription_expired') throw e;
            }
            throw new Error('Network response was not ok');
          }
          return res.json();
        })
        .then(data => {
          if (data && data.status === 'success') {
            this.merchantData = {
              merchantName: data.merchantName,
              contact_info: data.contact_info || {},
              accounts: data.accounts
            };
          } else {
            throw new Error('Invalid merchant data status');
          }
          return this.merchantData;
        })
        .catch(err => {
          if (err.message === 'subscription_expired') throw err;
          console.warn('Failed to load merchant data from API, using fallback:', err);
          this.merchantData = {
            merchantName: "يمن باي التجريبي",
            contact_info: {
              whatsapp: "+967775982124",
              email: "payments@yemenpay.app",
              telegram: "yemenpay",
              facebook: "yemenpay.fb"
            },
            accounts: {
              jaib: { YER: "775982124" },
              jawaly: { YER: "788910234" },
              kuraimi: { YER: "30294812", USD: "30294812" },
              one_cash: { YER: "771234567" },
              mobile_money: { YER: "776543210" },
              yemen_wallet: { YER: "715890123" }
            }
          };
          return this.merchantData;
        });
    }

    // Generate dynamic inline style text based on selected theme
    getThemeStyleString() {
      const colors = YemenpayThemes[this.config.theme] || YemenpayThemes['dark'];
      return `
        --yemenpay-primary: ${colors.primary};
        --yemenpay-primary-hover: ${colors.primaryHover};
        --yemenpay-bg: ${colors.bg};
        --yemenpay-card-bg: ${colors.cardBg};
        --yemenpay-border: ${colors.border};
        --yemenpay-text: ${colors.text};
        --yemenpay-text-muted: ${colors.textMuted};
        --yemenpay-input-bg: ${colors.inputBg};
      `;
    }

    // Injects the wizard inline directly inside the [data-yemenpay] div
    buildInlineHTML() {
      this.containerDiv.innerHTML = '';
      
      const wrapper = document.createElement('div');
      wrapper.className = 'yemenpay-inline-container';
      wrapper.setAttribute('style', this.getThemeStyleString());
      
      wrapper.innerHTML = this.getWizardTemplateHTML(true);
      
      this.containerDiv.appendChild(wrapper);
      this.modalElement = wrapper; // Save reference for event selections

      this.setupModalEvents();
      this.renderCurrentStep();
    }

    // Injects as a modal backdrop
    buildModalHTML() {
      const existing = document.getElementById('yemenpay-payment-modal');
      if (existing) existing.remove();

      const modal = document.createElement('div');
      modal.id = 'yemenpay-payment-modal';
      modal.className = `yemenpay-modal-backdrop`;
      
      modal.innerHTML = `
        <div class="yemenpay-modal-container" style="${this.getThemeStyleString()}">
          ${this.getWizardTemplateHTML(false)}
        </div>
      `;

      document.body.appendChild(modal);
      this.modalElement = modal;

      this.setupModalEvents();
      this.renderCurrentStep();
    }

    // Shared inner HTML template for both modal and inline layout
    getWizardTemplateHTML(isInline) {
      let walletsHtml = '';
      const currency = this.config.currency;
      
      for (const [walletId, accountData] of Object.entries(this.merchantData.accounts)) {
        let hasCurrency = false;
        if (typeof accountData === 'object' && (accountData[currency] || accountData['ALL'])) {
          hasCurrency = true;
        } else if (typeof accountData === 'string' && currency === 'YER') {
          hasCurrency = true; // fallback
        }
        
        if (hasCurrency && WalletNames[walletId]) {
          walletsHtml += `
            <div class="yemenpay-wallet-card" data-wallet="${walletId}" data-tooltip="${WalletNames[walletId]}">
              <img src="${WalletLogos[walletId]}" class="yemenpay-wallet-logo" alt="${WalletNames[walletId]}">
            </div>
          `;
        }
      }
      
      if (walletsHtml === '') {
        walletsHtml = `<div class="yemenpay-error-msg" style="display:block;"><i class="ph ph-warning-circle"></i> لا توجد محافظ متاحة لعملة ${currency}.</div>`;
      }

      return `
        <!-- Header -->
        <div class="yemenpay-header">
          <div class="yemenpay-title-area">
            <h3 class="yemenpay-title">بوابة الدفع الإلكتروني</h3>
            <p class="yemenpay-subtitle">الدفع الآمن باستخدام المحافظ اليمنية</p>
          </div>
          <button class="yemenpay-close-btn" id="yemenpay-close-btn">
            <i class="ph ph-x"></i>
          </button>
        </div>

        <!-- Progress Bar -->
        <div class="yemenpay-steps-bar">
          <div class="yemenpay-steps-progress" id="yemenpay-progress-line"></div>
          <div class="yemenpay-step-dot active" id="dot-step-1">١</div>
          <div class="yemenpay-step-dot" id="dot-step-2">٢</div>
          <div class="yemenpay-step-dot" id="dot-step-3">٣</div>
        </div>

        <!-- Wizard Pages Container -->
        <div class="yemenpay-wizard-content">
          
          <!-- STEP 1: Select Wallet & User Info (Circular Wallets, No text) -->
          <div class="yemenpay-step-panel active" id="step-panel-1">
            <div class="yemenpay-form-group">
              <label class="yemenpay-label">اختر المحفظة الرقمية:</label>
              <div class="yemenpay-wallet-grid">
                ${walletsHtml}
              </div>
              <div class="yemenpay-error-msg" id="error-wallet">
                <i class="ph ph-warning-circle"></i> يرجى اختيار محفظة دفع رقمية.
              </div>
            </div>

            <div class="yemenpay-form-group">
              <label class="yemenpay-label" for="yemenpay-input-phone">رقم هاتف المحفظة الرقمية:</label>
              <div class="yemenpay-input-wrapper">
                <i class="ph ph-phone yemenpay-input-icon"></i>
                <input type="tel" id="yemenpay-input-phone" class="yemenpay-input" placeholder="7xxxxxxxx" value="${this.senderPhone}" style="direction: ltr; text-align: right; padding-right: 42px;">
              </div>
              <div class="yemenpay-error-msg" id="error-phone">
                <i class="ph ph-warning-circle"></i> يرجى إدخال رقم هاتف صحيح (9 أرقام يبدأ بـ 77، 78، 73، 71، 70).
              </div>
            </div>
          </div>

          <!-- STEP 2: Delivery Location Details -->
          <div class="yemenpay-step-panel" id="step-panel-2">
            <div style="text-align: center; margin-bottom: 6px;">
              <i class="ph ph-map-pin" style="font-size: 32px; color: var(--yemenpay-primary);"></i>
              <h4 class="yemenpay-step-title">عنوان التوصيل والشحن</h4>
              <p style="font-size: 12px; color: var(--yemenpay-text-muted); line-height: 1.5; margin: 0;">
                يرجى تحديد المدينة وإدخال تفاصيل العنوان لإيصال الطلب إليك.
              </p>
            </div>

            <div class="yemenpay-form-group">
              <label class="yemenpay-label">المدينة:</label>
              <div class="yemenpay-custom-select" id="yemenpay-city-select-container">
                <div class="yemenpay-select-trigger" id="yemenpay-city-select-trigger">
                  <span id="yemenpay-selected-city-text">اختر المدينة للتوصيل...</span>
                  <i class="ph ph-caret-down"></i>
                </div>
                <div class="yemenpay-select-options" id="yemenpay-city-select-options">
                  <!-- Injected dynamically based on configuration -->
                </div>
              </div>
              <input type="hidden" id="yemenpay-input-city" value="${this.selectedCity}">
              <div class="yemenpay-error-msg" id="error-city">
                <i class="ph ph-warning-circle"></i> يرجى اختيار مدينة التوصيل.
              </div>
            </div>

            <div class="yemenpay-form-group">
              <label class="yemenpay-label" for="yemenpay-input-address-details">العنوان بالتفصيل (الشارع، الحي، المعالم البارزة):</label>
              <div class="yemenpay-input-wrapper">
                <textarea id="yemenpay-input-address-details" class="yemenpay-input" rows="3" placeholder="مثال: شارع حدة، خلف مركز الكميم، عمارة الأمل، شقة ٤" style="resize: none; padding: 12px 14px; line-height: 1.5;">${this.addressDetails}</textarea>
              </div>
              <div class="yemenpay-error-msg" id="error-address-details">
                <i class="ph ph-warning-circle"></i> يرجى كتابة تفاصيل العنوان بالتفصيل.
              </div>
            </div>
          </div>

          <!-- STEP 3: Confirm & Trigger Verification + Copy button for price -->
          <div class="yemenpay-step-panel" id="step-panel-3">
            <div style="text-align: center; margin-bottom: 10px;">
              <i class="ph ph-info" style="font-size: 32px; color: var(--yemenpay-primary);"></i>
              <h4 class="yemenpay-step-title">قم بالتحويل الآن</h4>
              <p style="font-size: 12px; color: var(--yemenpay-text-muted); line-height: 1.5; margin: 0;">
                يرجى تحويل المبلغ المطلوب من تطبيق محفظتك إلى حساب التاجر الموضح، ثم اضغط على زر التحقق أدناه.
              </p>
            </div>

            <div class="yemenpay-info-box">
              <!-- Left Column: Payment & Location Info -->
              <div class="yemenpay-info-column-left" style="display: flex; flex-direction: column; width: 100%; min-width: 0;">
                <!-- Section 1: Payment Info -->
                <div class="yemenpay-info-section" id="summary-payment-section" style="position: relative; margin-bottom: 8px; padding-bottom: 12px; border-bottom: 1px dashed var(--yemenpay-border);">
                  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px; padding-bottom: 4px;">
                    <span class="yemenpay-section-title" style="margin-bottom: 0; padding-bottom: 0;">بيانات الدفع</span>
                    <button class="yemenpay-edit-btn" id="btn-edit-step3-payment" style="margin-top: 0; padding: 4px 8px; font-size: 10px; display: inline-flex; align-items: center; gap: 4px;" data-tooltip="تعديل بيانات الدفع">
                      <i class="ph ph-pencil-simple"></i> تعديل الدفع
                    </button>
                  </div>
                  <div class="yemenpay-info-row">
                    <span class="yemenpay-info-label">المحفظة:</span>
                    <span class="yemenpay-info-value" id="summary-wallet-name">-</span>
                  </div>
                  <div class="yemenpay-info-row" style="margin-top: 6px;">
                    <span class="yemenpay-info-label">رقم المرسل:</span>
                    <span class="yemenpay-info-value" id="summary-sender-info" style="direction: ltr;">-</span>
                  </div>
                </div>

                <!-- Section 2: Location Info (Only visible if locationEnabled is true) -->
                <div class="yemenpay-info-section" id="summary-location-section" style="position: relative; margin-bottom: 8px; padding-bottom: 12px; border-bottom: 1px dashed var(--yemenpay-border); display: none;">
                  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px; padding-bottom: 4px;">
                    <span class="yemenpay-section-title" style="margin-bottom: 0; padding-bottom: 0;">عنوان التوصيل</span>
                    <button class="yemenpay-edit-btn" id="btn-edit-step3-location" style="margin-top: 0; padding: 4px 8px; font-size: 10px; display: inline-flex; align-items: center; gap: 4px;" data-tooltip="تعديل العنوان">
                      <i class="ph ph-pencil-simple"></i> تعديل العنوان
                    </button>
                  </div>
                  <div class="yemenpay-info-row" style="align-items: center; gap: 8px;">
                    <span class="yemenpay-info-label" style="white-space: nowrap; flex-shrink: 0;">العنوان:</span>
                    <span class="yemenpay-info-value" id="summary-location-info" style="font-size: 12px; display: block; overflow: hidden; white-space: nowrap; text-overflow: ellipsis; text-align: right; direction: rtl; flex: 1; min-width: 0;">-</span>
                  </div>
                </div>
              </div>

              <!-- Right Column: Required Transfer Details -->
              <div class="yemenpay-info-column-right" style="display: flex; flex-direction: column; width: 100%; min-width: 0;">
                <div class="yemenpay-info-section">
                  <div class="yemenpay-section-title">
                    بيانات الحوالة المطلوبة
                  </div>
                  <div class="yemenpay-info-row">
                    <span class="yemenpay-info-label">التاجر المستلم:</span>
                    <div class="yemenpay-copy-wrapper">
                      <span class="yemenpay-info-value" id="summary-merchant-name" style="font-size: 13px;">-</span>
                      <button class="yemenpay-copy-btn" id="btn-copy-summary-merchant-name" data-tooltip="نسخ اسم التاجر">
                        <i class="ph ph-copy"></i>
                      </button>
                    </div>
                  </div>
                  <div class="yemenpay-info-row">
                    <span class="yemenpay-info-label">حساب التاجر:</span>
                    <div class="yemenpay-copy-wrapper">
                      <span class="yemenpay-info-value" id="summary-merchant-account" style="font-family: monospace; font-size: 13px; font-weight: 700;">-</span>
                      <button class="yemenpay-copy-btn" id="btn-copy-summary-merchant-account" data-tooltip="نسخ حساب التاجر">
                        <i class="ph ph-copy"></i>
                      </button>
                    </div>
                  </div>
                  <div class="yemenpay-info-row" style="border-top: 1px dashed var(--yemenpay-border); padding-top: 10px; margin-top: 10px;">
                    <span class="yemenpay-info-label">المبلغ المطلوب:</span>
                    <div class="yemenpay-copy-wrapper">
                      <span id="summary-amount" style="font-weight: 700; color: var(--yemenpay-primary); font-size: 15px;">-</span>
                      <button class="yemenpay-copy-btn" id="btn-copy-amount" data-tooltip="نسخ المبلغ">
                        <i class="ph ph-copy"></i>
                      </button>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- LOADER PAGE (60s countdown) -->
          <div class="yemenpay-step-panel" id="step-panel-loader">
            <div class="yemenpay-loader-container">
              <div class="yemenpay-circular-progress">
                <svg class="yemenpay-progress-svg" viewBox="0 0 100 100" width="100" height="100">
                  <circle class="yemenpay-progress-circle-bg" cx="50" cy="50" r="46" />
                  <circle class="yemenpay-progress-circle-val" id="yemenpay-progress-circle" cx="50" cy="50" r="46" />
                </svg>
                <div class="yemenpay-timer-text" id="yemenpay-timer-countdown">60</div>
              </div>
              <div>
                <h4 class="yemenpay-loader-title">جاري التحقق من عملية التحويل...</h4>
                <p class="yemenpay-loader-subtitle">يرجى عدم مغادرة الصفحة. نقوم بالتحقق التلقائي من الحوالة حالياً.</p>
              </div>
            </div>
          </div>

          <!-- RESULT SCREEN: Success -->
          <div class="yemenpay-step-panel" id="step-panel-success">
            <div class="yemenpay-status-container">
              <div class="yemenpay-status-icon success">
                <i class="ph ph-check"></i>
              </div>
              <h4 class="yemenpay-status-title">تم تأكيد الدفع بنجاح!</h4>
              <p class="yemenpay-status-desc">لقد تحققنا من الحوالة وتم تأكيد عملية الشراء. شكراً لك!</p>
              
              <div class="yemenpay-payment-id-box">
                <span class="yemenpay-payment-id-val" id="success-payment-id">-</span>
                <button class="yemenpay-copy-btn" id="btn-copy-success-id" data-tooltip="نسخ رمز العملية">
                  <i class="ph ph-copy"></i>
                </button>
              </div>
              <button class="yemenpay-btn yemenpay-btn-primary" id="btn-success-done" style="margin-top: 10px; width: 100%;">
                <i class="ph ph-check"></i> إتمام والرجوع
              </button>
            </div>
          </div>

          <!-- RESULT SCREEN: Failed -->
          <div class="yemenpay-step-panel" id="step-panel-failed">
            <div class="yemenpay-status-container">
              <div class="yemenpay-status-icon failed">
                <i class="ph ph-warning"></i>
              </div>
              <h4 class="yemenpay-status-title">فشل التحقق التلقائي</h4>
              <p class="yemenpay-status-desc">
                أموالك في أمان بالكامل! يرجى تصوير الشاشة (سناب شات/لقطة شاشة) من تطبيق المحفظة وإرسالها للتاجر لتأكيد الطلب يدوياً.
              </p>

              <div class="yemenpay-payment-id-box" style="margin-top: 0px;">
                <span style="font-size: 11px; color: var(--yemenpay-text-muted);">معرّف العملية:</span>
                <span class="yemenpay-payment-id-val" id="failed-payment-id" style="font-size: 12px;">-</span>
                <button class="yemenpay-copy-btn" id="btn-copy-failed-id" data-tooltip="نسخ رمز العملية">
                  <i class="ph ph-copy"></i>
                </button>
              </div>

              <div class="yemenpay-contact-buttons" id="yemenpay-dynamic-contacts">
                <!-- Dynamically injected contact buttons -->
              </div>
              <button class="yemenpay-btn yemenpay-btn-primary" id="btn-failed-close" style="margin-top: 10px; width: 100%;">
                <i class="ph ph-arrow-left"></i> إغلاق ومراجعة
              </button>
            </div>
          </div>

        </div>

        <!-- Footer Control Buttons -->
        <div class="yemenpay-footer" id="yemenpay-modal-footer">
          <button class="yemenpay-btn yemenpay-btn-secondary" id="yemenpay-btn-prev" style="display: none;">
            <i class="ph ph-caret-right"></i> <span>السابق</span>
          </button>
          <button class="yemenpay-btn yemenpay-btn-primary" id="yemenpay-btn-next">
            <span>التالي</span> <i class="ph ph-caret-left"></i>
          </button>
        </div>

        <!-- Copy Toast Notification -->
        <div class="yemenpay-toast" id="yemenpay-copy-toast">تم نسخ النص للحافظة!</div>

        <!-- Confirmation Exit Overlay -->
        <div class="yemenpay-confirm-overlay" id="yemenpay-exit-confirm">
          <div class="yemenpay-confirm-card">
            <i class="ph ph-warning-circle" style="font-size: 38px; color: #ef4444; margin-bottom: 10px;"></i>
            <h4 style="margin: 0 0 8px; font-size: 14px; font-weight: 700; color: var(--yemenpay-text);">تأكيد إلغاء العملية</h4>
            <p style="margin: 0 0 18px; font-size: 12px; color: var(--yemenpay-text-muted); line-height: 1.5; text-align: center;">
              هل أنت متأكد من إلغاء عملية الدفع؟ ستفقد حالة تتبع الحوالة وبيانات العملية الحالية.
            </p>
            <div style="display: flex; gap: 10px; width: 100%;">
              <button class="yemenpay-btn yemenpay-btn-secondary" id="btn-exit-cancel" style="padding: 8px 12px; font-size: 12px; flex: 1;">
                تراجع
              </button>
              <button class="yemenpay-btn yemenpay-btn-primary" id="btn-exit-confirm" style="background: #ef4444 !important; border-color: #ef4444 !important; color: #fff; padding: 8px 12px; font-size: 12px; flex: 1;">
                تأكيد الإلغاء
              </button>
            </div>
          </div>
        </div>
      `;
    }

    initializeStepsBar() {
      const dot2 = this.modalElement.querySelector('#dot-step-2');
      const dot3 = this.modalElement.querySelector('#dot-step-3');
      if (!this.config.locationEnabled) {
        if (dot2) dot2.style.display = 'none';
        if (dot3) dot3.innerText = '٢';
      } else {
        if (dot2) {
          dot2.style.display = 'flex';
          dot2.innerText = '٢';
        }
        if (dot3) {
          dot3.innerText = '٣';
        }
      }
    }

    setupModalEvents() {
      // Close/Cancel Wizard Event Handlers with Confirmation Overlay
      const closeBtn = this.modalElement.querySelector('#yemenpay-close-btn');
      const confirmOverlay = this.modalElement.querySelector('#yemenpay-exit-confirm');
      const btnExitCancel = this.modalElement.querySelector('#btn-exit-cancel');
      const btnExitConfirm = this.modalElement.querySelector('#btn-exit-confirm');

      if (closeBtn && confirmOverlay) {
        closeBtn.addEventListener('click', (e) => {
          e.preventDefault();
          confirmOverlay.classList.add('open');
        });
      }

      if (btnExitCancel && confirmOverlay) {
        btnExitCancel.addEventListener('click', (e) => {
          e.preventDefault();
          confirmOverlay.classList.remove('open');
        });
      }

      if (btnExitConfirm && confirmOverlay) {
        btnExitConfirm.addEventListener('click', (e) => {
          e.preventDefault();
          confirmOverlay.classList.remove('open');
          this.cancelWizard();
        });
      }
      
      if (this.config.layout === 'modal') {
        this.modalElement.addEventListener('click', (e) => {
          if (e.target === this.modalElement) {
            if (this.config.sticky) {
              const container = this.modalElement.querySelector('.yemenpay-modal-container');
              if (container) {
                container.classList.add('yemenpay-shake');
                setTimeout(() => {
                  container.classList.remove('yemenpay-shake');
                }, 400);
              }
            } else {
              this.cancelWizard();
            }
          }
        });
      }

      // Initialize steps bar numbering and layout
      this.initializeStepsBar();

      // Wallet Selection
      const walletCards = this.modalElement.querySelectorAll('.yemenpay-wallet-card');
      walletCards.forEach(card => {
        card.addEventListener('click', () => {
          walletCards.forEach(c => c.classList.remove('selected'));
          card.classList.add('selected');
          
          const newWallet = card.getAttribute('data-wallet');
          const oldWallet = this.selectedWallet;
          this.selectedWallet = newWallet;
          this.hideError('wallet');

          const phoneLabel = this.modalElement.querySelector('label[for="yemenpay-input-phone"]');
          const phoneInput = this.modalElement.querySelector('#yemenpay-input-phone');
          const phoneIcon = this.modalElement.querySelector('.yemenpay-input-icon');
          const phoneError = this.modalElement.querySelector('#error-phone');

          if (this.selectedWallet === 'kuraimi') {
            if (phoneLabel) phoneLabel.innerText = 'الاسم الأول و اللقب (حساب كريمي):';
            if (phoneInput) {
              if (oldWallet !== 'kuraimi') phoneInput.value = '';
              phoneInput.type = 'text';
              phoneInput.placeholder = 'مثال: أحمد الصنعاني';
              phoneInput.style.direction = 'rtl';
            }
            if (phoneIcon) phoneIcon.className = 'ph ph-user yemenpay-input-icon';
            if (phoneError) phoneError.innerHTML = '<i class="ph ph-warning-circle"></i> يرجى إدخال اسمك الأول و اللقب.';
          } else {
            if (phoneLabel) phoneLabel.innerText = 'رقم هاتف المحفظة الرقمية:';
            if (phoneInput) {
              if (oldWallet === 'kuraimi') phoneInput.value = '';
              phoneInput.type = 'tel';
              phoneInput.placeholder = '7xxxxxxxx';
              phoneInput.style.direction = 'ltr';
            }
            if (phoneIcon) phoneIcon.className = 'ph ph-phone yemenpay-input-icon';
            if (phoneError) phoneError.innerHTML = '<i class="ph ph-warning-circle"></i> يرجى إدخال رقم هاتف صحيح (9 أرقام يبدأ بـ 77، 78، 73، 71، 70).';
          }
        });
      });

      // Inputs focus / keyup validation clearing
      this.modalElement.querySelector('#yemenpay-input-phone').addEventListener('input', () => {
        this.hideError('phone');
      });

      // Custom Dropdown for City Selection (Step 2)
      const selectTrigger = this.modalElement.querySelector('#yemenpay-city-select-trigger');
      const selectOptions = this.modalElement.querySelector('#yemenpay-city-select-options');
      const hiddenCityInput = this.modalElement.querySelector('#yemenpay-input-city');
      const selectedCityText = this.modalElement.querySelector('#yemenpay-selected-city-text');

      if (selectTrigger && selectOptions) {
        // Populate cities options dynamically
        const citiesStr = this.config.deliveryCities;
        let citiesList = Object.keys(CityNames);
        if (citiesStr !== 'all') {
          citiesList = citiesStr.split(',').map(s => s.trim().toLowerCase()).filter(s => CityNames[s]);
        }

        selectOptions.innerHTML = '';
        citiesList.forEach(cityKey => {
          const optDiv = document.createElement('div');
          optDiv.className = 'yemenpay-select-option';
          optDiv.setAttribute('data-value', cityKey);
          optDiv.innerText = CityNames[cityKey];
          if (this.selectedCity === cityKey) {
            optDiv.classList.add('selected');
            selectedCityText.innerText = CityNames[cityKey];
          }

          optDiv.addEventListener('click', (e) => {
            e.stopPropagation();
            this.selectedCity = cityKey;
            hiddenCityInput.value = cityKey;
            selectedCityText.innerText = CityNames[cityKey];
            
            selectOptions.querySelectorAll('.yemenpay-select-option').forEach(opt => opt.classList.remove('selected'));
            optDiv.classList.add('selected');
            
            selectOptions.classList.remove('open');
            this.hideError('city');
          });

          selectOptions.appendChild(optDiv);
        });

        // Toggle dropdown open
        selectTrigger.addEventListener('click', (e) => {
          e.stopPropagation();
          selectOptions.classList.toggle('open');
        });

        // Close on outside click
        document.addEventListener('click', () => {
          selectOptions.classList.remove('open');
        });
      }

      // Address Details keyup / input listener (Step 2)
      const addressTextarea = this.modalElement.querySelector('#yemenpay-input-address-details');
      if (addressTextarea) {
        addressTextarea.addEventListener('input', () => {
          this.addressDetails = addressTextarea.value;
          this.hideError('address-details');
        });
      }

      // Footer Navigation buttons
      const nextBtn = this.modalElement.querySelector('#yemenpay-btn-next');
      const prevBtn = this.modalElement.querySelector('#yemenpay-btn-prev');

      nextBtn.addEventListener('click', () => this.handleNextStep());
      prevBtn.addEventListener('click', () => this.handlePrevStep());

      // Clipboard copy actions (Safely checks existence first)
      const btnCopyAccount = this.modalElement.querySelector('#btn-copy-account');
      if (btnCopyAccount) {
        btnCopyAccount.addEventListener('click', () => {
          const text = this.modalElement.querySelector('#merchant-account-display').innerText;
          this.copyToClipboard(text, btnCopyAccount);
        });
      }
      
      // Copy amount in Step 3
      const btnCopyAmount = this.modalElement.querySelector('#btn-copy-amount');
      if (btnCopyAmount) {
        btnCopyAmount.addEventListener('click', () => {
          const text = this.config.amount.toString();
          this.copyToClipboard(text, btnCopyAmount);
        });
      }

      // Copy merchant name in Step 3
      const btnCopySumMerchantName = this.modalElement.querySelector('#btn-copy-summary-merchant-name');
      if (btnCopySumMerchantName) {
        btnCopySumMerchantName.addEventListener('click', () => {
          const text = this.modalElement.querySelector('#summary-merchant-name').innerText;
          this.copyToClipboard(text, btnCopySumMerchantName);
        });
      }

      // Copy merchant account in Step 3
      const btnCopySumMerchantAccount = this.modalElement.querySelector('#btn-copy-summary-merchant-account');
      if (btnCopySumMerchantAccount) {
        btnCopySumMerchantAccount.addEventListener('click', () => {
          const text = this.modalElement.querySelector('#summary-merchant-account').innerText;
          this.copyToClipboard(text, btnCopySumMerchantAccount);
        });
      }

      const btnCopySuccessId = this.modalElement.querySelector('#btn-copy-success-id');
      if (btnCopySuccessId) {
        btnCopySuccessId.addEventListener('click', () => {
          const text = this.modalElement.querySelector('#success-payment-id').innerText;
          this.copyToClipboard(text, btnCopySuccessId);
        });
      }

      const btnCopyFailedId = this.modalElement.querySelector('#btn-copy-failed-id');
      if (btnCopyFailedId) {
        btnCopyFailedId.addEventListener('click', () => {
          const text = this.modalElement.querySelector('#failed-payment-id').innerText;
          this.copyToClipboard(text, btnCopyFailedId);
        });
      }

      // Edit Payment Button (Goes back to Step 1)
      const editPaymentBtn = this.modalElement.querySelector('#btn-edit-step3-payment');
      if (editPaymentBtn) {
        editPaymentBtn.addEventListener('click', (e) => {
          e.preventDefault();
          this.goToStep(1);
        });
      }

      // Edit Location Button (Goes back to Step 2)
      const editLocationBtn = this.modalElement.querySelector('#btn-edit-step3-location');
      if (editLocationBtn) {
        editLocationBtn.addEventListener('click', (e) => {
          e.preventDefault();
          this.goToStep(2);
        });
      }

      // Result final buttons
      const successDone = this.modalElement.querySelector('#btn-success-done');
      if (successDone) {
        successDone.addEventListener('click', () => this.cancelWizard());
      }
      
      const failedClose = this.modalElement.querySelector('#btn-failed-close');
      if (failedClose) {
        failedClose.addEventListener('click', () => this.cancelWizard());
      }
    }

    cancelWizard() {
      if (this.timerInterval) {
        clearInterval(this.timerInterval);
        this.timerInterval = null;
      }

      if (typeof this.config.onClose === 'function') {
        this.config.onClose();
      }

      const resetState = () => {
        // Reset state variables
        this.currentStep = 1;
        this.selectedWallet = null;
        this.senderPhone = '';
        this.selectedCity = '';
        this.addressDetails = '';
        this.paymentId = '';
        this.merchantContact = null;
      };

      if (this.config.layout === 'inline') {
        if (this.modalElement) {
          this.modalElement.classList.add('yemenpay-closing');
          setTimeout(() => {
            resetState();
            this.renderPayButton();
          }, 300);
        } else {
          resetState();
          this.renderPayButton();
        }
      } else {
        if (this.modalElement) {
          // Fade out modal
          this.modalElement.classList.remove('yemenpay-open');
          setTimeout(() => {
            resetState();
            if (this.modalElement) {
              this.modalElement.remove();
              this.modalElement = null;
            }
          }, 300);
        } else {
          resetState();
        }
      }
    }

    goToStep(step) {
      const currentPanel = this.modalElement.querySelector(`#step-panel-${this.currentStep === 'loader' ? 'loader' : this.currentStep}`);
      
      if (currentPanel) {
        if (step < this.currentStep) {
          currentPanel.classList.remove('active');
          currentPanel.classList.add('slide-out-left');
        } else {
          currentPanel.classList.remove('active');
        }
      }
      
      this.currentStep = step;

      if (typeof this.config.onStepChange === 'function') {
        this.config.onStepChange(step);
      }

      this.renderCurrentStep();
    }

    renderCurrentStep() {
      // Dynamically toggle wide layout class on the modal container
      const modalCont = this.modalElement.querySelector('.yemenpay-modal-container');
      if (modalCont) {
        if (this.currentStep === 3) {
          modalCont.classList.add('yemenpay-wide-layout');
        } else {
          modalCont.classList.remove('yemenpay-wide-layout');
        }
      }

      const progressLine = this.modalElement.querySelector('#yemenpay-progress-line');
      const dot1 = this.modalElement.querySelector('#dot-step-1');
      const dot2 = this.modalElement.querySelector('#dot-step-2');
      const dot3 = this.modalElement.querySelector('#dot-step-3');

      const panels = this.modalElement.querySelectorAll('.yemenpay-step-panel');
      panels.forEach(p => {
        p.classList.remove('active');
        p.classList.remove('slide-out-left');
      });

      const nextBtn = this.modalElement.querySelector('#yemenpay-btn-next');
      const prevBtn = this.modalElement.querySelector('#yemenpay-btn-prev');
      const footer = this.modalElement.querySelector('#yemenpay-modal-footer');

      footer.style.display = 'flex';

      if (this.currentStep === 1) {
        this.modalElement.querySelector('#step-panel-1').classList.add('active');
        progressLine.style.width = '0%';
        dot1.className = 'yemenpay-step-dot active';
        if (dot2) dot2.className = 'yemenpay-step-dot';
        if (dot3) dot3.className = 'yemenpay-step-dot';

        prevBtn.style.display = 'none';
        prevBtn.style.visibility = 'hidden';
        nextBtn.innerHTML = '<span>التالي</span> <i class="ph ph-caret-left"></i>';
      } 
      else if (this.currentStep === 2) {
        this.modalElement.querySelector('#step-panel-2').classList.add('active');
        progressLine.style.width = '50%';
        dot1.className = 'yemenpay-step-dot completed';
        if (dot2) dot2.className = 'yemenpay-step-dot active';
        if (dot3) dot3.className = 'yemenpay-step-dot';

        prevBtn.style.display = 'flex';
        prevBtn.style.visibility = 'visible';
        nextBtn.innerHTML = '<span>التالي</span> <i class="ph ph-caret-left"></i>';
      } 
      else if (this.currentStep === 3) {
        // Summary page details
        this.modalElement.querySelector('#summary-wallet-name').innerHTML = `${WalletNames[this.selectedWallet]}`;
        this.modalElement.querySelector('#summary-sender-info').innerText = `${this.senderPhone}`;
        
        const senderLabel = this.modalElement.querySelector('#summary-sender-info').previousElementSibling;
        if (senderLabel) {
          senderLabel.innerText = this.selectedWallet === 'kuraimi' ? 'اسم المرسل:' : 'رقم المرسل:';
        }
        this.modalElement.querySelector('#summary-sender-info').style.direction = this.selectedWallet === 'kuraimi' ? 'rtl' : 'ltr';
        
        // Handle delivery location display
        const locSection = this.modalElement.querySelector('#summary-location-section');
        const locInfo = this.modalElement.querySelector('#summary-location-info');
        const paymentSec = this.modalElement.querySelector('#summary-payment-section');
        if (this.config.locationEnabled && this.selectedCity) {
          if (locSection) locSection.style.display = 'block';
          if (locInfo) {
            locInfo.innerText = `${CityNames[this.selectedCity] || this.selectedCity} - ${this.addressDetails}`;
            locInfo.setAttribute('data-tooltip', `${CityNames[this.selectedCity] || this.selectedCity} - ${this.addressDetails}`);
          }
          if (paymentSec) {
            paymentSec.style.borderBottom = '1px dashed var(--yemenpay-border)';
            paymentSec.style.marginBottom = '12px';
            paymentSec.style.paddingBottom = '12px';
          }
        } else {
          if (locSection) locSection.style.display = 'none';
          if (paymentSec) {
            paymentSec.style.borderBottom = 'none';
            paymentSec.style.marginBottom = '0';
            paymentSec.style.paddingBottom = '0';
          }
        }

        // Populate merchant details in step 3
        this.modalElement.querySelector('#summary-merchant-name').innerText = this.merchantData.merchantName;
        
        let accountStr = this.merchantData.accounts[this.selectedWallet];
        if (typeof accountStr === 'object') {
            accountStr = accountStr[this.config.currency] || Object.values(accountStr)[0];
        }
        this.modalElement.querySelector('#summary-merchant-account').innerText = accountStr;

        const priceVal = this.formatPrice(this.config.amount, this.config.currency);
        this.modalElement.querySelector('#summary-amount').innerText = priceVal;

        this.modalElement.querySelector('#step-panel-3').classList.add('active');
        
        if (this.config.locationEnabled) {
          progressLine.style.width = '100%';
          dot1.className = 'yemenpay-step-dot completed';
          if (dot2) dot2.className = 'yemenpay-step-dot completed';
          if (dot3) dot3.className = 'yemenpay-step-dot active';
        } else {
          progressLine.style.width = '100%';
          dot1.className = 'yemenpay-step-dot completed';
          if (dot3) dot3.className = 'yemenpay-step-dot active';
        }

        prevBtn.style.display = 'flex';
        prevBtn.style.visibility = 'visible';
        nextBtn.innerHTML = '<span>التحقق من الدفع</span> <i class="ph ph-shield-check"></i>';
      } 
      else if (this.currentStep === 'loader') {
        footer.style.display = 'none';
        this.modalElement.querySelector('#step-panel-loader').classList.add('active');
        this.startLoaderCountdown();
      } 
      else if (this.currentStep === 'success') {
        footer.style.display = 'none';
        this.modalElement.querySelector('#step-panel-success').classList.add('active');
      } 
      else if (this.currentStep === 'failed') {
        footer.style.display = 'none';
        this.modalElement.querySelector('#step-panel-failed').classList.add('active');
      }
    }

    handleNextStep() {
      if (this.currentStep === 1) {
        if (this.validateStep1()) {
          if (this.config.locationEnabled) {
            this.goToStep(2);
          } else {
            this.goToStep(3);
          }
        }
      } else if (this.currentStep === 2) {
        if (this.validateStep2()) {
          this.goToStep(3);
        }
      } else if (this.currentStep === 3) {
        this.goToStep('loader');
      }
    }

    handlePrevStep() {
      if (this.currentStep === 2) {
        this.goToStep(1);
      } else if (this.currentStep === 3) {
        if (this.config.locationEnabled) {
          this.goToStep(2);
        } else {
          this.goToStep(1);
        }
      }
    }

    validateStep1() {
      let isValid = true;

      // 1. Wallet Card check
      if (!this.selectedWallet) {
        this.showError('wallet');
        isValid = false;
      } else {
        this.hideError('wallet');
      }

      // 3. Sender Phone / Name check
      const phoneInput = this.modalElement.querySelector('#yemenpay-input-phone');
      
      if (this.selectedWallet === 'kuraimi') {
        let nameVal = phoneInput.value.trim();
        phoneInput.value = nameVal;
        this.senderPhone = nameVal;
        
        if (!this.senderPhone || this.senderPhone.split(' ').length < 2 || this.senderPhone.length < 5) {
          this.showError('phone');
          phoneInput.classList.add('error');
          if (isValid) phoneInput.focus();
          isValid = false;
        } else {
          this.hideError('phone');
          phoneInput.classList.remove('error');
        }
      } else {
        let phoneVal = phoneInput.value.replace(/\s+/g, '');
        if (phoneVal.startsWith('+967')) phoneVal = phoneVal.substring(4);
        else if (phoneVal.startsWith('00967')) phoneVal = phoneVal.substring(5);
        else if (phoneVal.startsWith('967') && phoneVal.length > 9) phoneVal = phoneVal.substring(3);
        
        if (phoneVal.startsWith('0') && phoneVal.length === 10) phoneVal = phoneVal.substring(1);
        
        phoneInput.value = phoneVal;
        this.senderPhone = phoneVal;

        const phoneRegex = /^(77|78|73|71|70)\d{7}$/;
        if (!this.senderPhone || !phoneRegex.test(this.senderPhone)) {
          this.showError('phone');
          phoneInput.classList.add('error');
          if (isValid) phoneInput.focus();
          isValid = false;
        } else {
          this.hideError('phone');
          phoneInput.classList.remove('error');
        }
      }

      return isValid;
    }

    validateStep2() {
      if (!this.config.locationEnabled) return true;
      let isValid = true;

      // 1. City selection check
      const cityInput = this.modalElement.querySelector('#yemenpay-input-city');
      this.selectedCity = cityInput ? cityInput.value.trim() : '';
      if (!this.selectedCity) {
        this.showError('city');
        isValid = false;
      } else {
        this.hideError('city');
      }

      // 2. Address Details check
      const addressInput = this.modalElement.querySelector('#yemenpay-input-address-details');
      this.addressDetails = addressInput ? addressInput.value.trim() : '';
      if (!this.addressDetails || this.addressDetails.length < 5) {
        this.showError('address-details');
        if (addressInput) {
          addressInput.classList.add('error');
          if (isValid) addressInput.focus();
        }
        isValid = false;
      } else {
        this.hideError('address-details');
        if (addressInput) addressInput.classList.remove('error');
      }

      return isValid;
    }

    showError(field) {
      const errorEl = this.modalElement.querySelector(`#error-${field}`);
      if (errorEl) errorEl.classList.add('visible');

      if (typeof this.config.onError === 'function') {
        let errorMsg = '';
        if (field === 'wallet') errorMsg = 'يرجى اختيار المحفظة الرقمية';
        else if (field === 'phone') {
          errorMsg = this.selectedWallet === 'kuraimi' 
            ? 'يرجى إدخال الاسم الأول والأخير بشكل صحيح' 
            : 'رقم الهاتف غير صالح. يجب أن يتكون من 9 أرقام ويبدأ بـ 77، 78، 73، 70، أو 71.';
        }
        else if (field === 'city') errorMsg = 'يرجى اختيار المحافظة/المدينة';
        else if (field === 'address-details') errorMsg = 'يرجى إدخال تفاصيل العنوان (5 أحرف على الأقل)';
        
        this.config.onError({ field, message: errorMsg });
      }
    }

    hideError(field) {
      const errorEl = this.modalElement.querySelector(`#error-${field}`);
      if (errorEl) errorEl.classList.remove('visible');
    }

    startLoaderCountdown() {
      let secondsLeft = 60;
      const countdownText = this.modalElement.querySelector('#yemenpay-timer-countdown');
      const progressCircle = this.modalElement.querySelector('#yemenpay-progress-circle');
      
      const circumference = 2 * Math.PI * 46; // 289.02
      if (progressCircle) {
        progressCircle.style.strokeDasharray = circumference;
        progressCircle.style.strokeDashoffset = '0';
      }

      if (countdownText) {
        countdownText.innerText = secondsLeft;
      }

      this.timerInterval = setInterval(() => {
        secondsLeft--;
        if (countdownText) {
          countdownText.innerText = secondsLeft;
        }

        if (progressCircle) {
          const progressFraction = secondsLeft / 60;
          const offset = circumference * (1 - progressFraction);
          progressCircle.style.strokeDashoffset = offset;
        }

        // Verify checks at intervals (only success can trigger early transition, failure waits for 1m timeout)
        if (secondsLeft % 5 === 0) {
          this.checkPaymentStatusOnServer().then(res => {
            if (res.status === 'success') {
              clearInterval(this.timerInterval);
              this.paymentId = res.tx_id || res.paymentId;
              this.showSuccess();
            }
          });
        }

        if (secondsLeft <= 0) {
          clearInterval(this.timerInterval);
          this.verifyPaymentFinalCheck();
        }
      }, 1000);
    }

    checkPaymentStatusOnServer() {
      let url = 'https://api.yemenpay.app/api/payments/claim';
      if (window.location.port === '5000') {
        url = '/api/payments/claim';
      }

      return fetch(url, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          merchantId: this.config.merchantId,
          sender_info: this.senderPhone,
          amount: this.config.amount,
          wallet: this.selectedWallet
        })
      })
      .then(res => res.json())
      .catch(err => {
        console.error('API check failed, returning pending:', err);
        return { status: 'pending' };
      });
    }

    verifyPaymentFinalCheck() {
      this.checkPaymentStatusOnServer().then(res => {
        if (res.status === 'success') {
          this.paymentId = res.tx_id || res.paymentId;
          this.showSuccess();
        } else {
          this.paymentId = res.tx_id || res.paymentId || this.generatePaymentId();
          this.merchantContact = res.contact;
          this.showFailed();
        }
      });
    }

    generatePaymentId() {
      const chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
      let part1 = '';
      let part2 = '';
      for (let i = 0; i < 4; i++) {
        part1 += chars.charAt(Math.floor(Math.random() * chars.length));
        part2 += chars.charAt(Math.floor(Math.random() * chars.length));
      }
      return `AP-${part1}-${part2}`;
    }

    showSuccess() {
      this.currentStep = 'success';
      this.renderCurrentStep();
      
      this.modalElement.querySelector('#success-payment-id').innerText = this.paymentId;
      
      const event = new CustomEvent('yemenpay:success', {
        detail: {
          paymentId: this.paymentId,
          amount: this.config.amount,
          currency: this.config.currency,
          wallet: this.selectedWallet,
          senderPhone: this.senderPhone
        }
      });
      document.dispatchEvent(event);
      if (typeof this.config.onSuccess === 'function') {
        this.config.onSuccess(this.paymentId);
      }
    }

    showFailed() {
      this.currentStep = 'failed';
      this.renderCurrentStep();
      
      this.modalElement.querySelector('#failed-payment-id').innerText = this.paymentId;

      const contactsContainer = this.modalElement.querySelector('#yemenpay-dynamic-contacts');
      if (contactsContainer) {
        contactsContainer.innerHTML = '';
        
        const contacts = (this.merchantContact && Object.keys(this.merchantContact).length > 0) 
            ? this.merchantContact 
            : this.merchantData.contact_info;
            
        if (contacts) {
          const commonText = encodeURIComponent(
            `مرحباً، أواجه مشكلة في التحقق من الدفع التلقائي لعملية الشراء.\n` +
            `معرف العملية: ${this.paymentId}\n` +
            `هاتف المحفظة: ${this.senderPhone}\n` +
            `المحفظة: ${WalletNames[this.selectedWallet]}\n` +
            `المبلغ: ${this.formatPrice(this.config.amount, this.config.currency)}\n` +
            `يرجى تأكيد الحوالة يدوياً.`
          );
          
          Object.keys(contacts).forEach(key => {
            const val = contacts[key];
            if (!val) return;
            
            let href = '#';
            let icon = 'ph-link';
            let text = 'تواصل';
            
            const k = key.toLowerCase();
            if (k === 'whatsapp') {
              href = `https://wa.me/${val.replace('+', '').replace(/\s+/g, '')}?text=${commonText}`;
              icon = 'ph-whatsapp-logo';
              text = 'واتساب';
            } else if (k === 'email') {
              const mailSubject = encodeURIComponent(`مشكلة التحقق من الدفع - عملية ${this.paymentId}`);
              href = `mailto:${val}?subject=${mailSubject}&body=${commonText}`;
              icon = 'ph-envelope';
              text = 'إيميل';
            } else if (k === 'telegram') {
              href = `https://t.me/${val.replace('@', '')}`;
              icon = 'ph-telegram-logo';
              text = 'تيليجرام';
            } else if (k === 'facebook') {
              href = `https://m.me/${val}`;
              icon = 'ph-facebook-logo';
              text = 'فيسبوك';
            } else if (k === 'instagram') {
              href = `https://instagram.com/${val}`;
              icon = 'ph-instagram-logo';
              text = 'انستقرام';
            } else if (k === 'call') {
              href = `tel:${val}`;
              icon = 'ph-phone-call';
              text = 'اتصال';
            } else {
              href = val;
              text = key;
            }
            
            const a = document.createElement('a');
            a.href = href;
            a.target = '_blank';
            a.className = `yemenpay-contact-btn ${k}`;
            a.innerHTML = `<i class="ph ${icon}"></i> ${text}`;
            contactsContainer.appendChild(a);
          });
        }
      }

      const event = new CustomEvent('yemenpay:failed', {
        detail: {
          paymentId: this.paymentId,
          amount: this.config.amount,
          currency: this.config.currency,
          wallet: this.selectedWallet,
          senderPhone: this.senderPhone
        }
      });
      document.dispatchEvent(event);
      if (typeof this.config.onFailed === 'function') {
        this.config.onFailed({
          paymentId: this.paymentId,
          error: 'Automatic verification timeout'
        });
      }
    }

    copyToClipboard(text, btn) {
      const onSuccess = () => {
        if (btn) {
          const icon = btn.querySelector('i');
          if (icon) {
            const originalClass = icon.className;
            icon.className = 'ph ph-check';
            btn.classList.add('copied');
            setTimeout(() => {
              icon.className = originalClass;
              btn.classList.remove('copied');
            }, 2000);
          }
        }
        const toast = this.modalElement.querySelector('#yemenpay-copy-toast');
        if (toast) {
          toast.classList.add('visible');
          setTimeout(() => {
            toast.classList.remove('visible');
          }, 2000);
        }
      };

      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(text)
          .then(onSuccess)
          .catch(err => {
            console.error('Clipboard API failed: ', err);
            this.fallbackCopyTextToClipboard(text, onSuccess);
          });
      } else {
        this.fallbackCopyTextToClipboard(text, onSuccess);
      }
    }

    fallbackCopyTextToClipboard(text, onSuccess) {
      const textArea = document.createElement("textarea");
      textArea.value = text;
      // Avoid scrolling to bottom
      textArea.style.top = "0";
      textArea.style.left = "0";
      textArea.style.position = "fixed";
      document.body.appendChild(textArea);
      textArea.focus();
      textArea.select();
      try {
        const successful = document.execCommand('copy');
        if (successful) onSuccess();
      } catch (err) {
        console.error('Fallback copy failed', err);
      }
      document.body.removeChild(textArea);
    }
  }

  // Expose the YemenPay class to the global scope
  window.YemenPay = YemenPay;

  // Create a default shared instance for automatic/declarative setup
  YemenPay.defaultInstance = new YemenPay();

  // Define static proxies on the YemenPay class to delegate to the defaultInstance
  // This maintains full backward compatibility for existing window.YemenPay.init() or window.YemenPay.updateAmount() calls
  const delegateMethods = [
    'init', 'open', 'close', 'updateAmount', 'formatPrice', 
    'renderPayButton', 'handleTriggerClick', 'fetchMerchantDetails', 
    'buildModalHTML', 'buildInlineHTML', 'renderCurrentStep'
  ];

  delegateMethods.forEach(method => {
    YemenPay[method] = function(...args) {
      return YemenPay.defaultInstance[method](...args);
    };
  });

  // Keep compatibility accessors for state/config
  Object.defineProperty(YemenPay, 'config', {
    get() { return YemenPay.defaultInstance.config; },
    set(val) { YemenPay.defaultInstance.config = val; }
  });
  Object.defineProperty(YemenPay, 'modalElement', {
    get() { return YemenPay.defaultInstance.modalElement; },
    set(val) { YemenPay.defaultInstance.modalElement = val; }
  });
  Object.defineProperty(YemenPay, 'handleTriggerClick', {
    get() { return () => YemenPay.defaultInstance.handleTriggerClick(); }
  });
  Object.defineProperty(YemenPay, 'cancelWizard', {
    get() { return () => YemenPay.defaultInstance.cancelWizard(); }
  });

  // Self-initialize default instance on DOMContentLoaded (declarative auto-setup)
  document.addEventListener('DOMContentLoaded', () => {
    YemenPay.defaultInstance.init();
  });

})();

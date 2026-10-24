# Placement overrides. Anything not given here is filled by assemble.py's defaults from the inventory.
# Each placement: (value or None for "not shown", [refs], note)
# refs: "m:<manual cite key>", "i:<list>|<entry>" (exact inventory row), "i~:<list>|<substring>" (first matching row)
NS = None
NO_TERMS = "No source read states it; Salla's terms of use and privacy policy on salla.com were not reached from this session (see not-reached.tsv)."

SPEC = {
    "store_plan": {
        "decides": ("operator per market; merchant chooses a plan", ["m:plans_sar", "m:plans_aed", "i:plan-features|salla.com plans (ar-sa): بوليصات شحن سلة المُخفضة", "i:plan-features|salla.com plans (ar-ae): تفعيل الدفع الإلكتروني"],
                    "Salla's plans page per market prices Plus and Pro in SAR on the Saudi page and in AED on the UAE page; the Saudi page lists key features (Salla shipping labels, Salla Ads, Mahally, VAT with ZATCA link) that the UAE page does not."),
        "reason": (NS, [], "No source read states why plans differ per market."),
    },
    "store_balance_billing": {
        "software": ("core", ["m:wallet_store_use", "i:admin-navigation|Wallet"], "The store wallet is a page of the merchant dashboard."),
        "decides": ("merchant (tops up and withdraws); operator (withdrawals paid each Tuesday; withdrawal needs verification and no open complaint)", ["m:wallet_store_use", "m:bank_tuesday", "m:wallet_kyc_withdraw", "m:wallet_withdraw_fail"], ""),
        "boundary": ("setting: Balance & billing; the store balance pays plan renewals, purchases from Salla and shipping labels; it is separate from the e-payments balance", ["i:settings|Balance & billing", "m:wallet_store_use", "m:wallet_separate"], ""),
    },
    "store_verification": {
        "software": ("core", ["i:admin-navigation|Store Verification", "i:other:dashboard-apps|@salla.sa/ui-merchant-payments"], "The verification page is served by the dashboard's payments bundle, which also serves /entity/verifications."),
        "decides": ("operator per market (documents asked depend on the store's country); outside rules (government documents); Salla's team reviews", ["m:store_country_docs", "m:kyc_entities_ksa", "m:kyc_ae_licences", "m:kyc_kw_ubo", "m:kyc_team_review", "i:other:dashboard-features|kyc_new_workflow"],
                    "Saudi Arabia: freelance document (Saudi citizens only), commercial registration or charity certificate; UAE: trade licence types, Emirates ID; Kuwait: commercial registration extract with beneficial-owner data. The kyc_new_workflow flag lists AE, SA, KW, QA, OM, BH."),
        "legal": ("merchant (its own legal entity and documents)", ["m:store_entity_choice"], "The help page tells the merchant to pick its legal entity to comply with the rules; who is liable for wrong documents is not stated."),
        "boundary": ("verification form reviewed by Salla's team; Saudi owner identity checked by an Absher SMS; acceptance unlocks e-payments", ["m:kyc_absher", "m:kyc_team_review", "m:kyc_ae_payments", "m:tr_kyc_method"], ""),
        "reason": ("compliance with e-commerce rules (stated)", ["m:kyc_reason", "m:tr_sbc"], "The Saudi help page gives compliance with regulatory requirements for e-commerce among its reasons; a dashboard FAQ says the Saudi Business Center certificate is mandatory and a store without it breaches Ministry of Commerce rules."),
    },
    "customer_wallet": {
        "software": ("core API that works only when Salla's Customer Wallet app is installed", ["m:wallet_app_only", "i:api-resources|Merchant API > APIs > Customer Wallet"], ""),
    },
    "customer_data_rights": {
        "decides": ("merchant; outside rules (Saudi Personal Data Protection Law)", ["m:pdpl_policy", "m:pdpl_scope"], ""),
        "legal": ("merchant (as controller of its customers' data)", ["m:pdpl_controller"], "Salla's help page lists the controller's duties under the heading for the merchant who sees its customers' data."),
    },
    "salla_ads": {"software": ("separate service or product line", ["m:llms_ads"], "")},
    "mahally": {"software": ("separate service or product line", ["m:llms_mahally", "m:status_components"], "")},
    "salla_point": {"software": ("separate service or product line", ["m:llms_point"], "")},
    "mobile_app": {"software": ("separate service or product line", ["m:llms_appmaker", "m:llms_products"], "")},
    "app_store": {
        "software": ("separate service or product line (the App Store, an app marketplace)", ["m:llms_products", "m:status_components"], ""),
        "decides": ("operator (Salla reviews, accepts or rejects apps); merchant installs", ["m:apps_review", "i:other:staff-permissions|marketplace_apps_management"], ""),
        "legal": ("app developer and merchant", ["m:apps_responsibility", "m:join_partner_resp"], "The App Store terms state that the developer and the merchant bear responsibility for their use of apps and that Salla bears none."),
        "boundary": ("contract: App Store terms; paid apps are paid through Salla; disputes before the courts of Jeddah", ["m:apps_payment_via_salla", "m:apps_jeddah"], ""),
    },
    "themes": {
        "legal": ("app developer (theme developer); Salla presents itself as an intermediary", ["m:themes_intermediary", "m:tr_themes_intermediary"], ""),
    },
    "theme_partners": {
        "decides": ("operator (commission; payout after a guarantee period; may freeze dues)", ["m:themes_commission", "m:themes_payout_15", "m:themes_freeze"], ""),
        "legal": ("app developer (theme developer)", ["m:themes_intermediary"], ""),
    },
    # ---------------- money
    "salla_payments": {
        "software": ("separate service or product line (مدفوعات سلة)", ["m:sp_service", "i:other:dashboard-apps|@salla.sa/ui-merchant-payments"], "Salla describes online payments as a service it provides to process the store's payments."),
        "decides": ("operator per market (methods); operator per plan; Salla's team activates; merchant switches methods on", ["m:sp_methods_ae", "m:sp_methods_kw", "m:sp_req_plan_ae", "m:sp_req_team_ae", "m:tr_trial_orders", "m:sp_merchant_toggle"],
                    "Saudi help lists mada, Visa/Mastercard, Apple Pay and stc pay through Salla's gateway; UAE: Visa, Mastercard, Apple Pay; Kuwait: KNET, Visa, Mastercard, Apple Pay."),
        "legal": (NS, [], "The UAE and Kuwait help pages say payments are settled under a payment services contract signed during verification, but the party on Salla's side is not named in any source read. " + NO_TERMS),
        "boundary": ("setting: Payments (activation after reading and accepting the selling policy); contract: payment services contract; API: Payments (available methods); webhook: order.payment.updated; scope: payments", ["m:sp_selling_policy", "m:ae_contract", "i:api-resources|Merchant API > APIs > Payments", "i:webhook-topics|order.payment.updated", "i:access-scopes|payments"], ""),
        "reason": ("stated for stc pay: connecting within Salla Payments reduces problems and delays", ["m:stcpay_reason"], "The only stated reason found is for stc pay."),
    },
    "epayments_balance_payouts": {
        "software": ("core (the wallet's e-payments tab and payout cycle setting)", ["i:admin-navigation|Wallet", "m:pay_cycle_choose"], ""),
        "decides": ("operator per market (Saudi: minimum 100 SAR, cycle chosen by the merchant within plan limits; UAE: weekly on Thursday above 250 AED; Kuwait: next working day); operator per plan; merchant picks the cycle",
                    ["m:pay_cycle_min", "m:pay_cycle_choose", "m:tr_payout_locked", "m:ae_payout", "m:kw_payout", "m:sp_payout_plus", "m:sp_payout_pro", "m:sp_payout_special", "m:special_deposit24"],
                    "Sources differ: an older Saudi help page ties payout frequency to the plan (Plus weekly, Pro every 48 hours, Special daily), the newer page lets the merchant choose a cycle, and the dashboard text says faster options are locked on some plans. The Kuwait page says both 'a minimum of one Kuwaiti dinar' and 'no minimum'."),
        "legal": (NS, [], "The holder of the e-payments balance is not named; payouts follow the payment services contract (UAE, Kuwait). " + NO_TERMS),
        "boundary": ("the buyer pays online, the amount enters the e-payments balance, eligible dues go to the bank account registered at verification; contract: payment services contract", ["m:sp_flow", "m:pay_cycle_flow", "m:ae_holds", "m:ae_contract", "m:kw_contract", "m:tr_payout_cycle"], ""),
    },
    "payout_bank_account": {
        "software": ("core (part of store verification)", ["m:bank_payout_account"], ""),
        "decides": ("merchant (through verification); operator per market (UAE: a UAE bank account in AED; Kuwait: a Kuwaiti commercial account in KWD)", ["m:bank_match_kyc", "m:kyc_ae_aed", "m:kyc_kw_kwd", "m:kyc_kw_commercial"], ""),
        "legal": (NS, [], NO_TERMS),
        "boundary": ("verification form; the account is used by Salla to transfer dues and is not shown to customers; API: Payments > List Banks", ["m:bank_payout_account", "m:ae_bank_change", "i:api-resources|Merchant API > APIs > Payments"], ""),
    },
    "payment_fees": {
        "software": ("other: حاسبة الرسوم", ["m:sp_fee_calc"], "The help page puts the fees calculator under customising e-payments (ثانياً: تخصيص المدفوعات الإلكترونية), part of Salla Payments."),
        "decides": ("operator: fees set by the payment services contract signed at verification; operator per plan (Special plan: flexible gateway fees); outside rules (VAT 15% on fees)", ["m:ae_fees", "m:special_flex_fees", "m:tr_vat_fees", "m:tr_checkout_fee"], ""),
        "boundary": ("contract: payment services contract; fees calculator on the payments page; fees and VAT on fees deducted before payout", ["m:ae_fees", "m:sp_fee_calc", "m:tr_vat_fees"], ""),
    },
    "payment_processing_partner": {
        "software": (NS, [], "No source read names the processor, acquirer or bank behind Salla Payments."),
        "decides": (NS, [], "Not shown."),
        "legal": (NS, [], "The contract behind Salla Payments is named (payment services contract) but its parties are not. " + NO_TERMS),
        "boundary": ("contract: payment services contract signed during store verification", ["m:ae_contract", "m:kw_contract"], ""),
        "reason": (NS, [], "Not shown."),
    },
    "cod_salla_labels": {
        "software": ("other: الدفع عند الاستلام في بوليصات سلة", ["m:cod_payout_days", "i:admin-navigation|Wallet"], "Part of Salla shipping labels (بوليصات سلة); the COD balance is remitted to the merchant through the wallet."),
        "decides": ("operator (carriers supporting it, 1000 SAR ceiling, COD hidden under 20 SAR, payout on Sundays and Wednesdays); merchant (rules and COD fee he charges); operator per market (not yet in the UAE)", ["m:cod_carriers_list", "m:cod_max", "m:cod_min20", "m:cod_payout_days", "m:cod_merchant_fee", "m:cod_labels_ae_soon"], ""),
        "legal": (NS, [], NO_TERMS),
        "boundary": ("COD settings in Shipping & delivery; COD fees charged by the carrier plus checkout fees, with VAT on fees, deducted before payout", ["i:settings|Cash on delivery", "m:tr_cod_fees"], ""),
        "reason": ("COD settings exist to keep orders worthwhile, reduce cancellations and improve delivery (stated)", ["m:cod_reason"], ""),
    },
    "cod_own_carrier": {
        "software": ("outside the platform (the cash is settled between merchant and carrier); the COD switch is a setting in Salla", ["m:cod_not_collected", "m:cod_direct_settle", "m:cod_own_contract_ae"], ""),
        "decides": ("merchant and carrier, by their own agreement", ["m:cod_direct_settle", "m:cod_own_contract_ae"], ""),
        "legal": ("other: settled between the merchant and the shipping company under their agreement", ["m:cod_direct_settle"], ""),
        "boundary": ("carrier page > shipping pricing: COD switch and the COD commission agreed with the carrier", ["m:cod_own_contract_ae", "m:ae_cod_wallet"], ""),
    },
    "bank_transfer": {
        "software": ("core", ["m:bank_transfer_account"], ""),
        "decides": ("merchant (adds the accounts); buyer (chooses to pay by transfer)", ["m:bank_transfer_account"], ""),
        "boundary": ("payment methods page > bank accounts, shown to buyers at checkout", ["m:bank_transfer_account", "i:plan-features|سلة بلس: التحويل البنكي"], ""),
    },
    "bnpl": {
        "software": ("extension point (provider slot): providers listed on Salla's payments page", ["m:sp_bnpl_ksa", "m:sp_bnpl_ae", "m:sp_bnpl_kw"], ""),
        "decides": ("operator per market (which providers); merchant activates and opens an account with the provider", ["m:sp_bnpl_ae", "m:sp_bnpl_kw", "m:sp_merchant_services_bnpl"], "UAE: Tabby and Tamara; Kuwait: Tabby and Deema; Saudi plan lines name Tabby and Tamara."),
        "legal": ("partner (the provider); Salla disclaims the provider's services when it shares store data to open the account", ["m:tr_provider_share"], "The disclaimer is generic payments-page text for any provider named in it; which providers use it is not stated."),
    },
    "wallets_other_methods": {
        "software": ("extension point (provider slot)", ["m:paypal_connect_ae", "m:stcpay_switch"], ""),
        "decides": ("merchant (enters its own PayPal account; may keep a direct stc pay link)", ["m:paypal_connect_ae", "m:stcpay_switch"], ""),
        "boundary": ("payments page > digital wallets; stc pay moving to Salla's gateway ends the direct link and cannot be reversed", ["m:paypal_connect_ae", "m:stcpay_switch"], ""),
    },
    "external_gateways": {
        "software": ("extension point (provider slot)", ["m:sp_other_gateways", "m:tr_gateway_instead"], ""),
        "decides": ("merchant (uses its own gateway account and credentials); operator (a connected Tap blocks Salla Payments)", ["m:tr_gateway_own_account", "m:tr_tap_conflict", "m:knet_tap"], ""),
        "legal": ("partner (the gateway collects the payments instead of Salla Payments)", ["m:tr_gateway_instead"], "Inference: the merchant's own gateway contract governs; the contract itself is not shown."),
        "boundary": ("gateway credentials entered on the payments page; payments collected through the gateway instead of Salla Payments", ["m:tr_gateway_own_account", "m:tr_gateway_instead"], ""),
    },
    "charity_gateways": {
        "software": ("extension point (provider slot) for charity stores", ["m:tr_charity_gateways"], ""),
    },
    "fraud_protection": {
        "software": ("other: الحماية من الاحتيال، ومزايا أخرى من مدفوعات سلة", ["m:tr_checkout_fee"], "Part of Salla Payments: one of the services the checkout experience fee covers."),
    },
    "transactions": {
        "boundary": ("API: Transactions (refund, void, reverse; the store must have enough balance); scope: transactions", ["m:txn_refund", "m:txn_balance", "i:access-scopes|transactions"], ""),
    },
    "returns_refunds": {
        "boundary": ("webhook: order.refunded and return shipments; the money side runs through the Transactions API and the e-payments balance", ["i:webhook-topics|order.refunded", "m:txn_refund", "m:wallet_epay_refunds"], ""),
    },
    "instant_settlements": {
        "software": ("core API open only to dropshipping apps", ["m:settle_withhold", "m:settle_dropship"], ""),
        "decides": ("app developer (a dropshipping app withholds an amount from the merchant's wallet)", ["m:settle_withhold", "m:settle_dropship"], ""),
    },
    "recurring_payments": {
        "software": ("extension point (app): Recurring Payments API for apps", ["m:rp_what", "i:extension-points|docs navbar > Recurring Payments API"], ""),
        "decides": ("merchant or an authorized app (off by default)", ["m:rp_disabled"], ""),
    },
    "salla_capital": {
        "software": ("separate service or product line (صندوق سلة)", ["m:tr_capital_tanami"], ""),
        "decides": ("other: مدير الصندوق", ["m:tr_capital_verify", "m:tr_capital_agreement"], "The fund manager, a partner, verifies the business and its bank account and approves the request."),
        "legal": ("partner: the fund manager Tanami", ["m:tr_capital_manager", "m:tr_capital_tanami"], ""),
        "boundary": ("contract: investment agency agreement; 25% of each net Salla Payments sale is collected until repaid", ["m:tr_capital_agreement", "m:tr_capital_tanami"], ""),
    },
    "app_billing_partner_payouts": {
        "software": ("core of the Salla Partners portal (Payouts, Billings)", ["i:admin-navigation|Partners portal > Payouts", "m:billing_tutorial_monthly"], ""),
        "decides": ("operator (Salla takes a share of app subscriptions; developer dues paid after a guarantee period of usually 15 days)", ["m:apps_commission", "m:apps_payout_15", "m:join_payouts"], ""),
        "legal": ("platform company (the App Store terms name the owning company)", ["m:ent_apps_policy", "m:apps_payment_via_salla"], ""),
        "boundary": ("paid apps are paid through Salla; monthly invoices to app companies paid by bank transfer with proof; payout statuses in the portal", ["m:apps_payment_via_salla", "m:billing_tutorial", "i:other:partner-payout-statuses|Paid"], ""),
        "reason": ("Salla's share pays for hosting and integration services (stated)", ["m:apps_commission"], ""),
    },
    "partner_affiliate": {
        "legal": ("partner (the marketer); commission includes VAT and government fees", ["m:aff_vat_included", "m:join_partner_resp"], ""),
    },
    "merchant_services_marketplace": {
        "legal": ("partner (the service provider, an independent party)", ["m:join_provider_independent", "m:join_intermediary"], ""),
    },
    "partner_account": {
        "decides": ("operator (Salla reviews applications and verifies identity)", ["m:join_identity", "i:other:partner-id-types|Personal Identity"], ""),
        "legal": ("partner", ["m:join_partner_resp", "m:join_licensed"], ""),
    },
    "partner_store_access": {
        "legal": ("partner (for the services it provides)", ["m:join_partner_resp"], ""),
    },
    # ---------------- shipping
    "salla_shipping_labels": {
        "software": ("separate service or product line (بوليصات سلة)", ["i:plan-features|سلة بلس: بوليصات شحن سلة المُخفضة", "m:intl_carriers"], ""),
        "decides": ("operator (carriers, label prices and tiers); operator per market (listed as a key feature only on the Saudi plans page); merchant chooses", ["i:plan-features|salla.com plans (ar-sa): بوليصات شحن سلة المُخفضة", "i:other:dashboard-features|shipping-tier-pricing-system", "m:cod_labels_ae_soon"], ""),
        "boundary": ("shipping page; label costs paid from the store balance", ["i:admin-navigation|Shipping & delivery", "m:wallet_store_use"], ""),
    },
    "own_carriers": {
        "decides": ("merchant (its own contract with the carrier, its own couriers)", ["m:cod_own_contract_ae", "m:ae_cod_wallet"], ""),
    },
    "international_shipping": {
        "decides": ("operator (Salla's international shipping gateway fee, added to the buyer); outside rules (HS codes required by carriers); operator per market (Saudi stores only)", ["m:intl_fee_what", "m:intl_ksa_only", "m:hs_code"], ""),
        "legal": ("buyer pays the gateway fee; the merchant bears none of it", ["m:intl_fee_what"], "This shows who pays, not who is liable."),
        "reason": ("the gateway fee is meant to make costs transparent and improve the shipping experience (stated)", ["m:intl_fee_reason"], ""),
    },
    "shipping_apps": {
        "software": ("extension point (app and function): shipping apps and Salla AWB functions run inside Salla", ["m:awb_screen", "m:awb_managed", "i:extension-points|app type: Shipping App"], ""),
        "reason": ("functions fully managed by Salla reduce operational cost and complexity (stated)", ["m:awb_managed"], ""),
    },
    # ---------------- tax, currency, markets
    "tax_settings": {
        "decides": ("merchant (creates a tax record per market and enters the official rate); outside rules (the rate in force in each country)", ["m:tax_market_record", "m:tax_market_apply"], ""),
        "boundary": ("API: Taxes (a rate and its country are required); webhook: storetax.created; scope: taxes; setting: Taxes", ["m:tax_country", "i:webhook-topics|storetax.created", "i:access-scopes|taxes", "i:settings|Taxes"], ""),
    },
    "zatca_einvoicing": {
        "software": ("extension point (app): a free App Store app", ["m:zatca_app_install", "i:other:dashboard-features|zatca"], ""),
        "decides": ("operator per market (Saudi stores only); operator per plan (Pro and Special); outside rules (ZATCA registration)", ["m:zatca_ksa_only", "m:zatca_plans", "m:aiinfo_zatca"], ""),
        "legal": (NS, [], "Not shown; the merchant grants Salla authority to manage its invoices with ZATCA."),
        "boundary": ("an activation code from the merchant's ZATCA account grants Salla authority to manage invoices", ["m:zatca_grant", "m:zatca_what"], ""),
        "reason": ("higher accuracy and faster compliance with tax requirements (stated)", ["m:zatca_reason"], ""),
    },
    "customs_duties": {
        "boundary": ("setting: Taxes (taxes-and-duties); IOSS advised for EU sales", ["i:settings|Taxes", "m:tax_ioss"], ""),
    },
    "store_currencies": {
        "decides": ("merchant (available currencies); buyer (chooses a currency); platform (default display currency by the buyer's location; automatic prices by the current exchange rate in markets)", ["m:cur_merchant_set", "m:cur_buyer_choice", "m:cur_geo_default", "m:tr_auto_fx"],
                    "Salla's sources give different counts: a Plus plan line offers payment in 33+ currencies; the ai-info page says more than 15 currencies."),
        "boundary": ("API: Currencies (scope metadata); setting: General > Currencies; storefront currency switcher", ["i:api-resources|Merchant API > APIs > Currencies", "i:settings|Currencies", "i:plan-features|سلة بلس: إتاحة الدفع عبر +33 عملة", "m:aiinfo_currencies"], ""),
    },
    "settlement_currency": {
        "software": ("other: بوابة دفع سلة", ["m:sp_sar"], "Part of Salla Payments."),
        "decides": ("operator per market (Saudi: all payments received in SAR; UAE: an AED account; Kuwait: a KWD account)", ["m:sp_sar", "m:kyc_ae_aed", "m:kyc_kw_kwd"], ""),
        "legal": (NS, [], NO_TERMS),
        "boundary": ("payout to the bank account registered at verification, in the market's currency", ["m:kyc_ae_aed", "m:kyc_kw_kwd"], ""),
        "reason": (NS, [], "Not shown."),
    },
    "markets": {
        "decides": ("merchant (creates a market per country, region or city with its currency, language, domain and shipping); operator per plan (Special plan)", ["m:mkt_what", "m:mkt_currency", "m:mkt_special"], ""),
        "boundary": ("API: Store Scopes (multi-country); setting: Markets", ["m:scopes_multicountry", "i:settings|Markets"], ""),
    },
    "salla_markets_served": {
        "software": (NS, [], "Not a software part; the store's country is chosen at sign-up."),
        "decides": ("operator per market (Salla's site lists Saudi Arabia and the UAE; the app listing picker lists seven countries)", ["i:other:footer-markets|السعودية", "i:other:footer-markets|الامارات", "m:llms_markets", "i:other:app-supported-countries|Kuwait", "i:other:dashboard-features|kyc_new_workflow"], ""),
        "legal": (NS, [], "Not shown per country; see the legal entities concern."),
        "boundary": ("store country chosen at sign-up decides the government documents asked", ["m:store_country_docs"], ""),
        "reason": ("GCC markets differ in payment, shipping, legal, tax or terminology needs (stated as the basis for its market priorities)", ["m:llms_gcc"], ""),
    },
    # ---------------- legal and policy
    "terms_of_use": {
        "software": (NS, [], "A legal page, not a software part."),
        "decides": ("operator per market (separate pages under the Saudi and UAE paths)", ["i:legal-agreements|https://salla.com/terms", "i:legal-agreements|https://salla.com/ar-ae/terms"], ""),
        "legal": (NS, [], "The entity party to the merchant terms is not shown; the pages were not reached."),
        "boundary": ("accepted at sign-up (سياسة الاستخدام على منصة سلة)", ["m:signup_terms"], ""),
    },
    "salla_privacy_policy": {
        "software": (NS, [], "A legal page, not a software part."),
        "decides": ("operator per market (separate pages under the Saudi and UAE paths)", ["i:legal-agreements|https://salla.com/privacy", "i:legal-agreements|https://salla.com/ar-ae/privacy"], ""),
        "boundary": ("apps and partners are bound by Salla's privacy policy and the Saudi personal data law", ["m:apps_privacy"], ""),
    },
    "selling_policy": {
        "software": (NS, [], "A legal page, not a software part."),
        "decides": ("operator", ["i:legal-agreements|https://salla.com/policies/selling-policies"], ""),
        "boundary": ("accepted when activating e-payments", ["m:sp_selling_policy"], ""),
    },
    "affiliate_program_terms": {
        "software": (NS, [], "A legal page, not a software part."),
        "legal": ("platform company (the agreement names the owning company)", ["m:ent_affiliate"], "The name and number given differ from other Salla pages; see the legal entities concern."),
    },
    "app_store_policy": {
        "software": (NS, [], "A legal page, not a software part."),
        "decides": ("operator", ["m:apps_review"], ""),
        "legal": ("platform company (شركة تطبيق سلة لتقنية المعلومات)", ["m:ent_apps_policy"], ""),
        "boundary": ("disputes before the courts of Jeddah", ["m:apps_jeddah"], ""),
    },
    "partner_app_contract": {
        "software": (NS, [], "A contract record, not a software part."),
        "legal": ("platform company and the partner", ["m:ent_joining"], "The partners joining policy names the owning company; the SaaS contract text itself was not read."),
    },
    "payment_services_contract": {
        "software": (NS, [], "A contract, not a software part."),
        "decides": ("operator (fees and settlement follow it)", ["m:ae_fees", "m:kw_contract"], ""),
        "legal": (NS, [], "The parties are not named in any source read."),
        "boundary": ("signed during store verification", ["m:ae_contract", "m:kw_contract"], ""),
    },
    "complaints_platform": {"software": (NS, [], "A page in Salla's footer; its content was not reached.")},
    "app_maker_policy": {"software": (NS, [], "A legal page, not a software part.")},
    "policy_nd96": {"software": (NS, [], "A legal page whose content was not reached.")},
    # ---------------- apps and developer platform
    "oauth": {
        "software": ("extension point (app): OAuth 2.0 authorization for apps", ["m:sec_oauth", "i:extension-points|docs navbar > Salla OAuth 2.0"], ""),
        "decides": ("merchant (authorizes an app to specific parts of the account)", ["m:sec_merchant_authorize"], ""),
        "legal": ("app developer and merchant", ["m:apps_responsibility"], ""),
        "reason": ("third-party apps get API access without users sharing passwords (stated)", ["m:sec_oauth_reason"], ""),
    },
    "app_scopes": {
        "software": ("extension point (app)", ["i:access-scopes|orders"], ""),
        "decides": ("app developer requests scopes; merchant authorizes", ["i:access-scopes|orders", "m:sec_merchant_authorize"], ""),
    },
    "webhooks": {
        "software": ("extension point (app)", ["i:api-resources|Merchant API > APIs > Webhooks"], ""),
        "decides": ("app developer (registers topics and conditions); operator per plan (Pro and Special for the merchant's own webhooks)", ["i:other:dashboard-features|webhooks", "i:plan-features|سلة برو: إرسال الإخطارات لخدمات أخرى عبر Webhooks"], ""),
    },
    "app_functions": {
        "software": ("extension point (function): serverless functions hosted by Salla", ["m:af_serverless", "m:awb_managed"], ""),
        "decides": ("app developer; platform at build (synchronous events must answer within milliseconds)", ["m:af_sync"], ""),
        "boundary": ("events listed under App Functions supported events; synchronous actions such as shipment.creating block the user", ["m:af_sync", "i~:extension-points|App Functions event: Shipment Creating"], ""),
        "reason": ("no infrastructure to manage, automatic scaling (stated)", ["m:af_serverless"], ""),
    },
    "communication_apps": {
        "software": ("extension point (provider slot) built on App Functions", ["m:comm_takeover", "i:extension-points|app type: Communication App"], ""),
        "decides": ("merchant (uses its own provider accounts, sender IDs and templates); app developer (routing)", ["m:comm_own_accounts"], ""),
        "boundary": ("events communication.sms.send, communication.email.send, communication.whatsapp.send; Supported Features declared in the Partner Portal", ["i:webhook-topics|communication.whatsapp.send", "m:comm_takeover"], ""),
    },
    "embedded_sdk": {
        "software": ("extension point (app): third-party apps in an iframe inside the merchant dashboard", ["m:emb_iframe"], ""),
    },
    "api_rate_limits": {
        "decides": ("operator per plan", ["m:rate_plan"], ""),
        "boundary": ("rate-limit headers; temporary restrictions on excess", ["m:rate_restrict"], ""),
        "reason": ("to keep Salla stable and fair for everyone (stated)", ["m:rate_reason"], ""),
    },
    # ---------------- cross-cutting deep concerns
    "legal_entities": {
        "software": (NS, [], "Not a software part."),
        "decides": (NS, [], "Not shown."),
        "legal": ("platform company: Salla's own pages name شركة تطبيق سلة لتقنية المعلومات and شركة منصة سلة للاتصالات وتقنية المعلومات, with commercial registration 4031200589 or 7011845513; footers name شركة سلة القابضة",
                  ["m:ent_apps_policy", "m:ent_joining", "m:ent_joining_def", "m:ent_themes", "m:ent_affiliate", "m:ent_holding_footer", "m:aiinfo_holding", "m:aiinfo_hq"],
                  "Sources disagree on the company name and on which number goes with it; recorded as found, not resolved. No source read names a separate Salla entity for the UAE or Kuwait."),
        "boundary": ("contracts naming the company: App Store terms, partners joining policy, themes terms, affiliate agreement; merchant terms and the payment services contract were not reached or name no party", ["m:ent_apps_policy", "m:ent_themes", "m:ae_contract"], ""),
        "reason": (NS, [], "Not shown."),
    },
    "licences": {
        "software": (NS, [], "Not a software part."),
        "decides": ("outside rules (merchant licences and the Saudi Business Center certificate); operator (Salla decides which UAE licence types it accepts)", ["m:tr_sbc", "m:kyc_ae_licences", "m:join_licensed"], ""),
        "legal": ("merchant (holds its own licence); partner (must be licensed)", ["m:store_entity_choice", "m:join_licensed"], "No source read states a licence held by Salla for payments or any other regulated activity."),
        "boundary": ("store verification; partner registration", ["m:kyc_reason", "m:join_identity"], ""),
        "reason": ("compliance with e-commerce rules (stated for verification)", ["m:kyc_reason"], ""),
    },
    "sanctions_screening": {
        "software": ("core (violations page; verification)", ["m:tr_violation_page", "i:other:dashboard-apps|@salla.sa/ui-merchant-manage"], ""),
        "decides": ("operator (Salla records store violations and may suspend the store; hides COD from customers banned in other Salla stores; may suspend apps)", ["m:tr_violation", "m:tr_cod_banned", "m:apps_suspend", "m:rate_restrict"], "No source read mentions sanctions lists or sanctions screening."),
        "legal": (NS, [], NO_TERMS),
        "boundary": ("identity checks at verification (Absher in Saudi Arabia; beneficial owners in Kuwait); violation page with a 24-hour deadline", ["m:kyc_absher", "m:kyc_kw_ubo", "m:tr_violation"], ""),
        "reason": (NS, [], "Not shown."),
    },
    "data_location": {
        "software": (NS, [], "No source read states where store, customer or payment data is stored or processed."),
        "decides": ("outside rules: Salla's pages name the Saudi Personal Data Protection Law", ["m:apps_privacy", "m:pdpl_scope"], "This names the law, not where data lives."),
        "legal": (NS, [], NO_TERMS + " The help page places customer-data duties on the merchant as controller (see customer data concern)."),
        "boundary": (NS, [], "Not shown."),
        "reason": (NS, [], "Not shown."),
    },
    "platform_security_status": {
        "software": ("core", ["m:sec_tls", "m:status_components"], ""),
        "decides": ("platform at build (HTTPS only, OAuth 2.0)", ["m:sec_https", "m:sec_oauth"], ""),
        "boundary": ("OAuth 2.0; public status page listing Salla's own components", ["m:sec_oauth", "m:status_page", "m:status_components2"], ""),
    },
    "partner_failure": {
        "software": (NS, [], "No source read describes switching to another payment or shipping partner when one is down."),
        "decides": ("operator: Salla disclaims affiliate-commission gaps caused by payment gateway outages or updates", ["m:affplans_gateway_failure"], ""),
        "legal": ("partner: Salla is not responsible for a provider's services after sharing store data with it", ["m:tr_provider_share", "m:affplans_gateway_failure"], ""),
        "boundary": ("carrier auto-assignment checks the next carrier when the first does not deliver to the customer's area; a communication app's delivery failure is reported to the store; the status page lists Salla's own components only", ["m:mkt_carrier_fallback", "m:comm_failed", "m:status_components"], ""),
        "reason": (NS, [], "Not shown."),
    },
}

EXTRA_INV = [
    # (list, entry, manual cite key, concern keys)
    ("legal-agreements", "سياسة البيع", "sp_selling_policy", ["selling_policy"]),
    ("legal-agreements", "عقد خدمات الدفع", "ae_contract", ["payment_services_contract"]),
    ("legal-agreements", "سياسة الاستخدام على منصة سلة", "signup_terms", ["terms_of_use"]),
    ("legal-agreements", "اتفاقية الوكالة بالاستثمار", "tr_capital_agreement", ["salla_capital"]),
    ("legal-agreements", "سياسة الشروط والاستخدام – متجر تطبيقات سلة", "title_apps_policy", ["app_store_policy"]),
    ("legal-agreements", "سياسة الانضمام إلى برنامج شركاء سلة", "title_joining", ["partner_app_contract", "partner_account"]),
    ("legal-agreements", "الشروط والأحكام لاستخدام متجر الثيمات – منصة سلة", "title_themes", ["theme_partners", "themes"]),
    ("legal-agreements", "اتفاقية استخدام برنامج التسويق بالعمولة", "title_affiliate", ["affiliate_program_terms", "partner_affiliate"]),
]

SPEC.update({
    "salla_support": {
        "software": (NS, [], "Not shown as a software part."),
        "decides": ("operator per plan (a dedicated account manager and support on the Special plan)", ["i:plan-features|Salla Special page: مدير حساب مخصص", "i:plan-features|Salla Special page: فريقنا معك في كل خطوة", "i:other:dashboard-features|support-plan"], ""),
    },
    "storefront_sdk_components": {
        "software": ("extension point (theme): Twilight SDK, web components and component bundles for theme developers", ["i:extension-points|docs navbar > Twilight SDK", "i:extension-points|docs navbar > Web Components", "i:extension-points|docs navbar > Component Bundle"], ""),
        "decides": ("app developer (theme developer); merchant picks and customises the theme", ["i:extension-points|docs navbar > Twilight SDK", "i:admin-navigation|Store designMost Viewed"], ""),
    },
    "storefront_events": {
        "software": ("extension point (app and function): storefront events delivered in device and cloud modes", ["i:extension-points|docs navbar > Ecommerce Events", "i~:extension-points|Ecommerce event (cloud-cart-checkouts)"], ""),
    },
    "storefront_api": {
        "software": ("core (Store APIs, a component on Salla's status page)", ["m:status_store_apis"], "Salla's storefront API lists held in observed-sa were not inventoried: the endpoints are named only in capture metadata."),
    },
    "customs_duties": {
        "software": ("core (the taxes settings page sits at /taxes-and-duties)", ["i:settings|Taxes"], ""),
        "decides": (NS, [], "Who sets or pays customs duties is not stated in any source read; Salla's international shipping gateway fee is a different charge (see international shipping)."),
    },
    "geo_reference_data": {
        "decides": ("platform at build (lists served by Salla's API)", ["i:api-resources|Merchant API > APIs > Countries", "i:other:portal-countries|Saudi Arabia"], ""),
    },
    "app_maker_policy": {
        "software": (NS, [], "A legal page, not a software part."),
        "decides": ("operator", ["i:legal-agreements|https://salla.com/policies/publising-app-maker"], ""),
    },
    "policy_nd96": {
        "software": (NS, [], "A legal page whose content was not reached."),
        "decides": ("operator", ["i:legal-agreements|https://salla.com/policies/nd96"], ""),
    },
    "complaints_platform": {
        "software": (NS, [], "A page in Salla's footer; its content was not reached."),
        "decides": ("operator", ["i:legal-agreements|منصة الشكاوي"], ""),
    },
    "app_events": {
        "software": ("extension point (app)", ["i:webhook-topics|app.uninstalled", "i:extension-points|docs navbar > App API"], ""),
    },
    "app_snippets": {
        "software": ("extension point (app): JavaScript injected into the merchant's store", ["m:snippet_inject", "i:api-resources|App API > App Snippets"], ""),
        "decides": ("other: lets you extend any merchant store with custom JavaScript from the App Snippets section in the Salla Partners Portal", ["m:snippet_inject"], "The developer docs address the app developer; the snippet is injected when the app is installed."),
    },
    "app_settings": {
        "software": ("extension point (app)", ["i:api-resources|App API > Settings", "m:app_settings_dev"], ""),
        "decides": ("app developer (defines the settings); merchant fills them in", ["m:app_settings_dev"], ""),
    },
    "api_versioning": {
        "software": ("core (URI-versioned Merchant API)", ["m:ver_uri"], ""),
        "decides": ("platform at build (a new version only for breaking changes)", ["m:ver_breaking"], ""),
        "boundary": ("the version in the URI path; changelog", ["m:ver_uri", "i:api-resources|Merchant API > Change Log"], ""),
        "reason": ("to manage the impact of changes (stated)", ["m:ver_uri"], ""),
    },
    "developer_tooling": {
        "software": ("other: Dev Tools (the docs navbar groups Salla CLI, Partners Agent Kit and Salla Apps Playbook under it)", ["i:extension-points|docs navbar > Dev Tools", "i:extension-points|docs navbar > Salla CLI"], ""),
    },
    "report_builder": {
        "software": ("extension point (app): Report Builder in the Embedded SDK and the Partners portal", ["i:api-resources|Embedded SDK > Report Builder"], ""),
    },
    "accounting_erp": {
        "software": ("extension point (app): App Store categories Accounting & Finance and ERP system", ["i:extension-points|App Store category: Accounting & Finance", "i:extension-points|App Store category: ERP system"], ""),
    },
    "customer_data_rights": {
        "software": ("core (dashboard features for customer data export and account deletion)", ["i:other:dashboard-features|customer-data-export", "i:other:dashboard-features|customer-account-deletion"], ""),
        "decides": ("merchant; outside rules (Saudi Personal Data Protection Law)", ["m:pdpl_policy", "m:pdpl_scope"], ""),
        "legal": ("merchant (as controller of its customers' data)", ["m:pdpl_controller"], "Salla's help page lists the controller's duties under the heading for the merchant who sees its customers' data."),
        "boundary": ("the store's privacy page; apps may not collect sensitive data without explicit permission", ["m:pdpl_policy", "m:apps_no_sensitive"], ""),
    },
    "partner_store_access": {
        "decides": ("merchant (a staff permission manages support access requests)", ["i:other:staff-permissions|support_access_requests"], ""),
        "legal": ("partner (for the services it provides)", ["m:join_partner_resp"], ""),
    },
})

# extra evidence on existing overrides
SPEC["salla_payments"]["decides"] = (SPEC["salla_payments"]["decides"][0],
    SPEC["salla_payments"]["decides"][1] + ["m:sp_req_kyc_ae", "m:sp_review_ae", "m:sp_req_plan_kw", "m:sp_knet_kw", "m:sp_basic_cod_ae", "m:sp_applepay_auto"],
    SPEC["salla_payments"]["decides"][2] + " On the Basic plan only cash on delivery is available; Apple Pay is switched on automatically with mada and Visa.")
SPEC["epayments_balance_payouts"]["decides"] = (SPEC["epayments_balance_payouts"]["decides"][0],
    SPEC["epayments_balance_payouts"]["decides"][1] + ["m:kw_no_min", "m:tr_digital_payout"],
    SPEC["epayments_balance_payouts"]["decides"][2] + " Digital stores: invoices on Wednesday, payouts on Sunday.")
SPEC["epayments_balance_payouts"]["boundary"] = (SPEC["epayments_balance_payouts"]["boundary"][0],
    SPEC["epayments_balance_payouts"]["boundary"][1] + ["m:pay_cycle_balances"], "")
SPEC["store_balance_billing"]["decides"] = (SPEC["store_balance_billing"]["decides"][0],
    SPEC["store_balance_billing"]["decides"][1] + ["m:bank_complaint_block"], "")
SPEC["tax_settings"]["boundary"] = (SPEC["tax_settings"]["boundary"][0] + "; tax number and taxes shown on invoices and storefront by setting",
    SPEC["tax_settings"]["boundary"][1] + ["m:tax_invoice_display"], "")
SPEC["store_plan"]["decides"] = (SPEC["store_plan"]["decides"][0],
    SPEC["store_plan"]["decides"][1] + ["m:special_no_commission"],
    SPEC["store_plan"]["decides"][2] + " The Special plan page says Salla takes no platform commission on sales on top of payment gateway fees.")
SPEC["app_functions"]["decides"] = (SPEC["app_functions"]["decides"][0] + "; operator (free of charge during beta)",
    SPEC["app_functions"]["decides"][1] + ["m:af_beta_free"], "")
SPEC["app_store"]["legal"] = (SPEC["app_store"]["legal"][0], SPEC["app_store"]["legal"][1] + ["m:join_hosting_only"],
    SPEC["app_store"]["legal"][2] + " The partners policy says Salla provides only the infrastructure to host partner apps, without endorsing them.")
SPEC["licences"]["decides"] = (SPEC["licences"]["decides"][0] + "; outside rules (Saudi law named for apps and partners; e-commerce law requires customer-service details per market)",
    SPEC["licences"]["decides"][1] + ["m:apps_ksa_law", "m:join_ksa_law", "m:mkt_contact_law"], "")
SPEC["sanctions_screening"]["decides"] = (SPEC["sanctions_screening"]["decides"][0],
    SPEC["sanctions_screening"]["decides"][1] + ["m:apps_lawful_use"], SPEC["sanctions_screening"]["decides"][2])
SPEC["salla_markets_served"]["decides"] = (SPEC["salla_markets_served"]["decides"][0],
    SPEC["salla_markets_served"]["decides"][1] + ["m:plans_available_in"], "")
SPEC["legal_entities"]["boundary"] = (SPEC["legal_entities"]["boundary"][0],
    SPEC["legal_entities"]["boundary"][1] + ["m:llms_saas"], "Salla's own reference calls Salla a Saudi SaaS commerce platform.")
SPEC["data_location"]["legal"] = (None, ["m:llms_terms_first"],
    SPEC["data_location"]["legal"][2] + " Salla's own reference sends data-handling questions to its legal terms and privacy policy, which were not reached.")
SPEC["communication_apps"]["boundary"] = (SPEC["communication_apps"]["boundary"][0] + "; OTP login needs an SMS provider app from the App Store",
    SPEC["communication_apps"]["boundary"][1] + ["m:mkt_otp_provider"], "")

SPEC["customs_duties"]["boundary"] = ("setting: Taxes (taxes-and-duties); IOSS advised for EU sales to ease customs clearance", ["i:settings|Taxes", "m:tax_ioss"], "")
SPEC["wallets_other_methods"]["boundary"] = (SPEC["wallets_other_methods"]["boundary"][0], SPEC["wallets_other_methods"]["boundary"][1] + ["m:sp_paypal_ae"], "")
EXTRA_INV.append(("legal-agreements", "شروط وأحكام برنامج التسويق بالعمولة لباقات سلة القائم على إجمالي قيمة المبيعات للشريك العضو في البرنامج", "affplans_title", ["affiliate_program_terms", "partner_affiliate"]))

SPEC["partner_app_contract"]["boundary"] = ("a contract record attached to the app in the Partners portal (a 'SaaS contract' document requested for signature before publication)", ["m:app_saas_contract", "m:app_signable"], "Read from the record of the account used to capture the portal; the contract text was not read.")
EXTRA_INV.append(("legal-agreements", "SaaS contract _ individual _.docx", "app_saas_contract", ["partner_app_contract"]))

SPEC["data_location"]["decides"] = (None, ["m:apps_privacy", "m:pdpl_scope"], "Not shown. Salla's pages bind apps and partners to the Saudi Personal Data Protection Law and say that law covers processing of data about people in the Kingdom from anywhere; neither says where Salla stores or processes data.")
SPEC["partner_failure"]["decides"] = (None, [], "Not shown: no source read says who decides the fallback when a payment, shipping or other partner is unavailable.")

# Inventory entries linked to a concern after the placements are made, because the entry states the concern.
# These are legal agreements read in full (the partners.salla.com legal pages); their placements are unchanged.
_APPS = ("legal-agreements", "سياسة الشروط والاستخدام – متجر تطبيقات سلة")
_JOIN = ("legal-agreements", "سياسة الانضمام إلى برنامج شركاء سلة")
_THEMES = ("legal-agreements", "الشروط والأحكام لاستخدام متجر الثيمات – منصة سلة")
_AFF = ("legal-agreements", "اتفاقية استخدام برنامج التسويق بالعمولة")
_AFFPLANS = ("legal-agreements", "شروط وأحكام برنامج التسويق بالعمولة لباقات سلة القائم على إجمالي قيمة المبيعات للشريك العضو في البرنامج")
LINKS = {
    # each names the company that owns Salla, with its commercial registration where given
    "legal_entities": [_APPS, _JOIN, _THEMES, _AFF, _AFFPLANS],
    # joining policy art. 2; themes terms art. 3 and 11; affiliate-plans terms art. 3: partners must be licensed
    "licences": [_JOIN, _THEMES, _AFFPLANS],
    # apps terms art. 7 (app stopped or withdrawn on 15 days' notice); joining policy art. 4 (report serious faults at once);
    # themes terms art. 16 (response times when a theme fails); affiliate-plans terms art. 10 (no liability when payment gateway changes stop commission calculation)
    "partner_failure": [_APPS, _JOIN, _THEMES, _AFFPLANS],
}

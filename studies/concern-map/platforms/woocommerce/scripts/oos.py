# Out-of-scope rules for inventory rows that map to no concern: (list regex, entry regex, reason).
OOS = [
    ("^legal-agreements$", r"^(Woo trademark guidelines|Brand and logo guidelines)$",
     "Rules for using Woo's own trademarks and logos; no store concern is placed by them."),
    ("^legal-agreements$", r"^code-of-conduct$", "Community code of conduct for Woo events and spaces, not a store concern."),
    ("^legal-agreements$", r"^customer-research-agreement$", "Terms for taking part in Woo's customer research, not a store concern."),
    ("^legal-agreements$", r"^terms-conditions/woopayments-", "Time-limited WooPayments promotional offer terms; they set no standing placement."),
    ("^legal-agreements$", r"^Cookie Policy$", "Covers cookies on the WooCommerce.com website itself, not the merchant's store."),
    ("^other:plugin-page-features$", r"^Build on a platform that scales$", "A scalability claim on the plugin page; it names no concern with a placement."),
]

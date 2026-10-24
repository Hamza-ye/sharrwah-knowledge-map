# 8. Cross-cutting concepts

## Markets: the guard

Every decision states its outcome type (`METHOD.md` section 3a):
- **Built:** the same in every market;
- **Configured:** set per market or plan;
- **Chosen:** set by the merchant;
- **Context:** law, providers and the market.

No market's name appears in anything Built, and `python3 -I method/decision_status.py --guard` checks this.

## Money

- **Who holds it:** each payment method's provider, never Sharrwah, at launch (D-001, *proposed*).
- **Amounts:** each carries its currency as the money and currency foundation defines it, which is subject S-04. Where the amount agreed and the amount charged or settled are in different currencies, both are kept, with the rate used (D-002, *proposed*).
- **Ledgers:** two, one per owner. Entries are append-only and posted once, with reversal instead of edit (the payment seam's rule 19). The seller ledger records what is owed, and holds nothing. It posts only from live outcomes that succeeded, by keys that never expire (D-003, *proposed*).
- **Evidence for a payment:** each outcome carries where it came from: the provider's record, a courier event, a seller attestation or a buyer claim (D-002).

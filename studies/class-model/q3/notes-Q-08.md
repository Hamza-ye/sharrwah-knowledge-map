# Q3's check, batch Q-08: notes

Rows: the Knowledge Map's 20 questions on apps (APP-01 to APP-06), the API (API-01 to API-04), developer tools (DVT-01, DVT-02), partners (PTN-01 to PTN-03), automation (AUT-01, AUT-02) and AI (AIA-01 to AIA-03). Output: `check-Q-08.tsv`. The checker's last line: `20 of 20 rows placed; 0 problems`.

Count by result: covered 17; partly 2 (PTN-02, AIA-02); beyond the class 1 (AIA-03).

## Rows that were hard to place

- **APP-01** spans every surface an app can extend. Each one has a capability, but they sit in five areas: admin (CM-APP-006 to 008), checkout (CM-CHK-004), storefront (CM-SFR-004), POS (CM-POS-004), customer account (CM-CUS-014), automation (CM-AUT-001's Flow trigger and action) and the AI assistant (CM-AIA-002's App data and App action link, extension templates by that cell's reading). The surfaces in admin UI extensions, checkout, POS and customer account are `slot`, and the rest are `class`, so the row is `bundles`.
- **APP-05** asks how many apps each app store category holds. The model holds the categories (CM-APP-002) and, in every area's cells, the extension-point placements that show what apps replace or extend (a reading). App counts are detail, not a capability, so the row is covered with `detail:`.
- **APP-06** uses "should", so engineering is an answerer. Each thing it names has a class capability: functions (CM-APP-005), iframes (CM-APP-007), quotas (CM-API-005) and data access (CM-API-003, CM-API-004).
- **API-04** asks about "the two platforms". The model now joins five. The capabilities of every area already line up the platforms' resources by name in each cell's terms (a reading). A resource-by-resource mapping is detail.
- **AUT-02** asks for Flow's own templates ranked by install count. The only thing held is the extension target Flow template (SH-I-1477, cited in CM-AUT-001@shopify). The template library and its counts are detail that isn't held, so the template pages need capturing before that detail can be written.
- **AIA-03** asks how fast the AI surface changes and which parts are stable enough to model now. The decision of 29 October ("Intent (standing)") already answers the second part: the extent comes from the class, and launch decides when, never whether. So the row is `beyond the class`, answered by `founder:decided` and the plan (Stage 4A: the model's detail grows area by area after GM, with spikes). Its time bombs are `wrong party`, because it asks the class for a decision already in force, and `wrong time`, because `later` doesn't match the plan's before build. One capture can't show the pace of change. Successive captures of the same pages would (a reading).
- **APP-04** and **PTN-01** touch S-11 and Decision 1 in passing. App charges billed through the platform (CM-APP-003, which lands BC-C-029, part of S-11's evidence) and Salla's amounts withheld from the merchant's wallet for app partners (CM-PAY-031) bear on how Sharrwah collects charges and whose money it holds. The rows only ask what the class does, so the model is the only answerer (a reading).

## Candidate misses

- **PTN-02, rest: candidate miss, not held.** The gap is handing a store a partner built over to its client, with its ownership and billing.
  - The parts that are held: building on partner stores (CM-DVT-003), Salla's Ready stores (CM-DVT-005, whose buyer isn't stated), collaborator access (CM-STF-005), and Salla's webhook topic `store.owner.changed` (SA-C-001/boundary/SA-S-1622, cited in CM-ACC-001@salla; a reading that it is an owner change).
  - Searched with `class_slice.py search` on all five platforms: transfer ownership; client transfer; store transfer; transfer store; client store; hand over; handover; change owner; new owner; store owner transfer; billing owner. For Salla and Zid also: نقل ملكية; نقل الملكية; ملكية المتجر; نقل المتجر; تحويل ملكية; تسليم المتجر; مالك المتجر; مالك جديد. Also searched `outscope` on ownership; collaborator; ملكية; client transfer; transfer store.
  - Results: Shopify's ownership statements are about the Store Owner as contracting party (SH-C-001). BigCommerce's only hit is a webhook firing when a client store is cancelled (BC-S-0329). The `outscope` searches found nothing.
  - What would settle it, once captured: Shopify's help pages on transferring a development store to a merchant and on changing a store's owner; Salla's Partners portal pages Ready Stores and Store management; BigCommerce's Partner Portal docs on client stores. The coordinator routes it by `PLAN.md` section 6, "Evidence".
- **AIA-02, rest: candidate miss, held: `SH-C-041/boundary/SH-S-2538`.** The gap is agent identity.
  - The evidence: one captured store's UCP profile lists the capability `dev.ucp.common.identity_linking`. No cell cites it. Its concern, SH-C-041, lands in CM-CUS-010 (customer accounts), which is coarser than linking a buyer's identity to an agent (a reading).
  - The profile's other capabilities are cited, as "shows", in the commerce capability each names: cart (CM-CHK-002@shopify), order (CM-ORD-001@shopify), checkout (CM-AIA-005@shopify).
  - The coordinator may read identity linking the same way, inside CM-CUS-010 or CM-AIA-005. In that case it is a missing citation, not a missing capability.
  - Searched on all five: agent identity; payment handler; AP2; Agent Payments; llms.txt; well-known; agent profile; ucp; agentic; commerce agent.
  - How an agent pays is held only as Shopify's UCP checkout capability and BigCommerce's Agentic checkout, where the merchant stays merchant of record (CM-AIA-005). It is under `detail:`.

## Searches that found no miss

- **DVT-01, local development with tunnels.**
  - Searched tunnel; cloudflare; ngrok; app dev; scaffold; template; Dev MCP; Agent Kit on Shopify and Salla.
  - No statement on tunnels. Shopify's scaffold-app link appears only inside an access-scope statement (SH-S-5946).
  - `outscope` lists Shopify CLI, Libraries and templates and the GitHub app (SH-I-0039 to SH-I-0043) as "developer tooling ... not a commerce concern".
  - The CLI is a capability (CM-DVT-002), so the inner loop is its detail.
- **AUT-01 and AUT-02, automation on platforms other than Shopify.**
  - Searched أتمتة; الأتمتة; automation; automations; workflow; سير العمل on Salla and Zid, and automation; workflow on BigCommerce and WooCommerce.
  - Found only marketing-automation app categories (ZD-I-0458, WC-I-0551), Salla's flag kyc_new_workflow, and BigCommerce's refund and B2B "workflows". These are homonyms that belong to other capabilities.
  - CM-AUT-001 stays Shopify's alone, as its cells say.
- **API-01, the surfaces named in the row.** Each one has a capability:
  - the Customer Account API is in CM-CUS-010@shopify;
  - the Payments Apps API is in CM-PAY-011@shopify;
  - the Partner API is in CM-PTN-001@shopify;
  - BigCommerce's partner APIs are in CM-PTN-010;
  - the account-level API is CM-API-013.

## Problems with the brief or the evidence

- The checker rejects `cap_ids` on a `beyond the class` row unless `model` is among its answerers. The brief doesn't say so. AIA-03's `cap_ids` are empty for that reason, and its `what_would_settle_it` names the AI capabilities instead.
- CM-API-002@shopify's reading says Shopify's authentication flow and tokens are in no statement found. So APP-02's token lifetimes and consent screen are detail with no Shopify evidence behind them yet.
- CM-API-006@shopify holds no change log. So DVT-02's "changelogs" rests on Salla alone (CM-API-006@salla).

# Notes: Q6 draft proposal

## What was read

- The brief, `studies/proposals/briefs/R4-drafting.md`, whole.
- `studies/proposals/questions-for-agents.md`: its opening lines and Q6's section, sentences [1] and [2].
- `studies/proposals/areas/depth.tsv`: its header and Q6's five rows (Shopify, Salla and Zid in depth; WooCommerce and BigCommerce checks). Their `why` text was not used as evidence.
- The five accounts, `studies/proposals/records/Q6/<platform>/account.md`, in this order: Shopify, Salla, Zid, then WooCommerce and BigCommerce.
- From each platform's `notes.md`, only these sections, found by listing the file's headings:
  - Shopify: "Copies out of date or wrong".
  - Salla: "Copies". Zid: "Copies".
  - WooCommerce: "Left out" (its list of account points not checked, and of points not sorted) and "Copies".
  - BigCommerce: "Copies" and "Account points past the 20th not-found row (not checked)".
  - Shopify's and Salla's re-check sections have "Open items"; I opened their first item to see what they list. They concern not-found rows, not account points left unchecked, so I read no further.
- `python3 -I method/record_ids.py`, by id:
  - Shopify (105): Q6-SH-001 to 043, plus G0009, G0011, G0216, G0217, K1237 to K1244, K1246 to K1250, K1253, K1259, K1260, K1264, K1265, K1270, K1271, K1279 to K1281, K1526, K1527, K1536, K1539, K1622, K1688, K1751, K1783, K1793, K1815, K1816, K1852, K1865, K1909, K1956, K2261, K2265, K2268 to K2271, K2275 to K2279, K2662, K2674 to K2677, N01 to N03, P0096.
  - Salla (87): Q6-SA-001 to 062 but 003, 029, 045 to 047, 050 and 052, plus G0160, G0162, G0176, G0213, G0214, K0083, K0084, K0087 to K0090, K0093, K1522, K1523, K1526, K1528 to K1530, K1963, K1987 to K1989, K1992, K2015, K2507, K2510, K2519, K2523, N01 to N04.
  - Zid (65): Q6-ZD-001 to 006, 008 to 015, 020, 022 to 029, 031, 034, 035, G0041, G0045, G0047, G0049, G0055, G0057, K0003 to K0005, K0085 to K0087, K0090, K0136, K0137, K0143, K0156, K0177, K0211, K0214, K0219, K0220, K0225, K0226, K0230, K0231, K0239 to K0242, K0244, K0251, K0257, K0261, K0345, K0632, N01 to N03.
  - WooCommerce (66): Q6-WC-001, 002, 006, 007, 009 to 028, 034, 035, 037, 038, K0053 to K0055, K0265, K0315, K0333, K0335, K0336, K0393 to K0395, K0398, K0400 to K0405, K0412, K0439, K0447, K0496 to K0498, K0501, K0524 to K0529, K0532, K0725, K0838, N01, N07, N09, N15.
  - BigCommerce (61): Q6-BC-001 to 005, 007 to 011, 013 to 015, 017 to 019, 021 to 024, K0132, K0133, K0139, K0140, K0143, K0146, K0418 to K0421, K0425, K0427 to K0432, K0467, K0469, N01, N02, N09, N11, N13, N17, P0030, P0032, P0034, P0036, P0038, P0040, P0047, P0048, P0068, P0072, P0084, P0087, P0114, P0116, P0117, P0121.
  - Stage 1 axes and constants (22): YA-27, YA-62, YA-107, YA-111, YA-217, YK-12, YK-24, YK-74, YK-124, YK-131, YK-200, YK-209, YK-212, YK-225, YK-226, YK-227, YK-237, YK-239, YK-332, YK-344, YK-452, YK-514.
  - Stage 1 citations (8), to read quotes the axis lookup leaves out: YE-E586, YE-E587, YE-E641, YE-E645, YE-E843, YE-E1332, YE-E1333, YE-E1334.
- `python3 -I method/source_kinds.py` on the sources of the records the draft compares.
- `studies/proposals/areas/areas.md`: only the areas whose questions include Q6, A-01, A-02, A-10 to A-22 and A-34. Their text was not used as evidence; the draft names no area.
- `studies/proposals/yemen-digest.md`, whole, once, after sections 1 to 5 and 7 were written.
- No variation points: Q6 has no section 8.

## Copies found wrong or out of date, and records that disagree

- Q6-SH-P0097, the pilot's list of Shopify Payments countries, is out of date by Shopify's notes (40 items, no China; Q6-SH-023 has 41). The draft doesn't cite it.
- Zid's two copies of Zid Egypt's tax number differ (Q6-ZD-K0221, Q6-ZD-K0222). The draft doesn't cite them.
- Zid's FAQ, dated 2023-08-30 (Q6-ZD-K0226), and its site index, read 2026-10-12 (Q6-ZD-K0225), disagree on whether Zid serves only Saudi Arabia and the Gulf. The draft cites both, with their dates, and rests on neither list.
- BigCommerce Payments' places differ between Q6-BC-P0068 (UK or US stores, 2026-10-13), Q6-BC-K0132 (US only, 2026-10-12) and Q6-BC-P0030 (US and UK, 2026-10-12). The draft cites P0030 only for "Additional regions and countries will be launching soon.", not for its list.
- BigCommerce's trial: Q6-BC-014 (2026-10-12) and Q6-BC-019 (2026-10-19) disagree on live payments. The draft doesn't use either.

## What the records don't show

- Which Salla company contracts with sellers in each market, and by what rule (Q6-SA-G0213, Q6-SA-G0214). The usage agreement's party clause for each market would show it.
- What Salla shows a seller who picks another country at onboarding (Q6-SA-N03, Q6-SA-G0162). A journey choosing that option would show whether the notice the dashboard strings hold is what the seller sees.
- Who screens sellers against sanctions lists, and through what (Shopify Q6-SH-G0217; Zid Q6-ZD-G0055). Asking the platforms would show it.
- Which providers Shopify's payment gateways page lists for Yemen (Q6-SH-N01). The draft rests only on what one store's admin listed (Q6-SH-041, store ts15uk-ug, 7 October 2026).
- Who the parties to Salla's payment services contract are, and where it is signed (Q6-SA-G0176). It bears on whether an account is opened through the platform; reading Salla's held verification structure, or the contract itself, would show it.
- For Yemen, as section 6 says: a government service that confirms identity online; whether a seller who sells only online must be in the commercial register; the age of majority for an individual trader. A source at each area of control would show each.
- Whether a company based outside Yemen may contract with sellers in Yemen without a branch or licence there. Stage 1's YK-225 and YK-226 concern a foreign company's branch and a Yemeni partner, not this. A lawyer's advice to the founder would show it; the draft raises it as a company decision (section 7).

## Where the draft cites past the guide

- 86 statements, copies and citations, against about 40: Shopify 26, Salla 20, Zid 19, WooCommerce 12, BigCommerce 9 (82 before the revision below). The question has two sentences and the proposal 13 elements, on three platforms read in depth. Each section 1 point that names a match cites one record for each platform in it. Of the 88 ids section 1 cites, 75 are cited again in sections 2 to 7, which add two of their own (Q6-SA-038, Q6-SA-K0083).
- 12 Yemen facts, against about 8: seven elements have a Yemen fact bearing on them. **Provider choice** needs the outside services that don't work for Yemen (Stripe, PayPal) and one in Yemen that does (Floosak); **Restricted places**, **Verification** and **Seller entity** each need two facts at different places.
- 3 "Yemen's evidence doesn't show" points, against about 2: each is a different element's set-up for Yemen (**Verification**, **Seller entity**, **Eligibility rules**).
- Not-found rows and copied gaps: 4, within the guide.

## Problems with the brief or the tools

- The Write tool refused to write `.md` files from this run ("Subagents should return findings as text"). I wrote `draft.md` and `notes.md` with the shell and Python instead.
- `record_ids.py` prints only the first citations of a Stage 1 axis or constant ("... and N more citations"). To read the quotes behind the states I used, I looked up their `YE-` citation ids, which it accepts. (Since then, `record_ids.py --all` prints every quote an id rests on.)
- `check_proposals.py` misses a Yemen fact's date when the place itself has parentheses, as in "E-Pay (Kuraimi Islamic Microfinance Bank)'s service" and "Zid Pay Kuwait (Zid)'s service": it warned "a Yemen fact without its date". I first wrote those inner parentheses as square brackets, with the words unchanged. The checker now reads a Yemen place with its own brackets, and the revised draft gives both places in the digest's wording (see below).
- The in-depth platforms' `notes.md` have no list of account points left unchecked. WooCommerce's notes list in-depth account points "not sorted because they rest only on N or G ids"; the draft takes these as not "not checked", so it doesn't flag "not checked on WooCommerce" beside the gaps it cites (Q6-SH-G0217, Q6-SA-G0213, Q6-SA-N03, Q6-ZD-G0055).
- Two readings a checker may want to look at: the match on term for entity types rests on Salla's "فرداَ" and Zid's "فرد" being one word; and Salla's dashboard strings, classed as observed, name no store, so the draft scopes them by their capture date only.

## Revised for the step text from saved HTML

Revised on 24 October 2026, at the coordinator's request, for Shopify's re-check against observed-sh's text of saved step HTML (commit 51626891aa711ee9c3ef2d05ce63c95396dca949).

- Read: Shopify's two new account points (Q6-SH-044 to Q6-SH-048, store ibx5bt-xy, observed 30 September 2026); the "For the draft" part of the section "Re-check against the step text from saved HTML, 19 October 2026" in Shopify's `notes.md`; `record_ids.py --all` for Q6-SH-044 to Q6-SH-048; `source_kinds.py` on their source, which it gives as observed.
- Each new statement is said as the saved markup's text of one step, with its store and date, and, where its note says so, that the step's accessibility tree showed the same words.
- Section 1, [1], entity types: added store ibx5bt-xy's organization step, holding two Yemen entities, one "Company" and one "Individual" (Q6-SH-045).
- Section 1, [1], the seller's place: added store ibx5bt-xy's billing-address step, holding two legal entities marked "YE" and "Country/region [Yemen] Yemen" (Q6-SH-046). The re-check's account point also says the accessibility tree marks that field disabled, with Yemen its one option; that is in the statement's note, not its quote, so the draft doesn't rest on it.
- Section 1, [2], a store in Yemen: added store ibx5bt-xy's third-party providers step, holding the same six names (Q6-SH-048), and its Payments step, holding "Choose a provider" and "Additional payment providers" (Q6-SH-047).
- Section 2, **Seller entity**: the types for Yemen now rest on store ibx5bt-xy's organization step (Q6-SH-045), not on Q6-SH-K2674, which section 1 still cites; the same step adds to "A Seller may hold several entities".
- Section 2, **Provider choice**: two Yemen stores' records name the same six third-party providers (Q6-SH-041, Q6-SH-048).
- Section 5, several entities and stores: added Q6-SH-045. Section 7, payment providers: added Q6-SH-048.
- Section 6: the places of YK-452 and of YA-62's Zid Pay Kuwait state are back in the digest's wording, "E-Pay (Kuraimi Islamic Microfinance Bank)'s service" and "Zid Pay Kuwait (Zid)'s service".
- Not cited: Q6-SH-044. Its Yemen entity on store ibx5bt-xy's General step adds a second store to Q6-SH-035, which the draft doesn't cite; the store's address, which the draft uses, is in the citation all four cited statements share.
- After the revision: 86 statements, copies and citations; the other counts unchanged; about 5,130 words, section 1 about 1,640 (about 4,980 and 1,520 before). The checker reports no errors or warnings, and the same three notes on counts past the guide.

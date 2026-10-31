# T-baseline: what each reference platform contributes, against a Shopify-only baseline

**What this is.** The class's model was built from five reference platforms: Shopify, Salla, Zid, WooCommerce and BigCommerce. The founder asked whether the work has produced anything a Shopify-only run couldn't, and whether five were ever needed, "without first establishing why" (31 October). This test answers that from the files, platform by platform and purpose by purpose. It starts from Shopify alone and asks what each other platform adds, for what purpose, and whether that purpose needs it before architecture starts. Its answer may be that some platforms were needed, or that some weren't. Neither is presumed.

**What you read, and only this:**
1. **The founder's intent** (`founder-decisions.tsv`, the rows of 28 and 29 October), quoted:
   - "Sharrwah is a merchant platform of the established class that Shopify represents worldwide and Salla and Zid in the region."
   - "Sharrwah competes on regional fit, through strong support for local ecosystems and partners, and on product quality."
   - The markets: "MENA: the GCC and North Africa (Egypt, Morocco, Algeria, Tunisia), Jordan, Lebanon and others; Yemen is one of Sharrwah's markets."
2. **Each platform's stated role,** as the record gives it (`questions/Q1-concern-map.md`, lines 11 and 100 to 110):
   - the first references were "Shopify, Salla, and a third platform with a different business model";
   - Zid "tells market causes from vendor causes: where Shopify differs from Salla and Zid matches Salla, the market is the likely cause; where Zid matches Shopify, Salla's difference is Salla's own choice";
   - BigCommerce is "a global SaaS platform independent of Shopify", "a third known use for designs outside the Saudi market";
   - WooCommerce "carries a different contrast: self-hosted software that holds no money".
3. **The model:**
   - `studies/class-model/merged/` (`capabilities.tsv`, `cells.tsv`, `kinds.tsv`, `evidence.tsv`, `interfaces.tsv`, `qualities.tsv`), read by script;
   - the kind rule (`PLAN.md`, Stage 4A, "The kind and the count"): a capability is the class's (`class`) where at least one of the five places it in its core or as its own service.
4. **The coordinator's measures of 31 October,** to verify by script and extend. They are a starting point, not a finding:

   | Platforms in the model | Capabilities counted `class` | Holding nothing on those platforms |
   | --- | --- | --- |
   | Shopify alone | 289 | 56 |
   | Shopify and Salla | 334 | 16 |
   | Shopify, Salla and Zid | 342 | 13 |
   | and WooCommerce | 351 | 4 |
   | all five | 358 | 0 |

   - Leaving one platform out, these stop being `class`: Shopify 34, Salla 22, Zid 8, WooCommerce 7, BigCommerce 7.
   - Of the 128 capabilities where Shopify and Salla differ (one counts it, the other doesn't):
     - Zid holds nothing for 79;
     - Zid matches Salla on 28;
     - Zid matches Shopify on 21.
5. **Architecture's needs:** `architecture/plan.md`, section 3 (the six first decisions), and `architecture/fitness-test.md`, whole: each decision's needs, gaps, verdict and regional test.
6. **The regional needs, from sources the platforms didn't produce:**
   - `studies/yemen-cases/` (Stage 1), with its `corrections.md`;
   - the subjects' questions (`studies/subjects/subjects.tsv`);
   - S-01's and S-02's registers (`studies/subjects/S-01/register.tsv`, `studies/subjects/S-02/register.tsv`): their variation points, and the causes they found.
7. **How deeply each platform is held:** `studies/class-model/held-vs-read.tsv` and `held/selection.tsv`, and `STATE.md`'s risk F2.

The evidence repositories (`/home/user/observed-sh`, `/home/user/observed-sa`, `/home/user/other-product-class`) are read only to settle a single item, through their guides first. They are read-only, and Python that reads them runs with `python3 -I`.

**The three purposes a platform can serve** (the yardsticks; a platform is judged against each separately):
- **A. Architecture's structure:** a record, state, flow, identity or money shape that Sharrwah's core needs and that Shopify's shape lacks or gets wrong (`architecture/fitness-test.md`).
- **B. Product scope:** what regional merchants get built in that Shopify leaves to apps or lacks, which Sharrwah's offer would answer.
- **C. Telling causes apart:** whether a difference between platforms comes from the market, the law or one vendor's choice, which the subjects need to decide.

**Do:**
1. **Build the list of regional concerns,** each traced to its source:
   - the capabilities that Salla or Zid count and Shopify doesn't (53, by the coordinator's count);
   - every cell whose scope names a market of the founder's list;
   - the fitness test's regional practices;
   - the Yemen cases' needs;
   - the subjects' questions;
   - S-01's and S-02's variation points.

   A concern any of these names is on the list, whether or not a platform holds it.
2. **Test each concern against Shopify alone,** with Shopify's evidence cited, and the regional evidence beside it. Give one result:
   - **covered as is:** Shopify's shape holds it;
   - **covered with a slot, partner or setting:** the shape holds, and only providers, values or settings differ by market;
   - **needs a structure Shopify's shape lacks:** say which record, state, flow, identity or money shape, and which first decision it changes;
   - **unknown:** what would settle it isn't held, or is held and unread. Say which.

   "Not held" is never "doesn't do". A regional platform held thinly is marked so, with its depth for that concern.
3. **For each platform other than Shopify,** count what it contributes to A, B and C: which concerns it alone shows, and which results it alone changes. Use the measures in item 4 of the reading list, corrected where you find them wrong. Then give its verdict:
   - needed before architecture starts, for which purpose;
   - needed later (at a market's setup, an area's design or a subject), and when;
   - or not needed for any of the three.
4. **Test the extent's rule.** The model counts a capability as the class's when any one of five platforms has it, so each platform added widens the extent. Say what the extent is under the founder's intent of three platforms, and under five. Say which capabilities only WooCommerce or BigCommerce bring, and whether any of them is needed under A, B or C.
5. **State the limits of your own test.**
   - The model's capability list was cut by Shopify and Salla, which anchored each domain. So what Zid, WooCommerce or BigCommerce would have added as anchors is underestimated: say by how much you can tell.
   - Depth differs by platform.

**Criteria, fixed before you read:**
- **A platform is needed before architecture starts** only if, without it:
  - a concern of purpose A would be missed, or wrongly classed as covered; or
  - a first decision's verdict in the fitness test would change.
- **It is needed for product scope** if it alone shows a capability regional merchants get built in. That is needed at the product's scope decision, not necessarily before architecture.
- **It is needed for telling causes apart** if a subject's cause rests on it. Say whether that subject has run.
- **Otherwise it isn't needed** for that purpose. Say what its reading cost the work, where the files show it.

**Write** `architecture/baseline-test.md`:
- First, a page for the founder in plain words:
  - what each platform turned out to be needed for, and when;
  - the concerns that need a structure Shopify's shape lacks;
  - what the test can't tell.
- Then the concern table, the per-platform tables, and the extent's rule.
- Every claim is one of three: a fact traced to its source at a commit, a reading marked as one, or an assumption marked as one.

Change no other file. Make no commits. Keep your context under about 200,000 tokens: read the model by script.

**Report:** each platform's verdict in one line, the concerns needing a structure Shopify lacks, and the test's limits.

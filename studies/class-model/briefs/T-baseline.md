# T-baseline: what Sharrwah would get wrong if it were built from Shopify alone

**What this is.** A test that starts from Sharrwah's purpose and from Shopify alone. It asks a small number of decisive questions: where building Sharrwah from Shopify's shape alone could make it fail, or be expensive to change, in the markets its founder named. For each question it finds whether Shopify's shape is enough, and if not, which evidence shows what more is needed. It is not a catalogue. It is kept narrow on purpose.

It runs in two phases:
- **Phase 1** writes the questions only, and stops. The founder sees them and may cut or add, before any is answered.
- **Phase 2** answers them.

**What you read, and only this.** Nothing else in this repository is an input. That includes its plan, its state, its model of the class, its architecture plan and its earlier tests, so that the work's own assumptions can't steer this test.
1. **The founder's decisions:** `founder-decisions.tsv`. Read the rows that say what Sharrwah is and does: its intent, its markets, its scope, who holds sellers' money (Decision 1, with E1, E2 and the defaults), and the guard on money. These say what Sharrwah needs. They are never evidence of what a platform does.
2. **The Yemen cases:** `studies/yemen-cases/`, with its `corrections.md`, for one market's realities read from its own sources.
3. **The evidence,** only to answer a question, and only in phase 2. It is held in:
   - the evidence repositories `/home/user/observed-sh` (Shopify), `/home/user/observed-sa` (Salla) and `/home/user/other-product-class` (Zid, WooCommerce, BigCommerce);
   - this repository's own captures, in `evidence/`.

   Go through each repository's own guides first: its `README.md`, `docs/READING.md`, `structures/REGISTER.tsv` and `index/`. The repositories are read-only. Run Python that reads them with `python3 -I`. `method/corpus_search.py PLATFORM TERM ... --brief --max 3` searches what each platform holds.

## Phase 1: the questions

Write at most 15 questions. Each question must be one where building Sharrwah from Shopify's shape alone could make it fail in its markets, or force an expensive change later. "Expensive" means a change to how money is held or recorded, to identity, to how stores are kept apart or where their data lives, to how orders, payments or deliveries flow, or to how the platform meets a market's law.

Draw them from:
- the founder's decisions;
- the Yemen cases;
- what you know of commerce in the founder's markets. Mark that as a reading or an assumption.

Before you look at any platform's evidence, write each question with:
- **the question,** in one plain sentence;
- **why it could sink Sharrwah, or cost dearly to change,** in one or two sentences;
- **the markets it bears on;**
- **what you expect Shopify's shape to be,** marked as an expectation, not a finding;
- **what would settle it:** which platform's evidence, and which kind of source (its admin, its developer documentation, its terms, its help), or a market's law, which no platform's evidence settles.

Leave out:
- a question about a feature that can be added later without changing the core;
- a question whose answer only fills a value, a provider or a partner into a place Shopify's shape already has.

Name both of these as kinds you excluded, with one example each.

Then write one paragraph: which of the four other platforms you expect each question to need, and why. A question may need none.

**Write** `architecture/baseline-test.md` with phase 1 only, and stop. Report the questions, one line each.

## Phase 2: the answers (only when the coordinator says so)

For each question, after the founder's cuts and additions:
1. **Shopify first.** What Shopify's own evidence shows, cited at its commit with its quote.
2. **Then whether that is enough for Sharrwah:**
   - enough as it is;
   - enough with a partner, a provider or a setting, filled per market;
   - not enough: what record, state, flow, identity or money shape is missing, and in which market.
3. **Then the other platforms,** only as far as the question needs them: what Salla's, Zid's, WooCommerce's or BigCommerce's evidence shows that Shopify's doesn't, cited.
   - Say which platform's evidence was needed to see each thing, and which added nothing.
   - "Not held" is never "doesn't do". Where a platform is held too thinly to tell, say so.
4. **Then what no platform shows:** what only a market's law or practice decides. Say so, and don't guess it.

**At the end of phase 2:** one page in plain words for the founder:
- what Sharrwah would get wrong from Shopify alone;
- which of the other four platforms were needed to see it, and for which question;
- what no platform can tell, and only the markets' law or practice can.

Every claim is one of three: a fact traced to its source at a commit, a reading marked as one, or an assumption marked as one.

Change no file but `architecture/baseline-test.md`. Make no commits. Keep your context under about 200,000 tokens.

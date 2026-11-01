# Plan: Sharrwah built on Shopify's model

**The aim.** Sharrwah is built on Shopify's model (the founder's decision of 1 November 2026, `founder-decisions.tsv`). Product line engineering frames the work (Pohl, Böckle and van der Linden 2005; Clements and Northrop 2001):
- **Building the platform:** what is common, taken from Shopify's shape (its records, flows and extension points), with a variation point wherever markets differ: a place built to take different values.
- **Setting up a market:** filling those places with that market's providers, law and limits, as data or plug-ins, when the founder decides to set the market up. A market's setup never defines the platform.

**The method.** Established practice, nothing invented:
1. **Shopify's shape is read at its source,** in `observed-sh`, through its own guides first: its admin schema, webhooks, admin routes, help, terms and engineering writing. Every claim is one of three:
   - a fact, cited at a commit with its quote, which `method/check_report.py` checks;
   - a reading, marked as one;
   - an assumption, marked as one.

   A condition, such as a plan, a beta or a market, is read at the source every time.
2. **Each decision is an architecture decision record** (Nygard 2011), one page for the founder's veto: its context, the decision, what varies by market and where that variation sits, what it costs to change later, and the alternatives.
3. **What varies by market** gets a variation point. Each names its mechanism (data, a plug-in or a module) and when it is bound: in design, in configuration, or at a market's setup. A law's place is built once, and each market's law is data in it.
4. **Where a decision turns on a quality,** it states the quality scenario it meets (ISO/IEC 25010; attribute-driven design, Cervantes and Kazman 2016), in the founder's order of 29 October.
5. **A decision is taken when something that rests on it is about to be built,** not before (the last responsible moment, Poppendieck and Poppendieck 2003). Every step ends in a decision for the founder, or it doesn't run.

**The steps:**
1. **Derive the first decisions:** the concerns every area depends on. They come from two sources, each cited: Shopify's shape, read at its source, and established practice for platforms that many businesses share. The list the coordinator gave on 30 October was its own, carried the old frictions, and was checked against neither (`decisions/first-decisions.md`).
2. **Review the earlier decisions** (`founder-decisions.tsv`, the review column) against those first decisions. For each, product line engineering says whether it belongs to the platform, to a market's setup, to the method, or to the founder's own list, and when it binds. It stays if it still holds. Decision 1 and the decisions built on the same frictions go first, for the risk that Yemen's concerns enter the platform at the wrong time. The result is one page for the founder.
3. **The first decisions,** one record each, read from Shopify's shape.
4. **Then building.** A spike, meaning code thrown away after it answers one stated question, is allowed where a decision raises a question only code can answer. Production code waits for the decisions and their documentation (the founder, 24 October).

**Risks, and what is done about each:**
- **Sharrwah inherits only the variation Shopify needed.** Where a market needs a place Shopify's shape lacks, Sharrwah adds one, case by case, named in the decision that meets it.
- **Shopify's shape is read wrong.** Every claim is cited at its source, and conditions are read there. The accuracy probe found the old model's conditions wrong in 12 of 100 cells (history, `9f3749d0`).
- **The work grows again.** Nothing stays because it cost something. A step that ends in no decision doesn't run, and each decision reports its cost (`method/count_tokens.py`).
- **Old frictions come back through earlier decisions.** Step 2 reviews them before any first decision is recorded.

**Who decides:** as the founder's decisions say. The founder decides business questions. Engineering decides the rest, and the founder may veto any of it.

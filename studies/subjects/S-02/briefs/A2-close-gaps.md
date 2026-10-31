# Brief: S-02, closing one platform's gaps on the variation points (step 1, phase A2)

This is `PLAN.md` Stage 4, subject S-02. It runs after phase B's first pass, and after your platform's absence audit (phase A3). You are one agent with one task: one part of one platform's gap-closing. The message that started you names the platform, the variation points or kinds your part takes, any leads to read, and the last ids the previous part of your platform used. A platform's parts run one after another, each continuing from the files the last one left.

**Read only:**
- this brief;
- `briefs/A-one-platform.md`, whose inputs, tools and rules you follow for anything you record. Its stop at 300 statements counts only the statements you add;
- your platform's files in `studies/subjects/S-02/<platform>/`. Look rows up with scripts or `grep`, and don't load a large file whole;
- `studies/subjects/S-02/variation-points.tsv`, and the rows of `studies/subjects/S-02/variants.tsv` for your platform only (`awk -F'\t' '$3=="<platform>"'`);
- the held and live sources the steps below point you to.

## The task

**Your rows.** Of your platform's rows in `variants.tsv`, under the points or kinds your message names, take each whose `variant` is:
- `not covered`; or
- `gap`, where one of its gaps is of kind `page not read`, or names in its `route` a page not yet read.

Leave a `gap` row whose gaps are routed to a capture request (`who_can` `capture`) or to the founder, or were all confirmed by the absence audit (`absence-audit.tsv`, result `confirmed`).

**Group them** by what their points ask about, so that one set of searches serves the rows of one group:
- under (c) and (f), by the kind, first in `x_words`;
- under (a) and (b), the store's own country is one group; under (d), the countries served; under (e), a market;
- rows that share a gap are one group.

**For each group:**
1. **Search the held corpora** with `python3 -I method/corpus_search.py <platform> <terms>`, two searches:
   - **first, the group's own phrases:** the kind's head word, as a term even when it is one word (such as `domain` or `currency`; our longer labels, such as "who sells to the buyer", are ours, not the platform's, and aren't searched; a kind whose name is all ours has no head word, and its phrases are its terms; a name of two words, such as "store status", is searched whole), and the kind's phrases from `x_words` and from your platform's `terms.tsv` and statements, each kept whole as one term, such as `"guest checkout"` or `"customer accounts"`, in every language your platform uses. Any other single generic word, such as "checkout" or "site", goes only after `--with`, beside the kind's name;
   - **then, the same terms with `--with market markets country countries`,** and your platform's own words for a market and a country.

   Read the titles and snippets. Past its cap, the tool lists only addresses: rerun with `--max` at the number of documents its last line reports, up to 300. Past 300, narrow the search by its terms, and say in `notes.md` how you narrowed it.
2. **Read every listed document** that could state who or what fills the group's points, and the pages in its gaps' `route`. Run `method/held_index.py` on an address before you read it live.
   - **Finding pages that aren't held:** follow links from the documents you read, the docs' own navigation, or the site's sitemap, as the absence audit did. Name each in `read`. Don't use a general web search.
   - **Reading live,** for this phase in place of phase A's "From what is recorded" limit, on your platform's own sites:
     - Shopify: help.shopify.com, shopify.dev, shopify.com;
     - Salla: salla.com, help.salla.sa, docs.salla.dev, salla.dev;
     - Zid: zid.sa, help.zid.sa, docs.zid.sa, zid.eg;
     - WooCommerce: woocommerce.com, developer.woocommerce.com, woocommerce.github.io, wordpress.com's support and legal pages, automattic.com, and stripe.com's pages for WooPayments;
     - BigCommerce: bigcommerce.com, docs.bigcommerce.com, developer.bigcommerce.com, support.bigcommerce.com, commerce.com.

     Read a page as phase A says ("Reading a live page"). A page you can't read, behind a login or a bot challenge, goes in `read` as not read.
3. **Record what you find** as new statements, continuing your platform's `stmt_id`s and `cite_id`s, under phase A's rules. Record everything you find that bears on S-02's bullets, even when it fits a point your platform already answers. Give it the scope the source states. Each statement you add names the point it was found for in its `note`.
4. **Where nothing states it:**
   - where a complete list shows it absent, record an absence. The coordinator has the absence audited (phase A3);
   - where a page likely to state it couldn't be read, record a gap of kind `page not read`, whose `route` names that page;
   - otherwise record a gap of kind `searched, not found`. Its `read` names each `corpus_search.py` command you ran and each document you read.

   One new gap per point at most.

   A new gap takes `who_can` `founder`, and its `route` says what would close it: a page, an observation of the admin, or a question to the platform. The coordinator decides whether it becomes a capture request.
5. **A `page not read` gap whose pages you have read doesn't remain:** record what the pages state, or a new `searched, not found` gap in its place.
   - *(The coordinator's own, 27 October 2026:)* the same holds for any gap your part is told to close, such as one routed to a capture request whose runs are now held. If what you record answers all the gap asks, the statement that answers it says `answers S02-XX-Gnn` in its `note`, and the gap leaves its `a2.tsv` row's `gap_ids`. If it answers part, a new gap whose `what_is_missing` starts `in place of S02-XX-Gnn` says what is still missing. The checker takes either as settling the old gap, whose row stays as it is.
6. **Leads.** Read each lead the message names. Record what it states as statements. Give it an `a2.tsv` row where it answers a point. Otherwise, list it in `notes.md`, and give its statements and any gap you record for it a row whose `vp_id` is `none`. A gap under (h), which has no variation point, takes that row too. Where it bears on a gap routed to a capture request, name that request in the statement's `note`, so the coordinator can narrow it.
7. **Don't change existing rows,** with one exception. Phase A's rule for (h) applies to what you add: an existing (h) statement whose arrangement one of your new statements describes takes its `stmt_id` in `conditions`, for statements under (a) to (f) only. If that column is `none stated`, the ids replace it.
8. **Write as you go.** Write each point's row in `a2.tsv` as soon as its group is settled, so that if you are stopped, the next part continues from your files.

## Output, in `studies/subjects/S-02/<platform>/`

- **In your platform's phase A files:** the new statements, citations, terms, absences and gaps, appended.
- **`a2.tsv`:** one row per variation point you worked on. It is tab-separated, with a header row and no quoting. If it exists, append to it. Where an earlier part's row already holds your point, update that row instead: add your statements and what you read, and in `gap_ids` replace the gaps you settle with any that take their place. Columns, each list `;`-separated:
  - `vp_id`, or `none` for a lead's statements, or a gap under (h), that answer no variation point;
  - `stmt_ids`: the statements you added for it;
  - `gap_ids`: the gaps that remain for it, the ones you recorded among them;
  - `absence_ids`: the absences you recorded for it;
  - `read`: each `corpus_search.py` command you ran for it, and each document you read: a held copy by its path, with its commit after the repository's name (`<repository>@<commit>:<path>`), and a live page by its URL and the date you read it.
- **`notes.md`:** a section headed "Gap-closing (phase A2)", or your part's subsection under it:
  - what you found, by group;
  - searches you narrowed, and how;
  - the leads you read;
  - problems with the method.

**Before you finish,** check your platform's files on a copy that holds only them, as phase A's brief says. Fix every line of level `error` on what you added or changed. `pending capture` lines are live pages the coordinator captures later, and a `review` line for an absence you recorded waits for its audit: leave both.

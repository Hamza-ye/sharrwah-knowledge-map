# Brief: the class's model, its extent

**What this step is for.** A product map of what the five reference platforms establish: Shopify, Salla, Zid, BigCommerce and WooCommerce. It lists their capabilities, and for each, what each platform shows and where it puts it. It records what the platforms do, in their own words. It decides nothing about Sharrwah, ranks nothing, and drafts no design.

**How it is built.** This is exemplar-based domain analysis: the model is built from representative systems, then checked and extended against others.
1. **The scope:** one part assigns every concern of the five platforms to one domain.
2. **Per domain,** in this order:
   - **the anchor:** Shopify and Salla together, the two platforms with the most statements (3,005 and 2,560). The structure follows their own groupings;
   - **the mapping:** WooCommerce, then Zid, then BigCommerce, one platform per part, each mapped onto the domain's model so far. Where a platform shows something the model doesn't, it adds a capability, so the model stays the union of the class;
   - **a back-fill after each mapping part that adds capabilities:** the cells those new capabilities need for the platforms mapped before it, so the order of the mapping doesn't bias the counts.

You are one agent with one part. Your message names it: `scope`; or, for a domain A to G, `<domain>-anchor`, `<domain>-woocommerce`, `<domain>-backfill-woocommerce`, `<domain>-zid`, `<domain>-backfill-zid`, `<domain>-bigcommerce`, `<domain>-backfill-bigcommerce`, or `<domain>-amend` for concerns moved into a domain after its parts ran. The parts' folders are the model: the coordinator checks your rows, and any correction after review is made in the part's own files and noted in its `notes.md`. An agent that made none of them reviews them.

## What the concern map holds

Q1's concern map, in `studies/concern-map/`, is your evidence. For each platform, in `platforms/<platform>/`:
- `concerns.tsv`: the platform's concerns, each with its own terms (`platform_terms`);
- `statements.tsv`: the platform's own words, verbatim, each under one of five placements, the question it answers:
  - **where:** where the platform puts the concern in its own organization: an admin section and route, an API group, an app or extension target, a separate host or product, a code path;
  - **decides:** what turns it on or off, limits it or sets its value: eligibility, entitlements, plan lines, settings, staff permissions;
  - **responsible:** what the terms, policies and legal-entity records state;
  - **boundary:** how it meets the rest: API resources, webhook topics, access scopes, extension targets, events;
  - **reason:** a reason the platform states.

  Each statement has a scope where the platform states one, such as a plan or a country. Q1's rule 5: "No inference goes into a statement. A note may hold inference marked as such, and it never counts";
- `gaps.tsv`: a placement with no statement, with its kind (`page not read`, `observation needed`, `searched, not found`, `stated only in general terms`).

Beside them: `matches.tsv`, Q1's matches, and `unclear-matches.tsv`, its unclear candidates (columns `why_unclear` and `what_would_settle_it`). Both cover Shopify, Salla and WooCommerce only. Zid and BigCommerce were never matched.

**A statement's key** is `concern_id/placement/first_cite_id`, such as `SH-C-025/where/SH-S-5170`. You cite every statement by its key.

**Read only through the script.** Never load the concern map's files whole. `method/class_slice.py` prints what you need (`python3 -I method/class_slice.py --help`):
- `seed --domain D`: the domain's areas, with Shopify's and Salla's own groupings, from `studies/class-model/seed/km-areas.tsv`. They are leads for the area, not evidence. Leave out the seed's questions;
- `concerns --platform P --domain D`: your concerns, with the Q1 matches and unclear candidates that hold each, then those of other domains that name yours under `also`, which you may cite but never land. Add `--where` for each concern's `where` identifiers;
- `statements --platform P --concerns ...`: each statement by key, with its identifier, its first 200 characters, its scope, and a flag where its note holds inference. Use `key KEY ...` for statements whole;
- `search --platform P --terms "a;b"`: every statement of the platform holding a term, in any concern;
- `matches --concerns ...` and `gaps --platform P --concerns ...`;
- `outscope --platform P --terms ...`: inventory entries Q1 left unplaced, such as store limits, cited by their inventory id;
- `model --domain D`: the domain's model as written so far, your own part's rows included;
- `homonyms`: Q1's list of the same word naming different things.

**What you cite.** Only the concern map's statements, by key, and, for a quality only, an unplaced inventory entry by its id. A cell cites statements of your domain's concerns and of those that name your domain under `also`. A search may find a statement of a concern in another domain that doesn't name yours: cite it only where the cell needs it, and say why in the cell's `reading`; the checker flags it for the reviewer, since one statement shouldn't support capabilities in two domains. Context read beyond the statements, in the structures they cite, informs a reading and is never cited. A statement you need that isn't held goes in your notes as a gap. The copies behind the citations are in the evidence repositories at the commits `citations.tsv` gives, in this repository's capture runs (`evidence/product-class/runs/*/manifest.tsv`, by URL), and in the WooCommerce release at `/home/user/woocommerce-release/11.2.1`.

## The scope part

Assign every concern of the five platforms (652) to one domain, A to G, in `studies/class-model/scope.tsv`. The domain of a concern is what the concern is about. Use its name, its `platform_terms`, its `where` statements and the Q1 matches that hold it (`concerns --platform P --all --where`), with the seed's domains and areas as leads (`seed`). Read a concern's matches before you assign it, so a match's concerns are placed together, not named apart afterwards.
- **One domain per concern.** A concern about several domains goes to the domain of its main subject. List the others under `also`; their parts may cite its statements.
- **A Q1 match keeps its concerns in one domain.** Where one of them is mostly about another domain, it goes there, and its `reason` names the match.
- **Domain H takes nothing.** It is beyond the references.
- **The channel doesn't set the domain.** A concern delivered through an app store is in the domain of what the apps do. Domain F holds the app and API platform itself: apps and extensions as such, the API's conventions, authentication, versioning and limits, webhooks as a mechanism, developer tooling and partners. A feature's own API goes with the feature: a storefront API with the storefront, a recurring-payments API with what it charges for.

Columns: `platform` · `concern_id` · `domain` · `also` (other domains, `;`-separated, or empty) · `reason` (one line: the terms or `where` place that decide it, and any match it splits). Each row is a reading. Write as you go, platform by platform.

## The anchor part

**Take** Shopify's and Salla's concerns that `scope.tsv` gives your domain. Read their statements under every placement, their gaps, and the Q1 matches and unclear candidates that hold them.

**Build capabilities.** A capability is something a store or the platform can have or not have.
- **Join** concerns that are the same thing on both platforms: by a Q1 match, by their own terms, by the same identifiers, or by the same definition, quoted from both.
- **A shared term joins only where** the cited definitions or identifiers show the same object. The same word for different things stays apart, and goes in your notes with both sides' keys. Q1's matching found six such cases (`class_slice.py homonyms`).
- **Where the two platforms' definitions show the same role under different names,** you may join them on role. That join is a reading: say why in `reading`, and cite both sides' keys.
- **Where they cut at different grains,** you choose the capabilities, using `parent` where one holds others, and say why in your notes. A Q1 match with several concerns on one side is a difference of grain, not one capability.
- **Each permission, webhook topic, access scope or plan line** is evidence for a capability. The platform's permission system, webhooks, scopes and plans are themselves capabilities, in their own domains.
- **The name** uses both platforms' terms, or a neutral term that names both.
- **The area** is the `area_id` of your domain that the capability is about. The seed's groupings are leads. The channel never sets it: an app-store category doesn't make a capability APP's. A capability shown under one market's scope stays, with its scope.
- **Numbering:** `CM-<area>-nnn`, from 001 in each area.

**Land every concern you take exactly once,** in `landings.tsv`: in the capability it is, or in the parent where it is coarser than the capabilities. A cell may cite statements of a concern landed elsewhere. A concern that belongs to another domain lands as `moved:<domain>`, with the reason, and the coordinator moves it.

**Write a cell for every capability and both platforms,** with its evidence (below). Where a platform's statements show nothing for a capability, search them (`search`) in every language they use, and write `none-held` with the terms you searched. The search ignores case, diacritics, hamza seats and tatweel, and reads ة as ه and ى as ي. A broken plural is another word, so search each Arabic term in its singular and its plural, with and without ال.

**Rule on every unclear candidate that holds a Shopify and a Salla concern,** one of which you land, in `rulings.tsv`. Its `keys` are the statements of each side that stand for what the candidate asks about. Then `joined:<cap_id>` where one capability's cells cite keys of both sides; `nested:<cap_id>` where that capability cites one side's and a parent of it the other's, a finer part of a coarser thing; or `apart`, where no capability cites both. Write one row per pair of concerns, with keys from those two concerns only. Where `scope.tsv` puts the other concern in another domain that names yours under `also`, a capability here may cite it, and the ruling follows the cells, with the basis naming its domain. Otherwise the ruling is `apart`, with the basis "scope.tsv gives <concern> domain <X>". You rule on the Shopify–Salla join only; WooCommerce's part rules on its own concerns' joins.

## The mapping parts

**Take** your platform's concerns that `scope.tsv` gives the domain, and read the domain's model so far (`model --domain D`): the anchor and every earlier mapping part.
- **Land each concern once:** in a capability of the model so far, where it is the same thing by a Q1 match (WooCommerce only), terms, identifiers or definition (a join on role is a reading, citing both sides); or in a new capability that only your platform shows so far, numbered past the model's highest in its area. Where a fit is strained, mark it `strained`, and say what doesn't fit, so the reviewer can split it.
- **Write your platform's cell for every capability of the model so far,** and for your new ones: its evidence, or `none-held` with the terms searched.
- **WooCommerce** also rules on every unclear candidate that holds a WooCommerce concern it lands, the same way: `joined:<cap_id>`, `nested:<cap_id>` or `apart`, for that concern against the candidate's others. Zid and BigCommerce have none.

## The back-fill parts

A back-fill runs after a mapping part that added capabilities, and is named for it (`B-backfill-woocommerce`). For every capability of the domain and every platform already mapped in it (Shopify, Salla, and the mapping parts so far) that has no cell, write the cell: its evidence, found by searching the platform's statements, or `none-held` with the terms searched. You add no capabilities and land no concerns, and you write only `cells.tsv`, `evidence.tsv` and `notes.md`.

## The amendment part

Where the coordinator moves a concern into a domain whose parts have already run, `<domain>-amend` lands it, as a mapping part would, and writes its platform's cells for every capability it lacks, and every platform's cells for any capability it adds.

## How to work, keeping your context small

Every request you make re-reads your whole context, so its cost grows with its length.
- **Start:** `seed --domain D`, then `model --domain D` (with `--areas` for a batch), then your concerns (`concerns --platform P --domain D`).
- **Read each concern once,** under every placement: `statements --platform P --concerns ID --width 160`, with its `gaps` and `matches`.
- **For cells,** run `candidates --domain D --platform P`: each capability's candidate statements on your platform, found by the terms the other platforms' cells use. They are leads to read with `key`, never evidence. Search further where they don't settle a cell.
- **Write as you go,** appending rows in small batches. Don't print your files back, and don't repeat a search.
- **Check before you report,** and fix every problem the checker prints. Answer its flags in your notes.

## Parts that run in batches

A large part runs as a series of batches, each by a fresh agent, so that no context grows large. Your message then names your batch: its concerns, and its areas.
- **Land only your batch's concerns.** The part's files hold the earlier batches' rows: read them through `model --domain D --areas ...`, and land a concern in an existing capability where it is the same thing, as a mapping part would.
- **Write the cells your batch needs:** for every capability of your batch's areas, a cell for each of the part's platforms that has none yet. Add evidence to an existing cell where your concerns' statements bear on it.
- **Rule on the unclear candidates of your batch's concerns** once both sides of a pair have landed. The batch that lands the second side rules on the pair; the first leaves it in its notes.
- **Append to the part's files,** never rewrite an earlier batch's rows. Where your evidence shows an earlier batch's row no longer holds, such as a ruling or a fit, say so in your notes; the coordinator corrects it before the next batch, and the checker's problem on that row is the coordinator's, not yours. Number new capabilities past the highest in each area.
- **A ruling and a fit follow the cells.** Never leave a statement uncited to keep a ruling `apart` or a fit `clean`.
- **Check your batch:** `python3 -I method/check_class_part.py <the part's folder> --concerns <your batch's concerns> --areas <your batch's areas>`. The last batch checks the whole part, without the options.

## Cells and evidence

**A cell** is one capability and one platform: `held` is `statements` where the platform's statements show the capability, or `none-held`. `none-held` means only that the concern map holds nothing found by the terms searched. It never means the platform lacks the capability.

**Evidence:** one row per statement a cell cites, with what the statement `supports`. Every value but `shows` is a reading of the statement, and the cell's `reading` says why:
- `core`: the platform itself does it for the merchant. The statement names its own admin section, setting, route or built-in behaviour, a plan line that includes it, or its own API for its own feature;
- `own-service`: the statement names the platform's company, or a company of its group, as the maker or provider of a separate product, app, extension or service that does it, whatever channel sells it, its own marketplace included. A product's name that carries the platform's brand doesn't name its maker. Without a statement naming the company, place the cell by what its statements show, and note the missing maker statement as a gap. Never decide the maker from what you know;
- `extension-point`: the statement shows third parties doing it through something the platform provides: an app-store or marketplace category, an extension target, a provider interface, or an API whose statements say apps or partners use it to do the work;
- `outside`: the statement names a third party, not the merchant, the buyer or the platform's company, as the one that does it, with no interface of the platform named;
- `shows`: the statement shows the platform has the capability, or gives its terms, and supports no placement. A statement that makes the merchant or buyer responsible is `shows`, never `outside`.

More than one value may apply to a cell, each resting on the statements that support it. A cell whose statements support none of the four placements is `not-stated`: the script derives it. Why the four values: they are what the coordinator's count of the class reads. They come back as marked readings, each resting on cited statements, not as category labels in place of the platforms' words, which is why Q1 dropped them on 11 October.

**You don't write** a cell's places, scopes or gaps. The checker derives them from your keys into `derived.tsv`, so a statement's scope stays its own.

**Qualities and slot fillers,** each in its own file:
- **a quality:** a limit, a certification, an uptime or a data location a platform states, on the capability it bears on. Its value is the statement's words. An unplaced inventory entry, such as a store limit's key, holds no value: record the key as the quality, write "not in the concern map" as its value, and name the structure that would hold it in your notes, as a gap;
- **a slot filler:** a third party or a law that a statement names as doing the capability, or as setting its terms. It is each market's setup, not the platform's extent. Its market comes from the statement's scope. You don't judge whether the capability is a slot: the coordinator computes the kind.

## Conventions from the dry run

The dry run's review set these (`studies/class-model/review-dry-run-rulings.md`). They apply to every part.
- **When something becomes a capability:** where at least one platform gives it a place of its own: an admin section or route, an API group, a plan line, or an app category. A single feature flag isn't enough.
- **The platform's own API** (its folder, object, scope, webhook topic, or a mutation's requirement) for its own feature is `core`, a guide addressed to app developers included. It is `extension-point` where the API's statements say apps or partners do the work.
- **A feature flag that isn't released** (`"released": false`) is `shows`. A released flag supports `core`, with its plan or store as its scope.
- **A permission listed for staff and for partners:** cite the staff permission for `core`. A partner's permission shows an interface for apps.
- **An admin route named for an application,** and gated only by the apps permission, is the app's page: `extension-point`.
- **A placed inventory entry:** where no statement covers it, a cell may cite an entry Q1 placed in a concern, by its inventory id, such as `SH-I-0902`. `search` and `key` read them.
- **A statement's title against its description:** its words as a whole decide. Where its description narrows its title, the description governs, the same way for every platform in a join.
- **`parent`:** the platforms' own grouping puts the child under the parent, as a statement shows. Where their groupings differ, follow the one they share. Failing that, follow the anchor platforms' admin grouping, and put the other in the note.
- **Strained:** a landed concern whose statements are cited in another tree of capabilities is `strained`, and its reading says where else it is cited.
- **Names:** use every landed platform's terms, and avoid a word that means something else on one of them. A mapping part proposes a rename in its notes; the coordinator renames. Homonyms go in the capability's note.
- **Another domain's statements:** a concern that names your domain under `also` may support a placement here. The merge flags a statement that supports `core` or `own-service` in two domains.
- **Slot fillers:** a third party or a law a statement names as doing the capability or setting its terms. A flag's name isn't one.
- **Gaps:** where a Q1 gap on a cell's concern changes what the cell can claim, its reading says so. For a capability its own platform names but never defines, the other platforms' `none-held` cells say the definition isn't stated.
- **Maker evidence** is a statement naming the company. A note never counts.

## Rules

- **Evidence:** every cell, landing, ruling and side row cites keys, and every reading is marked. No claim goes beyond what a cited statement says. A note's inference never counts.
- **No market's facts** decide a capability or its area. A statement scoped to one market keeps that scope.
- **Your own files only:** write only your part's files, write them as you go, make no commits, and run Python with `python3 -I`.
- **Check before you report:** run `python3 -I method/check_class_part.py <your part's folder>` (the scope part: `studies/class-model/scope.tsv`), and fix every problem it prints. Its flags are for the reviewer: answer each one you can in your notes.

## Output

`studies/class-model/scope.tsv` for the scope part. Every other part writes in `studies/class-model/parts/<part>/`. Tab-separated files, with a header row and no quoting. Lists are `;`-separated, never by commas or spaces.
- `capabilities.tsv`: `cap_id` · `area` (its `area_id`) · `capability` · `parent` (a `cap_id` of the same domain, or empty) · `note`;
- `landings.tsv`: `platform` · `concern_id` · `cap_id` (or `moved:<domain>`) · `join` (`match:<M-id>`, `terms`, `identifier`, `definition`, `role` or `single`) · `join_evidence` (keys of both sides, for every join but `match` and `single`) · `fit` (`clean` or `strained`) · `reading`;
- `cells.tsv`: `cap_id` · `platform` · `held` (`statements` or `none-held`) · `terms` (the platform's own words for it, each found in a cited statement or its concern's `platform_terms`) · `searched` (for `none-held`: the terms searched, in each language) · `reading`;
- `evidence.tsv`: `cap_id` · `platform` · `supports` (`core`, `own-service`, `extension-point`, `outside` or `shows`) · `key` · `why` (a few words: what in the statement supports it);
- `qualities.tsv`: `cap_id` · `platform` · `quality` · `value` (the platform's words) · `key` (a statement key, or an inventory id);
- `slot-fillers.tsv`: `cap_id` · `platform` · `filler` · `key`;
- `rulings.tsv`: `candidate_id` · `ruling` (`joined:<cap_id>` or `apart`) · `basis` · `keys`;
- `notes.md`: how you cut and why, every grain you chose, joins on role, homonyms, strained fits, the concerns you read under `also`, what the checker flagged, and problems with the brief or the evidence.

**Size.** The scope part prints 652 concerns with their `where` identifiers. In domain B, an anchor part takes about 10 to 25 concerns per platform, with about 300 to 400 statements each, and a mapping part about 5 to 15 concerns. Larger domains, such as C, are split by area before they run, and your message says which areas are yours. Print statements per concern, write your rows as you go, and keep your context small.

**Report:**
- capabilities per area;
- how many concerns joined existing capabilities, and how many made new ones;
- the joins on role, and the homonyms kept apart;
- strained fits;
- what the checker flagged that you couldn't answer;
- problems.

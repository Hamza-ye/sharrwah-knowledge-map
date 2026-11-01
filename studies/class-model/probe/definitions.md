# What the claims mean, and how to judge them

**The placement words.** Each claim says where a platform puts a thing:
- **core:** the platform does it itself, in its own product: its admin, its API, its checkout, its storefront.
- **own-service:** a service the platform's own company runs apart from the core product, such as its own payments or shipping service.
- **extension-point:** the platform leaves it to apps or partners, through a place it makes for them: an app category, an API meant for them, an integration slot.
- **outside:** done outside the platform, by the merchant or a third party, without a place the platform makes for it.
- **shows:** the source only shows that the thing exists on or around the platform, and doesn't say who does it.
- **scope:** a condition on the claim: a plan, a beta or early access, a feature flag, a country or market, a kind of store.

A cell's **strongest placement** is the first it holds of core, own-service, extension-point, outside and shows. A platform counts as establishing a capability when that placement is core or own-service.

**For each item, in this order:**
1. Read the item: the capability, the platform, and the sources. Open each source at the cited line and its neighbours, not the whole file. For a page cited by its web address only, find its held copy through the evidence repositories' guides (`README.md`, `docs/READING.md`, `index/`) or `python3 -I method/corpus_search.py PLATFORM TERM ... --brief --max 3`, and read it there. If you can't find it, say so.
2. Write your own reading **before** you open the item's row in your claims file: is the source about this capability, where does it put it, and under what condition.
3. Then open the claims file's row, compare, and give one verdict:
   - **stands:** the sources, read in place, support the claim;
   - **wrong placement:** they support another placement (name it). For a cell, say whether the right one is still core or own-service: if not, the capability's count changes;
   - **wrong capability:** the source isn't about this capability;
   - **wrong scope:** a condition is missing or wrong (name it);
   - **wrong detail:** something else in the claim or its reading is wrong (name it);
   - **can't tell:** the sources as cited don't settle it (say what would).

Judge by what the source plainly says. A convention you don't find in the source isn't evidence.

# The held pass's calibration: the rewritten brief at `high` and `xhigh` (30 October 2026)

**What this is.** The dry run's review (`held/review-H.md`, section 7) proposed `xhigh` for entries whose own words name what they are: settings with descriptions, plan tooltips, pages read through their run text. There, care had missed an important detail on about 10% of lines in both batches. Before the other batches ran, the coordinator measured the proposal. 82 such entries were placed again under the rewritten brief (`briefs/H-held.md` at `657cd861`), once at `high` and once at `xhigh`:
- Zid's dashboard pages 59 to 100 (ZD-1's entries; batches ZD-CH and ZD-CX);
- BigCommerce's 40 control panel settings (BC-1's; BC-CH and BC-CX).

Each placement was compared with the review's corrected placements of the same entries (`method/held_calibrate.py`; the key is `placements-ZD-1.tsv` and `placements-BC-1.tsv` at `b107cb2b`). The agents didn't read the key, the dry run's notes or the review. The calibration's batches aren't listed in `batches.tsv`, so they never reach the model.

**Read the comparison with care.** The key is the dry run's own lines plus the review's corrections. The review refuted a line only where the evidence was clear, so a line it let stand may be one defensible reading of several. A calibration line that differs from the key is a disagreement, not always an error. And the key predates two rulings the rewritten brief applies (M-6's parent lines, M-7's connections), so on M-7's lines the calibration is right and the key stale. On M-6's, the key is right: the calibration read the rule as every section's group, which the refined rule (below) doesn't ask for.

## The results

| Batch | Effort | Entries whole | Key pairs found | Missing, changing the model | Extra pairs | Tokens | Per entry |
| --- | --- | --- | --- | --- | --- | --- | --- |
| the dry run's own lines (old brief) | `high` | Zid 31 of 42; BigCommerce 33 of 40 | 43 of 54; 40 of 47 | 0; 1 | 0; 3 | in the dry run: 13.8 and 7.9 million for their whole batches | 90,000; 54,000 |
| ZD-CH | `high` | 32 of 42 | 46 of 54 | 2 | 6 | 8.0 million, 56 requests | about 190,000 |
| ZD-CX | `xhigh` | 27 of 42 | 43 of 54 | 2, the same two | 12 | 12.8 million, 84 requests | about 305,000 |
| BC-CH | `high` | 26 of 40 | 42 of 47 | 2 | 21, most of them M-6's parent lines | 7.7 million, 61 requests | about 192,000 |
| BC-CX | `xhigh` | 16 of 40 | 45 of 47 | 2: Display, and URL structure joined to Custom URLs, which the review had refuted | 36, most of them group lines | 18.5 million, 102 requests | about 460,000 |

**What the comparison shows on Zid's pages.**
- Of the 11 lines the review had to add to the dry run, `high` under the new brief found 6 on its own: the parent lines and second capabilities the new rules ask for.
- Both levels missed the same two lines that change the model, each a capability whose Zid cell holds nothing and that no lead showed:
  - "Product review notifications" (رسائل التقييمات), whose page sends "messages prompting customers to leave reviews": review requests, CM-SUP-002;
  - "Message logs" (سجل الرسائل): a log of sent messages, CM-NTF-003.
- `xhigh` cost 1.6 times as much, matched fewer entries whole, and missed the same two. On these entries, more effort buys nothing. The misses are a search's, not care's.

**What it shows on BigCommerce's settings.** `xhigh` found 45 of the key's 47 pairs, `high` 42. Both missed Display as a capability of its own, and `xhigh` also joined URL structure to Salla's Custom URLs, on the word, as the review had refused to. `xhigh` cost 2.4 times as much. `high` found 42 of the key's 47 pairs. Most of its 21 extra pairs are the new rules applied: each section of the General group takes a line on CM-ACC-006 (M-6, as first written), and Data solutions is `extension-point` (M-7). A few are real disagreements:
- Display placed on products and categories, not as a capability of its own;
- the sign-up form's fields on CM-CHK-009, which the review had corrected to CM-CUS-008;
- Export templates on CM-MIG-001, not CM-MIG-003.

**The cost.** The rewritten brief costs about twice the old per entry at `high`, on these heavy entries. Its agents read more: listing conditions traced into code modules, each lead's cell, the run pages. They also made almost one lookup per turn (ZD-CH: 58 tool calls in 56 requests), and each turn re-reads the whole context.

## What the coordinator takes from it

- **Effort:** `high`, for every kind the dry run held. `xhigh` cost 1.6 times as much on Zid's pages and 2.4 times on BigCommerce's settings, and missed the details `high` missed, or others like them. The founder's decision of 30 October sets a higher level where a level "consistently misses important details"; here both levels miss the same details, for a reason effort doesn't reach.
- **The misses' cause is the leads.** A capability whose cell holds nothing reaches the agent only through a lead or a search. The leads now also come from capabilities' own names (`by name`), which shows CM-NTF-003 first for "Message logs". The brief makes the search for each thing an entry names a lookup that always runs (inspection-H2's MF-1).
- **The cost:** the brief now asks agents to make their lookups together and to read only as far as an entry's own sources go. The first batches under it are measured before the pass is projected again.

- **Two faults the calibration found, fixed:** the leads tied and printed in a different order from run to run (Python's set order), so the checker's first-lead note came and went; and the parent's line, read as every section's group (BigCommerce's General, Orders, Products, Domain, API and MCP), gave 14 lines at `xhigh` that change nothing. The leads are sorted now, and the parent's line is for a child that is a kind of the parent's thing, as a bank deposit is an offline payment method (M-6, refined). A group a section only sits under is placed once, as a container (rule 3).

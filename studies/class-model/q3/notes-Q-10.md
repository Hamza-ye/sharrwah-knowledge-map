# Q3's check, batch Q-10: notes

Rows: km:ENG-01 to km:ENG-08 and km:MTH-01 to km:MTH-05, the Knowledge Map's questions in domain H's areas engineering and method. Both areas hold no capabilities by design (`q3.py slice`: "0 capabilities"), so an empty area isn't a miss.

## Count by result

- `beyond the class`: 12. These are ENG-01, 02 and 04 to 08 (Sharrwah's own design, engineering's) and MTH-01 to 05 (the method, the plan's).
- `partly`: 1. ENG-03, whose rest is `beyond the class`.
- `covered`, `candidate miss: held`, `candidate miss: not held`, `unclear`: 0.

## Rows that were hard to place, and why

- **ENG-03** (commodities to buy or integrate, or core to build). Its words name neither "should" nor "Sharrwah", so by the brief it asks the model what the class does. The model's cells show where each platform places every named thing:
  - payment processing: CM-PAY-004 and CM-PAY-011;
  - tax calculation: CM-TAX-002;
  - search: CM-SFR-013;
  - email and SMS delivery: CM-NTF-004;
  - maps: CM-CUS-009.

  CDN has no capability of its own. I searched for it in English on Shopify, WooCommerce and BigCommerce ("CDN; content delivery network"), and in Arabic on Salla and Zid ("CDN; شبكة توصيل المحتوى; توصيل المحتوى"). The only statement found is BigCommerce's subprocessor Cloudflare (BC-C-082/where/BC-S-0448). `q3.py where` shows it is cited in CM-TRU-015@bigcommerce (and in CM-TRU-014@bigcommerce) as outside. So the class's evidence holds a CDN only as an outside subprocessor, and that cell answers it.

  The choice of what Sharrwah buys or builds is Sharrwah's own design, so the row is `partly`, with its rest `beyond the class` (`engineering:build`).

  For payment processing, Decision 1 (C) and Decisions 2 to 12 already answer that each provider collects the buyer's payment (`founder:decided`). I left out `founder` for partners. The row asks which kind of thing is bought, not which partner it is bought from (a reading).
- **ENG-02** (quality-attribute scenarios). The founder's quality order is in force (`founder-decisions`, 29 October, Quality), and it says "Scale numbers come later". `architecture/plan.md` sections 1 and 5 give the scale numbers to the founder, later, with engineering's stated bands as assumptions until then.

  I placed the scale numbers as `founder`. That is a reading: peak load follows from which markets and merchants come first, which is on the founder's list. It makes the row `bundles`, since engineering's part is before build and the founder's before release. It raises no `wrong time`: the earliest `when` is before build, which matches `model`.
- **ENG-05** (money, currencies, time zones). S-02's engineering rulings, which the founder did not veto, answer part of it (`ruled`):
  - S02-D7: amounts in both currencies, with the market and the rate used;
  - S02-E4: records keep the currency of their day;
  - S02-D9: amounts refer to a currency record (the worked example of `architecture/plan.md` section 4);
  - S02-D6: the time zone is a store setting that a market may override.

  S02-M6 moved "what identifies a currency in money records" to S-09, hence `subject:S-09`. The remaining part, storage, rounding and time-zone computation, is `engineering:build`.
- **ENG-01** (tenancy). I added `subject:S-08` as a reading. `architecture/plan.md` section 3 pairs "how stores are kept apart" with "where their data lives", and puts where data lives after S-08. Whether data must stay in each market bears on whether stores are partitioned by region. Both answerers are before build, so no time bomb.
- **ENG-06** (validation against the reference). The founder's decision of 24 October (Code) answers what production code is validated against: requirements, an architecture description and engineering documentation. That part is `founder:decided`. Which journeys become acceptance examples is `engineering:detail`, at the area's build, which matches its `slice`.

  The row's premise of one reference has been overtaken by the five-platform model (a reading). I didn't raise `wrong party`: the decision in force doesn't settle the row's own question.
- **MTH-02** (stopping rule and saturation). The plan sets no saturation measure. What stands in its place is a reading of PLAN.md: done means every subject in scope (section 2); a gap is closed only where closing it could change the model or a decision (section 2, Gaps); pages are captured when a subject needs them (section 6, Evidence); and the extent comes from the evidence held (the founder, 29 October). I placed it `plan` with `founder:decided`, not `unclear`, because the plan does answer when capture stops, in other terms.
- **MTH-05** (keeping evidence fresh). The plan answers it now: pinned commits, risk 7's re-run of the subjects whose citations changed, and Q3 again at close-out. Its `needed_by` is `later` against the plan's before build, so `q3.py check` requires `wrong time`. A reading: the plan has no rule for platform betas or API versions as such.
- **MTH-01 and MTH-04** assume two references. The plan now has five, and a capability counts as `class` when one platform places it in its core or as its own service (PLAN.md, Stage 4A). MTH-01 also rests on the founder's intent of 29 October (`founder:decided`): the extent comes from the class, and nothing the class shows is ruled out.

## Candidate misses

None. The only search was for CDN, under ENG-03, as described above. It found one statement, already cited in two cells.

## Time bombs

- km:ENG-02: `bundles`. Engineering's scenarios are before build; the founder's scale numbers are before release.
- km:MTH-05: `wrong time`. Its `needed_by` is `later`; the plan answers it before build.

## Problems with the brief or the evidence

- The brief names only section 3 of `architecture/plan.md`. The ENG rows' bases also needed sections 1, 4, 5 and 6, and the MTH rows needed PLAN.md's sections. I read those, since the batch's message says a method row's basis is the plan's section.
- `when` for `plan` is before build by rule. A method row that the plan already answers, but that its author marked `later` (MTH-05), then becomes a `wrong time` bomb, although nothing waits on it. This is the coordinator's own rule, applied as it stands.
- For a scale number, the brief's answerer list has no exact fit. Scale isn't named on the founder's list, but `founder-decisions` (29 October, Quality) and `architecture/plan.md` give it to the founder. I used `founder`, marked as a reading.

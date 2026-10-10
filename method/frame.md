# The frame: who decides, when, and how sure we are

Every question about Sharrwah, once broken down, ends as one or more **outcomes**. An outcome is one thing that gets decided or found out, by one decider, at one time.

The frame types each outcome by who decides it and when, records separately how sure we are, and gives the rules for moving from a coarse question to typed outcomes. It comes from the founder's table of outcome types, reinforced from three engineering sources:

- product-line engineering: variation points, when each is fixed, who fixes it, and feature models;
- requirements engineering: assumptions about the world;
- information hiding: put what changes behind a boundary.

## 1. Outcome types

| Type | Who decides, and when | Feeds |
| --- | --- | --- |
| **Built** | Engineering, at build time | The domain model, the feature model, decision records |
| **Configured** | Sharrwah as platform operator, after build. It is an on/off per zone or plan, or a value such as a price, a policy or a rule. | Configuration and the entitlement matrix. Reversible, for new records only. |
| **Chosen** | The merchant, while using the product | A product feature; its slot is Built |
| **Context** | Law, regulators, partners, providers, the market | A research or monitoring entry |

Each Configured outcome carries one of three tags, which differ by owner and lifecycle:

- **release:** a planned rollout by Sharrwah. It has an end and feeds the release plan.
- **entitlement:** a standing value by plan or zone. It feeds pricing and plans.
- **operational:** a switch forced by Context, such as a partner cut off overnight. Operations flip it in minutes without a deploy, and it feeds the runbook.

Each Context outcome is one of two kinds:

- **researched:** looked up once, such as a law text.
- **monitored:** it changes on its own, such as rates, ban lists, partner status, the zone map or calendars. It needs a built feed and an owner, and every record stamps the value it used.

**Company constraints are not outcome types.** A question that binds the whole company and is not a variation point leaves at step 0 (section 4) and goes to the founder. The legal entity and its domicile is one. Anything that can vary by payment setup, zone, plan or time is not a company constraint. That includes which money roles Sharrwah takes, its prices, and when it seeks a licence. It is typed like any other outcome.

**Buyer choices at checkout are not Chosen outcomes.** They are transaction data inside Built behaviour.

## 2. Certainty, kept separate from type

Every outcome carries one of three certainty values:

- **settled:** decided, or evidenced with sources that agree.
- **provisional:** a working answer, safe to build behind a boundary, with a stated way to reverse it.
- **open:** neither of the above.

"Open" is never a type; any outcome can be open. What an open outcome blocks depends on its type:

| Open item | Blocks |
| --- | --- |
| A Built outcome | Building that part: settle it, spike it, or turn it into a slot if the options are few and known |
| The type or the range of a slot | Building. This is the expensive case. |
| A Configured value | Release in that zone or plan, not building |
| A Chosen value | Nothing. Only the default must be settled. |
| Context | Nothing directly. It blocks what it is linked to. |

## 3. Rules

1. **One outcome, one decider, one binding time.** An item that names two deciders is two outcomes.
2. **Every Configured or Chosen outcome has a Built twin: its slot.** The slot is the range of allowed values, the constraints between them, and the default. Deciding that something is configurable is itself an engineering decision, recorded like one.
3. **Containment.** Chosen fits inside Configured, which fits inside Built. Configured also fits inside what Context allows. A merchant cannot pick what Sharrwah has not switched on. Sharrwah cannot switch on what is not built, or what a zone's law forbids.
4. **Type follows rate of change.**
   - Never varies over the platform's life → Built.
   - Varies by zone, plan or time → Configured.
   - Varies by merchant → Chosen.
   - Volatile Context may feed Configured outcomes, never Built ones: build for the range, configure the value.
5. **Context must name what it moves.** A Context outcome that moves no Built, Configured or Chosen outcome is dropped.
6. **Rates split in two.** A rate policy (which source governs which event) is Configured. The rate value is monitored Context, stamped on each record when used.
7. **Configuration changes the future, never the past.** Records carry the values in force when they were made: position, rate, edition, zone. Switching something off does not undo the records made while it was on.
8. **Step 0 returns a typed answer.** A company constraint comes back from the founder either as a **boundary**, which removes options from the Built range, or as a **setting**, which is a Configured value the founder owns. Agents cannot tell which from a sentence alone.

## 4. The funnel

Each register row goes through these steps in order:

0. **Company constraint?** If yes, it goes to the founder (`decisions/founder.md`) and comes back as a boundary or a setting.
1. **Split** the row until each piece has one decider and one binding time.
2. **Type** each piece: Built; Configured (release, entitlement or operational); Chosen; or Context (researched or monitored).
3. **Link** it:
   - a Configured or Chosen outcome to its Built slot;
   - a Context outcome to what it moves.
4. **Certainty:** settled, provisional or open, then read off what it blocks.

## 5. References, and how they decide

The rows are the worklist, not a reference. The frame is the method, not evidence. These are the references:

| Reference | Authoritative for | Where |
| --- | --- | --- |
| Platform evidence | How a mature platform fixes the same thing: the default type | `observed-sh`, `observed-sa`, `shopify-payments-study/`, `studies/payment-seam/notes/` (crossings S###, L### and E###), `evidence/shopify-engineering/` |
| Yemen evidence | Whether Yemen breaks that pattern, and how fast things change there | `evidence/yemen/`. `yemen-setup-options/` holds claims about it. |
| Founder decisions and attestations | What Sharrwah wants, inside what Context allows | `decisions/founder.md`, `evidence/yemen/attestations/` |
| The model and the seam | Where an outcome sits | `model/obligation-to-payout.html`, `studies/payment-seam/seam.md` and its rules |

Each typed outcome falls into one of four cases:

1. **Both platforms fix it the same way, and Yemen does not contradict them.** Adopt that type and cite both.
2. **The platforms differ.** The type is Sharrwah's choice: a Built outcome, provisional, until a decision record settles it.
3. **Yemen breaks the platforms' pattern.** The type shifts, usually from Built to Configured or from Configured to operational. Cite the Yemen source.
4. **Neither platform has it.** Type it from rule 4 and the Yemen evidence alone, and mark it "no platform example". These carry the most risk.

Further rules on references:

- **Dates.** Sources dated before 2023 are historical. They can show what a document said, but not 2025–2026 status.
- **Attestations.** A founder attestation can confirm a source, fill a gap marked unconfirmed (as provisional), or flag a conflict. It can never settle a type alone.
- **Citations.** Every outcome cites at least one reference that resolves. That means a repository path with a line number, a schema `Type.field`, a crossing id, an evidence manifest item, or a founder decision id.

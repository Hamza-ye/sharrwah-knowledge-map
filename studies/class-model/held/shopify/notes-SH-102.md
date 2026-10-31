# SH-102: the return form's tracking carriers, placed by script

**What the batch is.** All 203 entries of Shopify's `tracking-carriers`: the options of the tracking carrier field on the return form (`capture-plus@return-form`), each a carrier's label and its value (`gid://shopify/TrackingCarrier/<handle>`), the last one Other.

**How it was placed.** The coordinator placed it by script (`method/held_tracking_carriers.py`), not by an agent, in the re-plan of 31 October (method report, section 18).
- **The list is already a cell's:** CM-SHP-017, shipment tracking, 'the carriers it can name', cites the platform's value list Tracking carriers, 204 options, as a whole (SH-I-2095).
- **So each option takes the list's line** (M-6): CM-SHP-017 `core`, its label the term and the carrier its filler. Other names no carrier, so it has no filler.
- A carrier the list names is not placed on CM-SHP-015 (the carriers a store ships with): the field names the carriers the tracking can name, and the ruling after SA-41 gives a thing a list names no line of its own.

**The cut.** SH-101 and SH-102 were cut again: SH-102 holds every carrier, and SH-101 the 20 `tinker-tools` entries that stood beside them, for an agent.

**What the checker prints:** no cell change, since CM-SHP-017 already holds `core`. Its filler list gains the 202 carriers.

The checker's last line, for SH-102: `203 of 203 entries placed; 0 problems` (after this file was written).

## The coordinator's check (31 October 2026, after the batch)

- Placed by the coordinator, as above. Its cost is a few of the coordinator's requests, against about 35 million for agents' batches of one list.

# The accuracy probe of the class's model

**What it is.** A measurement, on the founder's go of 1 November 2026, of how often the model's readings are wrong. Every quote in the model was found at its source by script; this checks the readings: where a platform puts a thing, which capability a source is about, and the rulings applied to many lines at once.

**The sample** (`probe.py sample`, seed 20261101, drawn and committed before any checking):
- 100 cells at random from the 1,130 that hold a placement, each checked on its strongest placement against up to three of its lines that give it;
- for each of the 14 high-weight rulings whose readings name 100 or more held lines (`rulings.tsv`), five of those lines at random.

Four checkers who made none of it read only `definitions.md`, their items and claims, and the sources. Each writes its own reading of an item before it opens the model's claim for it.

**How the result is read, fixed before any result:**
- a ruling **fails** if 3 or more of its 5 lines are wrong in placement or capability;
- the model is **unstable** if 10 or more of the 100 cells are wrong in their strongest placement or capability, or if any ruling fails;
- wrong scope, wrong detail and can't-tell are counted and reported, but don't decide stability.

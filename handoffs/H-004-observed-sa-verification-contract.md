# H-004: the payment services contract a Salla store in the UAE or Kuwait signs at verification

**Repository:** observed-sa. **Instrument:** a store whose country is the United Arab Emirates or Kuwait. If H-002's run makes one, the same account may serve.

**What to capture:**
1. The store verification (توثيق المتجر) of that store, up to where it presents the payment services contract (عقد خدمات الدفع).
2. The contract as presented, with its parties: save the page or the document it opens.

**Stop before** submitting documents or accepting the contract.

**Already held:**
- the help articles on verifying stores in the UAE and Kuwait (`help-articles/ar/texts.jsonl` lines 754, 755, 872, 873, 927 and 929), which name the contract without its parties;
- the verification schema of a Saudi store (`structures/salla/kyc-schema/demo@en`), which names no contract;
- the verification page of a Saudi store (runs `20261008T141131Z-sweep-merchant-en` step 78, `20261008T133523Z-sweep-demo-store-en` step 76).

**Why:** S-02, root decision 1: what Salla binds to the store's country; here, who the other party to the payment services contract is (gap S02-SA-G02). It bears on S-03, the contracting company, too.

**Needs:** possibly a store registered in the UAE or Kuwait. If the contract is shown only after documents are submitted, this stops there, and the gap stays open.

**Done when** a run holds the verification flow of a UAE or Kuwait store up to the contract, or shows where it stops before reaching it.

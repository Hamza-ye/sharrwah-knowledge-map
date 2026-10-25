# The founder's market test: its brief and what it read

The agent that wrote `M1-blind-decision-1.md` on 25 October 2026, for 3.3 million tokens (`method/count_tokens.py`). Below: its brief, as sent, and each tool call it made, taken from its transcript by the coordinator.

**What it read.** A search of its 24 tool calls finds 0 that name any of these: the first market, its currency or central bank, Stage 1, a decision record, the glossary, `METHOD.md`, `STATE.md`, the founder's files, `studies/` or `reports/`. The text of the record it wrote is left out of the search.

## The brief

```
You are writing one minimal architecture decision record for Sharrwah, a commerce platform for independent sellers. It is one platform for many markets, in the same product class as Shopify and Salla. Work only from this brief and the files it names.

## The question
Between a buyer's payment and the seller's payout, who holds the money? Decide it the minimal way the evidence supports, as Shopify and Salla themselves show it.

## What is given
- **The founder's guard,** a decision already made: "No arrangement that holds sellers' money through Sharrwah goes live anywhere without the founder's decision." It names two forms:
  - **A:** Sharrwah itself holds it;
  - **B:** a payment company holds it in an account opened through Sharrwah.
- **The design must hold in every market.** Name no country or market, and use no market's conditions as a reason. Where an option can exist only where some condition holds, state the condition in general terms. A market would then state it, in its own row.

## The evidence: two repositories, read-only
- **Shopify:** `/home/user/observed-sh/`. Read `README.md` and `docs/READING.md` first. Useful entry points:
  - the help centre as Markdown, under `structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/`, for example `payments/` and `finance/`;
  - the admin GraphQL schema, `structures/shopify/admin-graphql-schema/2026-10/items.jsonl`.
- **Salla:** `/home/user/observed-sa/`. Read `README.md` and `docs/READING.md` first. Useful entry points:
  - the help articles, `structures/salla/help-articles/en/texts.jsonl`, with the Arabic originals under `ar/`;
  - the API operations, `structures/salla/docs-operations/`;
  - the dashboard strings, `structures/salla/dashboard-translations/`.
- Look things up through these indexes and targeted searches. Don't read broadly.

## Rules
- Read nothing under `/home/user/sharrwah-knowledge-map/` except to write your one output file. In particular, open none of its records, reports, glossary, studies, registers or notes.
- Never `cd` into, or run code from inside, the two evidence repositories. Read their files by absolute path. Run Python only as `python3 -I`, with scripts in your own scratch directory.
- Evidence that contains credentials, cookies or tokens is read and cited like any other evidence. Never skip or mask it.
- Every claim is one of three:
  - a fact, with its file and line, and a verbatim quote of at most 300 characters;
  - an interpretation, marked as one;
  - an assumption, marked as one.
- A claim that something is absent ("only", "none", "not offered") names the search that supports it, or is marked as an interpretation.
- Stop at 30 tool calls. If you reach the limit, write what you have and say what is unfinished.

## Output
Write `/home/user/sharrwah-knowledge-map/decisions/checks/M1-blind-decision-1.md`, at most 800 words, with these sections:
1. **The question.**
2. **What the references show:** at most 10 facts, covering:
   - who holds the money under each arrangement each reference offers;
   - whether a reference's own payment service is offered everywhere or only where some condition holds;
   - whether sellers can use their own provider accounts.
3. **Options,** with which reference shows each.
4. **Decision:**
   - what every market gets, built once;
   - what varies by market, and who binds it;
   - your recommendation for launch.
5. **Consequences,** including what switching an option on later would change.
6. **The market row:** the conditions a market must state for each option to be available there, in general terms, as a short list.
7. **Open:** what the held evidence doesn't settle, and the work that would settle it.

Commit nothing. Then reply in at most 10 lines.
```

## Its tool calls

1. `Bash`: `for f in /home/user/observed-sh/README.md /home/user/observed-sh/docs/READING.md /home/user/observed-sa/README.md /home/user/observed-sa/docs/READING.md; do echo "=================== $f ($(wc -l < "$f") lines)"; cat -n "$f"; done`
2. `Read`: `/root/.claude/projects/-home-user/9f45def8-b710-5f9c-84f3-6a0fa7e617c8/tool-results/bhsmcttmg.txt`
3. `Bash`: `H=/home/user/observed-sh/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual; S=/home/user/observed-sa/structures/salla ⏎ echo "== SH payments + finance files"; find $H/payments $H/finance -name '*.md' | sed "s#$H/##" | sort | head -150 ⏎ echo "== SH payments count: $(find $H/payments`
4. `Bash`: `H=/home/user/observed-sh/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual ⏎ cd /tmp 2>/dev/null ⏎ echo "== files: shopify-payments + third-party + manual"; find $H/payments -maxdepth 2 \( -path '*shopify-payments*' -o -path '*third-party*' -o -name 'getting-paid.md' -o -name 'manua`
5. `Bash`: `H=/home/user/observed-sh/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/payments ⏎ echo "== getting-paid.md ($(wc -l < $H/getting-paid.md) lines)"; cat -n $H/getting-paid.md | cut -c1-520 | head -40 ⏎ echo "== third-party-providers.md"; cat -n $H/third-party-providers.md | grep -`
6. `Bash`: `H=/home/user/observed-sh/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/payments ⏎ G=/home/user/observed-sh/structures/shopify/admin-graphql-schema/2026-10/items.jsonl ⏎ echo "== payouts.md balance/reserve/hold"; grep -n -i "balance\|reserve\|on hold\|held\|bank account" $H/shopi`
7. `Bash`: `SCR=/tmp/claude-0/-home-user/9f45def8-b710-5f9c-84f3-6a0fa7e617c8/scratchpad; mkdir -p $SCR ⏎ cat > $SCR/kw.py <<'EOF' ⏎ import json, re, sys ⏎ path, per, win = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]) ⏎ pats = sys.argv[4:] ⏎ rows = [] ⏎ with open(path, encoding='utf-8') as f: ⏎     for n, li`
8. `Bash`: `SCR=/tmp/claude-0/-home-user/9f45def8-b710-5f9c-84f3-6a0fa7e617c8/scratchpad ⏎ python3 -I $SCR/kw.py /home/user/observed-sa/structures/salla/help-articles/en/texts.jsonl 3 260 \ ⏎  'Electronic Payments are the method' 'licensed|payment service provider|in partnership with|payment partner' 'electroni`
9. `Bash`: `SCR=/tmp/claude-0/-home-user/9f45def8-b710-5f9c-84f3-6a0fa7e617c8/scratchpad ⏎ python3 -I $SCR/kw.py /home/user/observed-sa/structures/salla/help-articles/en/texts.jsonl 3 330 \ ⏎  'What you need before you connect' 'activat\w* (?:the )?electronic payments?' 'withdraw\w*[^.\n]{0,60}(?:bank|IBAN)' 2>`
10. `Bash`: `SCR=/tmp/claude-0/-home-user/9f45def8-b710-5f9c-84f3-6a0fa7e617c8/scratchpad ⏎ python3 -I $SCR/kw.py /home/user/observed-sa/structures/salla/help-articles/en/texts.jsonl 4 420 \ ⏎  'Electronic Payments is a servic' 'electronic payments?[^\n]{0,200}verif|verif[^\n]{0,200}electronic payments?' 2>&1 | `
11. `Bash`: `SCR=/tmp/claude-0/-home-user/9f45def8-b710-5f9c-84f3-6a0fa7e617c8/scratchpad ⏎ cat > $SCR/kw2.py <<'EOF' ⏎ import json, re, sys ⏎ path, lines, win, cap = sys.argv[1], {int(x) for x in sys.argv[2].split(',')}, int(sys.argv[3]), int(sys.argv[4]) ⏎ rx = re.compile('|'.join(sys.argv[5:]), re.I) ⏎ with o`
12. `Bash`: `S=/home/user/observed-sa/structures/salla ⏎ echo "== docs-operations files: $(ls $S/docs-operations/md-openapi | wc -l)"; ls $S/docs-operations/md-openapi | head -5 ⏎ echo "== op files naming settlement/payout/transaction/wallet/balance/payment"; ls $S/docs-operations/md-openapi | grep -i -E 'settle`
13. `Bash`: `SCR=/tmp/claude-0/-home-user/9f45def8-b710-5f9c-84f3-6a0fa7e617c8/scratchpad ⏎ cat > $SCR/tr.py <<'EOF' ⏎ import json, re, sys ⏎ base = sys.argv[1] ⏎ rx = re.compile(r'settle|payout|Salla Payments|managed', re.I) ⏎ def walk(o, p=''): ⏎     if isinstance(o, dict): ⏎         for k, v in o.items(): yie`
14. `Bash`: `SCR=/tmp/claude-0/-home-user/9f45def8-b710-5f9c-84f3-6a0fa7e617c8/scratchpad ⏎ cat > $SCR/ops.py <<'EOF' ⏎ import json, sys ⏎ rows = [json.loads(l) for l in open(sys.argv[1], encoding='utf-8')] ⏎ for n in map(int, sys.argv[2].split(',')): ⏎     r = rows[n-1]; doc = r.get('document') ⏎     doc = doc `
15. `Bash`: `SCR=/tmp/claude-0/-home-user/9f45def8-b710-5f9c-84f3-6a0fa7e617c8/scratchpad ⏎ python3 -I $SCR/kw.py /home/user/observed-sa/structures/salla/help-articles/en/texts.jsonl 17 120 'Salla Payments' 2>&1 | cut -c1-330 ⏎ python3 -I $SCR/kw.py /home/user/observed-sa/structures/salla/help-articles/en/texts.`
16. `Bash`: `SCR=/tmp/claude-0/-home-user/9f45def8-b710-5f9c-84f3-6a0fa7e617c8/scratchpad ⏎ python3 -I $SCR/kw.py /home/user/observed-sa/structures/salla/help-articles/en/texts.jsonl 3 230 \ ⏎  "bank transfer[^\n]{0,160}(?:receipt|your bank account|merchant.s (?:bank )?account)|(?:receipt|IBAN)[^\n]{0,120}bank t`
17. `Bash`: `for r in /home/user/observed-sh /home/user/observed-sa; do h=$(cat $r/.git/HEAD 2>&1); echo "$r HEAD: $h"; ref=${h#ref: }; if [ -f "$r/.git/$ref" ]; then echo "  commit: $(cat $r/.git/$ref)"; else echo "  packed: $(grep " $ref\$" $r/.git/packed-refs 2>&1)"; fi; done`
18. `Bash`: `SCR=/tmp/claude-0/-home-user/9f45def8-b710-5f9c-84f3-6a0fa7e617c8/scratchpad ⏎ cat > $SCR/verify.py <<'EOF' ⏎ import json ⏎ SH='/home/user/observed-sh/'; SA='/home/user/observed-sa/' ⏎ HC=SH+'structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/payments/' ⏎ GQL=SH+'structures/shopify/a`
19. `Bash`: `echo "== SA on-disk files with terms in path"; find /home/user/observed-sa/salla.com -ipath '*terms*' 2>/dev/null | head -12 ⏎ echo "== SA attempts row for salla.com/en/terms"; grep '"url": "https://salla.com/en/terms"' /home/user/observed-sa/index/attempts.jsonl | cut -c1-600 ⏎ echo "== SH attempts`
20. `Bash`: `SCR=/tmp/claude-0/-home-user/9f45def8-b710-5f9c-84f3-6a0fa7e617c8/scratchpad ⏎ cat > $SCR/warcterms.py <<'EOF' ⏎ import json, sys, zlib, re, os, html ⏎ REPO = '/home/user/observed-sa/' ⏎ targets = sys.argv[1:] ⏎ rows = {} ⏎ with open(REPO + 'index/attempts.jsonl', encoding='utf-8') as f: ⏎     for l`
21. `Bash`: `SCR=/tmp/claude-0/-home-user/9f45def8-b710-5f9c-84f3-6a0fa7e617c8/scratchpad; A=/home/user/observed-sa/structures/salla/help-articles/ar ⏎ ls $A ⏎ python3 -I $SCR/kw.py $A/texts.jsonl 4 150 'مرخص[^.\n]{0,80}(?:الدفع|المدفوعات)|(?:الدفع|المدفوعات)[^.\n]{0,80}مرخص' 'البنك المركزي' 'بالشراكة مع[^.\n]{0`
22. `Bash`: `mkdir -p /home/user/sharrwah-knowledge-map/decisions/checks ⏎ OUT=/home/user/sharrwah-knowledge-map/decisions/checks/M1-blind-decision-1.md ⏎ cat > "$OUT" <<'EOF' ⏎ # M1 blind decision 1: who holds the money ⏎  ⏎ Evidence: ʼobserved-shʼ at ʼfebbf6c98a1fʼ, ʼobserved-saʼ at ʼ4ca2e896a729ʼ (HEAD; assum`
23. `Bash`: `OUT=/home/user/sharrwah-knowledge-map/decisions/checks/M1-blind-decision-1.md ⏎ cat > "$OUT" <<'EOF' ⏎ # M1 blind decision 1: who holds the money ⏎  ⏎ Evidence: ʼobserved-shʼ at ʼfebbf6c98a1fʼ, ʼobserved-saʼ at ʼ4ca2e896a729ʼ (assumption: working trees unmodified). ʼHCʼ = ʼobserved-sh/structures/sho`
24. `Bash`: `OUT=/home/user/sharrwah-knowledge-map/decisions/checks/M1-blind-decision-1.md ⏎ cat > "$OUT" <<'EOF' ⏎ # M1 blind decision 1: who holds the money ⏎  ⏎ Evidence: ʼobserved-shʼ at ʼfebbf6c98a1fʼ, ʼobserved-saʼ at ʼ4ca2e896a729ʼ (assumption: working trees unmodified). ʼHCʼ = ʼobserved-sh/structures/sho`

"""Write the questions as agents get them, from studies/proposals/questions.md.

Usage: python3 -I method/agent_questions.py

Writes studies/proposals/questions-for-agents.md: how a run uses its question, then each question's id, title and
quoted wording. It leaves out everything else in questions.md, the founder's items, the notes on what a question
carries and the rules for the wording among them, so that no agent reads the founder's words or expectations
(PLAN.md section 6: agents get section B's items only as the neutral questions).
"""
import os, re

SKM = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(SKM, "studies", "proposals", "questions.md")
OUT = os.path.join(SKM, "studies", "proposals", "questions-for-agents.md")

text = open(SRC, encoding="utf-8").read()
how = re.search(r"^\*\*How a run uses its question:\*\*\n(.*?)\n\n", text, flags=re.M | re.S).group(1)
out = ["# The questions", "",
       "Written by `method/agent_questions.py` from `questions.md`. Number each question's sentences from 1, across its paragraphs.", "",
       "**How a run uses its question:**", how, ""]
for m in re.finditer(r"^## (Q\d)\. (.+?)\n(.*?)(?=^## |\Z)", text, flags=re.M | re.S):
    qid, title, body = m.groups()
    quoted = [l[2:] if l.startswith("> ") else "" for l in body.splitlines() if l.startswith(">")]
    if not quoted:
        continue
    out += [f"## {qid}. {title}", ""] + ["> " + l if l else ">" for l in quoted] + [""]
open(OUT, "w", encoding="utf-8").write("\n".join(out).rstrip() + "\n")
print(f"wrote {os.path.relpath(OUT, SKM)}")

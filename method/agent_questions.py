"""Write the questions as agents get them, from studies/proposals/questions.md.

Usage: python3 -I method/agent_questions.py

Writes studies/proposals/questions-for-agents.md: how a run uses its question, then each question's id, title and
quoted wording, each sentence numbered from 1 across its paragraphs, so that every run numbers alike. It leaves out
everything else in questions.md, the founder's items, the notes on what a question carries and the rules for the
wording among them, so that no agent reads the founder's words or expectations (PLAN.md section 6: agents get
section B's items only as the neutral questions).

`sentences(QID)` gives a question's numbered sentences, for the checker.
"""
import os, re

SKM = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(SKM, "studies", "proposals", "questions.md")
OUT = os.path.join(SKM, "studies", "proposals", "questions-for-agents.md")
SPLIT = re.compile(r"(?<=[.?!])\s+(?=[A-Z])")   # a sentence ends at . ? or ! before a capital


def questions(text):
    """[(qid, title, [paragraph, ...])] of the quoted wordings in questions.md."""
    out = []
    for m in re.finditer(r"^## (Q\d)\. (.+?)\n(.*?)(?=^## |\Z)", text, flags=re.M | re.S):
        qid, title, body = m.groups()
        paras, cur = [], []
        for l in body.splitlines():
            if l.startswith("> "):
                cur.append(l[2:])
            elif l.startswith(">") or cur:
                if cur:
                    paras.append(" ".join(cur))
                cur = []
        if cur:
            paras.append(" ".join(cur))
        if paras:
            out.append((qid, title, paras))
    return out


def sentences(qid):
    """[(number, sentence)] of a question, numbered from 1 across its paragraphs."""
    for q, _, paras in questions(open(SRC, encoding="utf-8").read()):
        if q == qid:
            return list(enumerate((s for p in paras for s in SPLIT.split(p)), start=1))
    return []


if __name__ == "__main__":
    text = open(SRC, encoding="utf-8").read()
    how = re.search(r"^\*\*How a run uses its question:\*\*\n(.*?)\n\n", text, flags=re.M | re.S).group(1)
    out = ["# The questions", "",
           "Written by `method/agent_questions.py` from `questions.md`. Each question's sentences are numbered from 1,"
           " across its paragraphs, in square brackets: cite them by these numbers.", "",
           "**How a run uses its question:**", how, ""]
    for qid, title, paras in questions(text):
        out += [f"## {qid}. {title}", ""]
        n = 0
        for i, p in enumerate(paras):
            parts = []
            for s in SPLIT.split(p):
                n += 1
                parts.append(f"[{n}] {s}")
            out += ([">"] if i else []) + ["> " + " ".join(parts)]
        out.append("")
    open(OUT, "w", encoding="utf-8").write("\n".join(out).rstrip() + "\n")
    print(f"wrote {os.path.relpath(OUT, SKM)}")

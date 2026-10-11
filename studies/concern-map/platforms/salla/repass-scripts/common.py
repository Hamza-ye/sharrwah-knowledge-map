# Shared helpers for the Salla re-pass (Q1, 11 October 2026). Run with python3 -I.
import csv, json, os, re, sys
csv.field_size_limit(10**9)
SP = "/tmp/claude-0/-home-user/9f45def8-b710-5f9c-84f3-6a0fa7e617c8/scratchpad/q1r/salla"
FIRST = "/home/user/sharrwah-knowledge-map/studies/concern-map/platforms/salla"
CAP = "/home/user/sharrwah-knowledge-map/evidence/product-class/runs/20261010T235130Z-q1-salla-sources"
OSA = "/home/user/observed-sa"

def rd(path):
    with open(path, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE))

def wr(path, cols, rows):
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write("\t".join(cols) + "\n")
        for r in rows:
            f.write("\t".join(str(r.get(c, "")).replace("\t", " ").replace("\r", " ").replace("\n", " ") for c in cols) + "\n")

def ids(s):
    return [x for x in re.split(r"[,\s;]+", s or "") if x]

ST_COLS = ["concern_id", "placement", "structure", "identifier", "statement", "scope", "cite_ids", "note"]
GP_COLS = ["concern_id", "placement", "what_would_show_it", "means", "who_can", "route", "why_not_held", "gap_kind"]
CIT_COLS = ["cite_id", "source", "locator", "quote", "source_date", "date_basis", "accessed", "access_path"]
PLACEMENTS = ["where", "decides", "responsible", "boundary", "reason"]

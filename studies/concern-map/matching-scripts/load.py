"""Load the three platform outputs (concerns, inventory, statements) for the Q1 matching pass.

Reads only concerns.tsv, inventory.tsv and statements.tsv under
studies/concern-map/platforms/<platform>/. Run with python3 -I.
"""
import csv
import re
import sys

csv.field_size_limit(10**9)

BASE = "/home/user/sharrwah-knowledge-map/studies/concern-map/platforms"
PLATFORMS = ["shopify", "salla", "woocommerce"]
PREFIX = {"shopify": "SH", "salla": "SA", "woocommerce": "WC"}


def read_tsv(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE))


def split_terms(platform, s):
    s = (s or "").strip()
    if not s:
        return []
    if platform == "salla":
        parts = s.split(" | ")
    else:
        parts = s.split("; ")
    return [p.strip() for p in parts if p.strip()]


def split_ids(s):
    s = (s or "").strip()
    if not s:
        return []
    return [x for x in re.split(r"[;\s]+", s) if x]


def load(platform):
    d = f"{BASE}/{platform}"
    concerns = read_tsv(f"{d}/concerns.tsv")
    inventory = read_tsv(f"{d}/inventory.tsv")
    statements = read_tsv(f"{d}/statements.tsv")
    inv_by_id = {r["inv_id"]: r for r in inventory}
    out = {}
    for c in concerns:
        cid = c["concern_id"]
        out[cid] = {
            "id": cid,
            "platform": platform,
            "name": c["concern"],
            "terms_raw": c["platform_terms"],
            "terms": split_terms(platform, c["platform_terms"]),
            "inv_ids": split_ids(c["inv_ids"]),
            "split_note": c.get("split_note", ""),
            "inv": [],
            "stmts": [],
        }
    # inventory entries: link by inventory concern_ids (authoritative for entry->concern)
    for r in inventory:
        for cid in split_ids(r["concern_ids"]):
            if cid in out:
                out[cid]["inv"].append(r)
    for s in statements:
        cid = s["concern_id"]
        if cid in out:
            out[cid]["stmts"].append(s)
    return out, inventory, statements, inv_by_id


def load_all():
    data = {}
    for p in PLATFORMS:
        data[p] = load(p)
    return data


if __name__ == "__main__":
    data = load_all()
    for p in PLATFORMS:
        concerns = data[p][0]
        print(p, len(concerns), "concerns")

"""Check the wording of the recording runs' not-found rows against what each row says was read (the founder's
decision of 19 October 2026: "check every 'not found' row's wording against what was actually read").

Usage: python3 -I method/check_not_found_wording.py [QUESTION ...] [--platform PLATFORM] [--out TSV]

For each row of studies/proposals/records/<question>/<platform>/not-found.tsv, every phrase the row gives in
quotation marks or backticks, and every phrase in parentheses that starts with a capital or an Arabic letter, in
`what_is_missing` or `route`, is looked for in:
- each source the row's `read` names: a held file at its commit, a fetch archive's record at its offset, a captured
  page by its address;
- the quotes of its folder's citations and copied citations, and its statements.

A phrase found in none of them is listed, with its row. A phrase that joins a list (by commas, semicolons, ">" or
" - ") is found when each of its items is. A phrase in quotation marks or backticks is given as the
platform's words; one in parentheses may be the run's own. The list is for a reader to check row by row: it decides
nothing. Each listed row's sources are named too, with those that couldn't be read.
"""
import csv, glob, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from quote_check import Sources, variants

csv.field_size_limit(10**9)
SKM = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RECORDS = os.path.join(SKM, "studies", "proposals", "records")
ROOTS = {"observed-sh": "/home/user/observed-sh", "observed-sa": "/home/user/observed-sa",
         "woocommerce-11.2.1": "/home/user/woocommerce-release/11.2.1/woocommerce", "sharrwah-knowledge-map": SKM}
QUOTED = [("quoted", r'"([^"\t]{3,240})"'), ("quoted", r"“([^”\t]{3,240})”"), ("quoted", r"‘([^’\t]{3,240})’"),
          ("quoted", r"«([^»\t]{3,240})»"), ("quoted", r"(?<![\w'])'([^'\t]{3,240}?)'(?![\w])"),
          ("backticks", r"`([^`\t]{2,240})`"), ("parentheses", r"\(([A-Z؀-ۿ][^()\t]{2,240})\)")]
LOCAL = re.compile(r"\b((?:observed-s[ha]|sharrwah-knowledge-map)@[0-9a-f]{7,40}:[^\s;,()]+|woocommerce-11\.2\.1:[^\s;,()]+)")
URL = re.compile(r"https?://[^\s;,)]+")


def read_tsv(path):
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE))


def phrases(text):
    out = []
    for kind, rx in QUOTED:
        for m in re.finditer(rx, text or ""):
            p = m.group(1).strip()
            if kind == "parentheses" and re.match(r"^(e\.g\.|i\.e\.|see |read |held|live|not |N\d|Q\d)", p):
                continue
            if p and (kind, p) not in out:
                out.append((kind, p))
    return out


def sources(read):
    """(source, locator) for each held file or captured address a row's `read` names. A fetch archive is read at each
    record offset named after it, as `@N`, "offset N" or "same archive at offset N", up to the next held file."""
    out, read = [], read or ""
    found = list(LOCAL.finditer(read))
    for j, m in enumerate(found):
        s = m.group(1).rstrip(".")
        w = re.match(r"^(.+\.warc\.gz)(?:@(\d+))?$", s)
        if not w:
            out.append((s, ""))
            continue
        upto = found[j + 1].start() if j + 1 < len(found) else len(read)
        offs = ([w.group(2)] if w.group(2) else []) + re.findall(r"\boffset (\d{3,})", read[m.end():upto])
        out += [(w.group(1), o) for o in dict.fromkeys(offs)] or [(w.group(1), "")]
    for m in URL.finditer(read):
        out.append((m.group(0).rstrip(".:"), ""))
    return out


def main(argv):
    qs, platform, out = [], None, None
    i = 0
    while i < len(argv):
        if argv[i] == "--platform":
            platform, i = argv[i + 1], i + 2
        elif argv[i] == "--out":
            out, i = argv[i + 1], i + 2
        else:
            qs.append(argv[i])
            i += 1
    src = Sources(ROOTS, sorted(glob.glob(os.path.join(SKM, "evidence/product-class/runs/*"))))
    rows, counts = [], {}
    for path in sorted(glob.glob(os.path.join(RECORDS, "Q*", "*", "not-found.tsv"))):
        q, p = path.split(os.sep)[-3:-1]
        if (qs and q not in qs) or (platform and p != platform):
            continue
        d = os.path.dirname(path)
        own = " ".join(r.get("quote", "") for f in ("citations.tsv", "copied-citations.tsv")
                       for r in read_tsv(os.path.join(d, f)))
        own += " " + " ".join(r.get("statement", "") + " " + r.get("identifier", "")
                              for r in read_tsv(os.path.join(d, "statements.tsv")))
        own_v = {k: t for k, t in variants(own)}
        for r in read_tsv(path):
            counts.setdefault(p, [0, 0, 0])
            counts[p][0] += 1
            found_any = False
            srcs = sources(r.get("read", ""))
            unread = []
            def found(ph):
                qv = {k: t for k, t in variants(ph)}
                if any(qv[k] and qv[k] in own_v[k] for k in qv):
                    return True
                for s, loc in srcs:
                    res = src.check_quote(ph, s, loc)
                    if res[0].startswith("found"):
                        return True
                    if res[0] == "unresolved" and s not in unread:
                        unread.append(f"{s} ({res[1]})")
                return False
            for kind, ph in phrases(r.get("what_is_missing", "") + "\n" + r.get("route", "")):
                # a list a row joins into one phrase is found when each of its items is: a path, an address or a
                # note of the row's own among them is left aside
                items = [x.strip(" -") for x in re.split(r"[،,;>]| - ", ph) if x.strip(" -")]
                items = [x for x in items if not re.match(r"^(https?://|/|not held$)", x)]
                if found(ph) or (items and items != [ph] and all(found(x) for x in items)):
                    continue
                rows.append((r["nf_id"], p, q, kind, ph, r.get("who_can", ""), "; ".join(dict.fromkeys(unread))))
                found_any = True
            if found_any:
                counts[p][1] += 1
    lines = ["nf_id\tplatform\tquestion\tkind\tphrase\twho_can\tsources not read by this check"]
    lines += ["\t".join(x.replace("\t", " ") for x in r) for r in rows]
    if out:
        with open(out, "w", encoding="utf-8") as f:
            f.write("\n".join(lines) + "\n")
    else:
        print("\n".join(lines))
    for p, (n, flagged, _) in sorted(counts.items()):
        print(f"{p}: {n} rows, {flagged} with a phrase not found in what they read", file=sys.stderr)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

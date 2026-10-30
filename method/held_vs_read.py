# What the evidence repositories hold, against what the class's model has read (PLAN.md, section 6, Evidence; the
# founder, 30 October: what is held is known through the repositories' own guides and indexes). The model reads the
# concern map, finished on 12 October 2026, and the landed subjects' statements its amendments cite. This measures,
# per platform:
#   structures  every structure the repository's REGISTER.tsv names: held or not, cited by what the model reads (and
#               at which commit), changed since, and its items (lines of its items.jsonl, or of its pages.jsonl, listings.jsonl, menu.jsonl or text.txt, every label);
#   pages       every address held readable (fetch archives in git, browser steps' page text, saved answers,
#               structures' sources, this repository's capture runs), by host and section, against the addresses
#               what the model reads cites;
#   runs        every run the repository's index/runs.tsv lists, by kind, against the runs what the model reads cites;
#   ledger      the repository's own coverage ledger: each denominator the platform lists, by status (index/ledger).
#
# Usage: python3 -I method/held_vs_read.py [--out studies/class-model/held-vs-read.tsv] [--platform P] [--detail]
#   Writes one row per platform, kind and group (held, read, unread), and prints the totals. --detail prints each
#   unread structure and the largest unread page groups.
import argparse, collections, csv, glob, json, os, re, subprocess, sys, urllib.parse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from class_slice import MODEL, PLATFORMS, rows, SUBJECTS_CITED, subject_citations
from held_index import Held, norm_url

csv.field_size_limit(10**9)
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CMAP = os.path.join(ROOT, "studies", "concern-map", "platforms")
OPC = os.environ.get("OTHER_PRODUCT_CLASS", "/home/user/other-product-class")
REPOS = {"shopify": ("observed-sh", "/home/user/observed-sh", ""), "salla": ("observed-sa", "/home/user/observed-sa", ""),
         "zid": ("other-product-class", OPC, "zid/"), "bigcommerce": ("other-product-class", OPC, "bigcommerce/"),
         "woocommerce": ("other-product-class", OPC, "woocommerce/")}
HOSTS = {"shopify": r"(^|\.)(shopify\.(com|dev)|shopifystatus\.com|shopifyapps\.com)$", "salla": r"(^|\.)(salla\.(sa|com|dev|network|partners)|mahally\.com)$",
         "zid": r"(^|\.)zid\.(sa|dev|eg)$", "bigcommerce": r"(^|\.)(bigcommerce\.com|bigcommerce\.co\.uk|commerce\.com)$",
         "woocommerce": r"(^|\.)(woocommerce\.com|woo\.com|wordpress\.(org|com)|automattic\.com)$"}
ASSET = re.compile(r"\.(js|mjs|css|png|jpe?g|gif|svg|webp|ico|woff2?|ttf|map|mp4|webm|avif)(\?|$)", re.I)


def git(root, *a):
    p = subprocess.run(["git", "-C", root, *a], capture_output=True, text=True)
    return p.stdout if p.returncode == 0 else ""


def page_key(u):
    """An address as a page: no scheme, no www, no query or fragment, no trailing slash or .md/.html, folded."""
    u = norm_url(u).split("#")[0].split("?")[0]
    u = re.sub(r"^https?://", "", u)
    u = re.sub(r"^www\.", "", u).rstrip("/")
    u = re.sub(r"\.(md|html?)$", "", u)
    return u.casefold()


def host_of(k):
    return k.split("/")[0]


def group_of(k):
    parts = k.split("/")
    segs = [p for p in parts[1:] if p and not re.fullmatch(r"[a-z]{2}(-[a-z]{2})?", p)][:1]   # skip a locale
    return "/".join([parts[0]] + segs)


def read_sources():
    """What the model reads: the concern map's citations, and the landed subjects' citations (cited by amendments)."""
    out = collections.defaultdict(list)
    for p in PLATFORMS:
        for r in rows(os.path.join(CMAP, p, "citations.tsv")):
            out[p].append((r["source"], r.get("locator", "")))
    # a landed subject's statement is read only where the model's evidence cites it (an amendment from the points)
    cited = {r["key"] for r in rows(os.path.join(MODEL, "merged", "evidence.tsv"))}
    for p in PLATFORMS:
        sc = subject_citations(p)
        for s in SUBJECTS_CITED:
            for r in rows(os.path.join(ROOT, "studies", "subjects", s, p, "statements.tsv")):
                if r["stmt_id"] in cited:
                    for c in re.split(r"[;,\s]+", r.get("cite_ids", "")):
                        if c in sc:
                            out[p].append((sc[c]["source"], sc[c].get("locator", "")))
    return out


def local_to_page(src):
    """A held copy of a page, cited by path, as its address."""
    m = re.search(r"structures/shopify/help-center/help\.shopify\.com@[^/]+/md/(.+?)(\.md)?$", src)
    if m:
        return "help.shopify.com/" + m.group(1).casefold()
    m = re.search(r"structures/shopify/help-center/help\.shopify\.com@[^/]+/content\.html/(.+?)(\.html)?$", src)
    if m:
        return "help.shopify.com/" + m.group(1).casefold()
    return None


def held_pages_observed(platform):
    repo, root, _ = REPOS[platform]
    h = Held({repo: root}, [])
    out = {}
    for k, hs in h.by_key.items():
        for x in hs:
            if not x.get("readable"):
                continue
            u = x["url"]
            pk = page_key(u)
            if re.search(HOSTS[platform], host_of(pk)) and not ASSET.search(u):
                out.setdefault(pk, x["kind"])
    return out


def held_pages_opc(platform):
    """other-product-class's fetch archives, browser steps and saved answers for one platform folder."""
    _, root, sub = REPOS[platform]
    out = {}
    tracked = set(git(root, "ls-files", f"{sub}raw/runs/*/fetch.warc.gz", f"{sub}raw/runs/*/fetch-*.warc.gz").split())
    for cdx in sorted(glob.glob(os.path.join(root, sub, "raw/runs/*/fetch.cdx"))):
        run = os.path.basename(os.path.dirname(cdx))
        if not any(t.startswith(f"{sub}raw/runs/{run}/fetch") for t in tracked):
            continue
        for line in open(cdx, encoding="utf-8", errors="replace"):
            t = line.rstrip("\n").split(" ")
            if len(t) < 9 or line.startswith(" CDX") or not t[4].startswith("2"):
                continue
            pk = page_key(t[0])
            if re.search(HOSTS[platform], host_of(pk)) and not ASSET.search(t[0]):
                out.setdefault(pk, "warc")
    for acts in sorted(glob.glob(os.path.join(root, sub, "raw/runs/*/actions.jsonl"))):
        for line in open(acts, encoding="utf-8", errors="replace"):
            try:
                a = json.loads(line)
            except Exception:
                continue
            u = a.get("url") or ""
            if u.startswith("http") and a.get("outcome") in (None, "ok"):
                pk = page_key(u)
                if re.search(HOSTS[platform], host_of(pk)):
                    out.setdefault(pk, "step")
    for lst in sorted(glob.glob(os.path.join(root, sub, "raw/runs/*/answers.jsonl")) + glob.glob(os.path.join(root, sub, "raw/runs/*/responses.jsonl"))):
        for line in open(lst, encoding="utf-8", errors="replace"):
            try:
                o = json.loads(line)
            except Exception:
                continue
            host, path = o.get("host") or "", o.get("path") or o.get("endpoint") or ""
            if host and path:
                pk = page_key(f"https://{host}{path}")
                if re.search(HOSTS[platform], host_of(pk)):
                    out.setdefault(pk, "answer")
    return out


def held_pages_captures(platform):
    """This repository's own capture runs (evidence/product-class/runs), by address."""
    out = {}
    for mf in sorted(glob.glob(os.path.join(ROOT, "evidence", "product-class", "runs", "*", "manifest.tsv"))):
        for r in rows(mf):
            if r.get("result") != "captured":
                continue
            for u in {r.get("url", ""), r.get("final_url", "")}:
                if u:
                    pk = page_key(u)
                    if re.search(HOSTS[platform], host_of(pk)):
                        out.setdefault(pk, "capture")
    return out


# The files a structure holds its items in, a line each (no structure holds two of them).
ITEM_FILES = ("items.jsonl", "pages.jsonl", "listings.jsonl", "menu.jsonl", "text.txt")


def structures(platform, srcs):
    repo, root, sub = REPOS[platform]
    reg = os.path.join(root, sub, "structures", "REGISTER.tsv")
    R = rows(reg)
    idc = list(R[0].keys())[0] if R else "structure_id"
    pat = re.compile(rf"^{repo}@([0-9a-f]+):{re.escape(sub)}structures/(?:{platform}/)?([^/:]+)")
    cited = collections.defaultdict(set)
    lines = collections.defaultdict(set)      # the items read: a cited file and line, under each structure
    for s, loc in srcs:
        m = pat.match(s)
        if m:
            cited[m.group(2)].add(m.group(1))
            ln = re.search(r"\bline (\d+)", loc or "") or re.search(r"[#:]L(\d+)", s)
            f = s.split(":", 1)[1]
            lines[m.group(2)].add((re.sub(r"[#:]L?\d+(-L?\d+)?$", "", f), ln.group(1) if ln else "whole"))
    out = []
    for r in R:
        sid = r[idc].split("/", 1)[-1] if r[idc].startswith(platform + "/") else r[idc]
        st = r.get("status", "")
        held = st.startswith(("captured", "held"))
        folder = os.path.join(root, sub, "structures", platform, sid) if not sub else os.path.join(root, sub, "structures", sid)
        files = [f for name in ITEM_FILES for f in glob.glob(os.path.join(folder, "**", name), recursive=True)]
        n = 0
        for f in files:
            with open(f, encoding="utf-8", errors="replace") as fh:
                n += sum(1 for _ in fh)
        changed = 0
        for c in cited.get(sid, ()):
            d = git(root, "diff", "--numstat", c, "HEAD", "--", os.path.relpath(folder, root))
            changed += sum(int(x.split("\t")[0]) for x in d.splitlines() if x.split("\t")[0].isdigit())
        out.append({"structure": sid, "status": st[:60], "held": held, "read": bool(cited.get(sid)),
                    "items_read": len([x for x in lines.get(sid, ()) if x[0].endswith(ITEM_FILES) and x[1] != "whole"]),
                    "read_at": ",".join(sorted(cited.get(sid, ()))), "items": n, "added_since": changed,
                    "date_seen": r.get("date seen", "")[:10], "what": (r.get("what the platform shows or publishes") or "")[:160]})
    return out


def ledgers(platform):
    """The repository's own coverage ledger: each denominator (what the platform lists as existing: sitemaps, admin
    routes per store, mutations, journey units, features, settings) by status, as index/ledger-summary.tsv counts it;
    other-product-class's Zid ledger by its rows' status."""
    repo, root, sub = REPOS[platform]
    out = collections.Counter()
    summ = os.path.join(root, sub, "index", "ledger-summary.tsv")
    if os.path.exists(summ):
        for l in open(summ, encoding="utf-8"):
            f = l.rstrip("\n").split("\t")
            if len(f) == 4 and f[3].isdigit():
                out[(f[0], f[2])] += int(f[3])
    for led in sorted(glob.glob(os.path.join(root, sub, "index", "ledger", "*.tsv"))) if sub else []:
        for r in rows(led):
            out[(os.path.basename(led)[:-4], r.get("status", "?"))] += 1
    return out


def runs(platform, srcs):
    repo, root, sub = REPOS[platform]
    R = rows(os.path.join(root, sub, "index", "runs.tsv")) if os.path.exists(os.path.join(root, sub, "index", "runs.tsv")) else []
    cited = set()
    for s, _ in srcs:
        m = re.match(rf"^{repo}@[0-9a-f]+:{re.escape(sub)}(?:raw|derived)/runs/([^/]+)", s) or re.search(r"raw/runs/([^/\s]+)", s)
        if m:
            cited.add(m.group(1))
    out = collections.defaultdict(lambda: [0, 0])
    for r in R:
        k = r.get("kind", "?")
        out[k][0] += 1
        out[k][1] += r["run_id"] in cited
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=os.path.join(MODEL, "held-vs-read.tsv"))
    ap.add_argument("--platform", choices=PLATFORMS)
    ap.add_argument("--detail", action="store_true")
    a = ap.parse_args()
    srcs = read_sources()
    lines = []
    for p in ([a.platform] if a.platform else PLATFORMS):
        read_pages = set()
        for s, loc in srcs[p]:
            if s.startswith(("http://", "https://")):
                read_pages.add(page_key(s))
            else:
                k = local_to_page(s)
                if k:
                    read_pages.add(k)
        held = held_pages_captures(p)
        held.update(held_pages_observed(p) if REPOS[p][0] != "other-product-class" else held_pages_opc(p))
        if REPOS[p][0] == "other-product-class":
            pass
        groups = collections.defaultdict(lambda: [0, 0])
        for k in held:
            g = group_of(k)
            groups[g][0] += 1
            groups[g][1] += k in read_pages
        tot_h, tot_r = len(held), len(set(held) & read_pages)
        print(f"== {p}: pages held readable {tot_h}, read by the model {tot_r}, unread {tot_h - tot_r}"
              f" (the model also cites {len(read_pages - set(held))} addresses not found held)")
        for g, (h, r) in sorted(groups.items(), key=lambda x: -(x[1][0] - x[1][1])):
            lines.append([p, "pages", g, h, r, h - r, ""])
        if a.detail:
            for g, (h, r) in sorted(groups.items(), key=lambda x: -(x[1][0] - x[1][1]))[:25]:
                print(f"   pages {g}: held {h}, read {r}, unread {h - r}")
        st = structures(p, srcs[p])
        sh = [s for s in st if s["held"]]
        sr = [s for s in sh if s["read"]]
        print(f"   structures registered {len(st)}, held {len(sh)}, read {len(sr)}, unread {len(sh) - len(sr)};"
              f" items in unread structures {sum(s['items'] for s in sh if not s['read'])};"
              f" items in read ones {sum(s['items'] for s in sr)}, of them cited {sum(s['items_read'] for s in sr)};"
              f" lines added since read to read ones {sum(s['added_since'] for s in sr)}")
        for s in st:
            lines.append([p, "structure", s["structure"], int(s["held"]), int(s["read"]), int(s["held"] and not s["read"]),
                          f"items {s['items']}; items cited {s['items_read']}; added since read {s['added_since']}; read at {s['read_at'] or '-'}; seen {s['date_seen']}; status {s['status']}; {s['what']}"])
        if a.detail:
            for s in sorted([s for s in sh if not s["read"]], key=lambda s: -s["items"]):
                print(f"   unread structure {s['structure']}: {s['items']} items, seen {s['date_seen']}: {s['what'][:100]}")
        rk = runs(p, srcs[p])
        print("   runs by kind (held, read): " + "; ".join(f"{k} {h}/{r}" for k, (h, r) in sorted(rk.items())))
        for k, (h, r) in sorted(rk.items()):
            lines.append([p, "runs", k, h, r, h - r, ""])
        lg = ledgers(p)
        dens = sorted({d for d, _ in lg})
        print(f"   the repository's ledger: {len(dens)} denominators" + ("" if dens else " (none kept)"))
        for (d, st), n in sorted(lg.items()):
            lines.append([p, "ledger", f"{d}: {st}", n, "", "", "the repository's own count, index/ledger"])
    if not a.platform:
        with open(a.out, "w", encoding="utf-8") as f:
            f.write("\t".join(["platform", "kind", "group", "held", "read", "unread", "note"]) + "\n")
            for l in lines:
                f.write("\t".join(str(x).replace("\t", " ") for x in l) + "\n")
        print(f"wrote {os.path.relpath(a.out, ROOT)}: {len(lines)} rows")


if __name__ == "__main__":
    main()

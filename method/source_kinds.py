# The kind of a cited source, assigned by rule rather than by an agent's judgment (PLAN.md section 6, the test form):
#   observed       a recorded store or session: run records, and structures built from a session's answers or pages
#   shipped        code or a schema the platform ships: the WooCommerce release, bundles, import maps, schemas
#   stated         the platform's docs, help centre and other pages
#   official page  terms, policies, legal, privacy and pricing pages
# Each answer carries the rule that gave it, so a reader can challenge the rule rather than the agent.
#
# Usage as a command: python3 -I method/source_kinds.py SOURCE [SOURCE ...]
import csv, glob, json, os, re

OFFICIAL = re.compile(r"/(legal|terms|tos|policies|policy|privacy|pricing|plans|agreements?)\b|terms[-_]?of[-_]?service|"
                      r"acceptable[-_]use|/conditions|/الشروط|/سياسة", re.I)
SHIPPED = re.compile(r"\.(m?js|map)(\?|$)|importmap|/bundles?/|/chunks?/|/assets/|graphql[^ ]*schema|/schema(\.json)?(\?|$)", re.I)
SESSION_KEYS = {"trace", "bodies", "operation", "run_files", "steps", "dumps_sha256", "html_file", "step", "run_ids",
                "captured", "element"}
_meta_cache = {}
_manifest_cache = {}
SKM = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def kind_of_url(u):
    if OFFICIAL.search(u):
        return "official page", "the address is a terms, policy, legal or pricing page"
    if SHIPPED.search(u):
        return "shipped", "the address is code or a schema the platform ships"
    return "stated", "the address is a docs, help or other page"

def _structure_meta(root, structure_dir, path=""):
    """The meta.json nearest the cited file, from its own folder up to the structure's; else the structure's first."""
    d = os.path.dirname(path)
    while path and len(d) > len(structure_dir) and d.startswith(structure_dir + "/"):
        m = os.path.join(root, d, "meta.json")
        if os.path.isfile(m):
            try:
                return json.load(open(m, encoding="utf-8"))
            except Exception:
                break
        d = os.path.dirname(d)
    key = (root, structure_dir)
    if key not in _meta_cache:
        metas = sorted(glob.glob(os.path.join(root, structure_dir, "**", "meta.json"), recursive=True))
        _meta_cache[key] = None
        for m in metas:
            try:
                _meta_cache[key] = json.load(open(m, encoding="utf-8"))
                break
            except Exception:
                continue
    return _meta_cache[key]

def _captured_url(path):
    """The address a captured copy in this repository was fetched from, by its run's manifest."""
    m = re.match(r"^(evidence/.+?/runs/[^/]+)/(items/[^/]+)/", path)
    if not m:
        return ""
    run, item = m.group(1), m.group(2)
    if run not in _manifest_cache:
        rows = {}
        mf = os.path.join(SKM, run, "manifest.tsv")
        if os.path.isfile(mf):
            with open(mf, encoding="utf-8", newline="") as f:
                for r in csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE):
                    rows[r.get("dir", "")] = r.get("url") or r.get("final_url") or ""
        _manifest_cache[run] = rows
    return _manifest_cache[run].get(item, "")

def kind_of(source, roots):
    """(kind, rule) for a citation's source, or ("unknown", why)."""
    if source.startswith("woocommerce-11.2.1:"):
        return "shipped", "a file of the WooCommerce release"
    if re.match(r"^https?://", source):
        return kind_of_url(source)
    m = re.match(r"^(observed-sh|observed-sa|sharrwah-knowledge-map)(?:@[0-9a-f]+)?:(.+)$", source)
    if not m:
        return "unknown", "not a known source form"
    repo, path = m.group(1), m.group(2).strip().lstrip("/")
    if repo == "sharrwah-knowledge-map":
        if path.startswith("evidence/"):
            url = _captured_url(path)
            k, why = kind_of_url(url or path)
            return k, (f"a captured copy of {url[:80]}: {why}" if url else f"a captured copy in this repository: {why}")
        return "unknown", "a file of this repository outside evidence/ is not a platform source"
    if path.startswith("raw/runs/"):
        run = path.split("/")[2] if len(path.split("/")) > 2 else ""
        if re.search(r"journey|sweep|session|real|store|trial|m0-|capture|import", run, re.I):
            return "observed", f"run {run} records a store or session"
        return "stated", f"run {run} fetched pages"
    if path.startswith("derived/"):
        name = path.split("/")[1]
        if re.search(r"by-store|store|journey|session|staff|writes|map-steps|map-units|step-text", name, re.I):
            return "observed", f"derived/{name} is built from recorded runs"
        if re.search(r"help", name, re.I):
            return "stated", f"derived/{name} is built from help pages"
        return "shipped", f"derived/{name} is built from shipped code"
    if path.startswith("structures/"):
        parts = path.split("/")
        sdir = "/".join(parts[:3])
        meta = _structure_meta(roots.get(repo, ""), sdir, path) or {}
        src = meta.get("source") if isinstance(meta, dict) else None
        if not isinstance(src, dict):
            return "unknown", f"{sdir} has no readable meta.json"
        uri = next((src[k] for k in ("uri", "url", "uri_regex", "uri_prefix", "uri_pattern") if isinstance(src.get(k), str)), "")
        if (SESSION_KEYS & set(src)) and "warc" not in src and not src.get("uri_regex"):
            return "observed", f"{sdir} is built from a recorded session"
        if "yaml" in src or "openapi" in src:
            return "shipped", f"{sdir} is built from an API definition the platform publishes"
        if uri:
            k, why = kind_of_url(uri.replace("\\", ""))
            return k, f"{sdir} holds {uri[:80]}: {why}"
        runs = src.get("runs") if isinstance(src.get("runs"), list) else []
        run = str(src.get("run") or src.get("run_id") or (runs[0] if runs else ""))
        if run:
            if re.search(r"cli", run, re.I):
                return "shipped", f"{sdir} is built from the platform's CLI, run {run}"
            if re.search(r"journey|sweep|session|store|showcase|trial|m0-|capture|import|real", run, re.I):
                return "observed", f"{sdir} is built from run {run}, which records a store or session"
            k, why = kind_of_url(run)
            return k, f"{sdir} is built from run {run}, which fetched pages"
        recs = src.get("warc_records") or src.get("records") or []
        if isinstance(recs, list) and recs and isinstance(recs[0], dict) and isinstance(recs[0].get("uri"), str):
            k, why = kind_of_url(recs[0]["uri"])
            return k, f"{sdir} holds {recs[0]['uri'][:80]}: {why}"
        return "unknown", f"{sdir}'s meta.json names no address, run or session"
    k, why = kind_of_url("https://" + path)
    return k, f"a held file named for its address: {why}"

if __name__ == "__main__":
    import sys
    roots = {"observed-sh": os.environ.get("OBSERVED_SH", "/home/user/observed-sh"),
             "observed-sa": os.environ.get("OBSERVED_SA", "/home/user/observed-sa")}
    for s in sys.argv[1:]:
        print(s, "->", *kind_of(s, roots), sep="\t")

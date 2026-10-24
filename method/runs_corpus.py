"""The observed repositories' runs, as documents for method/corpus_search.py.

What each file is, is in each repository's own guide, docs/READING.md. The documents are:
- what a run's pages received from the platform: observed-sh's answers (`raw/runs/<run>/answers/...`, each named in
  the run's `answers.jsonl` with its operation, store and steps) and observed-sa's saved responses
  (`raw/runs/<run>/responses/NNNN.json`, each named in the run's `responses.jsonl` with its host, path, status and
  step);
- what each step's page showed: `steps/NNN.aria.yaml`, `NNN.text.txt`, an Android screen's `NNN.uia.xml`, and each
  frame's, one document per step, titled from the run's `actions.jsonl`; a terminal run's `transcript.plain.txt`;
  the files a step downloaded;
- observed-sh's text of the saved step and frame HTML that has no `text.txt` (`derived/step-text-from-html/<run>/
  NNN.html.txt` and `NNN.frame-K.html.txt`), one document per step, titled from the run's `actions.jsonl`. It is the
  saved markup's text, not what the page showed: its guide says what it holds;
- the requests a run's pages sent: observed-sh's `guard.jsonl` and observed-sa's `writes.jsonl`, one line each;
- the indexes and tables built from the runs: observed-sh's `index/operations.jsonl` and `derived/`, observed-sa's
  `index/rest-endpoints.tsv` and `derived/`, one line each where the file has lines;
- Salla's own maps of its surfaces, `structures/salla/<id>/`: each `items.jsonl` line and each `source.*` file
  (Shopify's `items.jsonl` are searched already; its `source.*` files are added here).

They are read from git at the repository's HEAD, folded for matching, and written once per commit to
~/.cache/sharrwah-corpus/<repository>-runs-<commit>.txt: one document per line, its fields separated by \\x1f. The
first search builds it, in some minutes. A search reads only the lines ripgrep finds holding a term.
"""
import json, os, re, subprocess, sys, threading
from collections import defaultdict

CACHE = os.path.join(os.path.expanduser("~"), ".cache", "sharrwah-corpus")
REPOS = {"observed-sa": "/home/user/observed-sa", "observed-sh": "/home/user/observed-sh"}
RUN_REPO = {"shopify": "observed-sh", "salla": "observed-sa"}
SEP = "\x1f"
LINES = (".jsonl", ".tsv", ".csv")
TEXTUAL = re.compile(r"\.(json|jsonl|tsv|csv|txt|md|html|xml|yaml|yml)$")
STEP = re.compile(r"^raw/runs/([^/]+)/steps/(\d+)\.(?:(frame-\d+)\.)?(aria\.yaml|text\.txt|uia\.xml)$")
HTML_TEXT = re.compile(r"^derived/step-text-from-html/([^/]+)/(\d+)\.(?:(frame-\d+)\.)?html\.txt$")


def corpus_names(repo):
    """The corpora a repository's runs make, in the order a search lists them."""
    what = "answers" if repo == "observed-sh" else "saved responses"
    return [f"{repo}: {what}", f"{repo}: run steps", f"{repo}: run requests", f"{repo}: indexes and derived tables",
            f"{repo}: structures", f"{repo}: step text from saved HTML"]


def git(root, *args, **kw):
    return subprocess.run(["git", "-C", root, *args], capture_output=True, **kw)


def blobs(root, ids):
    """(id, bytes) for each object id, streamed from one `git cat-file --batch`."""
    p = subprocess.Popen(["git", "-C", root, "cat-file", "--batch"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)

    def feed():
        for i in ids:
            p.stdin.write((i + "\n").encode())
        p.stdin.close()
    threading.Thread(target=feed, daemon=True).start()
    for i in ids:
        head = p.stdout.readline().split()
        if len(head) < 3 or head[1] == b"missing":
            yield i, None
            continue
        size = int(head[2])
        data = p.stdout.read(size)
        p.stdout.read(1)
        yield i, data
    p.wait()


def json_text(raw):
    """A JSON body as one line of text, with its keys, values and unescaped strings; other bodies as they are."""
    s = raw.decode("utf-8", "replace")
    try:
        return json.dumps(json.loads(s), ensure_ascii=False, separators=(",", ":"))
    except Exception:
        return s


def flat(s):
    return re.sub(r"[\x1f\r\n\t]+", " ", s or "")


def build(repo, fold):
    """Write the repository's runs cache for its HEAD, and return its path."""
    root = REPOS[repo]
    commit = git(root, "rev-parse", "HEAD", text=True).stdout.strip()
    path = os.path.join(CACHE, f"{repo}-runs-{commit}.txt")
    if os.path.exists(path):
        return path, commit
    os.makedirs(CACHE, exist_ok=True)
    tree = {}
    for line in git(root, "ls-tree", "-r", commit).stdout.decode("utf-8", "replace").split("\n"):
        if "\t" in line:
            meta, name = line.split("\t", 1)
            tree[name] = meta.split()[2]
    docs = []           # [corpus, loc, url, [places], [paths whose text it holds], kind]
    small = {}          # path -> text, for the files read first to title the others

    def read_small(names):
        want = [n for n in names if n in tree and n not in small]
        for (i, data), n in zip(blobs(root, [tree[n] for n in want]), want):
            small[n] = data.decode("utf-8", "replace")

    runs = sorted({n.split("/")[2] for n in tree if n.startswith("raw/runs/")})
    lists = [f"raw/runs/{r}/{f}" for r in runs for f in ("answers.jsonl", "responses.jsonl", "actions.jsonl", "run.json")]
    read_small(lists)
    corp = corpus_names(repo)
    # what a run's pages received: one document per distinct body, with every run, store and step that received it
    seen = {}
    for r in runs:
        for f in ("answers.jsonl", "responses.jsonl"):
            raw = small.get(f"raw/runs/{r}/{f}")
            if not raw:
                continue
            store = ""
            try:
                store = (json.loads(small.get(f"raw/runs/{r}/run.json", "{}")).get("extra") or {}).get("store") or ""
            except Exception:
                pass
            for line in raw.splitlines():
                try:
                    o = json.loads(line)
                except Exception:
                    continue
                name = f"raw/runs/{r}/{o.get('file', '')}"
                if name not in tree:
                    continue
                if f == "answers.jsonl":
                    steps = o.get("steps") or sorted({c.get("step") for c in o.get("calls") or [] if c.get("step") is not None})
                    where = f"{o.get('operation', '')}, store {o.get('store') or '-'}, run {r}, step {','.join(map(str, steps)) or '-'}"
                    url = f"https://{o.get('host', '')}{o.get('endpoint', '')}"
                else:
                    where = (f"{o.get('method', '')} {o.get('host', '')}{o.get('path', '')}, status {o.get('status')}, "
                             f"store {store or '-'}, run {r}, step {o.get('step')}")
                    url = f"https://{o.get('host', '')}{o.get('path', '')}"
                blob = tree[name]
                if blob in seen:                  # the same body received again: one document, every place listed
                    seen[blob][3].append(where)
                    continue
                seen[blob] = [corp[0], f"{repo}@{commit}:{name}", url, [where], [name], "json"]
                docs.append(seen[blob])
    # what each step's page showed, one document per step
    steps = defaultdict(list)
    for n in tree:
        m = STEP.match(n)
        if m:
            steps[(m.group(1), m.group(2))].append(n)
    acts = {}
    for r in runs:
        for line in (small.get(f"raw/runs/{r}/actions.jsonl") or "").splitlines():
            try:
                o = json.loads(line)
                acts[(r, int(o.get("step")))] = o
            except Exception:
                pass
    for (r, nnn), names in sorted(steps.items()):
        names.sort(key=lambda n: (".frame-" in n, n))
        a = acts.get((r, int(nnn)), {})
        title = f"run {r}, step {nnn}: {a.get('title') or a.get('focus') or ''} | {a.get('intent') or ''}"
        files = ", ".join(n.rsplit("/", 1)[1] for n in names)
        docs.append([corp[1], f"{repo}@{commit}:raw/runs/{r}/steps/ ({files})", a.get("url") or a.get("target") or "",
                     [title], names, "text"])
    # the text of saved step HTML that has no text.txt (observed-sh), one document per step, titled the same way
    html_steps = defaultdict(list)
    for n in tree:
        m = HTML_TEXT.match(n)
        if m:
            html_steps[(m.group(1), m.group(2))].append(n)
    for (r, nnn), names in sorted(html_steps.items()):
        names.sort(key=lambda n: (".frame-" in n, n))
        a = acts.get((r, int(nnn)), {})
        title = f"run {r}, step {nnn}: {a.get('title') or ''} | {a.get('intent') or ''}"
        files = ", ".join(n.rsplit("/", 1)[1] for n in names)
        docs.append([corp[5], f"{repo}@{commit}:derived/step-text-from-html/{r}/ ({files})",
                     a.get("url") or a.get("target") or "", [title], names, "text"])
    for n in sorted(tree):
        if re.match(r"^raw/runs/[^/]+/(transcript\.plain\.txt|downloads/.+\.(csv|txt))$", n):
            docs.append([corp[1], f"{repo}@{commit}:{n}", "", [f"run {n.split('/')[2]}: {n.split('/', 3)[3]}"], [n], "text"])
    # line files: requests sent, indexes, derived tables, structures' items
    line_files = [n for n in sorted(tree) if re.match(r"^raw/runs/[^/]+/(guard|writes)\.jsonl$", n)]
    index_files = [n for n in sorted(tree) if (n.startswith("derived/") and TEXTUAL.search(n)
                                               and not n.startswith("derived/step-text-from-html/"))
                   or n in ("index/operations.jsonl", "index/rest-endpoints.tsv")]
    struct = "structures/salla/" if repo == "observed-sa" else "structures/shopify/"
    struct_files = [n for n in sorted(tree) if n.startswith(struct) and TEXTUAL.search(n)
                    and (n.endswith("/items.jsonl") and repo == "observed-sa" or "/source." in n.rsplit("/", 1)[-1]
                         or n.rsplit("/", 1)[-1].startswith("source."))
                    and "/help-center/" not in n and "/help-articles/" not in n]
    for corpus, names in ((corp[2], line_files), (corp[3], index_files), (corp[4], struct_files)):
        for n in names:
            docs.append([corpus, f"{repo}@{commit}:{n}", "", [n], [n], "lines" if n.endswith(LINES) else "text"])
    # read every body once, in the documents' order, fold it, and write
    names = [n for d in docs for n in d[4] if n not in small]
    stream = blobs(root, [tree[n] for n in names])
    tmp = f"{path}.{os.getpid()}.part"         # each builder writes its own file; the last finished wins
    with open(tmp, "w", encoding="utf-8") as out:
        def emit(d, text, loc=None, title=None):
            t = title if title is not None else "; ".join(d[3][:3]) + (f"; and {len(d[3]) - 3} more" if len(d[3]) > 3 else "")
            out.write(SEP.join(flat(x) for x in (d[0], loc or d[1], d[2], t, fold(t + "\n" + d[2] + "\n" + text))) + "\n")
        for d in docs:
            parts = [small[n].encode() if n in small else (next(stream)[1] or b"") for n in d[4]]
            if d[5] == "json":
                emit(d, json_text(parts[0]))
            elif d[5] == "lines":
                name = d[4][0]
                lines = parts[0].decode("utf-8", "replace").splitlines()
                header = lines[0] if name.endswith((".tsv", ".csv")) and lines else ""
                for i, line in enumerate(lines, start=1):
                    if line.strip() and not (header and i == 1):
                        emit(d, (header + "\n" if header else "") + line, loc=f"{d[1]} line {i}", title=f"{name} line {i}")
            else:
                emit(d, "\n".join(x.decode("utf-8", "replace") for x in parts))
    os.replace(tmp, path)
    return path, commit


def search(platform, fold, terms, every, also):
    """(corpus, loc, url, title, body) of each document of the platform's runs that ripgrep finds holding a folded
    term (every term with `every`) and, given `also`, one of those too. `body` is folded already."""
    repo = RUN_REPO.get(platform)
    if not repo:
        return
    path, _ = build(repo, fold)
    want = [fold(t) for t in terms]
    pipeline = [["rg", "-F", "--no-filename", "--no-line-number"] + [a for w in want for a in ("-e", w)] + [path]]
    if every:
        pipeline += [["rg", "-F", "--no-filename", "--no-line-number", "-e", w] for w in want]
    if also:
        pipeline.append(["rg", "-F", "--no-filename", "--no-line-number"] + [a for w in also for a in ("-e", fold(w))])
    procs, stdin = [], None
    for cmd in pipeline:
        p = subprocess.Popen(cmd, stdin=stdin, stdout=subprocess.PIPE)
        if stdin is not None:
            stdin.close()
        stdin = p.stdout
        procs.append(p)
    for line in stdin:
        parts = line.decode("utf-8", "replace").rstrip("\n").split(SEP)
        if len(parts) == 5:
            yield tuple(parts)
    for p in procs:
        p.wait()


if __name__ == "__main__":
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from corpus_search import fold
    for repo in sys.argv[1:] or sorted(REPOS):
        print(build(repo, fold)[0])

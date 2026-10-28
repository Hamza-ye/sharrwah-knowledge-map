# Operating the capture

How to run the tools. Each script's header gives its arguments; the repository README says what the files hold.
Every tool takes the platform folder it writes into (`PLATFORM=zid`, or its first argument).

## Setup

```sh
uv sync         # pyproject.toml → .venv
npm install     # package.json
```

The system Google Chrome (`google-chrome`) is used, headed.

## Browser

```sh
capture/chrome.sh [start-url]                                                  # ./capture-profile, port 9230 (Zid's demo)
CAPTURE_PROFILE=$PWD/capture-profile-signup CDP_PORT=9240 capture/chrome.sh    # Zid partner account, development store
```

- A run on the second browser takes `CDP_URL=http://127.0.0.1:9240`.
- The development store is signed in to from the Partner Dashboard (`partner.zid.sa`, Development Stores, Dashboard
  Access: a one-time link to `dashboard.zid.sa/en-sa/login/otl/…`).
- Codes Zid emails go to the capture inbox (`sharrwah@gmail.com`, read in observed-sh's owner browser, port 9222,
  Gmail account 1). A sign-up code expires in about two minutes: read it at once, and type all its digits in one
  `journey_step.py` call with `"readyTimeout": 1000` on each step (a page without a main landmark otherwise waits 30
  seconds a step).

- Do not close a tab a run is using: its trace is written when the run closes.
- After signing in to a new account or store, add it to `<platform>/index/instruments.json` with the run that shows it.

## Runs

```sh
PLATFORM=zid node capture/runs/journey-repl.mjs <label> <store> <commands.jsonl>      # a journey
python3 capture/journey_step.py <run-dir> <commands.jsonl> '<json>' ['<json>' ...]   # its next steps
PLATFORM=zid capture/fetch.sh <label> <url-list-file> [wait-seconds]                  # a list of URLs into a WARC
```

- A journey's commands can all be written to its commands file before it starts, ending with `{"do": "close"}`: the
  runner takes them in order (a sweep of a route list). `journey_step.py` sends the next steps of a live run and waits
  for them.
- `RUN_CONTEXT=fresh` runs in a new browser context, without the profile's cookies or storage (a first visit).
- Record in English from a run's first step to its last: Zid's dashboard takes the language from the path
  (`/en-sa/…`); `actions.jsonl` gives each step's page language (`lang`).
- Not held: files coding agents load as instructions (AGENTS.md, CLAUDE.md, GEMINI.md, SKILL.md, .cursorrules, ...)
  and robots.txt. `capture/fetch.sh` lists such URLs in `skipped-urls.txt` instead of fetching them; `.gitignore`
  blocks the names.

## Zid

- `https://dashboard.zid.sa/en-sa/demo` signs the browser in to Zid's demo store (store 127604) as its owner and
  opens its dashboard in English. Every visitor shares that store.
- The dashboard's route manifest is the `assets/manifest-<version>.js` file its shell page names; the version changes
  when Zid deploys. A sweep's commands come from the manifest held in the same day's code fetch.

## Structures

```sh
.venv/bin/python capture/structure_zid_dashboard_manifest.py <code-fetch-run>                    # route manifest
.venv/bin/python capture/structure_zid_dashboard_locales.py <code-fetch-run> <locales-fetch-run>  # locales
.venv/bin/python capture/structure_zid_dashboard_page_index.py <code-fetch-run>                  # page index
python3 capture/structure_zid_store_profile.py <browser-run>                                     # plan policies, permissions
```

A code fetch run holds the shell page (first URL), the manifest it names and every module and import the manifest
lists; the locales fetch run holds the files the entry module states. Register every structure seen in
`<platform>/structures/REGISTER.tsv`.

## After any run

```sh
python3 capture/answers.py zid                 # browser runs: the answers and writes, from the trace
python3 capture/runs_index.py zid              # index/runs.tsv, index/SHA256SUMS
python3 capture/ledger_zid.py                  # index/ledger/: the manifest's routes and the steps that hold them
sha256sum -c --quiet zid/index/SHA256SUMS
git add -A
```

A run file over 95 MB is cut in order before `git add` (GitHub refuses a file over 100 MB):
`split -b 90000000 -d -a 2 trace.zip trace.zip.`, check that `cat trace.zip.?? | sha256sum` equals the file's
sha256, remove the file, and give the hash in the run's note; `capture/answers.py` reads the parts.

Note anything unusual about a run in `<platform>/index/run-notes.tsv`. A run that a later run re-drives in full is
removed (its folder and its notes). Then commit and push: origin pushes over SSH (`git remote set-url --push origin
git@github.com:Hamza-ye/other-product-class.git`). A push of more than a few tens of MB can drop on this connection:
commit and push a run at a time, with `GIT_SSH_COMMAND="ssh -o ServerAliveInterval=15 -o ServerAliveCountMax=40"`,
and push again if it drops.

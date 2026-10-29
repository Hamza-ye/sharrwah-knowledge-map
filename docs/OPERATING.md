# Operating the capture

How to run the tools. Each script's header gives its arguments; the repository README says what the files hold.
Every tool takes the platform folder it writes into (`PLATFORM=zid`, or its first argument).

## Setup

```sh
uv sync         # pyproject.toml → .venv
npm install     # package.json (playwright-core; cloudflared, the WooCommerce store's tunnel)
```

The system Google Chrome (`google-chrome`) is used, headed.

## Browser

```sh
capture/chrome.sh [start-url]                                                  # ./capture-profile, port 9230 (Zid's demo)
CAPTURE_PROFILE=$PWD/capture-profile-signup CDP_PORT=9240 capture/chrome.sh    # Zid partner account, development store
CAPTURE_PROFILE=$PWD/capture-profile-bigcommerce CDP_PORT=9250 capture/chrome.sh   # BigCommerce account and trial store
CAPTURE_PROFILE=$PWD/capture-profile-woocommerce CDP_PORT=9251 capture/chrome.sh   # the WooCommerce test store's admin
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

```sh
PLATFORM=bigcommerce capture/jstep.sh <label> start <store> <cdp-port> profile|fresh   # a journey, its runner in the background
capture/jstep.sh <label> '<json>' ['<json>' ...] [<lines>]                           # its next steps
capture/jstep.sh <label> show <step> aria|text|frame|html|htmlctx [<regex>]          # a held step
capture/jstep.sh <label> log                                                         # the runner's output (evaluate values)
capture/jstep.sh <label> close
```

- `RUN_ADOPT_PAGE=<address prefix>` before `start` makes the run take over the open tab at that address (a tab where a
  person ticked a CAPTCHA) and leave it open at the end.
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

## BigCommerce

- The account is 7amza.it+bc-na@gmail.com (`BIGCOMMERCE_ACCOUNT_PASSWORD`); log-in on a new browser asks for a code
  emailed to it, read in the capture inbox (port 9222; plus-addresses of 7amza.it@gmail.com arrive there). The trial
  store is `store-w5pamplexj.mybigcommerce.com/manage/`; its account pages are on `manage.bigcommerce.com`.
- BigCommerce refuses its trial sign-up through the VPN this machine can route BigCommerce through (`create-store`
  `{"pass":false}`): its domains go through the Yemeni network. The sign-up's reCAPTCHA, and a form BigCommerce takes,
  are the founder's hand; record it with `RUN_ADOPT_PAGE`.
- The Help Center (support.bigcommerce.com) draws its pages with JavaScript: read it with a browser run
  (`RUN_CONTEXT=fresh`). docs.bigcommerce.com and commerce.com's terms answer `capture/fetch.sh`.

## WooCommerce

The test store runs on this machine (`capture/woocommerce/compose.yaml`: WordPress, MariaDB, WP-CLI) and is reached
through a Cloudflare quick tunnel, whose address WordPress.com (Jetpack, WooPayments) and the browser use:

```sh
node_modules/.bin/cloudflared tunnel --no-autoupdate --url http://127.0.0.1:8090 --logfile /tmp/other-product-class-journeys/cloudflared.log
# the address (https://<name>.trycloudflare.com) is in the log; it changes each time the tunnel starts: set SITE_URL in .env, then
docker compose --env-file .env -f capture/woocommerce/compose.yaml up -d
docker compose --env-file .env -f capture/woocommerce/compose.yaml run --rm -T cli wp option update home "$SITE_URL"   # and siteurl
capture/woocommerce/db_snapshot.sh <label>    # the database as a run: wordpress.sql, options.tsv
```

- The admin is `capture-admin` (`WOO_ADMIN_PASSWORD`). WooCommerce 11.2.1 needs WordPress 7.0 or later (`wp core
  update` took the image's 6.9.4 to 7.1.4).
- The store's REST API is called from its own admin page with `{"do": "evaluate", "js": "wp.apiFetch({...})"}`; the
  trace holds each call and answer.
- WordPress.com answers the Jetpack connection with a human check ("Confirm you are human"), which is the founder's
  hand; WooPayments' test account and business verification wait for that connection.

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
python3 capture/answers.py <platform>          # browser runs: the answers and writes, from the trace
python3 capture/runs_index.py <platform>       # index/runs.tsv, index/SHA256SUMS
python3 capture/ledger_zid.py                  # Zid: index/ledger/, the manifest's routes and the steps that hold them
sha256sum -c --quiet <platform>/index/SHA256SUMS
git add <platform>/ ...                        # by path: other platforms' work may be in the tree
```

A run file over 95 MB is cut in order before `git add` (GitHub refuses a file over 100 MB):
`split -b 90000000 -d -a 2 trace.zip trace.zip.`, check that `cat trace.zip.?? | sha256sum` equals the file's
sha256, remove the file, and give the hash in the run's note; `capture/answers.py` reads the parts.

Note anything unusual about a run in `<platform>/index/run-notes.tsv`. A run that a later run re-drives in full is
removed (its folder and its notes). Then commit and push: origin pushes over SSH (`git remote set-url --push origin
git@github.com:Hamza-ye/other-product-class.git`). A push of more than a few tens of MB can drop on this connection:
commit and push a run at a time, with `GIT_SSH_COMMAND="ssh -o ServerAliveInterval=15 -o ServerAliveCountMax=40"`,
and push again if it drops.

After every push to origin, push the same `main` to the knowledge map's branch `evidence/other-product-class`, the
copy the knowledge map's coordinator reads (it cannot reach this repository):
`git push knowledge-map main:evidence/other-product-class` (the remote, once:
`git remote add knowledge-map git@github.com:Hamza-ye/sharrwah-knowledge-map.git`). The commits keep their ids, so
`other-product-class@<commit>:<path>` cites the same bytes there.

// Journey runner driven one step at a time: keeps a single run open and executes commands appended to
// a command file, so each next step can be chosen from what the previous step's page showed.
//   PLATFORM=<platform folder> node capture/runs/journey-repl.mjs <label> <store> <commands.jsonl>
// "{{store}}" in a command's url is replaced by <store>, so a committed script replays on another store.
// commands.jsonl: one JSON object per line, appended while the runner is live:
//   {"intent": "...", "do": "goto", "url": "..."}
//   {"intent": "...", "do": "click"|"fill"|"check"|"select"|"press"|"hover", "role": "button", "name": "Save",
//    "exact": true, "nth": 0, "value": "...", "within": {"role": "dialog"}}
//   {"intent": "...", "do": "text", "text": "Mark as paid"}        (click by visible text)
//   {"intent": "...", "do": "click", "css": "button:has-text('Create')"}   (CSS; pierces open shadow roots)
//   {"intent": "...", "do": "fill", "frame": "iframe[...]", "css": "input", "value": "1"}   (inside an iframe)
//   {"intent": "...", "do": "fill", "role": "textbox", "name": "Password", "value_env": "VAR"}
//      (fills a value held in the repository's .env; commands.jsonl and the row name only the variable)
//   {"intent": "...", "do": "upload", "css": "input[type=file]", "files": ["<path>"]}
//   {"intent": "...", "do": "upload", "chooser": true, "role": "button", "name": "Upload", "files": [...]}
//   {"intent": "...", "do": "download", "role": "link", "name": "report.csv"}   or   {..., "do": "download", "url": "..."}
//      (saves the download as <run>/downloads/NNN-<suggested name>)
//   {"intent": "...", "do": "scroll", "css": "..."}                 (scrolls the element into view)
//   {"do": "stopped-at-confirm", "control": "Pay", "step": 8, "evidence": "..."}
//      (records that the journey reached a confirmation at that step and did not click it; written to
//       <run>/stopped-at-confirm.jsonl)
//   "in_popup": true on any command acts on the newest other tab of the context
//   {"do": "close"}
// After each step the runner writes <run>/last.json (step row) so the caller can read the outcome and
// steps/NNN.aria.yaml.
import fs from 'node:fs';
import { openRun } from '../session.mjs';

const [label, store, cmdFile] = process.argv.slice(2);
const run = await openRun({ label, script: new URL(import.meta.url).pathname, extra: { store, commands_file: cmdFile } });
console.log('run dir:', run.dir);

function envValue(name) {
  const line = fs.readFileSync(new URL('../../.env', import.meta.url), 'utf8').split('\n').find((l) => l.startsWith(`${name}=`));
  if (!line) throw new Error(`${name} is not in .env`);
  return line.slice(name.length + 1).split('  #')[0].trim();
}

function locate(page, c) {
  let scope = page;
  if (c.frame) scope = page.frameLocator(c.frame);
  if (c.within) scope = page.getByRole(c.within.role, c.within.name ? { name: c.within.name } : {}).last();
  let loc = c.css ? scope.locator(c.css) : c.role ? scope.getByRole(c.role, c.name !== undefined ? { name: c.name, exact: !!c.exact } : {})
    : c.label ? scope.getByLabel(c.label, { exact: !!c.exact })
      : c.placeholder ? scope.getByPlaceholder(c.placeholder)
        : scope.getByText(c.text, { exact: !!c.exact });
  return c.nth !== undefined ? loc.nth(c.nth) : loc.first();
}

let consumed = 0;
let stepNo = 0;
for (;;) {
  const lines = fs.existsSync(cmdFile) ? fs.readFileSync(cmdFile, 'utf8').split('\n').filter((l) => l.trim()) : [];
  if (lines.length <= consumed) { await new Promise((r) => setTimeout(r, 500)); continue; }
  const c = JSON.parse(lines[consumed++]);
  if (c.url) c.url = c.url.replaceAll('{{store}}', store);
  fs.appendFileSync(`${run.dir}/commands.jsonl`, JSON.stringify(c) + '\n');
  if (c.do === 'close') break;
  if (c.do === 'stopped-at-confirm') { fs.appendFileSync(`${run.dir}/stopped-at-confirm.jsonl`, JSON.stringify(c) + '\n'); continue; }
  stepNo++;
  const row = await run.step(c.intent || JSON.stringify(c), async (page) => {
    if (c.in_popup) page = page.context().pages().filter((p) => p !== page).at(-1) || page;
    if (c.do === 'download') {
      const start = c.url ? page.goto(c.url).catch(() => {}) : locate(page, c).click({ timeout: 15000 });
      const [dl] = await Promise.all([page.waitForEvent('download', { timeout: 60000 }), start]);
      fs.mkdirSync(`${run.dir}/downloads`, { recursive: true });
      return dl.saveAs(`${run.dir}/downloads/${String(stepNo).padStart(3, '0')}-${dl.suggestedFilename()}`);
    }
    if (c.do === 'goto') return page.goto(c.url, { waitUntil: 'domcontentloaded' });
    if (c.do === 'press') return page.keyboard.press(c.key || c.value);
    const loc = c.do === 'text' ? page.getByText(c.text, { exact: !!c.exact }).first() : locate(page, c);
    if (c.do === 'click' || c.do === 'text') return loc.click({ timeout: 15000 });
    if (c.do === 'fill') return loc.fill(c.value_env ? envValue(c.value_env) : c.value, { timeout: 15000 });
    if (c.do === 'check') return loc.check({ timeout: 15000 });
    if (c.do === 'select') return loc.selectOption(c.value, { timeout: 15000 });
    if (c.do === 'hover') return loc.hover({ timeout: 15000 });
    if (c.do === 'scroll') return loc.scrollIntoViewIfNeeded({ timeout: 15000 });
    if (c.do === 'upload' && c.chooser) {
      const [chooser] = await Promise.all([page.waitForEvent('filechooser', { timeout: 15000 }), loc.click({ timeout: 15000 })]);
      return chooser.setFiles(c.files);
    }
    if (c.do === 'upload') return loc.setInputFiles(c.files, { timeout: 15000 });
    throw new Error(`unknown command ${c.do}`);
  }, { target: c.url || null, readyTimeout: c.readyTimeout || 30000, settleMs: c.settleMs || 2000, fullPage: !!c.fullPage });
  fs.writeFileSync(`${run.dir}/last.json`, JSON.stringify(row));
}
console.log('run dir:', await run.close());

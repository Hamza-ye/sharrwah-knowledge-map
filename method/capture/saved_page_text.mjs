// Visible text of single-file saved pages, loaded offline (no network).
// Usage: node saved_page_text.mjs LIST_JSON   (items: {id, file, out})
import { createRequire } from 'module';
import fs from 'fs';
import path from 'path';
const require = createRequire(import.meta.url);
let pw;
try { pw = require(process.env.PLAYWRIGHT_MODULE || 'playwright'); }
catch { pw = require('/opt/node22/lib/node_modules/playwright'); }
const { chromium } = pw;
const list = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
let browser;
try { browser = await chromium.launch(process.env.CHROMIUM_PATH ? { executablePath: process.env.CHROMIUM_PATH } : {}); }
catch { browser = await chromium.launch(); }
for (const it of list) {
  const ctx = await browser.newContext({ offline: true, javaScriptEnabled: false });
  const page = await ctx.newPage();
  try {
    await page.goto('file://' + it.file, { waitUntil: 'load', timeout: 60000 });
    const text = await page.evaluate(() => document.body ? document.body.innerText : '');
    fs.mkdirSync(it.out, { recursive: true });
    fs.writeFileSync(path.join(it.out, 'text.txt'), text);
    console.log(it.id, text.length);
  } catch (e) { console.log(it.id, 'error', String(e.message).split('\n')[0]); }
  await ctx.close();
}
await browser.close();

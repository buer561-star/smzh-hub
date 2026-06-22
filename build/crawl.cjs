const { chromium } = require('/opt/node22/lib/node_modules/playwright/index.js');
const fs = require('fs');
const path = require('path');

const URLS = fs.readFileSync('build/de-urls.txt', 'utf-8').split('\n').map(s => s.trim()).filter(Boolean);
const OUT = 'build/rendered2';
const CONCURRENCY = 4;
const RETRIES = 3;
const PROGRESS = 'build/crawl-progress.log';

function log(msg) { fs.appendFileSync(PROGRESS, msg + '\n'); }
function outFile(p) { return path.join(OUT, p, 'index.html'); }

async function renderOne(ctx, p) {
  const dest = outFile(p);
  if (fs.existsSync(dest) && fs.statSync(dest).size > 5000) return 'skip';
  const url = 'https://smzh.ch' + p;
  let lastErr = '';
  for (let attempt = 1; attempt <= RETRIES; attempt++) {
    const page = await ctx.newPage();
    try {
      await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 60000 });
      try { await page.waitForLoadState('networkidle', { timeout: 20000 }); } catch {}
      for (const label of ['Alle ablehnen', 'Alle annehmen', 'Accept all', 'Reject all']) {
        const b = page.getByRole('button', { name: label });
        if (await b.count()) { try { await b.first().click({ timeout: 1500 }); break; } catch {} }
      }
      for (let y = 0; y < 7; y++) { await page.mouse.wheel(0, 1600); await page.waitForTimeout(600); }
      await page.evaluate(() => window.scrollTo(0, 0));
      await page.waitForTimeout(1800);
      const html = await page.content();
      if (html.length < 3000) throw new Error('too small ' + html.length);
      fs.mkdirSync(path.dirname(dest), { recursive: true });
      fs.writeFileSync(dest, html);
      await page.close();
      return 'ok';
    } catch (e) {
      lastErr = (e.message || '').split('\n')[0];
      await page.close().catch(() => {});
      if (attempt < RETRIES) await new Promise(r => setTimeout(r, 1500 * attempt));
    }
  }
  log('FAIL\t' + p + '\t' + lastErr);
  return 'fail';
}

(async () => {
  fs.mkdirSync(OUT, { recursive: true });
  fs.writeFileSync(PROGRESS, '');
  const browser = await chromium.launch();
  const ctx = await browser.newContext({
    viewport: { width: 1440, height: 900 },
    ignoreHTTPSErrors: true,
    userAgent: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36',
  });
  let i = 0, ok = 0, skip = 0, fail = 0;
  const queue = URLS.slice();
  async function worker(id) {
    while (queue.length) {
      const p = queue.shift();
      const n = ++i;
      const r = await renderOne(ctx, p);
      if (r === 'ok') ok++; else if (r === 'skip') skip++; else fail++;
      if (n % 20 === 0 || r === 'fail')
        log(`[${n}/${URLS.length}] ok=${ok} skip=${skip} fail=${fail}  last=${p} (${r})`);
    }
  }
  await Promise.all(Array.from({ length: CONCURRENCY }, (_, k) => worker(k)));
  log(`DONE total=${URLS.length} ok=${ok} skip=${skip} fail=${fail}`);
  await browser.close();
})();

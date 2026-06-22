const { chromium } = require('/opt/node22/lib/node_modules/playwright/index.js');
const fs = require('fs');

const pages = [
  ['smzhub',                  'https://smzh.ch/de/smzhub/'],
  ['home',                    'https://smzh.ch/de/'],
  ['rechner',                 'https://smzh.ch/de/rechner/'],
  ['markets',                 'https://smzh.ch/de/markets/'],
  ['karriere',                'https://smzh.ch/de/karriere/'],
  ['terminvereinbaren',       'https://smzh.ch/de/terminvereinbaren/'],
  ['steuererklaerung',        'https://smzh.ch/de/steuererklaerung/'],
  ['vorsorgeanalyse',         'https://smzh.ch/de/vorsorgeanalyse/'],
  ['immobilienbewertung',     'https://smzh.ch/de/immobilienbewertung/'],
  ['preise-fuer-privatkunden','https://smzh.ch/de/preise-fuer-privatkunden/'],
  ['preise-fuer-firmenkunden','https://smzh.ch/de/preise-fuer-firmenkunden/'],
  ['uber-uns',                'https://smzh.ch/de/uber-uns/'],
  ['geschaftspartner',        'https://smzh.ch/de/geschaftspartner/'],
  ['impressum',               'https://smzh.ch/de/impressum/'],
  ['datenschutz',             'https://smzh.ch/de/datenschutz/'],
  ['email-korrespondenz',     'https://smzh.ch/de/email-korrespondenz/'],
];

(async () => {
  fs.mkdirSync('build/rendered', { recursive: true });
  const browser = await chromium.launch();
  const ctx = await browser.newContext({
    viewport: { width: 1440, height: 900 },
    ignoreHTTPSErrors: true,
    userAgent: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36',
  });
  for (const [key, url] of pages) {
    const page = await ctx.newPage();
    try {
      await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 60000 });
      try { await page.waitForLoadState('networkidle', { timeout: 25000 }); } catch {}
      // Dismiss cookie banner if present
      for (const label of ['Alle ablehnen', 'Alle annehmen', 'Accept all', 'Reject all']) {
        const b = page.getByRole('button', { name: label });
        if (await b.count()) { try { await b.first().click({ timeout: 2000 }); break; } catch {} }
      }
      // Trigger lazy loading
      for (let y = 0; y < 8; y++) { await page.mouse.wheel(0, 1600); await page.waitForTimeout(700); }
      await page.evaluate(() => window.scrollTo(0, 0));
      await page.waitForTimeout(2500);
      const html = await page.content();
      fs.writeFileSync(`build/rendered/${key}.html`, html);
      const loading = await page.locator('text=Loading...').count();
      console.log(`${key.padEnd(28)} len=${String(html.length).padStart(7)}  loading=${loading}`);
    } catch (e) {
      console.log(`${key.padEnd(28)} ERROR ${e.message.split('\n')[0]}`);
    }
    await page.close();
  }
  await browser.close();
})();

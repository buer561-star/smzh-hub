const { chromium } = require('/opt/node22/lib/node_modules/playwright/index.js');
const fs=require('fs');
(async () => {
  const b = await chromium.launch();
  const p = await b.newContext({viewport:{width:390,height:780}, isMobile:true, ignoreHTTPSErrors:true}).then(c=>c.newPage());
  async function reset(){await p.goto('https://smzh.ch/de/',{waitUntil:'domcontentloaded',timeout:60000});try{await p.waitForLoadState('networkidle',{timeout:12000});}catch{}}
  await reset();
  for(const l of ['Alle ablehnen','Alle annehmen']){const x=p.getByRole('button',{name:l});if(await x.count()){try{await x.first().click({timeout:1200});break;}catch{}}}
  async function openMenu(){await p.locator('.lucide-menu').first().locator('xpath=ancestor::button[1]').click();await p.waitForTimeout(700);}
  function snap(){return p.evaluate(()=>{
    const root=[...document.querySelectorAll('div.mobile')].find(n=>n.offsetParent);if(!root)return{links:[],drills:[]};
    const links=[...root.querySelectorAll('a[href^="/de"]')].map(a=>({text:a.textContent.trim().replace(/\s+/g,' '),href:a.getAttribute('href')})).filter(x=>x.text);
    const drills=[...root.querySelectorAll('button')].map(btn=>btn.textContent.trim().replace(/\s+/g,' ')).filter(t=>t&&t.length<40);
    return {links,drills};
  });}
  const tops=['Privatkunden','Firmenkunden','smzh Welt','Über smzh'];
  const out={};
  for(const top of tops){
    await reset(); await openMenu();
    await p.locator('div.mobile button:has-text("'+top+'")').first().click().catch(()=>{});
    await p.waitForTimeout(600);
    out[top]=await snap();
  }
  fs.writeFileSync('build/mobile-tree.json', JSON.stringify(out,null,1));
  for(const t of tops){console.log(`\n=== ${t}: links=${out[t].links.length} drills=${out[t].drills.length} ===`);
    out[t].links.slice(0,12).forEach(l=>console.log(`   ${l.text} -> ${l.href}`));
    console.log('   drills:', out[t].drills.join(' | '));}
  await b.close();
})();

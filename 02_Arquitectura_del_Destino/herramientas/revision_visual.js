// Revisión de páginas: desbordes, errores de consola, recursos rotos, contraste y tamaño de letra.
// Uso: node revisar.js BASE_URL ruta1 ruta2 ...   (VISTAS=tel,tab,esc)
const { chromium } = require(process.env.PLAYWRIGHT || 'playwright');
const [,, base, ...rutas] = process.argv;
const V = {tel:{width:390,height:844,s:2,m:true}, tab:{width:820,height:1180,s:1,m:true}, esc:{width:1366,height:900,s:1,m:false}};
(async()=>{
  const b = await chromium.launch({args:['--no-sandbox']});
  let malos=0;
  for (const v of (process.env.VISTAS||'tel,tab,esc').split(',')){
    const ctx = await b.newContext({viewport:{width:V[v].width,height:V[v].height},deviceScaleFactor:V[v].s,isMobile:V[v].m,hasTouch:V[v].m,reducedMotion:'reduce'});
    for (const r of rutas){
      const p = await ctx.newPage(); const errs=[];
      p.on('pageerror',e=>errs.push('JS: '+e.message)); p.on('console',m=>{if(m.type()==='error')errs.push('consola: '+m.text())});
      p.on('response',q=>{ if(q.status()>=400) errs.push('HTTP '+q.status()+' '+q.url()); });
      p.on('requestfailed',q=>errs.push('falló '+q.url()));
      await p.goto(base+r,{waitUntil:'networkidle'}); await p.waitForTimeout(300);
      const res = await p.evaluate(()=>{
        const lin=c=>{c/=255;return c<=.03928?c/12.92:Math.pow((c+.055)/1.055,2.4)};
        const L=([r,g,b])=>.2126*lin(r)+.7152*lin(g)+.0722*lin(b);
        const parse=s=>{const m=s.match(/rgba?\(([^)]+)\)/); if(!m) return null; const a=m[1].split(/[ ,\/]+/).filter(Boolean).map(Number); return [a[0],a[1],a[2],a.length>3?a[3]:1]};
        const mix=(f,bk)=>[0,1,2].map(i=>f[i]*f[3]+bk[i]*(1-f[3]));
        function fondo(el){ let capas=[]; let e=el; let img=false;
          while(e && e.nodeType===1){ const cs=getComputedStyle(e); if(cs.backgroundImage!=='none' && !/url\(/.test(cs.backgroundImage)) img=true;
            const c=parse(cs.backgroundColor); if(c && c[3]>0){ capas.push(c); if(c[3]>=1) break;} e=e.parentElement; }
          let bk=[13,12,11]; for(let i=capas.length-1;i>=0;i--) bk=mix(capas[i],bk); return {bk,img}; }
        const out=[]; const vistos=new Set();
        const walker=document.createTreeWalker(document.body,NodeFilter.SHOW_TEXT);
        let n; while(n=walker.nextNode()){
          if(!n.textContent.trim()) continue; const el=n.parentElement; if(!el||vistos.has(el)) continue; vistos.add(el);
          const cs=getComputedStyle(el); if(cs.visibility==='hidden'||cs.display==='none') continue;
          const rc=el.getBoundingClientRect(); if(rc.width===0||rc.height===0) continue;
          let op=1, e=el; while(e&&e.nodeType===1){op*=parseFloat(getComputedStyle(e).opacity); e=e.parentElement;}
          if(el.closest('[aria-hidden="true"]')) continue;
          const c=parse(cs.color); const {bk,img}=fondo(el); const fg=mix([c[0],c[1],c[2],c[3]*op],bk);
          const L1=L(fg),L2=L(bk); const cr=(Math.max(L1,L2)+.05)/(Math.min(L1,L2)+.05);
          const fs=parseFloat(cs.fontSize), grande=fs>=24||(fs>=18.66&&parseInt(cs.fontWeight)>=700);
          if(cr<(grande?3:4.5)) out.push({t:n.textContent.trim().slice(0,40),cr:cr.toFixed(2),fs,color:cs.color,img});
        }
        const claros=[]; for(const el of document.querySelectorAll('body *')){ const cs=getComputedStyle(el); if(cs.display==='none'||cs.visibility==='hidden') continue;
          const r=el.getBoundingClientRect(); if(r.width<40||r.height<14) continue; if(el.closest('[aria-hidden="true"]')) continue;
          let lum=0; const c=parse(cs.backgroundColor); if(c&&c[3]>0.3) lum=L(mix(c,[13,12,11]));
          const g=cs.backgroundImage.match(/rgba?\([^)]+\)/g)||[]; for(const x of g){const q=parse(x); if(q&&q[3]>0.3) lum=Math.max(lum,L(mix(q,[13,12,11])));}
          if(lum>0.12) claros.push(el.tagName.toLowerCase()+'.'+[...el.classList].join('.')+' L='+lum.toFixed(2)); }
        const chicos=[]; for(const el of document.querySelectorAll('p,li,dd,td,blockquote')){ const fs=parseFloat(getComputedStyle(el).fontSize); const r=el.getBoundingClientRect(); if(r.width>0&&el.textContent.trim().length>60&&fs<15.5) chicos.push(el.tagName.toLowerCase()+'.'+[...el.classList].join('.')+' '+fs+'px'); }
        const ps=[...document.querySelectorAll('p')].filter(p=>p.textContent.trim().length>120);
        const fsP=ps.length? Math.round(10*ps.map(p=>parseFloat(getComputedStyle(p).fontSize)).sort((a,b)=>a-b)[Math.floor(ps.length/2)])/10 : null;
        const de=document.documentElement; const anchos=[...document.querySelectorAll('body *')].filter(e=>e.getBoundingClientRect().right>de.clientWidth+1 && getComputedStyle(e).position!=='fixed').map(e=>e.tagName+'.'+e.className).slice(0,4);
        return {bajo:out, claros:[...new Set(claros)].slice(0,6), chicos:[...new Set(chicos)].slice(0,6), fsP, desborde: de.scrollWidth>de.clientWidth? anchos:[] , fuentes:[...document.fonts].filter(f=>f.status==='loaded').map(f=>f.family).filter((x,i,a)=>a.indexOf(x)===i)};
      });
      const prob = res.bajo.length||res.desborde.length||errs.length||res.claros.length||res.chicos.length;
      if(prob) malos++;
      console.log(`${v} ${r} · letra ${res.fsP}px · fuentes ${res.fuentes.join('/')}${res.desborde.length?' · DESBORDE '+res.desborde.join(','):''}${errs.length?' · '+errs.join(' | '):''}`);
      if(res.claros.length) console.log('    fondo claro: '+res.claros.join(' | '));
      if(res.chicos.length) console.log('    letra chica: '+res.chicos.join(' | '));
      for(const x of res.bajo.slice(0,8)) console.log(`    contraste ${x.cr} (${x.fs}px ${x.color}${x.img?' sobre degradado':''}): ${x.t}`);
      if(res.bajo.length>8) console.log(`    … y ${res.bajo.length-8} más`);
      await p.close();
    }
    await ctx.close();
  }
  await b.close(); console.log('páginas con observaciones:', malos);
})();

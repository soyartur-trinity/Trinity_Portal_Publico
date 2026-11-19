"""Enlaces internos rotos de todo el repositorio (archivo y ancla). Uso: enlaces.py RAIZ"""
import os,re,sys,glob,html
from urllib.parse import unquote,urlparse
R=os.path.abspath(sys.argv[1]); ids={}; rotos=[]; total=0
def ids_de(p):
    if p not in ids:
        try: t=open(p,encoding='utf-8').read()
        except Exception: ids[p]=None; return None
        ids[p]=set(re.findall(r'\b(?:id|name)\s*=\s*["\']([^"\']+)["\']',t))
    return ids[p]
for f in glob.glob(R+'/**/*.html',recursive=True):
    t=open(f,encoding='utf-8').read()
    t=re.sub(r'<!--.*?-->','',t,flags=re.S)
    for m in re.finditer(r'\b(href|src)\s*=\s*"([^"]+)"',t):
        u=html.unescape(m.group(2)).strip()
        if re.match(r'(https?:|mailto:|tel:|javascript:|data:|#$|\$\{)',u) or '${' in u or u.startswith('{'): 
            if not u.startswith('https://soyartur-trinity.github.io/Trinity_Portal_Publico/'): continue
            u=os.path.relpath(os.path.join(R,u.split('Trinity_Portal_Publico/',1)[1] or 'index.html'),os.path.dirname(f))
        total+=1
        pu=urlparse(u); path=unquote(pu.path); frag=unquote(pu.fragment)
        dest=os.path.normpath(os.path.join(os.path.dirname(f),path)) if path else f
        if os.path.isdir(dest): dest=os.path.join(dest,'index.html')
        if not os.path.exists(dest): rotos.append((os.path.relpath(f,R),u,'no existe')); continue
        if frag and dest.endswith('.html'):
            s=ids_de(dest)
            if s is not None and frag not in s: rotos.append((os.path.relpath(f,R),u,'sin ancla'))
print('enlaces internos:',total,'· rotos:',len(rotos))
for r in sorted(rotos): print('  ',*r)

"""Voseo -> tuteo en los seis primeros libros del Portal Público (19 de noviembre de 2026; Parte II del documento de
lectura, aprobada por Arturo con las voces citadas y el título del libro 6). El mapa de formas está en
tuteo_portal_1_6_mapa.py; las formas en -í que también son pretérito solo cambian donde son imperativo.
Uso: python3 tuteo_portal_1_6.py RUTA/Trinity_Portal_Publico/01_Libros [--informe]"""
import re,sys,glob,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from tuteo_portal_1_6_mapa import MAPA, IMPERATIVOS_I, PREPS, FRASES
L='A-Za-zÁÉÍÓÚÜÑáéíóúüñ'
def caso(orig,nuevo):
    if orig.isupper() and len(orig)>1: return nuevo.upper()
    if orig[0].isupper(): return nuevo[0].upper()+nuevo[1:]
    return nuevo
TOK=re.compile(r'(?<![%s])(%s)(?![%s])'%(L,'|'.join(sorted(MAPA,key=len,reverse=True)),L),re.I)
VOS=re.compile(r'(?<![%s])([%s]+)(\s+)(vos)(?![%s])|(?<![%s])(vos)(?![%s])'%(L,L,L,L,L),re.I)
def convertir(rel,t,registro):
    n=0
    for archivo,antes,despues in FRASES:
        if archivo!=rel: continue
        if t.count(antes)!=1: raise SystemExit('ancla frase %s %r'%(rel,antes))
        t=t.replace(antes,despues); n+=1; registro.append((rel,antes,despues))
    for archivo,forma,sigue,nuevo in IMPERATIVOS_I:
        if archivo!=rel: continue
        k=t.count(forma+sigue)
        if k!=1: raise SystemExit('ancla imperativo %s %s %r: %d'%(rel,forma,sigue,k))
        t=t.replace(forma+sigue,nuevo+sigue); n+=1; registro.append((rel,forma,nuevo))
    def f(m):
        o=m.group(1); r=caso(o,MAPA[o.lower()]); registro.append((rel,o,r)); return r
    t,k=TOK.subn(f,t); n+=k
    def g(m):
        if m.group(3):
            prev,esp,o=m.group(1),m.group(2),m.group(3)
            if prev.lower()=='con':
                r=caso(prev,'contigo'); registro.append((rel,prev+' '+o,r)); return r
            r=caso(o,'ti' if prev.lower() in PREPS else 'tú'); registro.append((rel,o,r)); return prev+esp+r
        o=m.group(4); r=caso(o,'tú'); registro.append((rel,o,r)); return r
    t,k=VOS.subn(g,t); n+=k
    return t,n
if __name__=='__main__':
    raiz=sys.argv[1]; registro=[]
    for f in sorted(glob.glob(os.path.join(raiz,'0[1-6]_*','*.html'))):
        rel=os.path.relpath(f,raiz); t=open(f,encoding='utf-8').read()
        nt,n=convertir(rel,t,registro)
        if nt!=t: open(f,'w',encoding='utf-8').write(nt)
    import collections
    c=collections.Counter(r[0].split('/')[0] for r in registro)
    for k,v in sorted(c.items()): print(k,v)
    print('total',len(registro))
    if '--informe' in sys.argv:
        for r in registro: print(*r,sep='\t')

"""La licencia al pie de los índices de los libros 7 a 39 del Portal Público (19 de noviembre de 2026).
Misma línea que el índice general y que los libros 1 a 6, y <link rel="license"> en la cabeza.
Escribe solo si encuentra cada anclaje una vez; lo que ya está hecho, lo deja.
Uso: licencia_7_39.py RAIZ_01_Libros"""
import os,re,sys,glob
R=sys.argv[1]
DEED='https://creativecommons.org/licenses/by-nc-sa/4.0/deed.es'
LIC='https://soyartur-trinity.github.io/Trinity-/licencia.html'
CABEZA='<link rel="license" href="%s">'%DEED
LINEA=('Lic. Arturo Rodríguez · Obra libre y gratuita · <a rel="license" href="%s" style="color:inherit">CC BY-NC-SA 4.0</a> · '
       '<a href="%s" style="color:inherit">Licencia y privacidad</a>'%(DEED,LIC))
P='<p class="pie-licencia" style="margin:1.1rem 0 0;font-size:.85em;line-height:1.7;opacity:.85;text-transform:none;letter-spacing:.02em">%s</p>'%LINEA
err=[]; n=0
for f in sorted(glob.glob(os.path.join(R,'*','index.html'))):
    num=int(os.path.basename(os.path.dirname(f))[:2])
    if not 7<=num<=39: continue
    t=open(f,encoding='utf-8').read(); o=t
    if LINEA not in t:
        if num==7:
            ancla='      Emergieron del campo. Al campo regresan.\n    </div>\n'
            if t.count(ancla)!=1: err.append(f); continue
            t=t.replace(ancla,ancla+'    <div class="colophon-txt" style="margin-top:14px">%s</div>\n'%LINEA)
        else:
            if t.count('</footer>')!=1: err.append(f); continue
            t=t.replace('</footer>',P+'</footer>')
    if CABEZA not in t:
        i=t.index('</title>')+len('</title>'); t=t[:i]+'\n'+CABEZA+t[i:]
    if t!=o: open(f,'w',encoding='utf-8').write(t); n+=1
if err: raise SystemExit('sin ancla: '+', '.join(err))
print('índices con licencia:',n)

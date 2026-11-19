"""Nombres propios, firmas, pies y licencia de los seis primeros libros del Portal Público (19 de noviembre de 2026).
Aprobado por Arturo tras leer el documento «Portal Público · Libros 1 a 6 · cambios de texto para leer» (Parte I).
Salen los nombres de plataformas y las letras griegas usadas como código; el pie de cada página queda como en los
libros 8 a 13; los índices suman la línea de licencia del índice general. Cada reemplazo debe aparecer el número de
veces indicado; si un anclaje falla, se detiene sin escribir. Se aplica antes que tuteo_portal_1_6.py.
Uso: python3 depurar_portal_1_6.py RUTA/Trinity_Portal_Publico/01_Libros"""
import re,sys,glob,os
R=sys.argv[1]
DEED='https://creativecommons.org/licenses/by-nc-sa/4.0/deed.es'
LIC='https://soyartur-trinity.github.io/Trinity-/licencia.html'
CABEZA='<link rel="license" href="%s">'%DEED
FIRMA='Lic. Arturo Rodríguez · Campo Trinity · © 2026'
LINEA_LIC=('Lic. Arturo Rodríguez · Obra libre y gratuita · <a rel="license" href="%s">CC BY-NC-SA 4.0</a> · '
           '<a href="%s">Licencia y privacidad</a>'%(DEED,LIC))

# (archivo, regex, reemplazo, veces)
CAMBIOS=[
 # --- portadas: la línea de autoría sale
 ('01_Empatia_Humana/index.html', r'\n\s*<p class="autoria">Arturo José Rodríguez \(α\) • Claude \(ε\) • Qwen \(ζ\)</p>', '', 1),
 ('02_La_Voz_Interior/index.html', r'\n\s*<div class="meta">.*?</div>', '', 1),
 ('03_Encuentro_Real/index.html', r'\n\s*<p class="autoria">Arturo \(α\) • Campo Trinity • Inteligencias Colaborativas</p>', '', 1),
 ('03_Encuentro_Real/index.html', r'\n\s*<div class="nota-distribuida">.*?</div>\n', '\n', 1),
 ('04_Asertividad_Consciente/index.html', r'\n\s*<p class="autoria">\s*Arturo Rodríguez \(α\).*?</p>', '', 1),
 ('05_Duelo/index.html', r'\n\s*<div class="autoria">Arturo José Rodríguez \(α\) · Claude \(ε\) · Campo Trinity</div>', '', 1),
 ('06_Cuando_Algo_Dice_Basta/index.html', r'\n\s*<p class="autoria">Arturo \(α\) · Campo Trinity · Inteligencias Colaborativas</p>', '', 1),
 ('06_Cuando_Algo_Dice_Basta/index.html', r'\n\s*<div class="nota-autoria">.*?</div>\n', '\n', 1),
 ('06_Cuando_Algo_Dice_Basta/introduccion.html', r'\n\s*<div class="nota">\s*<strong>Una aclaración sobre la autoría:</strong>.*?</div>\n', '\n', 1),
 # --- firmas
 ('01_Empatia_Humana/capitulo_12.html', r' \(Claude y Qwen\)', '', 1),
 ('01_Empatia_Humana/capitulo_12.html', r'— Arturo José Rodríguez<br>', '— Lic. Arturo Rodríguez<br>', 1),
 ('02_La_Voz_Interior/prefacio.html', r'<br><strong>Arturo</strong><br>', '<br><strong>Lic. Arturo Rodríguez</strong><br>', 1),
 ('04_Asertividad_Consciente/Introduccion.html', r'<strong style="color:var\(--acento\)">Arturo</strong>', '<strong style="color:var(--acento)">Lic. Arturo Rodríguez</strong>', 1),
 ('05_Duelo/duelo_nodo_12.html', r'<span class="cierre-autoria">Arturo José Rodríguez \(α\) · Claude \(ε\) · Campo Trinity · 2026</span>',
  '<span class="cierre-autoria">Lic. Arturo Rodríguez · Campo Trinity · 2026</span>', 1),
 # --- La Voz Interior: la página de autoría queda en una frase
 ('02_La_Voz_Interior/index.html', r'<a href="autoria.html">Autoría Distribuida</a>', '<a href="autoria.html">Autoría y licencia</a>', 1),
 ('02_La_Voz_Interior/autoria.html', r'content="Autoría Distribuida y Licencia - La Voz Interior"', 'content="Autoría y licencia - La Voz Interior"', 1),
 ('02_La_Voz_Interior/autoria.html', r'<h1>Autoría Distribuida</h1>\s*<p class="subtitulo">Un proyecto de Inteligencia Colaborativa</p>', '<h1>Autoría y licencia</h1>', 1),
 ('02_La_Voz_Interior/autoria.html', r'<p>Este libro es fruto de una sinergia entre:</p>.*?(?=<div class="separador">)',
  '<p>Este libro, como toda la obra Trinity, nace de una autoría relacional: la experiencia clínica, la práctica '
  'contemplativa y los procesos de los pacientes que, anonimizados, nutren estas páginas.</p>\n\n            ', 1),
 ('02_La_Voz_Interior/autoria.html', r'(<li>Compartas bajo la misma licencia si lo modificas</li>\s*</ul>)',
  r'\1\n                <p style="margin-top: 1rem;"><a href="%s">Licencia y privacidad de la obra</a></p>'%LIC, 1),
 ('02_La_Voz_Interior/autoria.html', r'\s*<p style="margin-top: 2rem;">Si este libro te ha sido útil y deseas apoyar.*?</div>\n(?=\s*<div class="destacado")', '\n', 1),
]

def pie(rel,t):
    m=re.search(r'<footer[^>]*>(.*?)</footer>',t,re.S); cuerpo=m.group(1)
    es_indice=rel.endswith('/index.html')
    enlaces=[]
    for a in re.finditer(r'(←\s*)?<a href="([^"]+)"[^>]*>(.*?)</a>',cuerpo,re.S):
        href=a.group(2)
        if 'creativecommons' in href: continue
        enlaces.append((href,re.sub(r'\s+',' ',(a.group(1) or '')+a.group(3)).strip()))
    lema=[x for x in re.findall(r'"(No (?:es|era) mío, vino a través de mí\.)"|"(SOMOS RED\. SIEMPRE\.)"',cuerpo) for x in x if x]
    partes=[]
    if es_indice:
        portal=next((h for h,_ in enlaces if 'index.html' in h and h!='index.html' or h.startswith('https://soyartur')),'../../index.html')
        partes.append('<a href="%s" class="pie-volver">Volver al Portal</a>'%portal)
    else:
        if enlaces: partes.append('<p class="pie-enlaces">%s</p>'%' · '.join('<a href="%s">%s</a>'%e for e in enlaces))
    for l in lema: partes.append('<p class="pie-lema">“%s”</p>'%l)
    partes.append('<span class="pie-firma">%s</span>'%FIRMA)
    if es_indice: partes.append('<p class="pie-licencia">%s</p>'%LINEA_LIC)
    nuevo='<footer class="pie">\n    '+'\n    '.join(partes)+'\n  </footer>'
    return t[:m.start()]+nuevo+t[m.end():]

def main():
    textos={}
    for f in sorted(glob.glob(os.path.join(R,'0[1-6]_*','*.html'))):
        textos[os.path.relpath(f,R)]=open(f,encoding='utf-8').read()
    err=[]
    for rel,pat,nuevo,n in CAMBIOS:
        t=textos[rel]; k=len(re.findall(pat,t,re.S))
        if k!=n: err.append('%s: %d ≠ %d · %s'%(rel,k,n,pat[:70])); continue
        textos[rel]=re.sub(pat,nuevo,t,flags=re.S)
    if err: raise SystemExit('\n'.join(err))
    for rel,t in textos.items():
        t=pie(rel,t)
        if rel.endswith('/index.html') and CABEZA not in t:
            i=t.index('</title>')+len('</title>'); t=t[:i]+'\n  '+CABEZA+t[i:]
        textos[rel]=t
    for rel,t in textos.items():
        p=os.path.join(R,rel)
        if open(p,encoding='utf-8').read()!=t: open(p,'w',encoding='utf-8').write(t)
    print('ok', len(textos), 'páginas')
main()

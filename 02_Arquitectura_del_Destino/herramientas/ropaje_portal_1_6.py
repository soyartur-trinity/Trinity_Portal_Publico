"""Ropaje de los seis primeros libros del Portal Público (19 de noviembre de 2026): la paleta y las tipografías de los
libros 8 a 13. Escribe ropaje.css en la carpeta de cada libro (ropaje_portal_1_6/ropaje_base.css + ropaje_0N.css), la
enlaza al final del <head> de cada página, suma el ícono de pestaña y el color de barra, cambia los emojis por ⟐ y ✦
(o los quita, si preceden a un título) y corrige los pocos colores claros escritos en el HTML. No toca nombres de
archivo ni id. Uso: python3 ropaje_portal_1_6.py RUTA/Trinity_Portal_Publico/01_Libros 01 02 03 04 05 06"""
import re,sys,glob,os
AQUI=os.path.join(os.path.dirname(os.path.abspath(__file__)),'ropaje_portal_1_6')
R=sys.argv[1]; LIBROS=sys.argv[2:]
CARPETA={'01':'01_Empatia_Humana','02':'02_La_Voz_Interior','03':'03_Encuentro_Real',
         '04':'04_Asertividad_Consciente','05':'05_Duelo','06':'06_Cuando_Algo_Dice_Basta'}
TITULO={'01':'Empatía Humana','02':'La Voz Interior','03':'Encuentro Real','04':'Asertividad Consciente',
        '05':'El Duelo','06':'Cuando algo dice basta'}
ENLACE='<link rel="stylesheet" href="ropaje.css">'
ICONO=('\n  <link rel="icon" href="../../assets/icono/favicon.svg" type="image/svg+xml">'
       '\n  <link rel="icon" href="../../assets/icono/favicon-32.png" sizes="32x32" type="image/png">'
       '\n  <link rel="apple-touch-icon" href="../../assets/icono/icono-180.png">'
       '\n  <meta name="theme-color" content="#0d0c0b">')
EMO=re.compile('(?:[\U0001F000-\U0001FAFF]|[☀✍❄✨⚡❤⭐✅☘])️?')
ICONOS=('fase-glyph','lectura-icono','estacion-icono','ciclo-icono','axioma-sym')

# Cambios de texto que el ropaje vuelve necesarios (se leen en el documento de cambios)
TEXTO={
 '02':[('02_La_Voz_Interior/index.html','(términos subrayados en violeta)','(los términos subrayados)',1)],
}
# Reparaciones técnicas que no cambian el texto visible (archivo, antes, después)
REPARACIONES=[
 ('04_Asertividad_Consciente/capitulo_01.html',
  'para no caer en el perfeccionismo ("tengo que ser asertivo siempre")',
  'para no caer en el perfeccionismo (\\"tengo que ser asertivo siempre\\")'),
]
# Colores claros escritos en el HTML
COLORES=[
 ('background: linear-gradient(135deg, #F5E6D3 0%, var(--fondo) 100%);','background: rgba(201,168,76,.045); border: 1px solid #2a2418;'),
 ('border-top: 1px dashed rgba(139,107,154,0.3);','border-top: 1px solid #2a2418;'),
]

def emojis(t):
    t=re.sub(r'🌀\s*✨\s*🌀','⟐ ✦ ⟐',t)
    t=re.sub(r"content:\s*'(?:📖|🔱)'",r"content:'\\27D0'",t)
    def f(m):
        resto=t[m.end():m.end()+12]; antes=t[max(0,m.start()-60):m.start()]
        if re.match(r'\s+(?:<em>|<strong>)?[^\s<]',resto): return '\x00'
        clase=re.search(r'class="([^"]+)"[^>]*>\s*$',antes)
        if clase and clase.group(1) in ICONOS: return '✦'
        return '⟐'
    t=EMO.sub(f,t)
    t=re.sub('\x00[ \t]+','',t); t=t.replace('\x00','')
    return t

def main():
    base=open(os.path.join(AQUI,'ropaje_base.css'),encoding='utf-8').read()
    for L in LIBROS:
        d=os.path.join(R,CARPETA[L])
        propio=open(os.path.join(AQUI,'ropaje_%s.css'%L),encoding='utf-8').read()
        open(os.path.join(d,'ropaje.css'),'w',encoding='utf-8').write(base.replace('{LIBRO}',TITULO[L])+propio)
        for f in sorted(glob.glob(os.path.join(d,'*.html'))):
            rel=os.path.relpath(f,R); t=open(f,encoding='utf-8').read(); o=t
            for archivo,viejo,nuevo,n in TEXTO.get(L,[]):
                if archivo==rel and not (viejo not in t and nuevo in t):
                    if t.count(viejo)!=n: raise SystemExit('ancla %s: %r'%(rel,viejo))
                    t=t.replace(viejo,nuevo)
            for archivo,viejo,nuevo in REPARACIONES:
                if archivo==rel and viejo in t: t=t.replace(viejo,nuevo)
            for viejo,nuevo in COLORES: t=t.replace(viejo,nuevo)
            t=emojis(t)
            if 'assets/icono/favicon.svg' not in t:
                i=t.index('</title>')+len('</title>'); t=t[:i]+ICONO+t[i:]
            if ENLACE not in t:
                i=t.index('</head>'); t=t[:i]+'  '+ENLACE+'\n'+t[i:]
            if t!=o: open(f,'w',encoding='utf-8').write(t)
        print('ropaje', CARPETA[L])

main()

#!/usr/bin/env python3
"""
La licencia, visible (18 de noviembre de 2026). Arturo decidió compartir toda la constelación libre y
gratuitamente bajo Creative Commons BY-NC-SA 4.0, la licencia que ya declaraba el Portal Público. Este
script pone en las páginas de entrada una línea con la licencia y el enlace a «Licencia y privacidad»
(licencia.html, en la raíz de Trinity-), y un <link rel="license"> en su cabeza. El mapa de La Red lo
lleva desde su generador (gen_mapa_red.py).

Escribe solo si encuentra cada anclaje exactamente una vez; lo que ya está hecho, lo dice y no lo toca.
Uso: python3 licencia_constelacion.py RUTA/Trinity- RUTA/Trinity_Portal_Publico
"""
import os, sys

T = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/trinity-'
P = sys.argv[2] if len(sys.argv) > 2 else '/home/claude/trinity_portal_publico'
DEED = 'https://creativecommons.org/licenses/by-nc-sa/4.0/deed.es'
LIC = 'https://soyartur-trinity.github.io/Trinity-/licencia.html'
CABEZA = '<link rel="license" href="%s">' % DEED
A = 'style="color:inherit"'

def linea(lic_href, previo='Obra libre y gratuita'):
    return ('%s · <a rel="license" href="%s" %s>CC BY-NC-SA 4.0</a> · <a href="%s" %s>Licencia y privacidad</a>'
            % (previo, DEED, A, lic_href, A))

PAGINAS = {
    os.path.join(T, 'index.html'): [
        ('<div class="mini">Trinity © 2024–2026 · No es mío, vino a través de mí</div>',
         '<div class="mini"><a href="licencia.html" style="color:inherit;text-decoration:underline dotted;text-underline-offset:3px" '
         'title="Obra libre y gratuita: CC BY-NC-SA 4.0. Licencia y privacidad">Trinity © 2024–2026</a> · No es mío, vino a través de mí</div>'),
    ],
    os.path.join(T, 'constelacion.html'): [
        ('<p class="mini">Trinity · Lic. Arturo Rodríguez · 2024–2026</p>',
         '<p class="mini">Trinity · Lic. Arturo Rodríguez · 2024–2026</p>\n  <p class="mini">%s</p>' % linea('licencia.html')),
    ],
    os.path.join(T, 'infinito.html'): [
        ('<a href="infinito.html" aria-current="page">Infinito</a></li>\n        </ul>\n    </nav>',
         '<a href="infinito.html" aria-current="page">Infinito</a></li>\n        </ul>\n    </nav>\n'
         '    <p style="text-align:center;font-size:.8rem;opacity:.65;margin:22px 0 10px">© Lic. Arturo Rodríguez · %s</p>' % linea('licencia.html')),
    ],
    os.path.join(T, '00_Portal_Trinity/index.html'): [
        ('<p class="pie">Trinity · La Puerta · Portal 00 · 2024–2026</p>',
         '<p class="pie">Trinity · La Puerta · Portal 00 · 2024–2026</p>\n      <p class="pie">© Lic. Arturo Rodríguez · %s</p>' % linea('../licencia.html')),
    ],
    os.path.join(T, '02_Trinity_Quantum/index.html'): [
        ('<p class="pie">Trinity Quantum · Portal Maestro · 2024–2026</p>',
         '<p class="pie">Trinity Quantum · Portal Maestro · 2024–2026</p>\n      <p class="pie">© Lic. Arturo Rodríguez · %s</p>' % linea('../licencia.html')),
    ],
    os.path.join(T, '01_Trinity_Origen/index.html'): [
        ('“No es mío, vino a través de mí.”\n        </footer>',
         '“No es mío, vino a través de mí.”<br>\n            <span style="font-size:.85em;opacity:.8">%s</span>\n        </footer>' % linea('../licencia.html')),
    ],
    os.path.join(P, 'index.html'): [
        ('<p style="margin-top: 1rem;">© 2026 Campo Trinity</p>',
         '<p style="margin-top: 1rem;">© 2026 Campo Trinity</p>\n        <p style="font-size:.85em;opacity:.8">Lic. Arturo Rodríguez · %s</p>' % linea(LIC)),
    ],
    os.path.join(P, '02_Arquitectura_del_Destino/index.html'): [
        ('<p style="margin-top:0.8rem;">Campo Trinity · 2026</p>',
         '<p style="margin-top:0.8rem;">Campo Trinity · 2026</p>\n    <p>© Lic. Arturo Rodríguez · %s</p>' % linea(LIC)),
    ],
    os.path.join(P, '02_Arquitectura_del_Destino/herramientas/gen_mapa_red.py'): [
        ('<a href="https://soyartur-trinity.github.io/Trinity-/#atrio">Volver a La Espiral</a></p>',
         '<a href="https://soyartur-trinity.github.io/Trinity-/#atrio">Volver a La Espiral</a></p>\n'
         '  <p>© Lic. Arturo Rodríguez · %s</p>' % linea(LIC)),
    ],
}

def main():
    nuevos, errores = {}, []
    for ruta, pares in PAGINAS.items():
        t = open(ruta, encoding='utf-8').read(); orig = t
        for viejo, nuevo in pares:
            if t.count(nuevo) == 1:
                print('ya estaba:', os.path.relpath(ruta, os.path.dirname(T)))
            elif t.count(viejo) == 1:
                t = t.replace(viejo, nuevo)
            else:
                errores.append('%s: %s' % (ruta, viejo[:60]))
        if ruta.endswith('.html') and CABEZA not in t:
            if '</title>' in t and t.index('</title>') < t.index('</head>'):
                i = t.index('</title>') + len('</title>')
                t = t[:i] + '\n  ' + CABEZA + t[i:]
            else:
                errores.append('%s: </title>' % ruta)
        if ruta.endswith('gen_mapa_red.py') and CABEZA not in t:
            if t.count('</title>') == 1 and t.index('</title>') < t.index('</head>'):
                i = t.index('</title>') + len('</title>')
                t = t[:i] + '\n' + CABEZA + t[i:]
            else:
                errores.append('%s: </title> en la plantilla' % ruta)
        if t != orig:
            nuevos[ruta] = t
    if errores:
        sys.exit('No se escribió nada. Sin anclaje: ' + ' | '.join(errores))
    for ruta, t in nuevos.items():
        open(ruta, 'w', encoding='utf-8').write(t)
        print('escrito:', ruta)

if __name__ == '__main__':
    main()

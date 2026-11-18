#!/usr/bin/env python3
"""Vueltas de las puertas nuevas de La Puerta (depuración del 18 de noviembre de 2026).

La Puerta abrió once puertas fractales. Cinco ya tenían su vuelta, porque Arquitectura del Destino enlazaba
esos nodos desde sus cierres (El Campo → 1, El Sonámbulo → 13, La Red → 2, La Obra → 8, Habitar → 13).
Las seis nuevas vuelven aquí:

  1. En los cierres de Arquitectura, debajo de las líneas «Vienen de…», una línea discreta «Viene de La Puerta»,
     como las de Quantum y Origen (la lista de puertas laterales de cada cierre queda intacta):
     La Grieta (Nodo 1), El Testigo (Nodo 3), El Peso (Nodo 10) y La Obra (Nodo 12).
  2. En el cierre de El tercero (Portal Público, Libro 15), una fila más en su bloque «Puertas laterales» (Nodo 7).
  3. En Origen IV.3, después de la verificación cruzada, una línea «Viene de» (Nodo 7), con el estilo de las
     vueltas legibles que el nodo ya tiene.

Además, las notas de La Red (Umbrales II y III) nombran secciones del Nodo 2 que cambiaron de nombre con la
depuración: «Protocolo de 7 días» pasa a «Práctica de 7 días» y «Códigos de activación» a «Para recordar»; lo mismo
en el registro de la serie (registro.md).

Cada reemplazo se aplica exactamente una vez; si un anclaje no aparece una sola vez, el script se detiene sin
escribir nada. Si la vuelta ya está, la salta.

Uso: python3 vuelta_puertas_puerta.py RUTA/Trinity_Portal_Publico RUTA/Trinity-
"""
import os, sys

PORTAL, TRINITY = sys.argv[1], sys.argv[2]
P = 'https://soyartur-trinity.github.io/Trinity-/00_Portal_Trinity/'


def vienen(nodo, titulo):
    return ('<div class="vienen"><p class="vienen-t">Viene de <em>La Puerta</em></p><ul><li><a class="vuelta" '
            'href="%snodo_%02d.html">Nodo %d: %s</a></li></ul></div>' % (P, nodo, nodo, titulo))


NOTAS = '<section class="notas" aria-label="Referencias">'
ARQ = os.path.join(PORTAL, '02_Arquitectura_del_Destino')

TAREAS = [
    (os.path.join(ARQ, 'libro-05-la-grieta/L05-cierre.html'), NOTAS, vienen(1, 'La Primera Grieta') + NOTAS, 'nodo_01.html'),
    (os.path.join(ARQ, 'libro-03-el-testigo/L03-cierre.html'), NOTAS, vienen(3, 'Tu Arquitectura Multidimensional') + NOTAS, 'nodo_03.html'),
    (os.path.join(ARQ, 'libro-08-el-peso/L08-cierre.html'), NOTAS, vienen(10, 'Maestría sin Esfuerzo') + NOTAS, 'nodo_10.html'),
    (os.path.join(ARQ, 'libro-12-la-obra/L12-cierre.html'), NOTAS, vienen(12, 'La Red Viviente') + NOTAS, 'nodo_12.html'),
    (os.path.join(PORTAL, '01_Libros/15_El_Tercero/cierre_delante_de_quien.html'),
     '<strong>Tecnología de Activación</strong></em></a></div>\n',
     '<strong>Tecnología de Activación</strong></em></a></div>\n'
     '  <div class="puerta"><a href="%snodo_07.html">⟐ <em>La Puerta, Nodo 7: <strong>Las IA como Espejos del Campo</strong></em></a></div>\n' % P,
     '00_Portal_Trinity/nodo_07.html'),
    (os.path.join(TRINITY, '01_Trinity_Origen/Libro_04/nodo_03.html'),
     'y lo que la idea sostiene cuando se la lleva a la vida de todos los días.</p>\n',
     'y lo que la idea sostiene cuando se la lleva a la vida de todos los días.</p>\n'
     '    <!-- Vuelta de la puerta de La Puerta, Nodo 7 (18 de noviembre de 2026). -->\n'
     '    <p class="viene">Viene de <em>La Puerta</em>: la clave de su arco, <a class="vuelta" href="../../00_Portal_Trinity/nodo_07.html">'
     'el espejo que no puede ser juez</a>, encuentra aquí su verificación.</p>\n',
     '00_Portal_Trinity/nodo_07.html'),
    (os.path.join(ARQ, 'libro-11-la-red/L11-U2.html'), '«El mito de la separación», «Protocolo de 7 días», día 6.',
     '«El mito de la separación», «Práctica de 7 días», día 6.', '«Práctica de 7 días», día 6.'),
    (os.path.join(ARQ, 'libro-11-la-red/L11-U3.html'), 'fases 1 y 2, y «Códigos de activación».',
     'fases 1 y 2, y «Para recordar».', 'fases 1 y 2, y «Para recordar».'),
    (os.path.join(ARQ, 'registro.md'), 'Nodo 2: «El mito de la separación», «Protocolo de 7 días», día 6.',
     'Nodo 2: «El mito de la separación», «Práctica de 7 días», día 6.', ''),
    (os.path.join(ARQ, 'registro.md'), 'fases 1 y 2, y «Códigos de activación».', 'fases 1 y 2, y «Para recordar».', ''),
]

escribir = {}
for ruta, ancla, nuevo, _ in TAREAS:
    t = escribir.get(ruta) or open(ruta, encoding='utf-8').read()
    agregado = nuevo.replace(ancla, '') if ancla in nuevo else nuevo
    if agregado in t:
        print('ya estaba:', ruta)
        continue
    n = t.count(ancla)
    if n != 1:
        sys.exit('%s: el anclaje aparece %d veces:\n%s' % (ruta, n, ancla[:160]))
    escribir[ruta] = t.replace(ancla, nuevo)

for ruta, t in escribir.items():
    with open(ruta, 'w', encoding='utf-8') as f:
        f.write(t)
    print('escrito:', ruta)

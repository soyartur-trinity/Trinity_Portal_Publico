#!/usr/bin/env python3
"""Vuelta de las puertas fractales de Origen X y XIII (noviembre de 2026).

Cada nodo depurado de Origen X y XIII abre una puerta hacia un umbral de
Arquitectura del Destino. Este script agrega, en las «Puertas laterales» del
cierre de cada libro de destino, el enlace de regreso a ese nodo, para que la
puerta sea de ida y vuelta.

Cada reemplazo se aplica exactamente una vez: si el texto de anclaje no aparece
una sola vez, el script se detiene sin escribir nada. Si la vuelta ya está, la
salta (se puede correr de nuevo sin duplicar).

Con un segundo argumento (la raíz del repositorio Trinity-) agrega además, en
el portal de Trinity Quantum, la línea «Viene de Trinity Origen», que devuelve
la puerta violeta de XIII.7 («La espiral sigue»).

Uso: python3 vuelta_puertas_origen.py RUTA/02_Arquitectura_del_Destino [RUTA/Trinity-]
"""
import os, sys

T = 'https://soyartur-trinity.github.io/Trinity-/01_Trinity_Origen/'


def li(libro, nodo, romano, titulo, em=False):
    t = '<em>%s</em>' % titulo if em else titulo
    return ('<li><a href="%sLibro_%02d/nodo_%02d.html">Trinity Origen, Libro %s, Nodo %d: %s</a></li>'
            % (T, libro, nodo, romano, nodo, t))


# Cada entrada: (cierre, anclaje existente, enlaces nuevos antes, enlaces nuevos después)
# El formato del título sigue el de cada cierre (solo El Cuerpo lleva <em>).
CAMBIOS = [
    ('libro-03-el-testigo/L03-cierre.html',
     li(13, 1, 'XIII', 'La Gran Amnesia'),
     [li(10, 4, 'X', 'La Mente como Portal de Sanación')],
     [li(13, 7, 'XIII', 'La Nueva Humanidad')]),
    ('libro-04-el-cuerpo/L04-cierre.html',
     li(10, 1, 'X', 'El Cuerpo como Templo Viviente', em=True),
     [],
     [li(10, 5, 'X', 'La Energía Vital y los Sistemas Sutiles', em=True)]),
    ('libro-05-la-grieta/L05-cierre.html',
     '<li><a href="%sLibro_03/nodo_07.html">Trinity Origen, Libro III, Nodo 7: Más allá del dolor, el portal abierto</a></li>' % T,
     [],
     [li(13, 2, 'XIII', 'Los Fragmentos del Alma')]),
    ('libro-06-las-pequenas-muertes/L06-cierre.html',
     '<li><a href="%sLibro_07/nodo_02.html">Trinity Origen, Libro VII, Nodo 2: Las Pequeñas Muertes</a></li>' % T,
     [],
     [li(10, 6, 'X', 'Sanación del Alma y Medicina Ancestral')]),
    ('libro-07-no-saber/L07-cierre.html',
     '<li><a href="%sLibro_06/nodo_05.html">Trinity Origen, Libro VI, Nodo 5: La paz del no-saber</a></li>' % T,
     [],
     [li(10, 7, 'X', 'La Gran Síntesis')]),
    ('libro-11-la-red/L11-cierre.html',
     '<li><a href="%sLibro_05/nodo_05.html">Trinity Origen, Libro V, Nodo 5: La Red Viva</a></li>' % T,
     [],
     [li(10, 2, 'X', 'La Red de Sanación Colectiva')]),
    ('libro-13-habitar/L13-cierre.html',
     li(13, 3, 'XIII', 'El Recuerdo del Origen'),
     [],
     [li(13, 4, 'XIII', 'La Naturaleza Holográfica')]),
]


# Portal de Trinity Quantum (repositorio Trinity-)
Q_ANCLA = '<aside class="puertas">\n        <p>Muchos nodos terminan'
Q_LINEA = ('<aside class="puertas">\n        <p class="viene">Viene de <em>Trinity Origen</em>: '
           'la espiral que deja abierta <a class="vuelta" href="../01_Trinity_Origen/Libro_13/nodo_07.html">'
           'el último nodo de <em>El Retorno a Casa</em></a> sigue aquí.</p>\n        <p>Muchos nodos terminan')
Q_CSS_ANCLA = '    .puertas p { margin: 0; }\n'
Q_CSS = Q_CSS_ANCLA + '    .puertas p + p { margin-top: 12px; }\n'


def quantum(trinity):
    ruta = os.path.join(trinity, '02_Trinity_Quantum', 'index.html')
    s = open(ruta, encoding='utf-8').read()
    if 'class="viene"' in s:
        print('ya estaba: 02_Trinity_Quantum/index.html')
        return
    for a in (Q_ANCLA, Q_CSS_ANCLA):
        if s.count(a) != 1:
            sys.exit('Anclaje no único en el portal de Quantum; no se escribe nada.')
    s = s.replace(Q_CSS_ANCLA, Q_CSS, 1).replace(Q_ANCLA, Q_LINEA, 1)
    open(ruta, 'w', encoding='utf-8').write(s)
    print('vuelta agregada: 02_Trinity_Quantum/index.html (+1)')


def main():
    raiz = sys.argv[1]
    nuevos = {}
    for archivo, ancla, antes, despues in CAMBIOS:
        ruta = os.path.join(raiz, archivo)
        s = nuevos.get(ruta) or open(ruta, encoding='utf-8').read()
        n = s.count(ancla)
        if n != 1:
            sys.exit('Anclaje encontrado %d veces en %s; no se escribe nada.' % (n, archivo))
        faltan_antes = [x for x in antes if x not in s]
        faltan_despues = [x for x in despues if x not in s]
        if not faltan_antes and not faltan_despues:
            print('ya estaba:', archivo)
            continue
        s = s.replace(ancla, ''.join(faltan_antes) + ancla + ''.join(faltan_despues), 1)
        nuevos[ruta] = s
        print('vuelta agregada: %s (+%d)' % (archivo, len(faltan_antes) + len(faltan_despues)))
    for ruta, s in nuevos.items():
        open(ruta, 'w', encoding='utf-8').write(s)
    print('Listo: %d cierres tocados.' % len(nuevos))
    if len(sys.argv) > 2:
        quantum(sys.argv[2])


if __name__ == '__main__':
    main()

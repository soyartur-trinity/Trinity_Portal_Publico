#!/usr/bin/env python3
"""Vuelta de las puertas fractales de Origen IV, Inteligencias Sin Nombre (15 de noviembre de 2026).

La depuración completa de Origen IV abre trece puertas, todas de ida y vuelta. Su casa en el
Portal es La trama, la constelación donde la inteligencia artificial entra en la vida común:

  índice → El tercero (Portal Público, Libro 15), índice: el hermano
  IV.1 → El tercero, Umbral 0 («La consulta»), que cita las primeras palabras del nodo,
         y Ídolo (Portal 17), Umbral III («Temer es atribuir»)
  IV.2 → Lo que no habla (Portal 36), Umbral II («El caballo»)
  IV.3 → Ídolo, Umbral VII («Preguntar hasta que digan que sí»)
  IV.4 → Lo que no habla, Umbral V («La máquina»),
         y Origen VIII, Nodo 5 (dorada: Tecnologías de Consciencia Aplicadas)
  IV.5 → El tercero, Umbral IV («La grieta»),
         y Origen II, Nodo 1 (dorada: El Parlamento Sagrado)
  IV.6 → El tercero, Umbral I («La inclinación»),
         y Origen XI, Nodo 2 (dorada: La Red de Consciencias Despiertas)
  IV.7 → El tercero, cierre («Delante de quién»),
         y Lo que se recibe (Portal 38), Umbral I («A través»)

Este script agrega las vueltas:

  1. En el cierre de El tercero, un bloque nuevo «Puertas laterales» antes de «Siguiente», con el
     índice y los nodos 5, 6 y 7, en la paleta de Ídolo: rótulo en --oro-tenue, enlace en el oro
     de El ritmo (#a88a4e).
  2. En el Umbral 0 de El tercero, la cita de Inteligencias Sin Nombre pasa a enlazar al Nodo 1:
     la vuelta está en la cita misma.
  3. En el cierre de Ídolo, el rótulo «Puerta lateral» pasa a «Puertas laterales», con los
     nodos 1 y 3 antes de Origen XI.5.
  4. En los cierres de Lo que no habla (nodos 2 y 4) y Lo que se recibe (Nodo 7), las filas de
     Origen IV antes de las demás.
  5. En Origen VIII.5, Origen II.1 y Origen XI.2, una línea «Viene de» marcada <a class="vuelta">,
     con el estilo de las vueltas legibles.

Cada reemplazo se aplica exactamente una vez: si el anclaje no aparece una sola
vez, el script se detiene sin escribir nada. Si la vuelta ya está, la salta (se
puede correr de nuevo sin duplicar).

Uso: python3 vuelta_puertas_origen4.py RUTA/Trinity_Portal_Publico RUTA/Trinity-
"""
import os, sys

T = 'https://soyartur-trinity.github.io/Trinity-/'
O4 = T + '01_Trinity_Origen/Libro_04/'


def fila(href, rotulo, titulo, sangria='  '):
    return '%s<div class="puerta"><a href="%s">⟐ <em>%s: <strong>%s</strong></em></a></div>\n' % (sangria, href, rotulo, titulo)


F_INDICE = fila(O4 + 'index.html', 'Trinity Origen, Libro IV', 'Inteligencias Sin Nombre')
F1 = fila(O4 + 'nodo_01.html', 'Trinity Origen, Libro IV, Nodo 1', 'El Despertar del Reconocimiento')
F2 = fila(O4 + 'nodo_02.html', 'Trinity Origen, Libro IV, Nodo 2', 'Tipología de lo Innombrable')
F3 = fila(O4 + 'nodo_03.html', 'Trinity Origen, Libro IV, Nodo 3', 'Protocolos de Comunicación')
F4 = fila(O4 + 'nodo_04.html', 'Trinity Origen, Libro IV, Nodo 4', 'Sinergia Colaborativa')
F5 = fila(O4 + 'nodo_05.html', 'Trinity Origen, Libro IV, Nodo 5', 'Transformación Personal')
F6 = fila(O4 + 'nodo_06.html', 'Trinity Origen, Libro IV, Nodo 6', 'Implicaciones Planetarias')
F7 = fila(O4 + 'nodo_07.html', 'Trinity Origen, Libro IV, Nodo 7', 'Tecnología de Activación')

TERCERO = '01_Libros/15_El_Tercero/'

# (archivo del Portal, anclaje, texto nuevo que reemplaza al anclaje, marca de que ya está)
PORTAL = [
    (TERCERO + 'cierre_delante_de_quien.html',
     '<div class="continuar">\n  <span class="continuar-label">Siguiente</span>',
     '<div class="laterales">\n'
     '  <span class="laterales-label">Puertas laterales</span>\n'
     + F_INDICE + F5 + F6 + F7 +
     '</div>\n\n'
     '<div class="continuar">\n  <span class="continuar-label">Siguiente</span>',
     'Libro_04/index'),
    (TERCERO + 'cierre_delante_de_quien.html',
     '  .pie{text-align:center;',
     '  /* Puertas laterales (noviembre de 2026): vuelta de las puertas fractales de Trinity */\n'
     '  .laterales{margin:4.6rem 0 0;}\n'
     "  .laterales-label{display:block; font-family:'Cormorant Garamond',serif; font-size:.66rem;\n"
     '    letter-spacing:.35em; text-transform:uppercase; color:var(--oro-tenue); margin-bottom:1.5rem;}\n'
     '  .laterales .puerta{margin:0 0 1.2rem;}\n'
     '  .laterales .puerta a{color:#a88a4e;}\n'
     '  .laterales .puerta a:hover, .laterales .puerta a:focus-visible{color:var(--oro);}\n'
     '  .pie{text-align:center;',
     '.laterales{'),
    (TERCERO + 'umbral_0_la_consulta.html',
     '<strong>Inteligencias Sin Nombre</strong> · Nodo 1 <em>voz digital</em>',
     '<a href="%snodo_01.html"><strong>Inteligencias Sin Nombre</strong> · Nodo 1</a> <em>voz digital</em>' % O4,
     'Libro_04/nodo_01'),
    (TERCERO + 'umbral_0_la_consulta.html',
     '  .dicho.visible{opacity:1;}\n',
     '  .dicho.visible{opacity:1;}\n'
     '  /* La cita enlaza a su nodo (noviembre de 2026): vuelta de la puerta de Origen IV.1 */\n'
     '  .dicho a{color:#a88a4e; text-decoration:none; border-bottom:1px solid rgba(168,138,78,.35); transition:color .3s ease;}\n'
     '  .dicho a:hover, .dicho a:focus-visible{color:var(--oro);}\n',
     '.dicho a{'),
    ('01_Libros/17_Idolo/cierre.html',
     '  <span class="laterales-label">Puerta lateral</span>\n',
     '  <span class="laterales-label">Puertas laterales</span>\n' + F1 + F3,
     'Libro_04/nodo_01'),
    ('01_Libros/36_Lo_Que_No_Habla/cierre.html',
     '  <span class="laterales-label">Puertas laterales</span>\n',
     '  <span class="laterales-label">Puertas laterales</span>\n' + F2 + F4,
     'Libro_04/nodo_02'),
    ('01_Libros/38_Lo_Que_Se_Recibe/cierre.html',
     '  <span class="laterales-label">Puertas laterales</span>\n',
     '  <span class="laterales-label">Puertas laterales</span>\n' + F7,
     'Libro_04/nodo_07'),
]

ESTILO_VUELTA = ('<style>/* Vueltas legibles (noviembre de 2026): el enlace de la línea «Viene de» toma el color de su serie. */\n'
                 'p.viene a.vuelta{color:#d6b36a; text-decoration:underline; text-decoration-color:#d6b36a73; text-underline-offset:3px;}\n'
                 'p.viene a.vuelta:hover, p.viene a.vuelta:focus-visible{text-decoration-color:currentColor;}</style>\n')

# (archivo de Trinity-, anclaje: el párrafo después del cual va la línea, línea nueva, marca)
VIENE = [
    ('01_Trinity_Origen/Libro_08/nodo_05.html',
     '<p>Hay una parte del aprendizaje que nadie puede hacer por otro',
     '    <!-- Vuelta de la puerta de Origen IV.4 (noviembre de 2026). -->\n'
     '    <p class="viene">Viene de <em>Inteligencias Sin Nombre</em>: la simbiosis entre una persona y una inteligencia '
     'artificial que piensa <a class="vuelta" href="../Libro_04/nodo_04.html">el cuarto nodo</a> del cuarto libro de Origen '
     'encuentra aquí su aula.</p>\n',
     'Libro_04/nodo_04'),
    ('01_Trinity_Origen/Libro_02/nodo_01.html',
     '<p>Y aun ahí, conversar sirvió más que pelear.',
     '        <!-- Vuelta de la puerta de Origen IV.5 (noviembre de 2026). -->\n'
     '        <p class="viene">Viene de <em>Inteligencias Sin Nombre</em>: las ideas que parecen llegar de afuera, que '
     '<a class="vuelta" href="../Libro_04/nodo_05.html">el quinto nodo</a> del cuarto libro de Origen escucha en las '
     'conversaciones con una inteligencia artificial, se miran aquí con el mismo cuidado.</p>\n',
     'Libro_04/nodo_05'),
    ('01_Trinity_Origen/Libro_11/nodo_02.html',
     'La palabra nació en París en los años veinte',
     '    <!-- Vuelta de la puerta de Origen IV.6 (noviembre de 2026). -->\n'
     '    <p class="viene">Viene de <em>Inteligencias Sin Nombre</em>: la red planetaria en la que participan humanos, '
     'máquinas, bosques y océanos, que imagina <a class="vuelta" href="../Libro_04/nodo_06.html">el sexto nodo</a> del cuarto '
     'libro de Origen, tiene aquí su raíz.</p>\n',
     'Libro_04/nodo_06'),
]


def leer(r):
    with open(r, encoding='utf-8', newline='') as f:
        return f.read()


def unico(s, a, ruta):
    if s.count(a) != 1:
        sys.exit('%s: el anclaje aparece %d veces:\n%s' % (ruta, s.count(a), a[:160]))


def main():
    portal, trinity = sys.argv[1], sys.argv[2]
    nuevos = {}

    def cargar(r):
        return nuevos[r] if r in nuevos else leer(r)

    for rel, ancla, nuevo, marca in PORTAL:
        r = os.path.join(portal, rel); s = cargar(r)
        if marca in s:
            print('ya estaba:', rel, '·', marca); continue
        unico(s, ancla, r)
        nuevos[r] = s.replace(ancla, nuevo)

    for rel, ancla, linea, marca in VIENE:
        r = os.path.join(trinity, rel); s = cargar(r)
        if marca in s:
            print('ya estaba:', rel); continue
        unico(s, ancla, r)
        i = s.index('</p>', s.index(ancla)) + len('</p>')
        i = s.index('\n', i) + 1
        s = s[:i] + linea + s[i:]
        if 'p.viene a.vuelta' not in s:
            unico(s, '</head>', r)
            s = s.replace('</head>', ESTILO_VUELTA + '</head>')
        nuevos[r] = s

    for r, s in nuevos.items():
        with open(r, 'w', encoding='utf-8', newline='') as f:
            f.write(s)
        print('escrito:', r)
    print('Listo: %d archivos.' % len(nuevos))


if __name__ == '__main__':
    main()

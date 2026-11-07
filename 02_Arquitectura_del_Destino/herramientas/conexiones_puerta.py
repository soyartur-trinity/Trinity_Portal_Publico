#!/usr/bin/env python3
"""La Puerta: títulos soñados y nombre del autor (3 de noviembre de 2026).

1. Los recuadros de conexiones nombraban cinco libros que no existen con ese nombre.
   Arturo aprobó a qué libro real apunta cada uno; los nueve renglones pasan a
   enlazar, con la forma del Nodo 2:
     Cuerpo-Mente-Espíritu (#10)    -> Sanación Integral (Origen X)
     El Navegante de Sueños (#6)    -> El Vacío Fértil, nodo 3, Navegación del Abismo
     La Medicina del Silencio (#8)  -> El Vacío Fértil, nodo 5, La paz del no-saber
     El Terapeuta Consciente (#11)  -> La Muerte como Maestra, nodo 3, El Arte del Acompañamiento
     La Alquimia Emocional (#7)     -> Psicología Cuántica, nodo 2, Las Emociones como Información Cuántica

2. El nombre del autor, a criterio de Claude por encargo de Arturo: queda donde
   cuenta la autoría y la colaboración como caso vivo (créditos del Nodo 13; la
   autoría relacional del Nodo 8; las fórmulas de los nodos 5 y 12) y sale donde el
   libro lo presentaba como modelo: el pasaje del Nodo 11 que lo ubicaba en el Nivel 3 de
   su escala, su nombre junto a Rogers, Gendlin, Shapiro y van der Kolk en
   el mismo nodo, y el renglón «modelo contemporáneo» de las conexiones del Nodo 8.

3. Los enlaces de los recuadros se veían con el azul del navegador en los nodos que
   no tenían estilo para enlaces: toman el oro de La Puerta, sin pisar los que ya
   tenían estilo propio.

Corre después de pulir_puerta.py. Cada reemplazo se aplica exactamente una vez;
si no, no se escribe nada.

Uso: python3 conexiones_puerta.py RUTA/Trinity-/00_Portal_Trinity
"""
import os, sys

O = '../01_Trinity_Origen/'


def fuerte(ruta, titulo, ref):
    return '<li><a href="%s%s"><strong>%s</strong></a> (Trinity Origen %s)' % (O, ruta, titulo, ref)


def simple(ruta, titulo, ref):
    return '<li><a href="%s%s">%s</a> (Origen %s)</li>' % (O, ruta, titulo, ref)


SANACION = ('Libro_10/index.html', 'Sanación Integral', '#10')
NAVEGACION = ('Libro_06/nodo_03.html', 'El Vacío Fértil', '#6, nodo 3: <em>Navegación del Abismo</em>')
PAZ = ('Libro_06/nodo_05.html', 'El Vacío Fértil', '#6, nodo 5: <em>La paz del no-saber</em>')
ACOMPANAR = ('Libro_07/nodo_03.html', 'La Muerte como Maestra', '#7, nodo 3: <em>El Arte del Acompañamiento</em>')
EMOCIONES = ('Libro_01/nodo_02.html', 'Psicología Cuántica', '#1, nodo 2: <em>Las Emociones como Información Cuántica</em>')

CAMBIOS = [
    (3, '<li><strong>Cuerpo-Mente-Espíritu</strong> (Trinity Origen #10)', fuerte(*SANACION)),
    (4, '<li><strong>La Medicina del Silencio</strong> (Trinity Origen #8)', fuerte(*PAZ)),
    (6, '<li><strong>El Navegante de Sueños</strong> (Trinity Origen #6)', fuerte(*NAVEGACION)),
    (6, '<li><strong>La Medicina del Silencio</strong> (Trinity Origen #8)', fuerte(*PAZ)),
    (8, '<li>El Terapeuta Consciente (Origen #11)</li>', simple(*ACOMPANAR)),
    (10, '<li>La Medicina del Silencio (#8)</li>', simple(*PAZ)),
    (11, '<li><strong>El Terapeuta Consciente</strong> (Trinity Origen #11)', fuerte(*ACOMPANAR)),
    (11, '<li><strong>La Alquimia Emocional</strong> (Trinity Origen #7)', fuerte(*EMOCIONES)),
    (11, '<li><strong>Cuerpo-Mente-Espíritu</strong> (Trinity Origen #10)', fuerte(*SANACION)),
    # El nombre del autor
    (8, '          <li>Lic. Arturo Rodríguez con Trinity (modelo contemporáneo)</li>\n', ''),
    (11, ' · Bessel van der Kolk · Lic. Arturo Rodríguez</p>', ' · Bessel van der Kolk</p>'),
    (11, '''  <p><strong>Arturo opera en Nivel 3.</strong></p>

  <p>40+ años integrando:</p>
  <ul>
    <li>Técnicas clínicas (ACT, mindfulness, compasión)</li>
    <li>Presencia contemplativa (meditación, budismo)</li>
    <li>Calibración al campo (protocolos diarios)</li>
  </ul>

  <p><strong>Resultado:</strong><br>
  No solo “aplica” terapia.<br>
  <strong>SE CONVIERTE en campo de sanación donde el paciente puede reorganizarse.</strong></p>

''', ''),
]


PARCHE = '    @media (max-width: 640px) { html { font-size: 115%; } }\n'
ENLACES = ('    :where(p, li) > a { color: #ecc96e; text-decoration-color: rgba(236, 201, 110, 0.5); '
           'text-underline-offset: 3px; }\n')


def main():
    carpeta = sys.argv[1]
    textos = {}
    for n in range(1, 14):
        textos[n] = open(os.path.join(carpeta, 'nodo_%02d.html' % n), encoding='utf-8').read()
        if textos[n].count(PARCHE) != 1:
            sys.exit('Nodo %d sin el pulido previo (pulir_puerta.py); no se escribe nada.' % n)
        textos[n] = textos[n].replace(PARCHE, PARCHE + ENLACES, 1)
    for n, viejo, nuevo in CAMBIOS:
        c = textos[n].count(viejo)
        if c != 1:
            sys.exit('Nodo %d: «%s» aparece %d veces; no se escribe nada.' % (n, viejo.strip()[:50], c))
        textos[n] = textos[n].replace(viejo, nuevo, 1)
    for n, s in textos.items():
        open(os.path.join(carpeta, 'nodo_%02d.html' % n), 'w', encoding='utf-8').write(s)
    print('Listo: %d cambios en los recuadros y el nombre; color de enlaces en los trece nodos.' % len(CAMBIOS))


if __name__ == '__main__':
    main()

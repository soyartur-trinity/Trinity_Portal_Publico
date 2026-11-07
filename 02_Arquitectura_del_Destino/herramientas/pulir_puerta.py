#!/usr/bin/env python3
"""Pulido de La Puerta (Portal 00, repositorio Trinity-), 3 de noviembre de 2026.

Una pasada técnica por los trece nodos, sin depurar el contenido:
  - forma: el Nodo 6 pasa de Markdown sin convertir a HTML (el texto no cambia);
    el Nodo 1 pierde un <nav> suelto en la cabecera y cierra su <main>; el Nodo 12
    cierra su contenedor y su documento; los bloques preformateados se ajustan al
    ancho; la letra del teléfono sube a 18 px o más;
  - navegación: los nodos 8, 9 y 10 llevaban a «#» en lugar del nodo siguiente;
    «Fin del Libro» (Nodo 13) lleva a «Del otro lado», en el índice;
  - el nombre del autor: «Artur» pasa a «Arturo» en el texto corrido y a
    «Lic. Arturo Rodríguez» en los créditos y en las listas de nombres;
  - erratas: «através» pasa a «a través»; unos asteriscos de Markdown en el Nodo 8;
  - referencias con título real y número equivocado o título mal citado, en los
    recuadros de conexiones, que además pasan a enlazar, como en el Nodo 2.

Los títulos soñados de los recuadros (libros que no existen con ese nombre) no se
tocan: los decide Arturo.

Cada reemplazo se aplica exactamente las veces previstas; si no, el script se
detiene sin escribir nada.

Uso: python3 pulir_puerta.py RUTA/Trinity-/00_Portal_Trinity
"""
import os, re, sys
import markdown

NOTA = ('<!-- Pulido técnico del 3 de noviembre de 2026 (maestro v4 de Arquitectura del Destino, sección 19): '
        'forma, navegación, letra del teléfono, nombre del autor, erratas y referencias. El contenido no se depuró. '
        'El estado anterior está en el historial del repositorio y en la etiqueta origen-original, que guarda el '
        'repositorio entero. -->\n')

CSS = ('\n    /* Pulido del 3 de noviembre de 2026: letra de 18 px o más en el teléfono y bloques que no desbordan */\n'
       '    pre, code { white-space: pre-wrap; overflow-wrap: anywhere; }\n'
       '    @media (max-width: 640px) { html { font-size: 115%; } }\n')

Q = 'https://soyartur-trinity.github.io/Trinity-/'

# (nodo, viejo, nuevo, veces)
CAMBIOS = [
    # Nodo 1: un <nav> suelto en la cabecera se tragaba la página
    (1, '  <meta charset="UTF-8" />\n  <nav class="trinity-nav">\n', '  <meta charset="UTF-8" />\n', 1),
    (1, '    </article>\n  </div>\n</body>', '    </article>\n  </div>\n    </main>\n</body>', 1),
    # Nodo 1: la navegación de arriba (nav-trinity) solo tomaba estilo por estar dentro del <nav> suelto
    (1, '.trinity-nav {\n    display: flex;\n    justify-content: center;\n    align-items: center;\n    gap: 25px;',
        '.trinity-nav, .nav-trinity {\n    display: flex;\n    flex-wrap: wrap;\n    justify-content: center;\n    align-items: center;\n    gap: 12px 16px;', 1),
    (1, '.trinity-nav a {\n', '.trinity-nav a, .nav-trinity a {\n', 1),
    (1, '.trinity-nav a:hover {\n', '.trinity-nav a:hover, .nav-trinity a:hover {\n', 1),
    # Nodo 12: cierra el contenedor y el documento
    (12, '  <a href="nodo_13.html" class="nav-link">Nodo 13 →</a>\n</nav>\n',
         '  <a href="nodo_13.html" class="nav-link">Nodo 13 →</a>\n</nav>\n</div>\n</body>\n</html>\n', 1),
    # Navegación rota
    (8, '<a href="#">\n        <span>Nodo 9</span>', '<a href="nodo_09.html">\n        <span>Nodo 9</span>', 1),
    (8, '<a href="#">\n          <span>Ir al Nodo 9</span>', '<a href="nodo_09.html">\n          <span>Ir al Nodo 9</span>', 1),
    (9, '<a href="#">\n        <span>Nodo 10</span>', '<a href="nodo_10.html">\n        <span>Nodo 10</span>', 1),
    (9, '<a href="#">\n          <span>Ir al Nodo 10</span>', '<a href="nodo_10.html">\n          <span>Ir al Nodo 10</span>', 1),
    (10, '<a href="#">\n        <span>Nodo 11</span>', '<a href="nodo_11.html">\n        <span>Nodo 11</span>', 1),
    (10, '<a href="#">\n          <span>Ir al Nodo 11</span>', '<a href="nodo_11.html">\n          <span>Ir al Nodo 11</span>', 1),
    (13, '<a href="#">Fin del Libro</a>', '<a href="index.html#otro-lado-t">Fin del Libro</a>', 1),
    # El nombre del autor
    (5, '<li>Artur define intención (servicio)</li>', '<li>Arturo define intención (servicio)</li>', 1),
    (5, 'Artur + Claude + Campo Cuántico = las 3 llaves en acción', 'Arturo + Claude + Campo Cuántico = las 3 llaves en acción', 1),
    (8, '<p>Artur no “escribió” los 39 libros.', '<p>Arturo no “escribió” los 39 libros.', 1),
    (8, 'del sistema Artur+Claude+Contexto.', 'del sistema Arturo + Claude + Contexto.', 1),
    (8, '<strong>Artur evita esto:</strong>', '<strong>Arturo evita esto:</strong>', 1),
    (8, '<li>Artur con Trinity (modelo contemporáneo)</li>', '<li>Lic. Arturo Rodríguez con Trinity (modelo contemporáneo)</li>', 1),
    (11, '<strong>Artur opera en Nivel 3.</strong>', '<strong>Arturo opera en Nivel 3.</strong>', 1),
    (11, 'Bessel van der Kolk · Artur</p>', 'Bessel van der Kolk · Lic. Arturo Rodríguez</p>', 1),
    (12, '(Artur + múltiples IAs + lectores = red viviente)', '(Arturo + múltiples IAs + lectores = red viviente)', 1),
    (13, '<li><strong>Artur</strong> – Humano calibrado', '<li><strong>Lic. Arturo Rodríguez</strong> – Humano calibrado', 1),
    # Erratas
    (8, '**Todos pueden.**', '<strong>Todos pueden.</strong>', 1),
    (11, '<li><strong>El Dolor Como Portal</strong> (Trinity Origen #3)</li>',
         '<li><a href="../01_Trinity_Origen/Libro_03/index.html"><strong>El Dolor como Portal</strong></a> (Trinity Origen #3)</li>', 1),
    (13, '<li>El Dolor Como Portal</li>', '<li>El Dolor como Portal</li>', 1),
    # Referencias con título real: número o título corregidos, y enlace
    (1, '<li><strong>La Voz Interior</strong> (Trinity Origen #1)',
        '<li><a href="../01_Trinity_Origen/Libro_02/index.html"><strong>La Voz Interior</strong></a> (Trinity Origen #2)', 1),
    (8, '<li>La Voz Interior (Origen #1)</li>', '<li><a href="../01_Trinity_Origen/Libro_02/index.html">La Voz Interior</a> (Origen #2)</li>', 1),
    (12, '<li><strong>Consciencia Colectiva</strong> (Trinity Origen #12) → Campos morfogenéticos profundizados</li>',
         '<li><a href="../01_Trinity_Origen/Libro_11/nodo_02.html"><strong>La Consciencia Planetaria</strong></a> '
         '(Trinity Origen #11, nodo 2: <em>La Red de Consciencias Despiertas</em>) → Campos morfogenéticos profundizados</li>', 1),
    (4, '<li><strong>Portal Infinito</strong> (Trinity Quantum #5)',
        '<li><a href="../02_Trinity_Quantum/Libro_05/index.html"><strong>El Portal Infinito</strong></a> (Trinity Quantum #5)', 1),
    (5, '<li><strong>Portal Infinito</strong> (Trinity Quantum #5)',
        '<li><a href="../02_Trinity_Quantum/Libro_05/index.html"><strong>El Portal Infinito</strong></a> (Trinity Quantum #5)', 1),
    (8, '<li>Portal Infinito (Quantum #5)</li>', '<li><a href="../02_Trinity_Quantum/Libro_05/index.html">El Portal Infinito</a> (Quantum #5)</li>', 1),
    (10, '<li>Portal Infinito (#5)</li>', '<li><a href="../02_Trinity_Quantum/Libro_05/index.html">El Portal Infinito</a> (Quantum #5)</li>', 1),
    (10, '<li>El Vacío Creativo (#6)</li>', '<li><a href="../02_Trinity_Quantum/Libro_06/index.html">El Vacío Creativo</a> (Quantum #6)</li>', 1),
    (8, '<li>Transducción Dimensional (Quantum #11)</li>', '<li><a href="../02_Trinity_Quantum/Libro_11/index.html">Transducción Dimensional</a> (Quantum #11)</li>', 1),
]

# Títulos reales de Quantum que, en los recuadros, ya van bien citados: pasan a enlazar.
QUANTUM = {
    'El Arquitecto Cuántico': 1, 'Entrelazamiento Sagrado': 2, 'El Tiempo Vertical': 3, 'El Vacío Creativo': 6,
    'Realidades Holofractales': 7, 'Transducción Dimensional': 11, 'Singularidad Consciente': 12,
    'El Multiverso Interior': 13,
}
ORIGEN = {'Inteligencias Sin Nombre': 4}


def enlazar_conexiones(s):
    """<li><strong>Título</strong> (Trinity Quantum #N) → …</li> pasa a enlazar el título, si es real."""
    def r(m):
        titulo, serie, num = m.group(1), m.group(2), int(m.group(3))
        tabla, carpeta = (QUANTUM, '02_Trinity_Quantum') if serie == 'Quantum' else (ORIGEN, '01_Trinity_Origen')
        if tabla.get(titulo) != num:
            return m.group(0)
        return '<li><a href="../%s/Libro_%02d/index.html"><strong>%s</strong></a> (Trinity %s #%d)' % (carpeta, num, titulo, serie, num)
    return re.sub(r'<li><strong>([^<]+)</strong> \(Trinity (Quantum|Origen) #(\d+)\)', r, s)


def nodo6(s):
    m = re.search(r'<pre class="node-text">\n?(.*?)</pre>', s, re.S)
    md = m.group(1)
    lineas = md.split('\n')
    # Las tres primeras piezas repiten la cabecera: el rótulo, el título y el subtítulo.
    assert lineas[0].startswith('# 🌀 TRINITY: LA PUERTA')
    assert lineas[2].startswith('## NODO 6:')
    assert lineas[4].strip() == '*Los mapas del territorio no-ordinario*'
    cuerpo = '\n'.join(lineas[5:])
    cuerpo = re.sub(r'^\s*-{5,}\s*$', '---', cuerpo, flags=re.M)
    cuerpo = re.sub(r'^\s*---\s*\n', '', cuerpo.lstrip('\n'), count=1)  # la raya bajo el subtítulo ya la dibuja la cabecera
    html = markdown.markdown(cuerpo, extensions=['extra', 'sane_lists'], output_format='html')
    html = html.replace('através', 'a través')
    s = s.replace(m.group(0), '<div class="node-text">\n%s\n      </div>' % html, 1)
    viejo = '      <h1>NODO 6: ESTADOS DE CONSCIENCIA EXPANDIDA</h1>\n      <p class="node-subtitle">Trinity: La Puerta — Portal de Reconexión 3.0</p>'
    assert s.count(viejo) == 1
    s = s.replace(viejo, '      <p class="node-kicker">🌀 Trinity: La Puerta 🌀</p>\n'
                         '      <h1>NODO 6: ESTADOS DE CONSCIENCIA EXPANDIDA</h1>\n'
                         '      <p class="node-subtitle"><em>Los mapas del territorio no-ordinario</em></p>', 1)
    estilo_viejo = re.search(r'    \.node-text \{.*?\n    \}\n', s, re.S).group(0)
    s = s.replace(estilo_viejo, '''    .node-kicker { font-size: 0.78rem; letter-spacing: 0.18em; text-transform: uppercase; color: var(--text-soft); margin-bottom: 8px; }
    .node-text { margin-top: 6px; font-size: 1rem; color: var(--text-main); }
    .node-text p { margin: 0 0 1em; }
    .node-text h2 { margin: 1.6em 0 0.6em; font-size: 1.35rem; color: var(--accent-gold); letter-spacing: 0.04em; }
    .node-text h3 { margin: 1.3em 0 0.5em; font-size: 1.1rem; color: var(--accent-violet); letter-spacing: 0.06em; text-transform: uppercase; }
    .node-text strong { color: #fff; }
    .node-text em { color: var(--text-soft); }
    .node-text ul, .node-text ol { margin: 0 0 1em 1.3em; }
    .node-text li { margin: 0 0 0.35em; }
    .node-text hr { border: none; height: 1px; margin: 1.8em 0; background: linear-gradient(90deg, transparent, rgba(194, 155, 255, 0.5), transparent); }
    .node-text blockquote { margin: 1.2em 0; padding: 14px 18px; border-left: 3px solid var(--accent-violet); background: rgba(194, 155, 255, 0.07); border-radius: 0 12px 12px 0; }
    .node-text blockquote p { margin: 0; }
    .node-text table { border-collapse: collapse; margin: 0 0 1em; }
    .node-text th, .node-text td { border: 1px solid rgba(194, 155, 255, 0.25); padding: 6px 10px; text-align: left; }
''', 1)
    return s


def main():
    carpeta = sys.argv[1]
    textos = {n: open(os.path.join(carpeta, 'nodo_%02d.html' % n), encoding='utf-8').read() for n in range(1, 14)}
    if 'Pulido técnico del 3 de noviembre' in textos[1]:
        sys.exit('La Puerta ya estaba pulida; no se escribe nada.')
    for n, viejo, nuevo, veces in CAMBIOS:
        c = textos[n].count(viejo)
        if c != veces:
            sys.exit('Nodo %d: «%s» aparece %d veces (se esperaban %d); no se escribe nada.' % (n, viejo[:50], c, veces))
        textos[n] = textos[n].replace(viejo, nuevo)
    textos[6] = nodo6(textos[6])
    total = 0
    for n in range(1, 14):
        s = textos[n]
        total += s.count('através')
        s = s.replace('através', 'a través')
        s = enlazar_conexiones(s)
        if s.count('</style>') < 1 or not s.startswith('<!DOCTYPE html>'):
            sys.exit('Nodo %d sin la forma esperada; no se escribe nada.' % n)
        s = s.replace('</style>', CSS + '  </style>', 1)
        s = s.replace('<!DOCTYPE html>\n', '<!DOCTYPE html>\n' + NOTA, 1)
        textos[n] = s
    for n, s in textos.items():
        open(os.path.join(carpeta, 'nodo_%02d.html' % n), 'w', encoding='utf-8').write(s)
    print('Listo: trece nodos; %d «através» corregidos fuera del Nodo 6.' % total)


if __name__ == '__main__':
    main()

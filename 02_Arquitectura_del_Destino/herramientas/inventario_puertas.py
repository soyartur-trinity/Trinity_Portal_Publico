#!/usr/bin/env python3
"""Inventario de la Red de puertas (Campo Trinity).

Recorre los dos repositorios y lee:
  1. los bloques <aside class="puerta ..."> de Trinity- (puertas fractales:
     de un nodo de la serie mayor hacia Arquitectura, el Portal o Trinity);
  2. la sección «Puertas laterales» de los cierres de Arquitectura del Destino;
  3. cualquier enlace de los libros del Portal Público (01_Libros) hacia Trinity-;
  4. los enlaces marcados <a class="vuelta">: en los portales de serie de Trinity-
     (por ejemplo, «Viene de Trinity Origen» en el portal de Quantum) y, desde el
     9 de noviembre de 2026, en los cierres de Arquitectura del Destino (la línea
     «Vienen de Trinity Quantum», debajo de las «Puertas laterales»).

Para cada puerta decide si vuelve: si el libro de destino enlaza de regreso
al nodo exacto de origen (o, para las puertas que salen de un cierre, si el
nodo de destino tiene una puerta hacia ese libro).

Uso:
  python3 inventario_puertas.py RUTA_TRINITY RUTA_PORTAL [salida.json]
Sin salida, imprime el resumen. Con salida, escribe además los datos
(desde, hacia, serie, vuelve) para el mapa de la Red.
"""
import html, json, os, re, sys
from urllib.parse import urljoin, urlparse

BASE_T = 'https://soyartur-trinity.github.io/Trinity-/'
BASE_P = 'https://soyartur-trinity.github.io/Trinity_Portal_Publico/'


def canon(href, desde_url):
    """Devuelve ('T'|'P', ruta) para un enlace, o None si sale de la constelación."""
    u = urljoin(desde_url, href.split('#')[0])
    for base, r in ((BASE_T, 'T'), (BASE_P, 'P')):
        if u.startswith(base):
            ruta = u[len(base):]
            if ruta == '' or ruta.endswith('/'):
                ruta += 'index.html'
            return r, ruta
    return None


# El índice de Arquitectura no enlaza la serie mayor: la puerta de Quantum 1.7,
# que llega a él, vuelve desde el cierre de El Campo, su primer libro (el mapa
# de la Red ya ubica el índice en el Libro 1).
ALIAS = {('P', '02_Arquitectura_del_Destino/index.html'):
         ('P', '02_Arquitectura_del_Destino/libro-01-el-campo')}


def libro_de(r, ruta):
    """El libro al que pertenece una página: la carpeta que la contiene."""
    return ALIAS.get((r, ruta), (r, os.path.dirname(ruta)))


def texto(s):
    return html.unescape(re.sub(r'<[^>]+>', '', s)).strip()


def serie(r, ruta):
    if r == 'T':
        if ruta.startswith('01_Trinity_Origen'): return 'Origen'
        if ruta.startswith('02_Trinity_Quantum'): return 'Quantum'
        if ruta.startswith('Trinity_Infinito'): return 'Infinito'
        if ruta.startswith('00_Portal_Trinity'): return 'La Puerta'
        return 'Trinity'
    if ruta.startswith('02_Arquitectura_del_Destino'): return 'Arquitectura'
    if ruta.startswith('01_Libros'): return 'Portal'
    return 'Portal'


def main():
    rt, rp = sys.argv[1], sys.argv[2]
    salida = sys.argv[3] if len(sys.argv) > 3 else None
    puertas = []

    # 1. Puertas fractales de Trinity-
    for raiz, _, archivos in os.walk(rt):
        for a in sorted(archivos):
            if not a.endswith('.html'):
                continue
            p = os.path.join(raiz, a)
            rel = os.path.relpath(p, rt).replace(os.sep, '/')
            s = open(p, encoding='utf-8').read()
            for m in re.finditer(r'<aside class="puerta( [^"]*)?"[^>]*>(.*?)</aside>', s, re.S):
                bloque = m.group(2)
                h = re.search(r'<a class="cruzar" href="([^"]+)"', bloque)
                t = re.search(r'<p class="p-texto">(.*?)</p>', bloque, re.S)
                if not h:
                    continue
                d = canon(h.group(1), BASE_T + rel)
                puertas.append({
                    'tipo': 'fractal', 'desde': ['T', rel],
                    'hacia': list(d) if d else [None, h.group(1)],
                    'texto': texto(t.group(1)) if t else '',
                    'clase': (m.group(1) or '').strip(),
                })

    # 2. Puertas laterales de los cierres de Arquitectura
    arq = os.path.join(rp, '02_Arquitectura_del_Destino')
    for libro in sorted(os.listdir(arq)):
        if not libro.startswith('libro-'):
            continue
        for a in os.listdir(os.path.join(arq, libro)):
            if not a.endswith('-cierre.html'):
                continue
            rel = '02_Arquitectura_del_Destino/%s/%s' % (libro, a)
            s = open(os.path.join(rp, rel), encoding='utf-8').read()
            m = re.search(r'<h2>Puertas laterales</h2><ul class="enlaces">(.*?)</ul>', s, re.S)
            if not m:
                continue
            for h, t in re.findall(r'<li><a href="([^"]+)">(.*?)</a></li>', m.group(1), re.S):
                d = canon(h, BASE_P + rel)
                puertas.append({
                    'tipo': 'lateral', 'desde': ['P', rel],
                    'hacia': list(d) if d else [None, h], 'texto': texto(t), 'clase': '',
                })

    # 3. Enlaces del Portal Público (01_Libros) hacia Trinity-
    lib = os.path.join(rp, '01_Libros')
    for raiz, _, archivos in os.walk(lib):
        for a in sorted(archivos):
            if not a.endswith('.html'):
                continue
            rel = os.path.relpath(os.path.join(raiz, a), rp).replace(os.sep, '/')
            s = open(os.path.join(rp, rel), encoding='utf-8').read()
            for h, t in re.findall(r'<a [^>]*href="([^"]*Trinity-/[^"]*)"[^>]*>(.*?)</a>', s, re.S):
                d = canon(h, BASE_P + rel)
                puertas.append({
                    'tipo': 'portal', 'desde': ['P', rel],
                    'hacia': list(d) if d else [None, h], 'texto': texto(t), 'clase': '',
                })

    # 4. Vueltas marcadas: portales de serie de Trinity- y cierres de Arquitectura
    for repo, base, raiz_v in (('T', BASE_T, rt), ('P', BASE_P, arq)):
        raiz_repo = rt if repo == 'T' else rp
        for raiz, _, archivos in os.walk(raiz_v):
            for a in sorted(archivos):
                if not a.endswith('.html'):
                    continue
                rel = os.path.relpath(os.path.join(raiz, a), raiz_repo).replace(os.sep, '/')
                s = open(os.path.join(raiz_repo, rel), encoding='utf-8').read()
                for h, t in re.findall(r'<a class="vuelta" href="([^"]+)">(.*?)</a>', s, re.S):
                    d = canon(h, base + rel)
                    puertas.append({
                        'tipo': 'vuelta', 'desde': [repo, rel],
                        'hacia': list(d) if d else [None, h], 'texto': texto(t), 'clase': '',
                    })

    # Vuelta: ¿el libro de destino enlaza de regreso a la página de origen?
    for x in puertas:
        x['serie_desde'] = serie(*x['desde'])
        x['serie_hacia'] = serie(*x['hacia']) if x['hacia'][0] else 'fuera'
        x['vuelve'] = False
        if not x['hacia'][0]:
            continue
        libro_dest = libro_de(*x['hacia'])
        for y in puertas:
            if y is x or not y['hacia'][0]:
                continue
            if libro_de(*y['desde']) == libro_dest and tuple(y['hacia']) == tuple(x['desde']):
                x['vuelve'] = True
                break
        # Un cierre que enlaza un nodo vuelve si ese nodo tiene puerta hacia el libro
        if not x['vuelve'] and x['tipo'] in ('lateral', 'portal', 'vuelta'):
            libro_orig = libro_de(*x['desde'])
            for y in puertas:
                if tuple(y['desde']) == tuple(x['hacia']) and y['hacia'][0] and libro_de(*y['hacia']) == libro_orig:
                    x['vuelve'] = True
                    break

    # Resumen
    def f(par):
        return '%s:%s' % tuple(par)
    fract = [x for x in puertas if x['tipo'] == 'fractal']
    lat = [x for x in puertas if x['tipo'] == 'lateral']
    por = [x for x in puertas if x['tipo'] == 'portal']
    print('Puertas fractales en Trinity-: %d' % len(fract))
    for s_ in ('Origen', 'Quantum'):
        n = [x for x in fract if x['serie_desde'] == s_]
        print('  %s: %d (vuelven %d)' % (s_, len(n), sum(x['vuelve'] for x in n)))
    print('Puertas laterales en los cierres de Arquitectura: %d (con vuelta %d)' % (len(lat), sum(x['vuelve'] for x in lat)))
    print('Enlaces del Portal Público hacia Trinity-: %d (con vuelta %d)' % (len(por), sum(x['vuelve'] for x in por)))
    vu = [x for x in puertas if x['tipo'] == 'vuelta']
    print('Vueltas marcadas: %d (en Trinity- %d, en los cierres de Arquitectura %d)' % (
        len(vu), sum(x['desde'][0] == 'T' for x in vu), sum(x['desde'][0] == 'P' for x in vu)))
    rotas = [x for x in puertas if not x['hacia'][0] or not os.path.exists(
        os.path.join(rt if x['hacia'][0] == 'T' else rp, x['hacia'][1]))]
    print('Destinos que no existen: %d' % len(rotas))
    for x in rotas:
        print('  ', x['desde'][1], '->', x['hacia'])
    sin = [x for x in fract if not x['vuelve']]
    if sin:
        print('Puertas fractales sin vuelta: %d' % len(sin))
        for x in sin:
            print('  → %-42s -> %s' % (x['desde'][1], f(x['hacia'])))
    print()
    print('Puertas fractales de Origen:')
    for x in fract:
        if x['serie_desde'] == 'Origen':
            print('  %s %-34s -> %-60s %s' % ('↔' if x['vuelve'] else '→', x['desde'][1], f(x['hacia']), x['clase']))
    if salida:
        json.dump({'puertas': puertas}, open(salida, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        print('\nDatos escritos en', salida)


if __name__ == '__main__':
    main()

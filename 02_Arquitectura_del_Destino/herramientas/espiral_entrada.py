#!/usr/bin/env python3
"""La espiral de la primera pantalla de La Espiral (9 de noviembre de 2026).

A pedido de Arturo, el sigilo ◈ de la primera pantalla de la entrada de Trinity-
(que es también el de Origen) se reemplaza por una espiral dibujada en oro, que
gira muy despacio.

Es una espiral logarítmica, la de crecimiento constante: su radio crece en la
proporción áurea (φ) a cada vuelta completa. (La «espiral áurea» clásica crece φ
en cada cuarto de vuelta: a este tamaño se ve como un gancho y no como una
espiral; con φ por vuelta se leen cuatro vueltas, casi centradas.) Se dibuja como
una cinta que se afina en sus dos puntas y nunca llega al polo: el centro queda
vacío, como en el mapa de la Red.

Al girar en el sentido en que se enrosca, una espiral logarítmica parece fluir
hacia su centro sin llegar nunca, porque girarla equivale a achicarla: es el
recorrido del lector, del anillo exterior hacia el centro vacío. Una vuelta cada
dos minutos. Con el dispositivo en menos movimiento, queda quieta.

El oro es el de la Red (#d9b56a), más claro hacia adentro.

Se aplica una sola vez: si la espiral ya está, no hace nada; si el sigilo no
aparece exactamente una vez, se detiene sin escribir.

Uso: python3 espiral_entrada.py RUTA/Trinity-
"""
import math, os, sys

PHI = (1 + 5 ** 0.5) / 2
B = math.log(PHI) / (2 * math.pi)   # crecimiento: φ por cada vuelta completa
VUELTAS = 4.0                       # vueltas visibles
R_EXT = 44.0                        # radio exterior, en un lienzo de 100 × 100
N = 420                             # puntos por borde


def cinta():
    """La espiral como una cinta cerrada: borde exterior de ida, interior de vuelta."""
    t_fin = VUELTAS * 2 * math.pi
    a = R_EXT / math.exp(B * t_fin)
    ida, vuelta = [], []
    for i in range(N + 1):
        t = t_fin * i / N
        r = a * math.exp(B * t)
        # ancho: crece con el radio y se afina en las dos puntas
        punta = min(1.0, (t_fin - t) / 1.4, t / 1.6)
        w = (0.062 * r + 0.55) * punta + 0.04
        # normal de la espiral logarítmica (tangente a ángulo constante)
        ang_t = t + math.atan2(1, B)          # dirección de la tangente
        nx, ny = math.cos(ang_t - math.pi / 2), math.sin(ang_t - math.pi / 2)
        x, y = r * math.cos(t), r * math.sin(t)
        ida.append((x + nx * w / 2, y + ny * w / 2))
        vuelta.append((x - nx * w / 2, y - ny * w / 2))
    pts = ida + vuelta[::-1]
    d = 'M' + ' L'.join('%.2f %.2f' % p for p in pts) + ' Z'
    return d


def svg():
    return ('<svg class="espiral" viewBox="-50 -50 100 100" aria-hidden="true" focusable="false">'
            '<defs><radialGradient id="oro-espiral" cx="0" cy="0" r="48" gradientUnits="userSpaceOnUse">'
            '<stop offset="0" stop-color="#f6e7bf"/><stop offset=".55" stop-color="#e3c27e"/>'
            '<stop offset="1" stop-color="#b8934f"/></radialGradient></defs>'
            '<g class="gira"><path d="%s" fill="url(#oro-espiral)"/></g></svg>' % cinta())


CSS = '''
    /* La espiral de la primera pantalla (9 de noviembre de 2026): reemplaza al sigilo ◈ */
    .espiral{ width:clamp(104px, 28vw, 124px); height:auto; display:block; margin:0 auto; overflow:visible;
      filter: drop-shadow(0 0 14px rgba(217,181,106,.28)); }
    .espiral .gira{ transform-box:view-box; transform-origin:50% 50%; animation: gira-espiral 120s linear infinite; }
    @keyframes gira-espiral{ to{ transform:rotate(360deg); } }
    @media (prefers-reduced-motion: reduce){ .espiral .gira{ animation:none; } }
'''

SIGILO = '<div class="sigil">◈</div>'
ANCLA_CSS = '    @keyframes pulse{ 0%,100%{transform:scale(1)} 50%{transform:scale(1.06)} }\n'


def main():
    ruta = os.path.join(sys.argv[1], 'index.html')
    s = open(ruta, encoding='utf-8').read()
    if 'class="espiral"' in s:
        print('ya estaba: la espiral de la entrada')
        return
    if s.count(SIGILO) != 1 or s.count(ANCLA_CSS) != 1:
        sys.exit('La entrada no tiene la forma esperada; no se escribe nada.')
    s = s.replace(SIGILO, svg(), 1).replace(ANCLA_CSS, ANCLA_CSS + CSS, 1)
    open(ruta, 'w', encoding='utf-8').write(s)
    print('espiral dibujada en la entrada (%d caracteres de trazo)' % len(cinta()))


if __name__ == '__main__':
    main()

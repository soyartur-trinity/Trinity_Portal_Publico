# -*- coding: utf-8 -*-
"""
Depuración de Trinity Quantum, Libro 1 · El Arquitecto Cuántico (octubre 2026).

Aplica, exactamente una vez cada uno, los reemplazos aprobados por Arturo
tarjeta por tarjeta (1.0 a 1.7), según la guía de depuración de Quantum
(Arquitectura del Destino, maestro v4, sección 5).
El original se conserva en la etiqueta quantum-original del repositorio Trinity-.

Uso: python3 depurar_quantum1.py ORIGEN DESTINO
  ORIGEN  = carpeta 02_Trinity_Quantum/Libro_01 original
  DESTINO = carpeta donde se escriben los archivos depurados
"""
import os
import sys

NOTA = ("<!-- Depurado en octubre de 2026 según la guía de depuración de Quantum "
        "(Arquitectura del Destino, maestro v4), con el veto de Arturo en cada nodo. "
        "El original se conserva en la etiqueta quantum-original del repositorio. -->\n")

CSS = """
    /* ============================================================
       Depuración · octubre 2026
       Letra más grande en el teléfono, firma y bloque fijo de las puertas.
       La puerta lleva el color de la serie a la que conduce.
       ============================================================ */
    .node-content p.signature{
      margin: 26px 0 8px;
      color: rgba(243, 209, 122, .85);
      font-size: 14px;
      letter-spacing: .04em;
    }
    .puerta{
      margin: 30px 0 10px;
      padding: 18px 20px 16px;
      border-radius: 16px;
      border: 1px solid var(--p-borde);
      background: var(--p-fondo);
      box-shadow: 0 10px 24px rgba(0,0,0,.28);
    }
    .puerta.arquitectura{
      --p-fondo: linear-gradient(180deg, rgba(6,13,26,.94), rgba(6,13,26,.74));
      --p-borde: rgba(168,196,224,.42);
      --p-acento: #a8c4e0;
      --p-texto: #e8eef6;
    }
    .puerta.portal{
      --p-fondo: linear-gradient(180deg, rgba(13,12,11,.94), rgba(13,12,11,.74));
      --p-borde: rgba(201,168,76,.42);
      --p-acento: #c9a84c;
      --p-texto: #e8e0d0;
    }
    .node-content .puerta .p-nombre{
      margin: 0 0 6px;
      font-size: 15px;
      font-style: italic;
      letter-spacing: .06em;
      color: var(--p-acento);
    }
    .node-content .puerta .p-texto{
      margin: 0 0 14px;
      color: var(--p-texto);
    }
    .puerta .cruzar{
      display: inline-flex;
      align-items: center;
      gap: 10px;
      padding: 9px 16px;
      border-radius: 999px;
      border: 1px solid var(--p-borde);
      color: var(--p-acento);
      font-size: 14px;
      letter-spacing: .04em;
      text-decoration: none;
      transition: border-color .18s ease, background .18s ease;
    }
    .puerta .cruzar:hover{ border-color: var(--p-acento); background: rgba(255,255,255,.04); }
    .puerta .cruzar:focus-visible{ outline: 2px solid var(--p-acento); outline-offset: 3px; }

    @media (max-width: 640px){
      .node-content p, .node-content li{ font-size: 18px; line-height: 1.7; }
      .node-content p.signature{ font-size: 15px; }
      .puerta{ padding: 16px 16px 14px; }
    }
    @media (prefers-reduced-motion: reduce){
      .puerta .cruzar{ transition: none; }
    }
"""

FIRMA = '<p class="signature"><strong>— Trinity Quantum · El Arquitecto Cuántico</strong></p>'

BASE_ARQ = "https://soyartur-trinity.github.io/Trinity_Portal_Publico/02_Arquitectura_del_Destino/"


def puerta_arquitectura(texto, href, indent=""):
    return (f'{indent}<aside class="puerta arquitectura" aria-label="Puerta hacia Arquitectura del Destino">\n'
            f'{indent}  <p class="p-nombre">Puerta</p>\n'
            f'{indent}  <p class="p-texto">{texto}</p>\n'
            f'{indent}  <a class="cruzar" href="{href}">Cruzar ⟶</a>\n'
            f'{indent}</aside>')


class Editor:
    def __init__(self, nombre, texto):
        self.nombre = nombre
        self.s = texto
        self.n = 0

    def rep(self, viejo, nuevo):
        c = self.s.count(viejo)
        if c != 1:
            raise SystemExit(f"[{self.nombre}] {c} coincidencias para:\n{viejo[:160]!r}")
        self.s = self.s.replace(viejo, nuevo, 1)
        self.n += 1

    def tramo(self, inicio, fin, nuevo):
        """Reemplaza desde `inicio` (incluido) hasta `fin` (excluido)."""
        for marca in (inicio, fin):
            c = self.s.count(marca)
            if c != 1:
                raise SystemExit(f"[{self.nombre}] marca con {c} coincidencias:\n{marca[:160]!r}")
        a = self.s.index(inicio)
        b = self.s.index(fin)
        if b <= a:
            raise SystemExit(f"[{self.nombre}] marcas en orden inverso: {inicio[:60]!r}")
        self.s = self.s[:a] + nuevo + self.s[b:]
        self.n += 1

    def comunes(self, con_css=True):
        self.rep("<!DOCTYPE html>\n", "<!DOCTYPE html>\n" + NOTA)
        if con_css:
            self.rep("  </style>", CSS + "  </style>")


# ------------------------------------------------------------------ NODO 1
def nodo_01(e):
    e.comunes()
    e.rep("  A tu poder.</em></p>", "  A tu oficio.</em></p>")
    e.tramo("<p>La física cuántica reveló el secreto más perturbador y liberador:<br>",
            "<p>¿Pero quién colapsa la función de onda del observador?<br>",
            """<p>La física cuántica encontró algo perturbador y liberador:<br>
antes de medirse, una partícula se describe<br>
como un abanico de estados posibles, todos a la vez.</p>

<p>Al medirla, aparece en uno solo:<br>
una cosa específica,<br>
en un lugar específico,<br>
en un momento específico.</p>

<p>Qué es exactamente medir sigue siendo<br>
uno de los grandes misterios abiertos de la ciencia.<br>
Aquí lo tomamos como imagen, y la imagen es exacta para tu vida:<br>
<span class="highlight"><strong>también tu próximo instante llega como abanico,<br>
y tu atención decide cuál de sus posibilidades se vuelve experiencia.</strong></span></p>

""")
    e.tramo("<h3>LA CIENCIA DEL COLAPSO</h3>",
            "<h3>EL EXPERIMENTO DE LA DOBLE RENDIJA DE TU VIDA</h3>",
            """<h3>LO QUE DICE EL COLAPSO</h3>

<p>Dicho en una frase:<br>
de todo lo que podría pasarte,<br>
tu atención elige qué se hace experiencia.</p>

<p><span class="highlight"><strong>No decide lo que el mundo trae.</strong></span><br>
<span class="highlight"><strong>Decide qué parte de eso se vuelve tu vida.</strong></span></p>

<div class="spacer"></div>

""")
    e.rep("<li>Sin observación: crean patrón de onda (todas las posibilidades)</li>",
          "<li>Si nada registra por cuál rendija pasa cada uno, dibujan en la pantalla un patrón de onda (todas las posibilidades)</li>")
    e.rep("<li>Con observación: crean patrón de partícula (una realidad específica)</li>",
          "<li>Si se registra, el patrón se vuelve de partícula (un camino específico)</li>")
    e.rep("Tu vida es este experimento a escala macro.", "Tu vida se parece a este experimento.")
    e.rep("<li>Eres víctima del colapso inconsciente</li>", "<li>El hábito elige por ti</li>")
    e.rep("<li>Colapses deliberadamente las funciones de onda</li>",
          "<li>Eliges deliberadamente dónde poner la atención</li>")
    e.rep("<li>Eliges qué probabilidad se vuelve realidad</li>",
          "<li>Ves más de una posibilidad antes de decidir</li>")
    e.rep("<li>Eres creador consciente de tu universo</li>",
          "<li>Habitas tu vida como autor, no como espectador</li>")
    e.rep("<h3>LOS NIVELES DEL COLAPSO</h3>\n\n<h4>Nivel 1: Colapso Inconsciente</h4>\n<p>Así vive el 99% de la humanidad:</p>",
          "<h3>LOS NIVELES DEL COLAPSO</h3>\n\n<p><em>No son clases de personas: son modos por los que cualquiera pasa, a veces en una misma tarde.</em></p>\n\n<h4>Nivel 1: Colapso Inconsciente</h4>\n<p>Así vive casi todo el mundo, casi todo el tiempo:</p>")
    e.rep("<li>Entienden que CREAN al observar</li>", "<li>Entienden que lo que miran crece en su vida</li>")
    e.rep("<li>Colapsan realidades antes imposibles</li>", "<li>Se atreven con lo que antes ni veían</li>")
    e.rep("<li>Mantienen múltiples realidades en superposición</li>",
          "<li>Sostienen varias posibilidades abiertas, sin angustia</li>")
    e.rep("<li>Navegan probabilidades como un menú</li>", "<li>Eligen sin apuro, cuando llega el momento</li>")
    e.rep("– Detén toda actividad mental", "– Detén por un instante lo que estás haciendo")
    e.rep("– El próximo momento existe en superposición", "– El próximo momento todavía está abierto")
    e.rep("– Infinitas versiones del próximo segundo flotan",
          "– Nota sus versiones posibles: seguir leyendo, levantar la vista, respirar más hondo, mover el cuerpo")
    e.rep("– Con tu consciencia, selecciona UNA versión específica", "– Toma una, sin apuro")
    e.rep("– Observa intensamente esa versión hasta que se solidifique", "– Entra en ella con toda tu atención")
    e.rep("– Experimenta el momento que acabas de crear", "– Experimenta el momento que acabas de elegir")
    e.tramo("<p>¿Sentiste el poder?<br>", "<h3>LA MATEMÁTICA DEL ARQUITECTO</h3>",
            """<p>¿Sentiste ese instante?<br>
¿Notaste el momento exacto en que una posibilidad se volvió gesto?</p>

<div class="quote-block">
  <p><em>Ese lugar, justo antes del gesto,<br>
  es el taller del Arquitecto.</em></p>
</div>

<div class="spacer"></div>

""")
    e.tramo("<h4>Teorema del Colapso Intencional:</h4>",
            "<div class=\"activation\">\n  <p>“Yo Soy el Observador Cuántico de mi realidad.</p>",
            """<p>La matemática del Arquitecto es sencilla:<br>
no cuenta la fuerza con que miras,<br>
sino cuántas veces vuelves a mirar.</p>

<p>Una atención que regresa sin apretar, día tras día,<br>
rinde más que un esfuerzo intenso de una tarde.</p>

<p>Y cada creencia que estrecha lo posible,<br>
cuando se afloja,<br>
deja ver otro tramo del campo.</p>

<div class="spacer"></div>

<h3>PARA RECORDAR</h3>

""")
    e.rep("  <p>Mis células responden a mi consciencia.</p>\n  <p>Mi ADN se reorganiza según mi observación.</p>\n", "")
    e.rep("  <p>La realidad es mi creación.”</p>", "  <p>Mi vida es mi obra.”</p>")
    e.rep("<p><em>Siente cómo tus células responden.<br>\nNota cómo tu campo cuántico se reorganiza.<br>\nObserva cómo la realidad comienza a ondular.</em></p>\n\n", "")
    e.rep("tu capacidad de colapso se vuelve ilimitada.</p>", "tu elección deja de ser solo tuya.</p>")
    e.rep("- Una decisión consciente reorganiza mil probabilidades</li>",
          "- Una decisión consciente reordena muchas otras</li>")
    e.rep("<li><strong>Revertir Colapsos</strong><br>\n      - Lo que fue colapsado puede volver a la superposición<br>\n      - El pasado es más fluido de lo que crees<br>\n      - La retroactividad cuántica es real</li>",
          "<li><strong>Volver a Mirar lo Colapsado</strong><br>\n      - El pasado no se borra, pero su sentido se mueve<br>\n      - La memoria se rehace un poco cada vez que recuerdas<br>\n      - Puedes cambiar el peso que lo vivido tiene en ti</li>")
    e.rep("- El poder exponencial del colapso grupal</li>", "- La fuerza de lo que se mira entre muchos</li>")
    e.rep("<strong>Día 1-2:</strong>", "<strong>Días 1 y 2:</strong>")
    e.rep("<strong>Día 3-4:</strong>", "<strong>Días 3 y 4:</strong>")
    e.rep("<strong>Día 5-6:</strong> Intenta colapsos mayores (el día completo, encuentros específicos)<br>",
          "<strong>Días 5 y 6:</strong> Amplíalos a un tramo del día (un trayecto, una conversación)<br>")
    e.rep("<strong>Día 7:</strong> Realiza tu primer Colapso Maestro (elige y colapsa una realidad “imposible”)</p>",
          "<strong>Día 7:</strong> Elige una situación que creías imposible de vivir distinto y mírala desde un lugar nuevo, sin forzar ningún resultado</p>")
    e.rep("Nota cómo la realidad responde.<br>", "Nota cómo cambia tu mirada.<br>")
    e.rep("<h3>LA ACTIVACIÓN FINAL</h3>", "<h3>EL DESPERTAR DEL ARQUITECTO</h3>")
    e.rep("<p>Al cerrar este primer nodo, el campo cuántico te reconoce:</p>",
          "<p>Al cerrar este primer nodo, algo ya cambió en tu manera de ver:</p>")
    e.rep("<p><strong>Eres un Arquitecto Cuántico activado.</strong></p>",
          "<p><strong>Eres un Arquitecto Cuántico despierto.</strong></p>")
    e.rep("<p>Cada vez que tu realidad responda a tu observación,<br>",
          "<p>Cada vez que tu vida cambie porque cambiaste la mirada,<br>")
    e.rep("Es el mecanismo por el cual<br>\nla consciencia se convierte en experiencia,<br>\nel potencial se vuelve actual,<br>\ny tú te conviertes<br>\nen el creador consciente<br>\nde tu realidad.</p>",
          "Es la imagen de cómo<br>\nla consciencia se convierte en experiencia,<br>\nel potencial se vuelve acto<br>\ny tú te vuelves<br>\nautor consciente<br>\nde lo que vives.</p>")
    e.rep("<p><em>[Fin del Nodo 1: El Colapso de la Función de Onda]</em></p>", FIRMA)
    # Resto de producción: el enlace «Nodo anterior» del primer nodo apuntaba a sí mismo.
    e.rep('          <a class="nav-link" href="nodo_01.html">← Nodo anterior</a>\n', "")


# ------------------------------------------------------------------ NODO 2
def nodo_02(e):
    e.comunes()
    # Restos de producción en la cabecera: faltaban charset, viewport y título,
    # y la navegación superior estaba dentro de <head>.
    e.tramo("  <!-- META DEL NODO -->\n<section class=\"node-meta\">\n  <</header>",
            "  <link rel=\"stylesheet\" href=\"../assets/css/trinity-quantum.css\" />",
            "  <meta charset=\"UTF-8\" />\n  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />\n"
            "  <title>Libro 1 · Nodo 2 — El Observador como Creador</title>\n\n")
    e.rep("  <div class=\"portal-shell\">\n",
          "  <div class=\"portal-shell\">\n\n"
          "    <nav class=\"top-nav\">\n"
          "      <a class=\"top-nav-link\" href=\"nodo_01.html\">← Nodo anterior</a>\n"
          "      <a class=\"top-nav-link\" href=\"nodo_03.html\">Nodo siguiente →</a>\n"
          "      <a class=\"top-nav-link\" href=\"index.html\">Índice del Libro</a>\n"
          "      <a class=\"top-nav-link\" href=\"../index.html\">Portal Maestro</a>\n"
          "    </nav>\n\n")
    e.rep("<h2 class=\"highlight\">De Testigo Pasivo a Arquitecto Activo de Realidades</h2>",
          "<h2 class=\"highlight\">De Testigo Pasivo a Arquitecto Despierto</h2>")
    e.tramo("<p>La física cuántica reveló la verdad inversa:<br>",
            "<p>No eres testigo de la creación.<br>",
            """<p>La física cuántica ofrece una imagen que invierte la frase,<br>
y la ciencia de la percepción dice algo parecido a escala humana:<br>
tu cerebro no fotografía el mundo,<br>
lo construye a partir de lo que espera ver.</p>

<p><span class="highlight"><strong>“Conoce tu manera de observar, porque da forma a la realidad que vives.”</strong></span></p>

<p>No ves todo lo que existe.<br>
<strong>Existe, para ti, lo que miras.</strong></p>

""")
    e.rep("<h3>LA FÍSICA DE LA CREACIÓN POR OBSERVACIÓN</h3>", "<h3>LA IMAGEN DE LA CREACIÓN POR OBSERVACIÓN</h3>")
    e.rep("<li>Las partículas no tienen posición definida hasta ser observadas</li>",
          "<li>Las partículas no tienen posición definida hasta ser medidas</li>")
    e.rep("<li>No tienen siquiera una existencia “sólida” hasta el momento de la observación</li>",
          "<li>Lo que llamamos solidez es, a esa escala, una nube de probabilidades</li>")
    e.rep("<p><strong>¿Qué significa esto a escala humana?</strong></p>",
          "<p><strong>¿Qué sugiere esta imagen a escala humana?</strong></p>")
    e.rep("<li>Tu futuro no existe hasta que lo creas observándolo</li>",
          "<li>Tu futuro todavía no tiene forma, y tu manera de mirarlo es parte de la que tomará</li>")
    e.tramo("<h4>Ecuación Sagrada #2:</h4>", "<div class=\"spacer\"></div>\n\n<h3>LOS TIPOS DE OBSERVADOR</h3>",
            """<h4>Mirar, Querer, Atender</h4>

<p>Sin alguien que mire, nada se vive.<br>
Una mirada sin intención se dispersa.<br>
Una intención sin atención se apaga.<br>
<strong>Las tres juntas, sostenidas: eso es arquitectura.</strong></p>

""")
    e.rep("<h3>LOS TIPOS DE OBSERVADOR</h3>\n\n<h4>El Observador Dormido</h4>",
          "<h3>LOS TIPOS DE OBSERVADOR</h3>\n\n<p><em>Cualquiera pasa por los cinco, a veces en un mismo día.</em></p>\n\n<h4>El Observador Dormido</h4>")
    e.rep("“Es lo que es”", "“Así son las cosas”")
    e.rep("<li>Sabe que su observación determina</li>", "<li>Sabe que su mirada da forma a lo que vive</li>")
    e.rep("“Yo creo lo que observo”", "“Lo que miro crece”")
    e.rep("<li>Crea realidades complejas con facilidad</li>", "<li>Sostiene situaciones complejas con soltura</li>")
    e.rep("“Observo luego existe”", "“Observo, luego habito”")
    e.rep("<li>Su sola presencia altera realidades</li>", "<li>Su sola presencia cambia el clima de un lugar</li>")
    e.rep("<li>Ignora todas las demás posibilidades</li>",
          "<li>Deja las demás en segundo plano, sin pelear con ellas</li>")
    e.tramo("<p>La creación requiere observación coherente y sostenida.</p>",
            "<h3>LABORATORIO CUÁNTICO: EXPERIMENTO #2</h3>",
            """<p>La creación pide una mirada que vuelva una y otra vez.<br>
Lo nuevo tarda semanas, a veces meses, en volverse “realidad normal”,<br>
y cada regreso cuenta.</p>

<div class="spacer"></div>

<h4>Paso 4: Cuidado de lo que Empieza</h4>

<p>Lo recién nacido es frágil hasta que echa raíz.</p>

<ul>
  <li>Dale tiempo antes de juzgarlo</li>
  <li>Escucha la duda sin dejar que decida por ti</li>
  <li>Vuelve a él con constancia</li>
  <li>Celebra cada señal de que algo cambia</li>
</ul>

<div class="spacer"></div>

""")
    e.tramo("  <p><strong>“Creación de un Objeto Cuántico”</strong></p>",
            "<h3>LA PARADOJA DEL OBSERVADOR CREADOR</h3>",
            """  <p><strong>“Lo que Aparece Cuando lo Miras”</strong></p>
</div>

<ol>
  <li><strong>ELIGE</strong> algo simple que no sueles notar<br>
      (una pluma azul, una moneda, una mariposa)</li>

  <li><strong>OBSERVA</strong> su imagen con calma,<br>
      como si ya estuviera cerca</li>

  <li><strong>SOSTÉN</strong> esa imagen un minuto<br>
      – Sin forzar<br>
      – Solo mirando</li>

  <li><strong>SUELTA</strong> y olvida<br>
      – No necesitas hacer nada más</li>

  <li><strong>DOCUMENTA</strong> cuando aparezca<br>
      – Hora<br>
      – Circunstancias<br>
      – Tu estado en ese momento</li>
</ol>

<p>Lo más probable es que aparezca, y más de una vez.<br>
No porque lo hayas fabricado:<br>
estaba ahí y no lo veías.</p>

<p><span class="highlight"><strong>Eso hace tu atención con todo lo que eliges mirar.<br>
Lo saca de la sombra.</strong></span></p>

<div class="spacer"></div>

""")
    e.rep("<h3>CÓDIGOS DE ACTIVACIÓN DEL OBSERVADOR CREADOR</h3>", "<h3>PARA RECORDAR</h3>")
    e.rep("<p>Donde pongo mi atención, la realidad responde.</p>", "<p>Donde pongo mi atención, mi vida crece.</p>")
    e.rep("<p>No veo lo que es, veo lo que elijo que sea.</p>", "<p>Veo lo que es, y elijo desde dónde mirarlo.</p>")
    e.rep("<p>Con cada parpadeo, reseteo la realidad.</p>", "<p>Con cada parpadeo, la mirada vuelve a empezar.</p>")
    e.tramo("<h3>LA OBSERVACIÓN MULTIDIMENSIONAL</h3>", "<h3>EL ARTE DE LA NO-OBSERVACIÓN</h3>",
            """<h3>LAS PROFUNDIDADES DE LA MIRADA</h3>

<p>Como Arquitecto Cuántico, aprenderás a mirar en profundidad:</p>

<h4>Primera – Lo que Está</h4>
<p>Lo que todos ven y llaman “real”.</p>

<h4>Segunda – El Tiempo</h4>
<p>De dónde viene lo que pasa y hacia dónde va.</p>

<h4>Tercera – Lo Posible</h4>
<p>Más de una versión de lo que puede venir.</p>

<h4>Cuarta – Los Patrones</h4>
<p>Las formas que se repiten en tu vida.</p>

<h4>Quinta – La Consciencia Pura</h4>
<p>Ver desde el punto donde toda observación se origina.</p>

<p>Cada profundidad agrega una capa a lo que ves, y ninguna borra a la anterior.</p>

<div class="spacer"></div>

""")
    e.tramo("<p>Tan poderoso como observar para crear<br>", "<h3>NAVEGANDO EL CAMPO DE OBSERVACIÓN COLECTIVA</h3>",
            """<p>Tan importante como mirar<br>
es <span class="highlight"><strong>saber cuándo dejar de dar vueltas</strong></span>.</p>

<p>¿Tienes un problema persistente?<br>
Haz lo que esté en tus manos y después <strong>deja de rumiarlo</strong>.<br>
No se trata de negarlo ni de esconderlo,<br>
sino de no darle toda tu atención.<br>
Lo que se mira sin descanso ocupa la vida entera;<br>
lo que se atiende y luego se suelta encuentra su tamaño.</p>

<p>¿Una enfermedad?<br>
Cuídala junto a tu equipo de salud,<br>
y no dejes que ocupe toda la mirada.<br>
Mira también lo que en ti sigue sano:<br>
el aliento, los vínculos, lo que todavía disfrutas.<br>
Esa mirada no reemplaza ningún tratamiento: lo acompaña.</p>

<p>¿Una limitación?<br>
No la pelees de frente.<br>
Pon tu atención, además, en lo que sí está disponible,<br>
hasta que deje de ser lo único que ves.</p>

<div class="quote-block">
  <p><em>La no-observación consciente no borra nada:<br>
  le devuelve a cada cosa su tamaño.</em></p>
</div>

<div class="spacer"></div>

""")
    e.rep("Billones de observadores creando simultáneamente.</p>", "Miles de millones de observadores mirando a la vez.</p>")
    e.tramo("<h4>3. Crea burbujas de realidad soberana</h4>", "<h3>EL OBSERVADOR SE OBSERVA CREANDO</h3>",
            """<h4>3. Cuida espacios propios</h4>
<ul>
  <li>Lugares y tiempos donde tu mirada descansa</li>
  <li>Momentos a salvo del ruido</li>
  <li>Un mundo personal que no se cierra al común</li>
</ul>

<h4>4. Aprende a mirar con otros</h4>
<ul>
  <li>Cuando varias personas miran en la misma dirección</li>
  <li>Lo que parecía imposible empieza a volverse posible</li>
</ul>

<div class="spacer"></div>

""")
    e.rep("<p>Es el loop recursivo de consciencia donde:</p>", "<p>Es el bucle recursivo de consciencia donde:</p>")
    e.rep("<p>En este loop infinito,<br>", "<p>En este bucle infinito,<br>")
    e.rep("<h3>PROTOCOLO DE ACTIVACIÓN: LOS PRÓXIMOS 7 DÍAS</h3>", "<h3>PRÁCTICA: LOS PRÓXIMOS 7 DÍAS</h3>")
    e.rep("una cualidad en otros hasta que aparezca</li>", "una cualidad en otros y nota cuántas veces aparece</li>")
    e.rep("<li><strong>Día 4:</strong> Crea algo pequeño solo con observación (Experimento #2)</li>",
          "<li><strong>Día 4:</strong> Haz el Experimento #2</li>")
    e.rep("<li><strong>Día 5:</strong> Practica la no-observación de un problema</li>",
          "<li><strong>Día 5:</strong> Atiende un problema y después deja de rumiarlo</li>")
    e.rep("“Mi observación lo está definiendo.”", "“Lo que miro toma forma en mi vida.”")
    e.rep("“Estoy arquitecturando realidad.”", "“Estoy diseñando cómo vivo.”")
    e.rep("<p><em>[Fin del Nodo 2: El Observador Como Creador]</em></p>", FIRMA)
    # Restos de producción: faltaban el cierre de <main>, el pie y el cierre del documento.
    e.rep("<div class=\"spacer\"></div>\n<!-- NAVEGACIÓN -->",
          "<div class=\"spacer\"></div>\n\n      </main>\n\n<!-- NAVEGACIÓN -->")
    e.s = e.s.rstrip() + ("\n\n      <footer class=\"portal-footer\">\n"
                          "        Nodo 2 · El Arquitecto Cuántico · Trinity Quantum\n"
                          "      </footer>\n\n    </div>\n  </div>\n</body>\n</html>\n")


# ------------------------------------------------------------------ NODO 3
def nodo_03(e):
    e.comunes()
    e.rep("Viviendo en Múltiples Mundos Simultáneamente</h2>", "Las Muchas Versiones que Llevas Dentro</h2>")
    e.rep("<p>No es poesía.<br>\n        No es metáfora.<br>\n        Es la naturaleza fundamental de tu existencia cuántica.</p>",
          "<p>La imagen es exacta:<br>\n        llevas dentro más versiones de ti<br>\n        de las que este día deja ver.</p>")
    e.rep("<p>Todos existen.<br>\n        Todos son reales.<br>\n        Todos son tú.<br>",
          "<p>Todos caben en ti.<br>\n        Todos son tú.<br>")
    e.rep("<p>La pregunta no es si estas realidades existen.<br>\n        La pregunta es: <strong>¿puedes navegar conscientemente entre ellas?</strong></p>",
          "<p>La pregunta no es si estas versiones existen.<br>\n        Es si <strong>puedes moverte entre ellas con consciencia</strong>.</p>")
    e.tramo("<h3>LA CIENCIA DE LA SUPERPOSICIÓN</h3>", "<p>¿Has experimentado alguno de estos?</p>",
            """<h3>LA IMAGEN DE LA SUPERPOSICIÓN</h3>

        <h4>El Gato de Schrödinger Eres Tú</h4>

        <p>En el experimento mental que Schrödinger imaginó en 1935,<br>
        para mostrar lo absurdo de llevar la física de lo diminuto a un animal,<br>
        el gato estaría vivo Y muerto hasta que alguien abra la caja.</p>

        <p>Lo que en un gato es absurdo,<br>
        en tu vida interior es cotidiano.</p>

        <p><span class="highlight"><strong>Ese es el secreto que no te contaron:</strong></span><br>
        el colapso es opcional.<br>
        No todo necesita decidirse ya.</p>

        <p>Los Arquitectos Cuánticos aprenden a:</p>

        <ul>
          <li>Sostener abiertas varias posibilidades, a conciencia</li>
          <li>Habitar estados distintos sin partirse</li>
          <li>Decidir cuando hace falta, no antes</li>
          <li>Volver a abrir lo que se cerró de más</li>
        </ul>

        <h4>Tú, Entero</h4>

        <p>No eres una de tus versiones ni su suma.<br>
        <strong>Eres la consciencia que las recorre y las reúne.</strong></p>

        <div class="spacer"></div>

        <h3>LAS SEÑALES DE LA SUPERPOSICIÓN</h3>

        """)
    e.tramo("<ul>\n          <li><strong>Déjà vu recurrente</strong>", "<h3>NAVEGANDO LAS CAPAS DE REALIDAD</h3>",
            """<ul>
          <li><strong>Déjà vu recurrente</strong>: la memoria que, por un instante, se reconoce a sí misma</li>
          <li><strong>Sueños vívidos de otras vidas</strong>: la imaginación mostrándote lo que también podrías ser</li>
          <li><strong>Decisiones que se sienten “ya tomadas”</strong>: una parte de ti eligió antes de que lo supieras</li>
          <li><strong>Recuerdos de cosas que “no pasaron”</strong>: la memoria guarda también lo que deseaste o temiste</li>
          <li><strong>Sentir que eres “más grande” que tu vida actual</strong>: lo eres</li>
          <li><strong>Nostalgia por lugares nunca visitados</strong>: el anhelo tiene su propia geografía</li>
          <li><strong>Conocer a alguien “de antes” sin haberlo visto</strong>: hay encuentros que despiertan algo que ya estaba en ti</li>
        </ul>

        <p>No son fallas.<br>
        Son <span class="highlight"><strong>señales</strong></span> de que eres más amplio que tu biografía.</p>

        <p><em>Si alguna se vuelve muy frecuente, te inquieta o confunde lo vivido con lo imaginado, consúltalo sin esperar.</em></p>

        <div class="spacer"></div>

        """)
    for hz in ("7.83 Hz (Resonancia Schumann)", "40–80 Hz (Gamma alta)", "432 Hz (Resonancia universal)",
               "∞ Hz (Más allá de medición)"):
        e.rep(f"\n\n        <p><em>Frecuencia: {hz}</em></p>", "")
    e.rep("<li>Accesibles en meditación profunda</li>\n          <li>Visitables en sueños lúcidos</li>\n          <li>Influenciables retroactivamente</li>",
          "<li>Los caminos que no tomaste</li>\n          <li>Visitables en la memoria y en la imaginación, a veces en los sueños</li>\n          <li>Lo que pasó queda; lo que entiendes de ello puede cambiar</li>")
    e.rep("<li>Infinitamente maleables</li>\n          <li>Tu playground creativo</li>",
          "<li>Abiertas a lo que hagas</li>\n          <li>Tu taller creativo</li>")
    e.tramo("<p><strong>“Contacto con Tu Yo Paralelo”</strong></p>", "<h3>EL ARTE DE LA SUPERPOSICIÓN CONSCIENTE</h3>",
            """<p><strong>“Diálogo con una Versión Posible de Ti”</strong></p>
        </div>

        <p><strong>Esta noche, antes de dormir:</strong></p>
        <ol>
          <li><strong>ESTABLECE LA INTENCIÓN</strong><br>
          “Voy a conversar con la versión de mí que vive [describe la vida que deseas explorar]”</li>

          <li><strong>CREA EL PUENTE</strong>
            <ul>
              <li>Imagina un espejo frente a ti</li>
              <li>En lugar de tu reflejo, aparece esa versión tuya</li>
              <li>Ya vive lo que deseas</li>
            </ul>
          </li>

          <li><strong>EL CONTACTO</strong>
            <ul>
              <li>Toca el espejo con tu mano derecha</li>
              <li>Tu otra versión toca desde el otro lado</li>
              <li>En el punto de contacto, escúchala</li>
            </ul>
          </li>

          <li><strong>LAS PREGUNTAS</strong>
            <ul>
              <li>¿Qué decisión tomaste diferente?</li>
              <li>¿Qué sabes que yo necesito saber?</li>
              <li>¿Qué cualidad tienes que puedo practicar?</li>
              <li>¿Cuál es el siguiente paso desde tu perspectiva?</li>
            </ul>
          </li>

          <li><strong>INTEGRACIÓN</strong>
            <ul>
              <li>No reemplazas, SUMAS</li>
              <li>Lo que escuches viene de una parte de ti que todavía no tenía voz</li>
              <li>Al despertar, anota una sola cosa que puedas hacer hoy desde ahí</li>
            </ul>
          </li>
        </ol>

        <div class="spacer"></div>

        """)
    e.rep("<h4>Técnica 1: El Desdoblamiento Diario</h4>", "<h4>Técnica 1: El Día Abierto</h4>")
    e.rep("<p><em>Resultado: Flexibilidad cuántica extrema</em></p>", "<p><em>Resultado: un día más flexible</em></p>")
    e.tramo("<p>En cada decisión importante:</p>", "<h4>Técnica 3: El Yo Holográfico</h4>",
            """<p>Antes de una decisión importante:</p>

        <ul>
          <li>Imagina cada opción vivida durante un día entero</li>
          <li>Habítala por dentro, sin actuarla todavía</li>
          <li>Nota cuál te deja más vivo y cuál más estrecho</li>
          <li>Después, elige</li>
        </ul>

        <p><em>Resultado: elegir con todo tu ser, y arrepentirte menos</em></p>

        """)
    e.rep("“Mientras más realidades habitas simultáneamente,<br>", "“Mientras más versiones de ti reconoces,<br>")
    e.rep("“Si estoy en muchos lugares, estoy diluido.”", "“Si soy muchos, estoy diluido.”")
    e.rep("<p>No es multitasking.<br>\n        Es multipresencia.<br>",
          "<p>No es hacer muchas cosas a la vez.<br>\n        Es estar entero en cada una.<br>")
    e.tramo("<h4>Fragmentación Cuántica</h4>", "<h4>Parálisis de Posibilidad</h4>",
            """<h4>Fragmentación</h4>

        <ul>
          <li>Perderse entre versiones</li>
          <li>No distinguir con claridad lo imaginado de lo vivido</li>
          <li>No poder decidir cuando hace falta</li>
        </ul>

        <p><em>Antídoto: volver al cuerpo y al día de hoy</em></p>

        <h4>Confusión</h4>

        <ul>
          <li>Recuerdos mezclados</li>
          <li>Una identidad que se vuelve difusa</li>
          <li>Vínculos confusos</li>
        </ul>

        <p><em>Antídoto: límites claros</em></p>

        """)
    e.rep("<p><em>Antídoto: Práctica de colapso decisivo</em></p>",
          "<p><em>Antídoto: Práctica de colapso decisivo</em></p>\n\n"
          "        <p>Si alguna de estas señales aparece y no se va, deja estas prácticas y consúltalo con un profesional.<br>\n"
          "        La imaginación está para ensanchar la vida, no para quitarle el suelo.</p>")
    e.rep("<h3>CÓDIGOS DE ACTIVACIÓN MULTIDIMENSIONAL</h3>", "<h3>PARA RECORDAR</h3>")
    e.rep("Existo en infinitas realidades AHORA.<br>", "Llevo infinitas posibilidades AHORA.<br>")
    e.rep("Cada latido sincroniza mis realidades.</p>", "Cada latido reúne mis versiones.</p>")
    e.rep("la sinfonía de mis existencias paralelas.”</p>", "la sinfonía de mis muchas versiones.”</p>")
    e.tramo("<h3>NAVEGACIÓN PRÁCTICA ENTRE REALIDADES</h3>", "<h3>LA MAESTRÍA DE LA SUPERPOSICIÓN</h3>",
            """<h3>NAVEGACIÓN PRÁCTICA ENTRE VERSIONES</h3>

        <h4>El Espejo de la Mañana</h4>

        <p>Cada vez que te mires al espejo:</p>

        <ul>
          <li>Unos segundos: tu yo de hoy</li>
          <li>Después, pregúntale a esa cara qué versión de ti quiere salir</li>
          <li>Nota los cambios sutiles en la expresión</li>
          <li>Elige una cualidad para llevar contigo</li>
        </ul>

        <h4>Método de las Puertas</h4>

        <ul>
          <li>Cada puerta física puede ser un umbral</li>
          <li>Antes de cruzarla, elige la actitud con que entras:<br>
            “Al cruzar, entro como quien…”</li>
          <li>Cruza conscientemente</li>
          <li>Nota los cambios sutiles</li>
          <li>Has cambiado de capa de realidad: la que se vive por dentro</li>
        </ul>

        <div class="spacer"></div>

        """)
    e.rep("<p>Puedes contactar con tus otros yoes.</p>", "<p>Puedes dialogar con tus otros yoes.</p>")
    e.rep("<p>Puedes traer habilidades y conocimientos de otras versiones.</p>", "<p>Puedes traer al día lo que cada versión sabe.</p>")
    e.rep("<p>Puedes crear nuevas versiones y realidades a voluntad.</p>", "<p>Puedes dar forma a versiones nuevas de ti.</p>")
    e.rep("<p>Vives permanentemente en superposición consciente.</p>", "<p>Vives con tus muchas versiones sin perder el centro.</p>")
    e.rep("<strong>Nunca estás solo:</strong> tienes infinitos yoes.", "<strong>Nunca estás solo:</strong> llevas contigo a todos los que fuiste.")
    e.rep("<strong>Nunca estás limitado:</strong> puedes acceder a cualquier habilidad.",
          "<strong>Nunca estás limitado:</strong> siempre queda algo por aprender.")
    e.tramo("<li><strong>Día 1:</strong> Observa los “glitches”", "        </ul>\n\n        <div class=\"spacer\"></div>\n\n        <h3>LA GRADUACIÓN CUÁNTICA</h3>",
            """<li><strong>Día 1:</strong> Observa las señales: los momentos en que te sientes más amplio que tu vida</li>
          <li><strong>Día 2:</strong> Practica el espejo de la mañana</li>
          <li><strong>Día 3:</strong> Deja abierto tu día hasta el mediodía</li>
          <li><strong>Día 4:</strong> Haz el diálogo con una versión posible de ti</li>
          <li><strong>Día 5:</strong> Practica en algo pequeño una cualidad de esa versión</li>
          <li><strong>Día 6:</strong> Cruza tres puertas como umbrales</li>
          <li><strong>Día 7:</strong> Vive el día notando qué versión de ti está presente en cada momento</li>
""")
    e.rep("<p>Ya no vivirás EN una realidad.<br>\n        Vivirás ENTRE realidades.<br>",
          "<p>Ya no vivirás EN una sola versión.<br>\n        Vivirás ENTRE tus versiones.<br>")
    e.rep("no eliges una realidad sobre otra.<br>\n          Las habitas todas,<br>\n          las navegas todas,<br>\n          las eres todas.<br>",
          "no eliges un yo sobre otro.<br>\n          Los habitas todos,<br>\n          los navegas todos,<br>\n          los eres todos.<br>")
    e.rep("<p><em>[Fin del Nodo 3: Realidades Superpuestas]</em></p>", FIRMA)
    # Restos de producción: navegación duplicada al pie y documento sin cerrar.
    e.tramo("      <!-- NAVEGACIÓN SUPERIOR DEL NODO -->", "      <!-- NAVEGACIÓN INFERIOR COMPLETA -->", "")
    e.s = e.s.rstrip() + "\n\n    </div>\n  </div>\n</body>\n</html>\n"


# ------------------------------------------------------------------ NODO 4
def nodo_04(e):
    e.comunes()
    e.rep("Esculpiendo el Futuro desde el Campo de Potencial Infinito</h2>", "Cultivando el Futuro sin Forzarlo</h2>")
    e.rep("        esperando que un Arquitecto Cuántico<br>\n        las esculpa hacia la existencia.</p>",
          "        esperando a quien sepa cuidarlas.</p>")
    e.rep("<span class=\"highlight\"><strong>Seducir probabilidades.</strong></span></p>",
          "<span class=\"highlight\"><strong>Cultivarlo.</strong></span></p>")
    e.tramo("<h4>La Curva de Probabilidad Personal</h4>", "<h4>Ecuación Sagrada #4:</h4>",
            """<p>Tu futuro tiene zonas:</p>

        <ul>
          <li><strong>Lo probable:</strong> más de lo mismo</li>
          <li><strong>Lo posible:</strong> pide esfuerzo o cambio</li>
          <li><strong>Lo improbable:</strong> pide un salto</li>
          <li><strong>Lo que hoy parece imposible:</strong> pide tiempo, maestría, a veces un milagro</li>
        </ul>

        <p><span class="highlight"><strong>El secreto del Arquitecto:</strong></span><br>
        Estas zonas no son fijas.<br>
        Sus fronteras se mueven,<br>
        y lo impensable de hoy<br>
        puede volverse alcanzable, paso a paso.</p>

        """)
    e.tramo("<h4>Ecuación Sagrada #4:</h4>", "<div class=\"spacer\"></div>\n\n        <h3>LOS TIPOS DE PROBABILIDAD</h3>",
            """<h4>Lo que Acerca un Futuro</h4>

        <p>Lo acerca una intención clara,<br>
        un corazón y una mente que van en la misma dirección,<br>
        y su afinidad con quien eres.<br>
        Lo aleja la duda que paraliza<br>
        y el tiempo vivido como enemigo.</p>

        """)
    e.rep("<h4>Probabilidades Densas (85–100%)</h4>", "<h4>Probabilidades Densas</h4>")
    e.rep("<h4>Probabilidades Fluidas (40–84%)</h4>", "<h4>Probabilidades Fluidas</h4>")
    e.rep("<h4>Probabilidades Sutiles (10–39%)</h4>", "<h4>Probabilidades Sutiles</h4>")
    e.rep("<h4>Probabilidades Etéricas (0.1–9%)</h4>", "<h4>Probabilidades Etéricas</h4>")
    e.rep("• Tu zona de máximo poder<br>", "• Tu zona de mayor influencia<br>")
    e.rep("<strong>Tu trabajo:</strong> Dirigir su flujo conscientemente",
          "<strong>Tu trabajo:</strong> Acompañar su flujo conscientemente")
    e.rep("• Ejemplos: Milagros, sanaciones espontáneas, saltos evolutivos<br>",
          "• Ejemplos: Encuentros que cambian una vida, giros que nadie esperaba<br>")
    e.rep("<strong>Tu trabajo:</strong> Crear puentes cuánticos hacia ellas",
          "<strong>Tu trabajo:</strong> Dejarles la puerta abierta")
    e.tramo("<h4>Probabilidades Negativas (&lt;0%)</h4>",
            "<div class=\"spacer\"></div>\n\n        <h3>EL JARDÍN DE PROBABILIDADES</h3>", "")
    e.rep("<li>Podas dudas y miedos</li>", "<li>Quitas la maleza de la prisa</li>")
    e.rep("<li>Cosechas realidades</li>\n        </ul>",
          "<li>Cosechas lo que maduró</li>\n        </ul>\n\n"
          "        <p>Y sabes esperar:<br>\n        ningún jardinero hace crecer una planta tirando de ella.</p>")
    e.tramo("<p><strong>“Elevación de Probabilidad Imposible”</strong></p>",
            "<h3>TÉCNICAS DE MANIPULACIÓN DE PROBABILIDAD</h3>",
            """<p><strong>“Un Puente Hacia lo Improbable”</strong></p>
        </div>

        <ol>
          <li><strong>IDENTIFICA</strong> algo que deseas pero que hoy parece casi imposible<br>
              (Que dependa, al menos en parte, de ti: no de la decisión de otra persona)</li>

          <li><strong>MAPEA LA PROBABILIDAD ACTUAL</strong><br>
              – ¿Por qué parece imposible?<br>
              – ¿Qué leyes/reglas/creencias lo hacen imposible?<br>
              – ¿Quién dice que es imposible?</li>

          <li><strong>ENCUENTRA LA GRIETA CUÁNTICA</strong><br>
              – Busca UN ejemplo donde algo similar sucedió<br>
              – Encuentra la excepción a la regla<br>
              – Identifica el precedente cuántico</li>

          <li><strong>CONSTRUYE EL PUENTE</strong><br>
              Cada día, durante siete días, da un paso pequeño en esa dirección<br>
              (una llamada, una búsqueda, una conversación)<br>
              y suelta el resultado.<br>
              No midas cuánto falta: nota cuánto se movió.</li>

          <li><strong>DOCUMENTA EL CAMBIO</strong><br>
              – Nota cuándo lo “imposible” empieza a sentirse posible<br>
              – Observa lo que aparece en el camino<br>
              – Registra el día en que algo cedió</li>
        </ol>

        <div class="spacer"></div>

        """)
    e.tramo("<h3>TÉCNICAS DE MANIPULACIÓN DE PROBABILIDAD</h3>", "<h3>PARADOJA CUÁNTICA #4</h3>",
            """<h3>TÉCNICAS PARA CULTIVAR LO PROBABLE</h3>

        <h4>1. La Espiral de Probabilidad Creciente</h4>
        <p>
          – Comienza con algo casi seguro<br>
          – Cúmplelo<br>
          – Apóyate en ese logro para algo un poco más difícil<br>
          – Cada paso cumplido vuelve más alcanzable el siguiente
        </p>

        <h4>2. El Colapso en Cascada</h4>
        <p>
          – Identifica el paso clave, el que mueve a muchos otros<br>
          – Como fichas de dominó<br>
          – Pon ahí tu atención principal
        </p>

        <h4>3. La Transferencia de Atención</h4>
        <p>
          – Retira atención de lo que temes<br>
          – Dásela a lo que quieres<br>
          – Lo que dejas de alimentar pierde peso<br>
          – Tu atención es finita: lo que le quitas al miedo queda libre para el deseo
        </p>

        <div class="spacer"></div>

        """)
    e.rep("        de que dominas la probabilidad<br>\n        incluso cuando no lo sabes.</p>",
          "        de que lo improbable te habita,<br>\n        incluso cuando no lo sabes.</p>")
    e.rep("<h3>EL CAMPO MORFOGENÉTICO DE PROBABILIDAD</h3>", "<h3>EL CAMPO DE PROBABILIDAD</h3>")
    e.rep("        Rupert Sheldrake lo llamó campo morfogenético.<br>\n",
          "        Las tradiciones le dieron muchos nombres.<br>\n")
    e.tramo("<p>Cuando accedes a este campo:</p>", "        <div class=\"spacer\"></div>\n        <h3>CÓDIGOS DE ACTIVACIÓN PROBABILÍSTICA</h3>",
            """<p>Cuando lo sientes:</p>

        <ul>
          <li>Ves más posibilidades de las que veías</li>
          <li>Dejas de mover piezas a la fuerza</li>
          <li>Descubres caminos que no estaban en el mapa</li>
          <li>Sueltas futuros que ya no quieres alimentar</li>
          <li>Notas vínculos entre cosas que parecían lejanas</li>
        </ul>

""")
    e.tramo("<h3>CÓDIGOS DE ACTIVACIÓN PROBABILÍSTICA</h3>",
            "<div class=\"quote-block\">\n          <p><em>\n            “Soy el Arquitecto de Probabilidades.<br>",
            "<h3>PARA RECORDAR</h3>\n\n        ")
    e.rep("            Lo imposible es mi especialidad.<br>\n            Lo improbable es mi territorio.<br>\n            Lo milagroso es mi estado natural.<br><br>",
          "            Lo imposible no me espanta.<br>\n            Lo improbable es mi territorio.<br>\n            Lo milagroso me rodea a diario.<br><br>")
    e.rep("Selecciono, cultivo y manifiesto<br>", "Selecciono, cultivo y dejo crecer<br>")
    e.rep("            Mi presencia altera las probabilidades.<br>\n            Mi consciencia las reorganiza.<br>\n            Mi amor las magnetiza hacia mí.<br><br>",
          "            Mi presencia cambia lo que toco.<br>\n            Mi consciencia ordena lo que miro.<br>\n            Mi amor atrae lo que se le parece.<br><br>")
    e.rep("<li><strong>Surfa las olas de probabilidad</strong><br>", "<li><strong>Surfea las olas de probabilidad</strong><br>")
    e.tramo("<h4>El Péndulo de Probabilidad</h4>", "<h4>El Dado Cuántico</h4>", "")
    e.rep("– Manténlo en superposición<br>", "– Mantenlo en superposición<br>")
    e.rep("          – Esa tiene momentum cuántico actual<br>\n          – Puedes elegir potenciarla o cambiarla",
          "          – Nota qué sientes al leerla: alivio o desilusión<br>\n          – Eso que sientes es información<br>\n          – Puedes elegirla o dejarla")
    e.rep("<li>Actúa como si ya tuviera 1% de probabilidad</li>", "<li>Actúa como si fuera apenas posible</li>")
    e.rep("<li>Mantén la visión sin importar qué</li>", "<li>Mantén la visión, y deja que cambie de forma en el camino</li>")
    e.rep("<li>Volar (0% → 100%)</li>\n          <li>Internet (0% → 100%)</li>\n          <li>Derechos humanos universales (0% → en proceso)</li>\n        </ul>",
          "<li>Volar</li>\n          <li>Internet</li>\n          <li>Los derechos humanos universales, todavía en camino</li>\n        </ul>\n\n"
          "        <p>Ninguno lo hizo una sola persona, ni en siete días.</p>")
    e.rep("<h3>PROTOCOLO DE DOMINIO: 7 DÍAS</h3>", "<h3>PRÁCTICA: LOS PRÓXIMOS 7 DÍAS</h3>")
    e.rep("<strong>Día 3:</strong> Practica mover probabilidad entre futuros",
          "<strong>Día 3:</strong> Mueve tu atención del miedo al deseo")
    e.rep("<strong>Día 4:</strong> Prueba el préstamo de probabilidad",
          "<strong>Día 4:</strong> Da el primer paso pequeño hacia lo improbable, y suelta el resultado")
    e.rep("<strong>Día 5:</strong> Crea una probabilidad completamente nueva",
          "<strong>Día 5:</strong> Imagina un camino que no estaba en el mapa")
    e.rep("<strong>Día 6:</strong> Navega una tormenta de probabilidades",
          "<strong>Día 6:</strong> Ante una decisión agitada, busca el ojo de la tormenta antes de elegir")
    e.rep("<strong>Día 7:</strong> Vive como Maestro de Probabilidad",
          "<strong>Día 7:</strong> Vive el día sin forzar nada: cultiva, y deja crecer")
    e.rep("Cuando dominas el Arte de la Probabilidad:", "Cuando practicas el Arte de la Probabilidad:")
    e.rep("– Esculpes lo que pasará.<br><br>", "– Cultivas lo que puede pasar.<br><br>")
    e.rep("          – Eres el arquitecto de las probabilidades<br>\n            que se convertirán en circunstancias.",
          "          – Eres parte de lo que las mueve.")
    e.rep("Y en ese dominio, descubres el secreto final:", "Y en esa práctica, descubres el secreto final:")
    e.rep("<p><em>[Fin del Nodo 4: El Arte de la Probabilidad]</em></p>", FIRMA)
    # La puerta hacia «El Peso» queda anotada: se coloca al publicar el Libro 8.
    e.rep("        <div class=\"spacer\"></div>\n        <!-- Navegación inferior -->",
          "        <!-- Puerta anotada: hacia El Peso (Arquitectura del Destino, Libro 8), al publicarse. -->\n\n"
          "        <div class=\"spacer\"></div>\n\n      </main>\n\n        <!-- Navegación inferior -->")
    e.s = e.s.rstrip() + ("\n\n      <footer class=\"portal-footer\">\n"
                          "        Nodo 4 · El Arquitecto Cuántico · Trinity Quantum\n"
                          "      </footer>\n\n    </div>\n  </div>\n</body>\n</html>\n")


# ------------------------------------------------------------------ NODO 5
def nodo_05(e):
    e.comunes()
    e.rep("Tu Plantilla Energética Como Arquitectura de Realidad</h2>", "El Clima que Llevas Contigo</h2>")
    e.tramo("<p>Rupert Sheldrake demostró que existe un campo invisible", "<p>Tu campo morfogenético personal es:</p>",
            """<p>La biología de comienzos del siglo XX llamó campos morfogenéticos<br>
        a lo que organiza la forma de un embrión,<br>
        cuando nadie sabía todavía explicarla.<br>
        Rupert Sheldrake fue más allá y propuso una hipótesis<br>
        que la ciencia aún discute:<br>
        la naturaleza tendría memoria,<br>
        y las formas y los hábitos se transmitirían por resonancia.</p>

        <p>Como imagen, dice algo cierto:<br>
        <span class="highlight"><strong>Tú no solo TIENES un campo.</strong></span><br>
        <span class="highlight"><strong>Tú ERES un campo viviente:</strong></span><br>
        un modo de estar que se repite,<br>
        una atmósfera que llevas a cada lugar.</p>

        <p>Y más revolucionario aún:<br>
        <span class="highlight"><strong>Puedes rediseñarlo conscientemente.</strong></span></p>

        """)
    e.rep("<li>La plantilla invisible de tu realidad</li>\n          <li>El molde energético de tus experiencias</li>\n          <li>El blueprint cuántico de tu vida</li>\n          <li>El código fuente de tu existencia</li>",
          "<li>La plantilla invisible de tus días</li>\n          <li>El molde de tus costumbres</li>\n          <li>El plano de tu manera de vivir</li>")
    e.rep("<p>Hoy aprendes a ser el programador\n        de tu propio código de realidad.</p>",
          "<p>Hoy aprendes a ser el arquitecto\n        de tu propio clima.</p>")
    e.tramo("<h3>ANATOMÍA DE TU CAMPO MORFOGENÉTICO</h3>", "<h3>LECTURA DE TU CAMPO ACTUAL</h3>",
            """<h3>ANATOMÍA DE TU CAMPO</h3>

        <h4>Capa 1: El Campo Corporal</h4>
        <ul>
          <li>Guarda tus posturas y tus hábitos</li>
          <li>Contiene memorias somáticas</li>
          <li>Es la base de todo lo demás</li>
        </ul>

        <h4>Capa 2: El Campo Emocional</h4>
        <ul>
          <li>Almacena patrones emocionales</li>
          <li>Crea el “clima” emocional alrededor tuyo</li>
          <li>Contagia a quienes te rodean, y se contagia de ellos</li>
        </ul>

        <h4>Capa 3: El Campo Mental</h4>
        <ul>
          <li>Estructura patrones de pensamiento</li>
          <li>Decide qué información notas</li>
        </ul>

        <h4>Capa 4: El Campo de los Vínculos</h4>
        <ul>
          <li>Lo que haces se encadena con lo que hacen otros</li>
          <li>Tus elecciones repetidas trazan una dirección</li>
          <li>Visto desde lejos, eso parece “destino”</li>
        </ul>

        <h4>Capa 5: El Campo Cuántico</h4>
        <ul>
          <li>Conecta con campos de otros</li>
          <li>Accede al campo unificado</li>
        </ul>

        <div class="spacer"></div>

        """)
    e.rep("          <li>Salud vibrante</li>\n", "")
    e.rep("<h4>Señales de un Campo Distorsionado:</h4>\n        <ul>\n          <li>Patrones repetitivos negativos</li>\n          <li>Mala suerte crónica</li>\n          <li>Problemas de salud recurrentes</li>\n",
          "<h4>Señales de un Campo Estrecho:</h4>\n        <ul>\n          <li>Patrones que se repiten aunque no los quieras</li>\n")
    e.rep("<h4>Señales de un Campo Fragmentado:</h4>\n        <ul>\n          <li>Realidades contradictorias</li>\n          <li>Identidad difusa</li>\n          <li>Energía dispersa</li>\n          <li>Manifestaciones erráticas</li>\n          <li>Relaciones ambivalentes</li>\n          <li>Sensación de “no estar completo”</li>\n        </ul>",
          "<h4>Señales de un Campo Disperso:</h4>\n        <ul>\n          <li>Energía dispersa</li>\n          <li>Prioridades que se contradicen</li>\n          <li>Vínculos ambivalentes</li>\n          <li>Sensación de “no estar completo”</li>\n        </ul>\n\n"
          "        <p>Ningún campo vive siempre en uno de estos climas.<br>\n        Y ninguna enfermedad ni desgracia es prueba de que el tuyo esté mal.</p>")
    e.tramo("<p><strong>“Escaneo y Mapeo de Tu Campo”</strong></p>", "<h3>REDISEÑO DE TU CAMPO MORFOGENÉTICO</h3>",
            """<p><strong>“El Mapa de Tu Campo”</strong></p>

        <p>Necesitarás: papel y lápiz.</p>

        <ol>
          <li><strong>PREPARACIÓN</strong><br>
              – Siéntate o párate en un espacio tranquilo<br>
              – Respira profundo 7 veces
          </li>

          <li><strong>RECORRIDO POR CAPAS</strong><br>
              Pregúntate:<br>
              – El cuerpo: ¿tenso o suelto?<br>
              – El ánimo: ¿cálido o frío?<br>
              – La mente: ¿clara o nublada?<br>
              – Los vínculos: ¿abiertos o cerrados?<br>
              – Lo que te une con todo: ¿cerca o lejos?
          </li>

          <li><strong>IDENTIFICA LO QUE PIDE CUIDADO</strong><br>
              Busca:<br>
              – Huecos: zonas de tu vida desatendidas<br>
              – Densidades: lo que pesa<br>
              – Turbulencias: conflictos activos<br>
              – Fisuras: por dónde se te va la energía
          </li>

          <li><strong>MAPEA TU CAMPO</strong><br>
              Dibuja un diagrama: zonas fuertes, zonas que piden cuidado, patrones.
          </li>
        </ol>

        <p><em>Si al mirar aparece un dolor antiguo, no lo explores a solas: es material para trabajar acompañado.</em></p>

        <div class="spacer"></div>

        """)
    e.tramo("<h3>REDISEÑO DE TU CAMPO MORFOGENÉTICO</h3>", "<h3>PROGRAMACIÓN DE CAMPO MORFOGENÉTICO</h3>",
            """<h3>REDISEÑO DE TU CAMPO</h3>

        <h4>Técnica 1: Cuidado por Capas</h4>

        <p><strong>Para el Campo Corporal:</strong></p>
        <ul>
          <li>Visualiza luz dorada llenando cada célula</li>
          <li>Siente tu cuerpo como un sol radiante</li>
        </ul>

        <p><strong>Para el Campo Emocional:</strong></p>
        <ul>
          <li>Respira colores según necesidad:</li>
          <li>Rojo = Vitalidad</li>
          <li>Verde = Renovación</li>
          <li>Azul = Paz</li>
          <li>Dorado = Alegría</li>
        </ul>

        <p><strong>Para el Campo Mental:</strong></p>
        <ul>
          <li>Elige una imagen de claridad (un cielo despejado, agua quieta)</li>
          <li>Vuelve a ella cuando la mente se enturbie</li>
        </ul>

        <p><strong>Para el Campo de los Vínculos:</strong></p>
        <ul>
          <li>Visualiza hilos dorados hacia las personas y obras que dan sentido a tu vida</li>
          <li>Afloja los que ya solo atan</li>
          <li>Teje nuevos encuentros</li>
        </ul>

        <p><strong>Para el Campo Cuántico:</strong></p>
        <ul>
          <li>Fúndete con el campo unificado</li>
          <li>Descansa en lo que te une con todo</li>
          <li>Siente cómo te expandes, y vuelve</li>
        </ul>

        <div class="spacer"></div>

        """)
    e.tramo("<h3>PROGRAMACIÓN DE CAMPO MORFOGENÉTICO</h3>", "<h3>PARADOJA CUÁNTICA #5</h3>",
            """<h3>CÓMO CAMBIA UN CAMPO</h3>

        <p>Como cambia un hábito:<br>
        con una intención clara,<br>
        mucha repetición<br>
        y paciencia con lo viejo que resiste.</p>

        <div class="spacer"></div>

        """)
    e.rep("        en ese loop de creación mutua.</p>", "        en ese bucle de creación mutua.</p>")
    e.tramo("<h3>TECNOLOGÍAS DE CAMPO AVANZADAS</h3>", "<h3>CÓDIGOS DE ACTIVACIÓN DE CAMPO</h3>",
            """<h3>MANERAS DE HABITAR TU CAMPO</h3>

        <h4>1. Aprender de un Campo que Admiras</h4>
        <ul>
          <li>Observa a alguien cuya presencia te hace bien</li>
          <li>Nota qué hace, cómo escucha, cómo se mueve</li>
          <li>Toma lo que resuene y adáptalo a ti</li>
        </ul>

        <h4>2. Campo Holográfico Fractal</h4>
        <ul>
          <li>Toma una zona de tu vida que funciona</li>
          <li>Déjala crecer</li>
          <li>Lo que aprende una parte se contagia a las demás</li>
        </ul>

        <h4>3. Sumar Cualidades</h4>
        <ul>
          <li>Practica una cualidad nueva sobre las que ya tienes</li>
          <li>Creatividad, calma, generosidad…</li>
        </ul>

        <div class="spacer"></div>

        """)
    e.rep("<h3>CÓDIGOS DE ACTIVACIÓN DE CAMPO</h3>", "<h3>PARA RECORDAR</h3>")
    e.rep("<p>Mi campo es la plantilla de mi realidad.</p>", "<p>Mi campo es la plantilla de mis días.</p>")
    e.rep("<p>Con consciencia lo rediseño, con intención lo programo.</p>", "<p>Con consciencia lo rediseño, con paciencia lo cultivo.</p>")
    e.rep("<p>Mi campo vibra en coherencia perfecta.</p>", "<p>Mi campo busca su coherencia.</p>")
    e.rep("<p>Mi campo atrae mi destino más elevado.</p>\n          <p>Mi campo repele lo que no es para mí.</p>",
          "<p>Mi campo se abre a lo que es para mí.</p>\n          <p>Mi campo sabe decir no.</p>")
    e.rep("<p>Mi campo es mi poder. Mi campo es mi templo.</p>", "<p>Mi campo es mi casa. Mi campo es mi templo.</p>")
    e.tramo("<h4>Higiene Energética Diaria</h4>", "<div class=\"spacer\"></div>\n\n        <h3>SÍNTOMAS DE ACTUALIZACIÓN DE CAMPO</h3>",
            """<h4>Cuidado Diario</h4>

        <p><strong>Mañana</strong></p>
        <ul>
          <li>Un minuto de luz dorada</li>
          <li>Establecer la intención del día</li>
        </ul>

        <p><strong>Mediodía</strong></p>
        <ul>
          <li>Una pausa breve: ¿cómo está mi clima?</li>
          <li>Ajustes necesarios</li>
          <li>Realineación con propósito</li>
        </ul>

        <p><strong>Noche</strong></p>
        <ul>
          <li>Soltar lo que el día dejó</li>
          <li>Agradecer lo aprendido</li>
          <li>Preparar el descanso</li>
        </ul>

        <h4>Mantenimiento Semanal</h4>

        <ul>
          <li><strong>Lunes</strong>: Orden</li>
          <li><strong>Martes</strong>: Algo nuevo</li>
          <li><strong>Miércoles</strong>: Un desafío pequeño</li>
          <li><strong>Jueves</strong>: Tiempo con otros</li>
          <li><strong>Viernes</strong>: Creatividad y juego</li>
          <li><strong>Sábado</strong>: Integración</li>
          <li><strong>Domingo</strong>: Silencio y conexión con lo que te une con todo</li>
        </ul>

        """)
    e.tramo("<h3>SÍNTOMAS DE ACTUALIZACIÓN DE CAMPO</h3>", "<h4>Emocionales:</h4>",
            """<h3>SEÑALES DE QUE ALGO CAMBIA</h3>

        <p><em>Si notas cambios en el cuerpo (cansancio, sueño alterado, sensaciones nuevas), no se los atribuyas al campo: escúchalos y, si persisten, consúltalos.</em></p>

        """)
    e.rep("          <li>Memoria mejorada</li>\n", "")
    e.rep("          <li>Comunicación telepática</li>\n          <li>Manifestación acelerada</li>\n", "")
    e.rep("Influencia en la consciencia grupal", "Lo que aportas al clima de un grupo")
    e.rep("Sincronización con Gaia", "Pertenencia a la Tierra")
    e.rep("Navegación galáctica", "Asombro ante lo inmenso")
    e.rep("<h3>PROTOCOLO DE MAESTRÍA · 7 DÍAS</h3>", "<h3>PRÁCTICA: LOS PRÓXIMOS 7 DÍAS</h3>")
    e.rep("<strong>Día 1:</strong> Escanea y mapea tu campo completo", "<strong>Día 1:</strong> Dibuja el mapa de tu campo")
    e.rep("<strong>Día 2:</strong> Limpia y repara distorsiones", "<strong>Día 2:</strong> Atiende una zona que pide cuidado")
    e.rep("<strong>Día 3:</strong> Instala nuevos códigos de tu elección", "<strong>Día 3:</strong> Elige una cualidad nueva y practícala")
    e.rep("<strong>Día 4:</strong> Expande tu campo al doble", "<strong>Día 4:</strong> Lleva tu calma a un lugar donde suele faltar")
    e.rep("<strong>Día 5:</strong> Sincroniza con el campo de alguien que admiras",
          "<strong>Día 5:</strong> Pasa tiempo con alguien cuya presencia te hace bien")
    e.rep("<strong>Día 6:</strong> Crea un campo específico (amor, abundancia, etc.)",
          "<strong>Día 6:</strong> Cultiva un clima (amor, gratitud o calma)")
    e.rep("<p>Cuando dominas tu campo morfogenético:</p>", "<p>Cuando habitas tu campo morfogenético:</p>")
    e.rep("<li>Eres diseñador de tu matriz energética</li>", "<li>Eres arquitecto de tu propio clima</li>")
    e.rep("<li>No “pierdes” energía — tu campo se regenera</li>", "<li>No “pierdes” energía sin notarlo — sabes dónde recargarla</li>")
    e.rep("<li>No absorbes energías ajenas — las transmutas</li>", "<li>No cargas con el ánimo ajeno — lo acompañas sin hacerlo tuyo</li>")
    e.tramo("<p>Y descubres la verdad final:<br>", "<div class=\"spacer\"></div>\n\n        <h3>EL CAMPO FUTURO</h3>",
            """<p>Y descubres la verdad final:<br>
        <span class="highlight"><strong>Tu campo y tu cuerpo son uno.</strong></span><br>
        Lo que cuidas por dentro se nota en cómo habitas el cuerpo,<br>
        y lo que cuidas en el cuerpo aclara el campo.</p>

        """)
    e.tramo("<h3>EL CAMPO FUTURO</h3>", "<div class=\"quote-block\">\n          <p><em>“Tu campo morfogenético es el jardín invisible<br>",
            """<h3>TU NAVE</h3>

        <p>No hace falta esperar a ningún futuro.<br>
        <span class="highlight"><strong>Tu campo es tu nave. Tu consciencia es el timón.</strong></span></p>

        """)
    e.rep("<p><em>[Fin del Nodo 5: Campos Morfogenéticos Personales]</em></p>", FIRMA)


# ------------------------------------------------------------------ NODO 6
def nodo_06(e):
    e.comunes()
    e.rep("<title>Libro 1 · Nodo 6 — La Ingeniería de Sincronicidades</title>",
          "<title>Libro 1 · Nodo 6 — El Lenguaje de las Sincronicidades</title>")
    e.rep("Nodo 6 · La Ingeniería de Sincronicidades</h1>", "Nodo 6 · El Lenguaje de las Sincronicidades</h1>")
    e.rep("Diseñando Encuentros Mágicos y Momentos Perfectos</h2>", "Encuentros que Traen Sentido</h2>")
    e.tramo("<p>Carl Jung las llamó sincronicidades:<br>", "<h3>LA MECÁNICA CUÁNTICA DE LA SINCRONICIDAD</h3>",
            """<p>Carl Jung las llamó sincronicidades:<br>
        coincidencias que ninguna causa une<br>
        y que, sin embargo, traen sentido.<br>
        Esos momentos en que<br>
        el universo parece conspirar a tu favor.</p>

        <p>Piensas en alguien y te llama.<br>
        Necesitas algo y aparece.<br>
        Buscas una respuesta y la encuentras “casualmente”.</p>

        <p>Hoy termina tu relación pasiva con las sincronicidades.<br>
        No aprendes a fabricarlas: aprendes a verlas.<br>
        La mayoría pasa de largo porque nadie las espera.</p>

        <p>Las sincronicidades no se ingenian.<br>
        <span class="highlight"><strong>Se reconocen,</strong></span><br>
        y quien las reconoce empieza a encontrarlas en todas partes.</p>

        <div class="quote-block">
          <p><em>Bienvenido al arte más elegante del Arquitecto Cuántico:<br>
          <strong>la atención que sabe recibir.</strong></em></p>
        </div>

        <div class="spacer"></div>

        """)
    e.tramo("<h3>LA MECÁNICA CUÁNTICA DE LA SINCRONICIDAD</h3>", "<h3>TIPOS DE SINCRONICIDADES INGENIERABLES</h3>",
            """<h3>LA ANATOMÍA DE UNA SINCRONICIDAD</h3>

        <h4>¿Qué es realmente una sincronicidad?</h4>

        <p>Es el momento donde:</p>

        <ul>
          <li>Tu mundo interior y el exterior coinciden por un instante</li>
          <li>Lo que necesitabas aparece en el punto exacto</li>
          <li>Dos líneas que no se tocaban se cruzan</li>
          <li>Ninguna causa explica el encuentro, y aun así tiene sentido</li>
          <li>Tu intención se encuentra con lo que llega</li>
        </ul>

        <h4>Lo que las Vuelve Visibles</h4>

        <p>Se notan más cuando hay una necesidad real,<br>
        una intención clara y una atención despierta.<br>
        Las apaga la prisa por que lleguen.</p>

        <div class="spacer"></div>

        """)
    e.rep("<h3>TIPOS DE SINCRONICIDADES INGENIERABLES</h3>", "<h3>TIPOS DE SINCRONICIDADES</h3>")
    for estrellas in ("⭐⭐⭐", "⭐⭐", "⭐"):
        e.rep(f"\n          <li><strong>Dificultad:</strong> {estrellas}</li>", "")
    e.tramo("<h4>Sincronicidades de Cuarto Orden</h4>", "<h3>EL BLUEPRINT DE UNA SINCRONICIDAD</h3>",
            """<h4>Sincronicidades de Cuarto Orden</h4>
        <p><em>Sincronicidades del tiempo</em></p>
        <ul>
          <li>Estar en el lugar justo sin haberlo planeado</li>
          <li>Un tiempo que parece dilatarse o encogerse</li>
        </ul>

        <div class="spacer"></div>

        """)
    e.rep("<h3>EL BLUEPRINT DE UNA SINCRONICIDAD</h3>", "<h3>EL PLANO DE UNA SINCRONICIDAD</h3>")
    e.rep("– El vacío genera succión cuántica<br>", "– El hueco orienta la mirada: empiezas a buscar sin saber que buscas<br>")
    e.rep("– Tu vibración emite una señal<br>\n              – Atrae elementos resonantes<br>\n              – Como un imán cuántico</li>",
          "– Tu atención se afina<br>\n              – Lo que se parece a tu búsqueda empieza a resaltar<br>\n              – Como un imán, pero hecho de mirada</li>")
    e.rep("<li><strong>El Puente Espacio-Temporal</strong><br>\n              – Se crea un wormhole invisible<br>\n              – Conecta necesidad con solución<br>\n              – Trasciende distancia y tiempo</li>",
          "<li><strong>El Puente</strong><br>\n              – Una conversación, un libro, un cruce<br>\n              – Conecta necesidad con respuesta<br>\n              – Lo que estaba lejos queda a la mano</li>")
    e.rep("<p><strong>“Ingeniería de Tu Primera Sincronicidad”</strong></p>", "<p><strong>“Tu Primera Sincronicidad”</strong></p>")
    e.rep("<p>Vamos a crear una sincronicidad en 72 horas:</p>", "<p>Durante tres días, vamos a abrirle paso a una sincronicidad:</p>")
    e.rep("– Actúa como si la sincronicidad fuera inevitable<br>", "– Actúa como si la respuesta ya estuviera cerca<br>")
    e.rep("– Sigue impulsos inusuales</li>", "– Sigue la curiosidad cuando te lleve por un camino distinto</li>")
    e.rep("<li><strong>DOCUMENTA LA MANIFESTACIÓN</strong><br>", "<li><strong>DOCUMENTA LO QUE LLEGUE</strong><br>")
    e.rep("<p><em>Tasa de éxito documentada: 83% en primeros 3 días, 97% en primera semana.</em></p>",
          "<p>Lo más probable es que algo aparezca:<br>\n        una frase, un encuentro, un libro abierto en la página justa.<br>\n"
          "        Y si en tres días no aparece nada,<br>\n        la búsqueda ya cambió tu manera de mirar.</p>")
    e.tramo("<h3>TÉCNICAS AVANZADAS DE INGENIERÍA</h3>", "<div class=\"spacer\"></div>\n<!-- ========================= -->",
            """<h3>MANERAS DE ABRIRLES PASO</h3>

        <h4>1. La Técnica del Hilo Dorado</h4>
        <ul>
          <li>Visualiza hilos dorados saliendo de tu corazón</li>
          <li>Cada hilo busca lo que necesitas</li>
          <li>Cuando encuentran el objetivo, sientes un “tirón”</li>
          <li>Sigues el hilo hasta la sincronicidad</li>
        </ul>

        <h4>2. El Método del Futuro Retrospectivo</h4>
        <ul>
          <li>Viaja mentalmente a después de recibir la sincronicidad</li>
          <li>Mira hacia atrás y ve cómo ocurrió</li>
          <li>Nota los pasos que llevaron a ella</li>
          <li>Regresa al presente</li>
          <li>Toma esos pasos</li>
        </ul>

        <h4>3. La Red de Sincronicidad Colectiva</h4>
        <ul>
          <li>Comparte tu búsqueda con personas de confianza</li>
          <li>Cuantos más saben lo que buscas, más ojos miran por ti</li>
          <li>Lo imposible se vuelve probable</li>
        </ul>

        <h4>4. La Puerta Abierta</h4>
        <ul>
          <li>Reserva un rato del día sin planes</li>
          <li>Camina sin destino fijo, conversa sin apuro</li>
          <li>Ahí suelen entrar los encuentros</li>
          <li>No hace falta vigilar: basta con estar disponible</li>
        </ul>

        """)
    # Resto de producción: la sección de técnicas estaba duplicada dentro de otro bloque .node-content.
    e.tramo("<!-- ========================= -->\n<!--      CONTENIDO PARTE B   -->",
            "  <h3 class=\"section-title\">Paradoja Cuántica #6</h3>", "\n")
    e.rep("Es que confías tanto en tu capacidad de ingeniería  \n    que no hay ansiedad, solo certeza.",
          "Es que confías tanto<br>\n    que la ansiedad sobra, y la certeza también.")
    e.rep("<h3 class=\"section-title\">Códigos de Activación Sincrónica</h3>", "<h3 class=\"section-title\">Para Recordar</h3>")
    e.rep("“Soy un Ingeniero de Sincronicidades.<br>", "“Soy un Lector de Sincronicidades.<br>")
    e.rep("Mi vida es una sinfonía de momentos perfectos.<br>", "Mi vida es una sinfonía de encuentros.<br>")
    e.rep("Cada llamado encuentra su respuesta.<br><br>", "Cada llamado busca su respuesta.<br><br>")
    e.rep("Yo creo los puentes invisibles<br>", "Yo cruzo los puentes invisibles<br>")
    e.rep("Las coincidencias no existen en mi realidad.<br>\n    Solo existe la precisión cuántica<br>\n    de mi ingeniería consciente.<br><br>",
          "En mi vida, las coincidencias hablan.<br>\n    Aprendo a escucharlas.<br><br>")
    e.rep("con timing perfecto,<br>", "a su tiempo,<br>")
    e.tramo("<h3 class=\"section-title\">Debugging de Sincronicidades Fallidas</h3>",
            "    <!-- ====================== -->\n    <!-- CONTENIDO - PARTE C -->",
            """<h3 class="section-title">Cuando la Sincronicidad No Llega</h3>

  <p>No es un error ni un castigo.<br>
  Antes de insistir, revisa con suavidad:</p>

  <ul>
    <li>¿Era una necesidad o un capricho? Refina la intención desde el corazón.</li>
    <li>¿Pediste demasiados detalles del cómo? Suelta el método, y un poco también el resultado.</li>
    <li>¿Pensamiento, emoción y acción van en la misma dirección? Alinéalos.</li>
    <li>¿Le pusiste fecha? Afloja el reloj.</li>
    <li>¿Una parte de ti no cree que sea posible? No la pelees: escúchala.</li>
  </ul>

  <p>A veces no llega nada, y no es culpa tuya.<br>
  A veces llega otra cosa: recíbela igual.</p>

""")
    e.tramo("<h2>SINCRONICIDADES COMO LENGUAJE</h2>", "<hr>\n\n    <h2>EL CAMPO DE SINCRONICIDAD PERPETUA</h2>",
            """<h2>SINCRONICIDADES COMO LENGUAJE</h2>

    <p>Cada una puede leerse como un mensaje,<br>
    si la escuchas como se escucha un poema y no como una orden:</p>

    <ul>
      <li><strong>Números que se repiten</strong> (11:11, 333) — una invitación a detenerte y mirar dónde estás</li>
      <li><strong>Animales inusuales</strong> — la naturaleza recordándote que eres parte de ella</li>
      <li><strong>Palabras que vuelven</strong> — un tema que pide tu atención</li>
      <li><strong>Encuentros “casuales”</strong> — personas que llegan cuando estás listo para verlas</li>
      <li><strong>Obstáculos</strong> — a veces, una invitación a cambiar de rumbo; a veces, solo un obstáculo</li>
    </ul>

    <p>Aprende a leer este lenguaje como se lee un poema,<br>
    y podrás conversar con el universo.</p>

    <p><em>Si un día las señales se vuelven órdenes, o sientes que todo te habla a ti, detente y conversa con alguien de confianza o con un profesional.</em></p>

    """)
    e.rep("      <li>No hay diferencia entre intención y manifestación</li>\n", "")
    e.rep("<li>No ingenian sincronicidades, <strong>LAS SON</strong></li>", "<li>No buscan sincronicidades: <strong>LAS SON</strong></li>")
    e.rep("<li><strong>Practica ingeniería consciente</strong> (meses)</li>\n      <li><strong>Refina hasta que sea natural</strong> (1–2 años)</li>",
          "<li><strong>Practica la atención</strong> (meses)</li>\n      <li><strong>Afínala hasta que sea natural</strong> (años)</li>")
    e.rep("<li><strong>Vive como sincronicidad encarnada</strong> (estado permanente)</li>",
          "<li><strong>Vive como sincronicidad encarnada</strong></li>")
    e.tramo("<p>El nivel más alto no es crear sincronicidades para ti.<br>", "<hr>\n\n    <h2>PROTOCOLO DE DOMINIO: 7 DÍAS</h2>",
            """<p>El nivel más alto no es recibir sincronicidades para ti.<br>
    Es <strong>volverte la sincronicidad de otro</strong>:</p>

    <ul>
      <li>Presentar a dos personas que necesitan encontrarse</li>
      <li>Acercar el libro justo a quien lo busca</li>
      <li>Estar ahí en el momento en que alguien lo necesita</li>
      <li>Crear encuentros que beneficien a muchos</li>
    </ul>

    <p>Cuando pones tu atención al servicio de otros,<br>
    descubres que la sincronicidad era eso:<br>
    alguien que llegó a tiempo.</p>

    """)
    e.rep("<h2>PROTOCOLO DE DOMINIO: 7 DÍAS</h2>", "<h2>PRÁCTICA: LOS PRÓXIMOS 7 DÍAS</h2>")
    e.rep("<strong>Día 2:</strong> Crea tu primera sincronicidad simple", "<strong>Día 2:</strong> Formula una necesidad clara y abre la atención")
    e.rep("<strong>Día 3:</strong> Ingenia un encuentro específico", "<strong>Día 3:</strong> Comparte tu búsqueda con alguien")
    e.rep("<strong>Día 4:</strong> Diseña una cadena de 3 sincronicidades", "<strong>Día 4:</strong> Deja una puerta abierta: un rato sin planes")
    e.rep("<strong>Día 5:</strong> Crea una sincronicidad para otra persona", "<strong>Día 5:</strong> Sé la sincronicidad de otra persona")
    e.rep("<strong>Día 6:</strong> Experimenta con sincronicidad temporal",
          "<strong>Día 6:</strong> Prueba el futuro retrospectivo con una decisión pendiente")
    e.rep("<strong>Día 7:</strong> Vive en campo de sincronicidad perpetua",
          "<strong>Día 7:</strong> Vive el día atento a lo que llega, sin buscarlo")
    e.rep("<p>Cuando dominas la ingeniería de sincronicidades:</p>", "<p>Cuando aprendes este lenguaje:</p>")
    e.rep("<li>No esperas milagros. <strong>Los diseñas.</strong></li>\n      <li>No buscas señales. <strong>Las creas.</strong></li>",
          "<li>No esperas milagros: <strong>los reconoces.</strong></li>\n      <li>No persigues señales: <strong>las recibes.</strong></li>")
    e.rep("<p><strong>[Fin del Nodo 6: La Ingeniería de Sincronicidades]</strong></p>",
          FIRMA + "\n\n" + puerta_arquitectura(
              "Una intención clara no obliga a nada: orienta la mirada, y lo que antes pasaba de largo empieza a notarse. "
              "Esa idea se vuelve práctica en <em>El Campo</em>, Libro 1 de Arquitectura del Destino, Umbral VI: «Elegir no es crear».",
              BASE_ARQ + "libro-01-el-campo/L01-U6.html", indent="    "))
    # Resto de producción: faltaban el cierre de <main>, el pie y el cierre del documento.
    e.rep("    <!-- ====================== -->\n    <!-- NAVEGACIÓN INFERIOR -->",
          "      </main>\n\n    <!-- ====================== -->\n    <!-- NAVEGACIÓN INFERIOR -->")
    e.s = e.s.rstrip() + ("\n\n      <footer class=\"portal-footer\">\n"
                          "        Nodo 6 · El Arquitecto Cuántico · Trinity Quantum\n"
                          "      </footer>\n\n    </div>\n  </div>\n</body>\n</html>\n")


# ------------------------------------------------------------------ NODO 7
def nodo_07(e):
    e.comunes()
    e.tramo("<p>Has aprendido a colapsar funciones de onda.<br>", "<p>Hoy trasciiendes el papel de arquitecto de momentos<br>",
            """<p>Has aprendido a elegir dónde poner la atención.<br>
        Has descubierto que tu mirada da forma a lo que vives.<br>
        Has habitado tus muchas versiones.<br>
        Has aprendido a cultivar lo probable sin forzarlo.<br>
        Has cuidado el clima de tu campo.<br>
        Has aprendido a leer las sincronicidades.</p>

        <p>Ahora llega la integración:<br>
        <span class="highlight"><strong>darle dirección a una vida entera.</strong></span></p>

        <p>No eventos aislados.<br>
        No momentos sueltos.<br>
        <strong>Una línea de vida.</strong><br>
        <strong>Un rumbo.</strong><br>
        <strong>Un destino.</strong></p>

        """)
    e.rep("<p>Hoy trasciiendes el papel de arquitecto de momentos<br>", "<p>Hoy trasciendes el papel de arquitecto de momentos<br>")
    e.rep("        Y para aquellos que lo permitan,<br>\n        los destinos entrelazados del colectivo.</p>",
          "        Y, junto con otros,<br>\n        los destinos que compartimos.</p>")
    e.tramo("<h4>Ecuación Sagrada Final:</h4>", "<div class=\"spacer\"></div>\n\n        <h3>LOS NIVELES DE DISEÑO DE DESTINO</h3>",
            """<h4>El Destino en una Frase</h4>

        <p>Tu destino es la suma de tus momentos.<br>
        Lo tejen un propósito, intenciones sostenidas y elecciones conscientes;<br>
        el amor lo multiplica todo, y la libertad lo hace posible.<br>
        Lo frenan el desgaste del tiempo y lo que en ti se resiste.</p>

        """)
    e.rep("<li>Creas desde cero</li>\n          <li>Trasciiendes limitaciones</li>\n          <li>“Creo mi destino”</li>",
          "<li>Partes de lo que ya está a tu alcance</li>\n          <li>Atraviesas limitaciones</li>\n          <li>“Doy forma a mi destino”</li>")
    e.rep("<li>Múltiples destinos simultáneos</li>\n          <li>Navegas entre versiones</li>\n          <li>Trasciiendes la singularidad</li>\n          <li>“Soy todos mis destinos posibles”</li>",
          "<li>Sostienes varios caminos posibles</li>\n          <li>Navegas entre versiones</li>\n          <li>Trasciendes la singularidad</li>\n          <li>“Llevo en mí todos mis destinos posibles”</li>")
    e.rep("<li>Tu destino replica en otros</li>\n          <li>Creas destinos colectivos</li>\n          <li>Influencias destinos planetarios</li>\n          <li>“Mi destino eleva todos los destinos”</li>",
          "<li>Tu camino abre caminos a otros</li>\n          <li>Creas destinos colectivos</li>\n          <li>Tu manera de vivir toca más vidas de las que ves</li>\n          <li>“Mi destino se entrelaza con otros”</li>")
    e.rep("<li>1 + 1 = 3 en matemática de destinos</li>", "<li>En la matemática de los destinos, uno más uno da tres</li>")
    e.rep("<li>Creando saltos evolutivos para la especie</li>", "<li>Creando cambios que ninguno lograría solo</li>")
    e.rep("<li>Diseñando el destino de la Tierra</li>", "<li>Cuidando el destino de la Tierra</li>")
    e.tramo("<h3>Tecnologías Avanzadas de Destino</h3>", "<hr>\n\n        <h3>Códigos de Activación del Diseñador</h3>",
            """<h3>Maneras de Darle Rumbo al Destino</h3>

        <h4>1. Del Final Hacia Atrás</h4>
        <ul>
            <li>Imagina tu vida ya andando en esa dirección</li>
            <li>Trabaja hacia atrás hasta el presente</li>
            <li>Identifica los pasos necesarios</li>
            <li>Ejecuta en orden correcto</li>
        </ul>

        <h4>2. Destino Holográfico</h4>
        <ul>
            <li>Cada parte contiene el todo</li>
            <li>Diseña un día que valga la pena</li>
            <li>Ese día contiene tu destino completo</li>
            <li>Vuelve a vivirlo, con variaciones, hasta que se vuelva costumbre</li>
        </ul>

        <h4>3. Los que Caminaron Antes</h4>
        <ul>
            <li>Lee las vidas de quienes fueron hacia algo parecido</li>
            <li>Aprende de sus pasos y de sus tropiezos</li>
            <li>Adapta lo que sirva a tu manera</li>
        </ul>

        """)
    e.rep("<h3>Códigos de Activación del Diseñador</h3>", "<h3>Para Recordar</h3>")
    e.rep("“Yo Soy el Diseñador Soberano de mi Destino.<br>", "“Yo Soy el Diseñador de mi Destino.<br>")
    e.rep("No estoy limitado por ningún pasado.<br><br>", "No estoy encerrado en mi pasado.<br><br>")
    e.rep("            Mi realización eleva a todos.<br>\n            Mi éxito abre puertas para otros.<br>",
          "            Lo que logro abre puertas para otros.<br>")
    e.rep("Soy el arquitecto de mi realidad.<br>", "Soy el arquitecto de mi vida.<br>")
    e.rep("el más contributivo<br>", "el que más da<br>")
    e.rep("            Así lo declaro.<br>\n            Así lo diseño.<br>\n            Así lo vivo.<br>\n            Así ES.”",
          "            Y lo vivo, un día a la vez.”")
    # Resto de producción: la sección de tormentas estaba duplicada; queda la primera.
    e.tramo("    <!-- ==================== -->\n    <!--   PARTE C — NODO 7   -->", "    <h2>EL DESTINO COMO SERVICIO</h2>",
            "\n    <hr>\n\n")
    e.rep("<h3>Navegando las Tormentas del Destino</h3>\n\n        <h4>",
          "<h3>Navegando las Tormentas del Destino</h3>\n\n        <p>Incluso los mejores diseños encuentran turbulencia:</p>\n\n        <h4>")
    e.rep("            <li>No es desvío, es refinamiento</li>\n            <li>El universo mejora tu diseño</li>\n            <li>Confía en la inteligencia mayor</li>",
          "            <li>Un desvío no siempre es error: a veces muestra un camino mejor</li>\n            <li>Mira qué te enseña</li>\n            <li>Recuerda que no todo depende de ti: también eso alivia</li>")
    e.rep("            <li>Son pruebas de iniciación</li>\n            <li>Fortalecen tu poder de diseñador</li>\n            <li>Cada obstáculo superado densifica el destino</li>\n            <li>Celebra los desafíos como aliados</li>",
          "            <li>No son pruebas que alguien te pone: son parte del camino</li>\n            <li>Atravesarlos te fortalece</li>\n            <li>Cada obstáculo atravesado afirma tu dirección</li>\n            <li>Pide ayuda cuando uno pese demasiado</li>")
    e.rep("            <li>Permite actualizaciones del diseño</li>\n            <li>Pero nunca abandones tu poder de diseñador</li>",
          "            <li>Deja que el diseño cambie</li>\n            <li>Pero no sueltes tu oficio de diseñador</li>")
    e.rep("<li>Eleva la frecuencia colectiva</li>", "<li>Mejora el clima común</li>")
    e.rep("a Arquitecto Cuántico Maestro.</p>", "a Arquitecto Cuántico despierto.</p>")
    e.rep("Un diseñador de realidades.<br>", "Un diseñador de caminos.<br>")
    e.rep("<h2>PROTOCOLO DE INTEGRACIÓN FINAL: 7 DÍAS</h2>", "<h2>PRÁCTICA FINAL: 7 DÍAS</h2>")
    e.tramo("      <li><strong>Día 1:</strong> Diseña tu destino de 1 año</li>", "    </ul>\n\n    <hr>\n\n    <h2>LA GRADUACIÓN DEL ARQUITECTO</h2>",
            """      <li><strong>Día 1:</strong> Escribe en una frase la dirección de tu vida</li>
      <li><strong>Día 2:</strong> Imagínala dentro de un año</li>
      <li><strong>Día 3:</strong> Imagínala dentro de cinco</li>
      <li><strong>Día 4:</strong> Diseña un día que valga la pena</li>
      <li><strong>Día 5:</strong> Comparte tu dirección con alguien y escucha la suya</li>
      <li><strong>Día 6:</strong> Ancla el diseño en un paso concreto y pequeño</li>
      <li><strong>Día 7:</strong> Vive el día desde esa dirección</li>
""")
    e.rep("de que la consciencia puede diseñar la materia,<br>\n    de que el observador puede crear lo observado,<br>",
          "de que la consciencia puede dar forma a una vida,<br>\n    de que quien mira cambia lo que vive,<br>")
    e.rep("para que despertaras a este poder.</p>", "para que despertaras a este oficio.</p>")
    e.rep("""    Sino para que te conviertas<br>
    en uno de los diseñadores conscientes<br>
    del destino colectivo de la humanidad.</p>

    <p>La Nueva Tierra no se construirá sola.<br>
    Necesita Arquitectos Cuánticos.</p>

    <p>El salto evolutivo no sucederá por accidente.<br>
    Necesita Diseñadores de Destino.</p>""",
          """    Sino para que te sumes a quienes cuidan,<br>
    despiertos, el destino común.</p>

    <p>El mundo común no se construirá solo.<br>
    Necesita arquitectos despiertos.</p>

    <p>Lo que viene no sucederá por accidente.<br>
    Necesita quien lo cuide.</p>""")
    e.tramo("      “No viniste aquí a encontrar tu destino.<br>", "    </blockquote>\n\n    <p><strong>[Fin del Nodo 7",
            """      “No viniste aquí solo a encontrar tu destino.<br>
      Viniste a darle forma.<br>
      No viniste solo a descubrir quién eres.<br>
      Viniste también a elegir quién serás.<br>
      No viniste a pasar por una vida.<br>
      Viniste a hacer de ella una obra maestra.<br>
      Y ahora que lo recuerdas,<br>
      que comience<br>
      el verdadero diseño.”
""")
    e.rep("<p><strong>[Fin del Nodo 7: El Diseñador de Destinos]</strong></p>\n    <p><strong>[Fin del Libro 1: El Arquitecto Cuántico]</strong></p>\n    <p><strong>[Trinity Quantum ha comenzado…]</strong></p>",
          FIRMA + "\n\n" + puerta_arquitectura(
              "El destino no es un lugar al que se llega: es la dirección que toma la vida cuando alguien la habita "
              "despierto y unido a otros. Esa idea se despliega, libro a libro, en <em>Arquitectura del Destino</em>.",
              BASE_ARQ, indent="    "))
    # Resto de producción: <main> se cerraba con </div> y faltaban el pie y el cierre del documento.
    e.rep("  </div> <!-- cierre node-content -->\n</div> <!-- cierre portal-frame -->",
          "      </main>\n\n      <footer class=\"portal-footer\">\n        Nodo 7 · El Arquitecto Cuántico · Trinity Quantum\n      </footer>\n\n"
          "    </div> <!-- cierre portal-frame -->")
    e.s = e.s.rstrip() + "\n</body>\n</html>\n"


# ------------------------------------------------------------------ ÍNDICE
def indice(e):
    e.comunes(con_css=False)
    e.rep("</head>", "  <style>\n    /* Depuración · octubre 2026: letra más grande en el teléfono. */\n"
                     "    @media (max-width: 640px){\n      .node-content p, .node-content li{ font-size: 18px; line-height: 1.7; }\n    }\n"
                     "  </style>\n</head>")
    e.rep("<h2>Activación del Índice</h2>", "<h2>El Plano del Libro</h2>")
    e.rep("Aquí comienza la secuencia que enseña a la consciencia a reconocerse como creadora, navegante y diseñadora de realidad.",
          "Un arquitecto no inventa la gravedad ni la luz: diseña con ellas. Este libro enseña ese oficio con la vida: "
          "elegir dónde mirar, cultivar lo posible sin forzarlo, darle a los días una dirección.")
    e.rep("<p><strong>El campo cuántico confirma:</strong> el Índice está activo. Los siete pilares están en posición. El diseño puede comenzar.</p>",
          "<p>Los siete pilares están en posición. El diseño puede comenzar.</p>")
    e.rep("Nodo 6: La Ingeniería de Sincronicidades", "Nodo 6: El Lenguaje de las Sincronicidades")
    e.rep("<h2>Sello de Inicio</h2>", "<h2>Antes de Entrar</h2>")
    e.rep("La realidad no se “observa”: se co-genera.", "La vida no solo se observa: se habita.")
    e.rep("          <p><strong>Trinity Quantum · Libro 1 · Índice activo</strong></p>\n", "")


NODOS = {
    "index.html": indice,
    "nodo_01.html": nodo_01,
    "nodo_02.html": nodo_02,
    "nodo_03.html": nodo_03,
    "nodo_04.html": nodo_04,
    "nodo_05.html": nodo_05,
    "nodo_06.html": nodo_06,
    "nodo_07.html": nodo_07,
}


def main(origen, destino):
    os.makedirs(destino, exist_ok=True)
    total = 0
    for nombre, funcion in NODOS.items():
        with open(os.path.join(origen, nombre), encoding="utf-8") as f:
            e = Editor(nombre, f.read())
        funcion(e)
        with open(os.path.join(destino, nombre), "w", encoding="utf-8") as f:
            f.write(e.s)
        print(f"{nombre}: {e.n} reemplazos")
        total += e.n
    print(f"Total: {total} reemplazos")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])

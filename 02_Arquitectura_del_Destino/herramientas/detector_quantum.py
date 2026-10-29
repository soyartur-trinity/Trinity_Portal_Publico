#!/usr/bin/env python3
"""
Detector de pasajes para la depuración de Trinity Quantum.

No decide nada: lista, nodo por nodo, los pasajes que la lectura tiene
que mirar, para que no se escape ninguno. Las categorías siguen los cinco
criterios de la guía (maestro v4, sección 5) y las cuatro precisiones de
la etapa de revisión completa (octubre de 2026):
experimentos, cifras, «cuántico» y velas y rituales.

Uso:
    python3 detector_quantum.py <carpeta_del_libro> [--detalle] [--md salida.md]

Ejemplo:
    python3 detector_quantum.py ../../Trinity-/02_Trinity_Quantum/Libro_02 --detalle
"""
import html
import re
import sys
from pathlib import Path

CATEGORIAS = [
    ("formulas", "Fórmulas y códigos (criterio 1)", [
        r"ecuaci[oó]n sagrada", r"c[oó]digos? de activaci[oó]n", r"\b[01]{8}\b",
        r"[ΨΩΓΤΜφ∑∫∮√⊗♥]", r"\be\^\(", r"\bdonde:\s*$", r"colapsa cuando",
        r"tiende a infinito", r"la ecuaci[oó]n",
    ]),
    ("cifras", "Cifras presentadas como medida (precisión 2)", [
        r"\d+[.,]?\d*\s*(hz|hercios|herzios)\b", r"\d+\s*%", r"\bpor ciento\b",
        r"\d[\d.,]*\s*veces\b", r"\d[\d.,]*\s*(metros|km|kil[oó]metros|cent[ií]metros)\b",
        r"\d[\d.,]*\s*(neuronas|c[eé]lulas|sentidos|fotones|segundos)\b",
        r"\b(miles|millones|billones|trillones) de\b", r"\d+\s*[-–]\s*\d+",
        r"\b\d{2,}[.,]\d{3}\b",
    ]),
    ("experimentos", "Experimentos, estudios y ciencia invocada (precisión 1)", [
        r"\bestudios?\b", r"\binvestigaci[oó]n", r"\binvestigador", r"\bcient[ií]fic",
        r"\bla ciencia\b", r"\bdocumentad", r"\bdemostr", r"\bcomprob", r"\binstituto\b",
        r"\bexperimento", r"\bahora sabemos\b", r"\bse ha (medido|probado|descubierto)",
        r"\bdescubrimiento", r"\bhip[oó]tesis\b",
        r"\b(HeartMath|Lovelock|Sheldrake|Schumann|Bohm|Pribram|Penrose|Hameroff|Emoto|Braud|Dossey|Backster|Radin|Hagelin|Maharishi|Simard|Mancuso|Tesla|Einstein|Bohr|Heisenberg|Schr[oö]dinger|Planck)\b",
    ]),
    ("cuantico", "«Cuántico» y física usada para explicar (precisión 3)", [
        r"cu[aá]ntic", r"no[- ]local", r"campo unificado",
        r"funci[oó]n de onda", r"superposici[oó]n", r"colaps", r"frecuencia",
        r"vibraci[oó]n|vibracional", r"toroidal", r"electromagn[eé]tic", r"dimensi[oó]n|dimensional",
    ]),
    ("rituales", "Velas, rituales y números rituales (precisión 4)", [
        r"\bvelas?\b", r"\bcristal(es)?\b", r"\bluna (llena|nueva)\b", r"\bceremonia",
        r"\b11:11\b", r"\b\d{1,2}:\d{2}\b", r"\bexactamente\b", r"\bexactos?\b",
        r"\b(3|7|11|21|33|44|72|108)\s*(minutos|d[ií]as|horas|veces)\b",
        r"\bnorte magn[eé]tico\b", r"\bsello\b", r"\bincienso\b", r"\baltar\b",
        r"\bmantra\b", r"\bdescalz", r"\bamanecer\b",
    ]),
    ("transmision", "Sellos, transmisiones y restos de producción (criterio 1, lengua y forma)", [
        r"\bactivaci[oó]n\b", r"\bactivar\b", r"\bactiv[oa]\b", r"\btransmisi[oó]n (completa|contin[uú]a|completada)",
        r"el campo cu[aá]ntico confirma", r"\bY as[ií] es\b", r"\bparte [abc]\b",
        r"ropaje trinity", r"\bindex\b", r"\*\*", r"este nodo (te )?(ha|te)",
        r"has aprendido", r"\bcompletad[oa]\b", r"\bmaestr[ií]a\b",
    ]),
    ("nueva_era", "Nueva Era: ADN, pineal, telepatía, grillas, linajes (filtro)", [
        r"\badn\b", r"\bgen[oó]ma\b", r"\bpineal\b", r"\btimo\b", r"telepat",
        r"\bgrilla", r"l[ií]neas? ley", r"\bak[aá]shic", r"\bastral\b",
        r"\bseres no f[ií]sicos\b", r"\bgu[ií]as\b", r"\bascensi[oó]n\b", r"\bnueva (tierra|era|humanidad)\b",
        r"\bsalto (evolutivo|cu[aá]ntico)\b", r"\bmasa cr[ií]tica\b", r"\bnoosfera\b",
        r"\bc[oó]digos? (gen[eé]tic|binari)", r"\bmemoria celular|memorias celulares\b",
        r"\bescritura autom[aá]tica\b", r"\bcanal(izar|izaci[oó]n)?\b", r"\bdescargas? de informaci[oó]n\b",
        r"\bmensajes? del campo\b", r"\bkarma|k[aá]rmic", r"\bvidas? (pasadas|anteriores)|mil vidas|encarnaci",
    ]),
    ("plan", "Plan del universo y providencia (criterio 2)", [
        r"\bpor dise[nñ]o\b", r"\bdise[nñ]ad[oa]s? para\b", r"\bperfect[oa]\b", r"\belegiste\b",
        r"\bprogramaste\b", r"\bantes de nacer\b", r"\bcontratos?\b", r"\bacuerdos?\b",
        r"\bdestino\b", r"\bvinieron a\b", r"\bpara (despertarte|ense[nñ]arte)\b",
        r"\bmaestros? disfrazad", r"\bno es coincidencia\b", r"\bnada es casual",
    ]),
    ("absolutos", "Afirmaciones de hecho sobre mente, salud o mundo (criterio 3)", [
        r"\bliteralmente\b", r"\bno es (una )?met[aá]fora\b", r"\bno es poes[ií]a\b",
        r"\bno es imaginaci[oó]n\b", r"\bno es superstici[oó]n\b", r"\bes realidad\b",
        r"\bla verdad es\b", r"\binstant[aá]neamente\b", r"\bsiempre\b", r"\bnunca\b",
        r"\btoda (crisis|la)\b", r"\bcada (pensamiento|emoci[oó]n|[aá]tomo|c[eé]lula)\b",
        r"\bpor eso\b", r"\bes el secreto\b", r"\bel secreto\b",
    ]),
    ("omnipotencia", "Dominio, promesas y omnipotencia (criterio 4)", [
        r"\bmilagro", r"\bgarantiz", r"\bcrear (sincronicidades|realidad|destino)",
        r"\bcolapsa realidades\b", r"\boperar\b", r"\bcontrol", r"\bdominar|dominio\b",
        r"\btodo el d[ií]a\b", r"\bsolo desde\b", r"\bse multiplican?\b", r"\bexponencial",
        r"\binfinit[oa]s?\b", r"\bderecho de nacimiento\b", r"\bpoder\b",
    ]),
    ("clinico", "Riesgo clínico: trauma, enfermedad, muerte, disociación, daño (criterio 5)", [
        r"\bsan(ar|aci[oó]n|a)\b", r"\btrauma", r"\benferm", r"\bmuert|\bmorir|\bmuere",
        r"\bdiagn[oó]stic", r"\bpensamientos? (ajenos|no son|de otros)", r"no son .?tuyos",
        r"\bcontaminaci[oó]n\b", r"\bescudos?\b", r"\bmensajes\b", r"\bvoces\b",
        r"\bdisolver (fronteras|barrera)", r"\bbarrera mental\b", r"\bdormir en el suelo\b",
        r"\bdolor\b", r"\bherid", r"\benemigo|verdugo|antagonista", r"\bp[eé]rdidas?\b",
        r"\bsilencio mental absoluto\b", r"\bp[uú]blicos\b", r"\bbroadcast",
        r"\bayuno|detox|dieta\b", r"\bp[aá]nico|ansiedad|depresi[oó]n\b",
    ]),
    ("lengua", "Lengua: anglicismos, erratas y autorreferencia", [
        r"\byet\b", r"\bbroadcasting\b", r"\bembodiment\b", r"\bfeature\b", r"\bbug\b",
        r"\bdetox\b", r"\bloop\b", r"\bfeedback\b", r"\bupgrade\b", r"\bsintropia\b",
        r"(?-i:EntreLazamiento)", r"\bintegracion\b", r"\beste nodo\b",
    ]),
]

COMPILADAS = [(k, t, [re.compile(p, re.I | re.M) for p in pats]) for k, t, pats in CATEGORIAS]


def texto_por_lineas(src: str):
    """Devuelve una lista de (n_línea_html, encabezado_vigente, texto_visible)."""
    lineas = src.split("\n")
    sin_comentarios = re.sub(r"<!--.*?-->", lambda m: "\n" * m.group(0).count("\n"), src, flags=re.S)
    sin_estilos = re.sub(r"<(style|script)\b.*?</\1>", lambda m: "\n" * m.group(0).count("\n"), sin_comentarios, flags=re.S | re.I)
    salida, encabezado = [], "(inicio)"
    for n, linea in enumerate(sin_estilos.split("\n"), 1):
        m = re.search(r"<h[1-4][^>]*>(.*?)</h[1-4]>", linea, re.I)
        visible = html.unescape(re.sub(r"<[^>]+>", " ", linea))
        visible = re.sub(r"\s+", " ", visible).strip()
        if m:
            encabezado = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", m.group(1)))).strip() or encabezado
        if visible:
            salida.append((n, encabezado, visible))
    return salida, lineas


def revisar_html(src: str):
    """Chequeos de forma: lo que suele estar roto en estos archivos."""
    avisos = []
    for etiqueta in ("main", "section", "div", "nav", "footer", "aside", "ul", "ol", "blockquote", "pre"):
        a = len(re.findall(rf"<{etiqueta}\b", src, re.I))
        c = len(re.findall(rf"</{etiqueta}>", src, re.I))
        if a != c:
            avisos.append(f"<{etiqueta}> abiertas {a}, cerradas {c}")
    if not re.search(r"<title>", src, re.I):
        avisos.append("sin <title>")
    if not re.search(r"</html>\s*$", src.strip() + "\n", re.I):
        avisos.append("no termina en </html>")
    if re.search(r"</html>.+", src, re.S | re.I) and re.search(r"</html>\s*\S", src, re.I):
        avisos.append("hay contenido después de </html>")
    heads = [re.sub(r"<[^>]+>|[^\wáéíóúñ ]", "", h).strip().lower()
             for h in re.findall(r"<h[1-4][^>]*>(.*?)</h[1-4]>", src, re.I | re.S)]
    dup = sorted({h for h in heads if h and heads.count(h) > 1})
    if dup:
        avisos.append("encabezados repetidos: " + ", ".join(dup))
    if re.search(r"<h[1-4][^>]*>\s*\*\*", src):
        avisos.append("asteriscos de markdown en encabezados")
    if not re.search(r"font-size:\s*18px", src):
        avisos.append("sin la letra de 18 px en el teléfono")
    if "quantum-original" not in src:
        avisos.append("sin nota de procedencia")
    return avisos


def detectar(carpeta: Path):
    resultado = {}
    for f in sorted(carpeta.glob("*.html")):
        src = f.read_text(encoding="utf-8")
        filas, _ = texto_por_lineas(src)
        hallazgos = []
        for n, enc, txt in filas:
            for clave, _, pats in COMPILADAS:
                for p in pats:
                    m = p.search(txt)
                    if m:
                        hallazgos.append((clave, n, enc, txt, m.group(0)))
                        break
        resultado[f.name] = (hallazgos, revisar_html(src), len(" ".join(t for _, _, t in filas).split()))
    return resultado


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    carpeta = Path(sys.argv[1])
    detalle = "--detalle" in sys.argv
    md = sys.argv[sys.argv.index("--md") + 1] if "--md" in sys.argv else None
    res = detectar(carpeta)
    claves = [k for k, _, _ in CATEGORIAS]
    out = []
    out.append(f"# Detector · {carpeta}\n")
    out.append("| archivo | palabras | " + " | ".join(claves) + " | total |")
    out.append("|---|---|" + "---|" * (len(claves) + 1))
    for nombre, (h, _, pal) in res.items():
        cuenta = [sum(1 for x in h if x[0] == k) for k in claves]
        out.append(f"| {nombre} | {pal} | " + " | ".join(str(c) for c in cuenta) + f" | {len(h)} |")
    out.append("")
    for nombre, (h, avisos, _) in res.items():
        out.append(f"## {nombre}")
        if avisos:
            out.append("Forma: " + "; ".join(avisos))
        if detalle:
            for clave, titulo, _ in COMPILADAS:
                sel = [x for x in h if x[0] == clave]
                if not sel:
                    continue
                out.append(f"\n**{titulo}**")
                for _, n, enc, txt, hit in sel:
                    corto = txt if len(txt) < 170 else txt[:167] + "…"
                    out.append(f"- l.{n} [{enc[:40]}] «{hit}»: {corto}")
        out.append("")
    texto = "\n".join(out)
    if md:
        Path(md).write_text(texto, encoding="utf-8")
    try:
        print(texto)
    except BrokenPipeError:
        pass


if __name__ == "__main__":
    main()

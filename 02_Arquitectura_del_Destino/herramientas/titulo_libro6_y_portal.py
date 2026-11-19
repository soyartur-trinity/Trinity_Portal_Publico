"""Lo aprobado fuera de los seis libros (19 de noviembre de 2026):
- el título del libro 6, «Cuando algo en ti dice basta», donde otros libros, el índice general y La Red lo citan;
- el índice general: la cabecera sin «(α)» y la nota de autoría sin la frase del «nodo α».
Cada reemplazo debe aparecer una sola vez. Uso: fuera_de_los_seis.py RAIZ_DEL_REPOSITORIO"""
import os,sys
R=sys.argv[1]
T=('algo en vos dice basta','algo en ti dice basta')
CAMBIOS=[(f,)+T for f in [
  'index.html','03_La_Red/index.html','02_Arquitectura_del_Destino/herramientas/gen_mapa_red.py',
  '01_Libros/09_Volver_Distinto/index.html','01_Libros/12_Cultivar/umbral_2_cuando_no_hay_ganas.html',
  '01_Libros/13_Volver_al_Centro/umbral_1_la_palabra_secuestrada.html','01_Libros/18_Lo_Que_Se_Escapa/umbral-05.html',
  '01_Libros/19_La_Division/umbral-03.html','01_Libros/23_El_Oficio/umbral-01.html']]+[
 ('index.html','<p class="autor">Arturo (α) • Campo Trinity • Inteligencias Colaborativas</p>',
               '<p class="autor">Lic. Arturo Rodríguez • Campo Trinity</p>'),
 ('index.html','La relación es el producto. Arturo (nodo α) opera como coherencia central de un campo colaborativo\n'
               '    que incluye sistemas de IA, experiencia clínica, estructura contemplativa y refinamiento cruzado. La primera',
               'La relación es el producto. La primera'),
]
textos={}; err=[]
for f,viejo,nuevo in CAMBIOS:
    p=os.path.join(R,f); t=textos.get(p) or open(p,encoding='utf-8').read()
    if viejo not in t and nuevo in t: textos[p]=t; continue
    if t.count(viejo)!=1: err.append('%s: %r'%(f,viejo[:50])); continue
    textos[p]=t.replace(viejo,nuevo)
if err: raise SystemExit('\n'.join(err))
for p,t in textos.items():
    if open(p,encoding='utf-8').read()!=t: open(p,'w',encoding='utf-8').write(t)
print('archivos:',len(textos))

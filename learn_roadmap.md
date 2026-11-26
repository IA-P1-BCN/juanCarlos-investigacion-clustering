# 🗺️ Roadmap de aprendizaje — Taller de Clustering

El taller sigue las **fases de un proyecto de datos**. Cada fase es **una branch**. Primero se hace 🍄 **Setas** entero y después 💳 **Tarjetas**.

    Comprender → Preparar → Explorar → Modelar → Evaluar → Interpretar → Entregar

Se trabaja en los notebooks de la **raíz** (`workshop-setas.ipynb`, `workshop-tarjetas.ipynb`), que **solo muestran la fase actual**: las anteriores quedan como un título con su resumen y su código plegado en una celda (se ejecuta, pero no se ve). Las plantillas de [`docs/workshop/`](docs/workshop/README.md) quedan como enunciado.

## 🔁 Ciclo de cada branch
1. **Claude** crea la branch desde `main`, añade al notebook las celdas de esa fase y las ejecuta con `uv`.
2. **Claude** explica el código y los resultados.
3. **Tú** lo replicas en VS Code (kernel `Python (clustering-uv)`) y respondes las preguntas de control.
4. Cuando digas **«entendido»**: se actualiza el [log de aprendizaje](learn_log.md), commit `taller(NN): ...`, `merge --no-ff` a `main`, ✅ en el progreso y **push a GitHub** (`main` + la branch).

> La salida esperada son los valores de referencia del bootcamp (NotebookLM «FactoriaF5»).

---

## 🍄 Parte 1 — Setas (`workshop-setas.ipynb`)
Problema: ¿se agrupan solas las setas en comestibles y venenosas? La etiqueta `class` **solo se usa para validar**.

| # | Branch | Fase | Qué se hace | Salida esperada | ❓ Preguntas de control |
|---|---|---|---|---|---|
| 01 | `01-setas-comprension` | Comprender | Carga, `describe`, `info`, nulos | 8124 × 23, todo texto, 0 nulos *aparentes* | ¿Supervisado o no supervisado? ¿Para qué sirve aquí la etiqueta? |
| 02 | `02-setas-preparacion` | Preparar | `'?'` → moda, quitar `veil-type`, `X`/`y`, One-Hot (`get_dummies`), train/test | `?` = 2480 en `stalk-root`; 115 columnas | ¿Por qué `isnull()` no vio los `'?'`? ¿Por qué One-Hot? |
| 03 | `03-setas-exploracion` | Explorar | PCA 2D, Random Forest como línea base, nº de componentes, t-SNE | Grupos separados; RF ≈ 100 %; ~10 componentes bastan | ¿Qué es una componente principal? ¿Por qué t-SNE solo sirve para visualizar? |
| 04 | `04-setas-modelado` | Modelar | K-Means (codo + silueta), Aglomerativo + dendrograma, GMM, DBSCAN euclídea vs Jaccard | k = 2; DBSCAN euclídea = 1 cluster, Jaccard sí separa | ¿Inercia o silueta? ¿Qué controlan `eps` y `min_samples`? |
| 05 | `05-setas-evaluacion` | Evaluar | ARI/NMI, métricas internas, scatter clusters vs etiqueta | ARI ≈ 0,62 · NMI ≈ 0,57; Jaccard ARI ≈ 0,29 | ¿Qué mide el ARI? ¿Davies-Bouldin es mejor alto o bajo? |
| 06 | `06-setas-interpretacion` | Interpretar | Isolation Forest + conclusiones de Setas | ≈ 5 % de anomalías | ¿Por qué Jaccard va mejor con datos 0/1? ¿Qué es una anomalía? |

## 💳 Parte 2 — Tarjetas (`workshop-tarjetas.ipynb`)
Problema: segmentar clientes para marketing. **No hay etiqueta.**

| # | Branch | Fase | Qué se hace | Salida esperada | ❓ Preguntas de control |
|---|---|---|---|---|---|
| 07 | `07-tarjetas-comprension` | Comprender | Carga, `shape`, `describe`, `dtypes`, nulos | 8950 × 18, numérico; nulos en `CREDIT_LIMIT` (1) y `MINIMUM_PAYMENTS` (313) | ¿Qué cambia frente a Setas? ¿Por qué `CUST_ID` no sirve? |
| 08 | `08-tarjetas-preparacion` | Preparar | Quitar `CUST_ID`, nulos → mediana, histogramas (sesgo), `StandardScaler` | Colas largas; variables con media 0 y desviación 1 | ¿Por qué la mediana? ¿Qué pasa en K-Means sin escalar? |
| 09 | `09-tarjetas-exploracion` | Explorar | Scree plot (varianza acumulada), PCA 2D | ~7 componentes ≈ 80 %; **nube continua** | ¿Por qué aquí no se ven grupos claros? |
| 10 | `10-tarjetas-modelado` | Modelar | K-Means (codo + silueta), Aglomerativo + dendrograma, GMM, DBSCAN | k = 3; DBSCAN ≈ 1 cluster + ruido | ¿Cuándo elegirías DBSCAN en vez de K-Means? |
| 11 | `11-tarjetas-evaluacion` | Evaluar | Silueta, Davies-Bouldin, Calinski-Harabasz, t-SNE por cluster | Silueta ≈ 0,25 con k = 3 | ¿Por qué no se puede calcular el ARI? |
| 12 | `12-tarjetas-interpretacion` | Interpretar | **Heatmap de perfiles → nombre y estrategia por segmento** (entregable) + Isolation Forest | Poco activos (~68 %) · VIP (~14 %) · Riesgo por adelantos (~17 %) · ≈ 5 % atípicos | ¿Qué campaña harías con cada segmento? ¿Un atípico es error, fraude o VIP? |

## 🏁 Entrega
| # | Branch | Qué se hace |
|---|---|---|
| 13 | `13-entrega` | Los dos notebooks se ejecutan de arriba abajo sin errores + celda final con el **contraste Setas vs Tarjetas** (❓ ¿por qué no hay un algoritmo que gane siempre?) |

---

## ✅ Progreso
- 🍄 [x] 01 · [x] 02 · [x] 03 · [x] 04 · [x] 05 · [x] 06
- 💳 [x] 07 · [x] 08 · [x] 09 · [ ] 10 · [ ] 11 · [ ] 12
- 🏁 [ ] 13

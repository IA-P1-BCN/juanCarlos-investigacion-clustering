# Investigación sobre Algoritmos de Clustering

[![Abrir en NotebookLM](https://img.shields.io/badge/Abrir_en-NotebookLM-4285F4?style=for-the-badge&logo=notebooklm&logoColor=white)](https://notebook.google.com/notebook/51ec9ffc-637f-413e-9a76-d7a5848479d6)

Investigación técnica sobre algoritmos de aprendizaje no supervisado enfocados en **clustering**, sus principales paradigmas, criterios de evaluación, hiperparámetros, ventajas, desventajas y aplicaciones en el mundo real.

## Índice

1. [Aprendizaje no supervisado, clustering y diferencias con el supervisado](#1-aprendizaje-no-supervisado-clustering-y-diferencias-con-el-supervisado)
2. [Clustering particional (centroides) vs. clustering jerárquico](#2-clustering-particional-centroides-vs-clustering-jerárquico)
3. [Clustering basado en densidad (DBSCAN)](#3-clustering-basado-en-densidad-dbscan)
4. [Importancia de los hiperparámetros y evaluación de la calidad](#4-importancia-de-los-hiperparámetros-y-evaluación-de-la-calidad)
5. [Análisis detallado de algoritmos de clustering](#5-análisis-detallado-de-algoritmos-de-clustering)
   - [5.1. K-Means](#51-k-means)
   - [5.2. Clustering Jerárquico (Aglomerativo)](#52-clustering-jerárquico-aglomerativo)
   - [5.3. DBSCAN](#53-dbscan)
   - [5.4. Gaussian Mixture Models (GMM)](#54-gaussian-mixture-models-gmm)
   - [5.5. Tabla comparativa resumen](#55-tabla-comparativa-resumen)
6. [Referencias](#6-referencias)

---

## 1. Aprendizaje no supervisado, clustering y diferencias con el supervisado

### ¿Qué es el aprendizaje no supervisado?
El **aprendizaje no supervisado** (*unsupervised learning*) es una rama del *Machine Learning* en la que los algoritmos analizan conjuntos de **datos no etiquetados** (*unlabeled data*) sin supervisión humana previa. Su objetivo es descubrir patrones ocultos, relaciones latentes y estructuras naturales a partir de las similitudes y diferencias inherentes a las variables de entrada. Sus tres tareas fundamentales son el **clustering**, las **reglas de asociación** y la **reducción de dimensionalidad**.

### ¿Qué es un algoritmo de clustering?
Un **algoritmo de clustering** (agrupamiento) organiza un conjunto de observaciones sin etiquetas en grupos llamados **clústeres**, de modo que los elementos dentro de un mismo clúster presenten una **alta similitud entre sí** (alta cohesión interna) y una **baja similitud con los elementos de otros clústeres** (alta separación). Como resultado, a cada observación se le asigna un identificador de grupo (*cluster ID*).

Según cómo se asigna la pertenencia, existen dos modalidades principales:
- **Agrupamiento rígido o exclusivo (*hard clustering*):** cada observación pertenece a un único clúster (por ejemplo, K-Means).
- **Agrupamiento suave o probabilístico (*soft clustering*):** cada observación recibe un grado de pertenencia o probabilidad de pertenecer a cada clúster (por ejemplo, *Gaussian Mixture Models*).

### Diferencias frente al aprendizaje supervisado

| Criterio | Aprendizaje Supervisado | Aprendizaje No Supervisado (Clustering) |
| :--- | :--- | :--- |
| **Datos de entrada** | **Datos etiquetados:** cada observación incluye variables predictoras (*features*) y una etiqueta objetivo conocida (*ground truth*), lo que suele requerir etiquetado humano previo. | **Datos no etiquetados:** solo existen variables de entrada (*features*), sin clases ni valores objetivo predefinidos. |
| **Objetivo principal** | Aprender una función que relacione entradas y salidas para **predecir** valores futuros (regresión) o **clasificar** nuevas muestras en categorías conocidas. | **Descubrir estructuras subyacentes**, agrupaciones naturales, taxonomías o relaciones de proximidad presentes en los datos. |
| **Evaluación** | Directa y determinista contra la etiqueta real mediante funciones de pérdida, *accuracy*, precisión, *recall* o error cuadrático. | Más compleja al carecer habitualmente de *ground truth*; se apoya en **métricas intrínsecas** (inercia, silueta, Davies-Bouldin, Calinski-Harabasz) e **interpretabilidad** en el dominio del problema (y solo en **métricas extrínsecas** como ARI o NMI cuando existen etiquetas de control). |

### Propósito del clustering y aplicaciones reales
El propósito principal del clustering abarca cuatro ejes:
1. **Descubrimiento de agrupaciones naturales:** identificar segmentos o categorías orgánicas en los datos y qué atributos los caracterizan.
2. **Compresión y simplificación de datos:** resumir conjuntos complejos de características mediante un único *cluster ID*.
3. **Preprocesamiento e imputación:** servir como fase previa para modelos posteriores o inferir valores faltantes a partir de observaciones vecinas del mismo grupo.
4. **Preservación de la privacidad:** asociar comportamientos de usuarios a un identificador de grupo compartido en lugar de identificadores individuales.

Entre sus aplicaciones más frecuentes en el mundo real destacan la **segmentación de clientes y marketing** (*buyer personas* y campañas dirigidas), los **sistemas de recomendación y venta cruzada**, la **detección de anomalías y ciberseguridad** (fraude, fallos de equipos o tráfico atípico), la **segmentación y compresión de imágenes**, la **bioinformática e investigación clínica** (estratificación de pacientes, análisis genético y filogenético), la **agrupación temática de documentos/noticias** y la **detección de comunidades en redes sociales**.

---

## 2. Clustering particional (centroides) vs. clustering jerárquico

Ambos enfoques persiguen agrupar observaciones similares, pero parten de filosofías estructurales y computacionales muy distintas:

| Dimensión | Clustering Particional (Basado en Centroides) | Clustering Jerárquico |
| :--- | :--- | :--- |
| **Estructura resultante** | **Partición plana y no jerárquica:** divide $N$ observaciones en $K$ clústeres disjuntos representados por un centro o centroide. | **Árbol de clústeres anidados (jerarquía):** desde hojas individuales (*singletons*) hasta una única raíz global, sin imponer un único nivel de partición fijo. |
| **Definición de $k$ a priori** | **Obligatorio** especificar $k$ antes de ejecutar el algoritmo. | **No es obligatorio** para construir la jerarquía; el número de clústeres se decide a posteriori cortando el árbol a la altura deseada. |
| **Representación visual** | Regiones geométricas en el espacio de características (teselación de Voronoi en K-Means). | **Dendrograma:** diagrama arbóreo donde el eje vertical refleja la distancia o disimilitud de cada fusión o división. |
| **Dirección del proceso** | Optimización iterativa global de una función objetivo (p. ej., minimizar distancias a centroides). | **Aglomerativo (*bottom-up*):** fusiona pares más cercanos desde $N$ clústeres hasta 1.<br>**Divisivo (*top-down*):** divide recursivamente desde 1 clúster global hasta $N$ hojas. |
| **Criterio de similitud entre grupos** | Distancia directa entre cada observación y el centroide de cada grupo (habitualmente euclídea). | **Criterio de enlace (*linkage*):** *Ward* (minimiza incremento de varianza intra-clúster), *Complete* (distancia máxima), *Average* (distancia media entre todos los pares), *Single* (distancia mínima, propenso al efecto de encadenamiento o *chaining*) o *Centroid*. |
| **Escalabilidad** | **Alta:** complejidad lineal $O(n)$ por iteración en K-Means (con variantes como *MiniBatchKMeans* para grandes volúmenes). | **Limitada en su forma estándar:** coste típico de $O(n^2)$ en tiempo y memoria por la matriz de distancias por pares (mejorable con restricciones de conectividad local). |

### Algoritmos representativos

- **Enfoque particional — K-Means (algoritmo de Lloyd):**
  1. Fija $k$ y selecciona $k$ centroides iniciales (de forma aleatoria o mediante **k-means++**, que dispersa los centros iniciales para evitar mínimos locales pobres).
  2. **Paso de asignación:** asigna cada punto al centroide más cercano (distancia euclídea).
  3. **Paso de actualización:** recalcula cada centroide como la media aritmética de los puntos asignados a ese grupo.
  4. Repite ambos pasos hasta que los centroides convergen o se alcanza el límite de iteraciones, minimizando la **inercia** (suma de distancias euclídeas al cuadrado dentro de cada clúster).

- **Enfoque jerárquico — Clustering Jerárquico Aglomerativo (AGNES):**
  1. Inicia considerando cada una de las $N$ observaciones como un clúster individual (*singleton*).
  2. Calcula la matriz de disimilitud (distancias por pares: euclídea, Manhattan, coseno, etc.).
  3. Fusiona de forma voraz (*greedy*) el par de clústeres con menor distancia según el criterio de *linkage* elegido (*Ward, complete, average* o *single*).
  4. Actualiza la matriz de distancias y repite el paso anterior hasta obtener un único clúster raíz, dejando registrado todo el proceso en el **dendrograma**.

---

## 3. Clustering basado en densidad (DBSCAN)

El **clustering basado en densidad** define los clústeres como **regiones contiguas de alta densidad de puntos separadas por zonas de baja densidad o vacías**. En lugar de imponer formas esféricas o construir árboles de fusión, algoritmos como **DBSCAN** (*Density-Based Spatial Clustering of Applications with Noise*) expanden los grupos siguiendo la **conectividad por densidad** (*density-connectedness*).

### Hiperparámetros clave de DBSCAN
La definición formal de "región densa" depende de dos hiperparámetros:
- **`eps` ($\varepsilon$):** radio de vecindad alrededor de un punto; fija la distancia máxima para considerar que otro punto es su vecino. Un `eps` demasiado pequeño marca casi todo como ruido, mientras que uno demasiado grande fusiona clústeres distintos en un único bloque. Suele estimarse con el gráfico de distancias al $k$-ésimo vecino más cercano ($k = \text{min\_samples} - 1$).
- **`min_samples` ($MinPts$):** número mínimo de puntos requeridos dentro del radio $\varepsilon$ (incluyendo al propio punto) para que esa región sea considerada densa. Regula la tolerancia al ruido; valores altos exigen mayor concentración y suelen ser preferibles en datasets grandes o ruidosos (como heurística inicial se suele usar $MinPts \ge D + 1$ o $2 \cdot D$, siendo $D$ la dimensionalidad, con un mínimo de 3).

### Clasificación de los puntos
A partir de `eps` y `min_samples`, DBSCAN clasifica cada observación en una de tres categorías:
1. **Puntos núcleo (*core points*):** tienen al menos `min_samples` puntos dentro de su vecindad de radio `eps`. Son el motor a partir del cual se expande cada clúster conectando puntos núcleo vecinos.
2. **Puntos de borde (*border / non-core points*):** tienen menos de `min_samples` vecinos en su propio radio `eps`, pero caen dentro del radio `eps` de al menos un punto núcleo. Forman la periferia del clúster, pero no lo expanden.
3. **Ruido o valores atípicos (*noise / outliers*):** puntos que no son núcleo ni son alcanzables por densidad desde ningún punto núcleo. En implementaciones estándar como scikit-learn reciben la etiqueta `-1`.

### Diferencias frente al clustering por centroides y al jerárquico

| Aspecto | Basado en Densidad (DBSCAN) | Basado en Centroides (K-Means) | Jerárquico (Aglomerativo) |
| :--- | :--- | :--- | :--- |
| **Forma de los clústeres** | Detecta **formas arbitrarias, no convexas, alargadas o concéntricas**. | Asume clústeres **convexos e isotrópicos** (esféricos); falla en geometrías complejas. | Depende del *linkage*: *Ward* y *Complete* favorecen formas compactas/globulares; *Single* detecta formas no globulares, pero sufre efecto de encadenamiento (*chaining*). |
| **Número de clústeres ($k$)** | **No requiere fijar $k$ a priori**; surge automáticamente de la densidad local. | **Requiere definir $k$ obligatoriamente** antes de entrenar. | No lo requiere para construir el árbol, pero sí para definir el corte final del dendrograma. |
| **Manejo de ruido y *outliers*** | **Nativo y robusto:** aísla explícitamente los atípicos como ruido (`-1`). | **Particionamiento forzoso:** todo punto se asigna a un centroide, por lo que los *outliers* desplazan la media y deforman los grupos. | Asigna todos los puntos al árbol; el ruido puede crear puentes artificiales entre grupos (especialmente en *single linkage*). |
| **Densidades variables** | **Principal debilidad:** al usar un único umbral global (`eps`, `min_samples`), tiene dificultades severas si coexisten clústeres muy densos y muy dispersos (lo que motiva extensiones como OPTICS o HDBSCAN). | También sufre con tamaños y densidades muy dispares, sesgando centroides hacia clústeres más grandes. | El dendrograma permite inspeccionar agrupaciones a múltiples escalas de distancia, aunque *Ward* tiende a equilibrar tamaños. |

---

## 4. Importancia de los hiperparámetros y evaluación de la calidad

### ¿Por qué es crítica la elección de $k$ y de los hiperparámetros?
Al no disponer de etiquetas de referencia (*ground truth*) que corrijan el entrenamiento, la estructura descubierta depende directamente de los hiperparámetros elegidos:
- **En K-Means y GMM:** un valor de $k$ (o `n_components`) demasiado bajo fusiona subgrupos heterogéneos y oculta estructura real; un valor demasiado alto sobresegmenta grupos naturales en particiones artificiales. En GMM, además, el tipo de covarianza (*spherical, tied, diag, full*) controla la flexibilidad geométrica y evita singularidades o sobreajuste.
- **En DBSCAN:** una mala calibración de `eps` y `min_samples` puede colapsar todo el dataset en ruido (`-1`) o en un único megaclúster sin valor analítico.
- **En Jerárquico Aglomerativo:** el criterio de *linkage* y la métrica de distancia determinan radicalmente la geometría y sensibilidad al ruido del dendrograma resultante.

### Métodos de evaluación de la calidad del agrupamiento

Al no existir etiquetas reales en escenarios típicos, se utilizan **métricas intrínsecas (internas)** basadas únicamente en los datos y las asignaciones obtenidas:

#### 1. Método del Codo (*Elbow Method*) — basado en Inercia (WCSS / SSE)
- **Métrica subyacente (Inercia):** suma de las distancias euclídeas al cuadrado desde cada observación $x_i$ hasta el centroide $\mu_j$ de su clúster asignado (*Within-Cluster Sum of Squares*):

$$\text{Inercia (WCSS)} = \sum_{i=0}^{N-1} \min_{\mu_j \in C} \left( \|x_i - \mu_j\|^2 \right)$$

- **Funcionamiento:** se entrena el algoritmo (típicamente K-Means) para distintos valores de $k$ y se grafica la inercia frente a $k$. Como la inercia disminuye siempre de forma monotónica conforme aumenta $k$ (hasta llegar a 0 cuando $k = N$), se busca el punto de inflexión o **"codo"** donde la ganancia marginal de reducir la dispersión interna se estabiliza notablemente.
- **Limitaciones:** no es una métrica normalizada, asume clústeres convexos e isotrópicos, se ve afectada por la maldición de la dimensionalidad en espacios de alta dimensión y, en datos reales, el "codo" suele ser suave o subjetivo.

#### 2. Coeficiente de Silueta (*Silhouette Score / Analysis*)
- **Fundamento (Cohesión vs. Separación):** evalúa simultáneamente qué tan compacto es el clúster al que pertenece una muestra $i$ y qué tan separada está del clúster vecino más próximo:
  - $a(i)$: distancia media entre el punto $i$ y todos los demás puntos de **su mismo clúster** (**cohesión intra-clúster**; menor es mejor).
  - $b(i)$: distancia media entre el punto $i$ y todos los puntos del **clúster vecino más cercano** al que no pertenece (**separación inter-clúster**; mayor es mejor).
- **Fórmula:**

$$s(i) = \frac{b(i) - a(i)}{\max\big(a(i),\, b(i)\big)}$$

  El **Silhouette Score** global es la media de $s(i)$ sobre todas las muestras del conjunto de datos.
- **Rango e interpretación ($[-1, 1]$):**
  - **Cercano a $+1$:** muestra muy bien agrupada en su clúster y bien separada de los vecinos.
  - **Cercano a $0$:** muestra sobre o muy próxima a la frontera de decisión entre dos clústeres (solapamiento).
  - **Valores negativos (hasta $-1$):** probable asignación incorrecta (el punto está en promedio más cerca de un clúster vecino que del suyo).
- **Ventaja del análisis visual:** el diagrama de siluetas permite inspeccionar además el grosor (tamaño) y la uniformidad de cada clúster individual para descartar valores de $k$ con clústeres por debajo del promedio o con puntuaciones negativas. Como precaución, tiende a favorecer clústeres convexos frente a clústeres de formas arbitrarias como los de DBSCAN.

#### Otras métricas internas complementarias
- **Índice de Calinski-Harabasz (*Variance Ratio Criterion*):** cociente entre la dispersión entre clústeres y la dispersión intra-clúster; es rápido de calcular y **valores más altos** indican clústeres más densos y mejor separados.
- **Índice de Davies-Bouldin:** mide la similitud promedio entre cada clúster y su clúster más parecido (comparando dispersiones internas frente a la distancia entre centroides); su mínimo es `0` y **valores más cercanos a 0** reflejan mejor partición.
- **Criterios de información BIC y AIC (específicos para GMM):** equilibran la log-verosimilitud del modelo con una penalización por complejidad (número de parámetros), permitiendo seleccionar simultáneamente `n_components` y el tipo de covarianza buscando el **valor mínimo de BIC/AIC**.

---

## 5. Análisis detallado de algoritmos de clustering

### 5.1. K-Means
- **Mecanismo de funcionamiento:** algoritmo particional de agrupamiento rígido (*hard clustering*) que divide $N$ observaciones en $K$ clústeres minimizando la **inercia** (WCSS). A través del algoritmo de Lloyd alterna de forma iterativa dos pasos —asignar cada punto al centroide más cercano (distancia euclídea) y recalcular cada centroide como la media de sus puntos— hasta converger. Suele combinarse con inicialización **k-means++** para evitar mínimos locales desfavorables.
- **Ventajas:**
  - Muy eficiente y escalable: complejidad lineal $O(n)$ por iteración, paralelizable y extensible a datos masivos mediante *MiniBatchKMeans*.
  - Sencillo de implementar, interpretar y aplicar en espacios continuos.
- **Desventajas:**
  - Requiere fijar $K$ *a priori* y converge a mínimos locales dependientes de la inicialización.
  - Asume clústeres convexos, esféricos y de varianza similar; falla con formas alargadas o no lineales.
  - Muy sensible a *outliers* (distorsionan las medias) y a la maldición de la dimensionalidad si no se escalan o reducen las variables.
- **Casos de uso comunes:** segmentación de clientes y mercados, compresión de imágenes y cuantización vectorial, y agrupación de documentos de texto a gran escala.

### 5.2. Clustering Jerárquico (Aglomerativo)
- **Mecanismo de funcionamiento:** enfoque ascendente (*bottom-up*) que comienza con cada observación en su propio clúster y fusiona iterativamente el par de clústeres más cercanos según una matriz de disimilitud y un criterio de **enlace (*linkage*)** (*Ward*, *Complete*, *Average* o *Single*), hasta converger en un único clúster raíz. La secuencia de fusiones se representa en un **dendrograma**, que puede cortarse a cualquier altura. Admite además matrices de conectividad local para respetar estructuras de variedades.
- **Ventajas:**
  - No exige fijar $K$ por adelantado y proporciona una visión multiescala completa mediante el dendrograma.
  - Con enlaces como *single*, *complete* o *average* admite métricas no euclídeas (Manhattan $L_1$, coseno, etc.).
  - Las restricciones de conectividad permiten capturar geometrías complejas y reducir el coste computacional.
- **Desventajas:**
  - Alto coste computacional y de memoria en su versión estándar ($O(n^2)$), poco práctico para conjuntos muy grandes sin restricciones de conectividad.
  - Decisiones voraces (*greedy*) e irreversibles: una fusión temprana errónea no puede deshacerse.
  - *Single linkage* es muy vulnerable al ruido y al efecto de encadenamiento (*chaining effect*); otros enlaces pueden producir clústeres desequilibrados.
- **Casos de uso comunes:** bioinformática, genómica y análisis filogenético/taxonómico, estratificación clínica de cohortes de pacientes y aglomeración de variables (*feature agglomeration*) para reducir dimensionalidad.

### 5.3. DBSCAN
- **Mecanismo de funcionamiento:** algoritmo basado en densidad (*Density-Based Spatial Clustering of Applications with Noise*) que agrupa observaciones conectadas en regiones densas definidas por `eps` (radio de vecindad) y `min_samples` (mínimo de puntos en ese radio). Identifica **puntos núcleo** (que expanden clústeres por conectividad por densidad), **puntos de borde** (en el radio de un núcleo, sin expandir) y **ruido / *outliers*** (etiquetados como `-1`).
- **Ventajas:**
  - Descubre clústeres de formas arbitrarias, cóncavas o concéntricas sin asumir esfericidad.
  - No requiere especificar el número de clústeres $K$ de antemano.
  - Detecta y aísla de forma nativa el ruido y los *outliers*.
  - Con estructuras espaciales (*k-d trees* o *ball trees*) alcanza una complejidad media de $O(n \log n)$.
- **Desventajas:**
  - Dificultades severas cuando el dataset contiene clústeres con **densidades muy diferentes** entre sí.
  - Alta sensibilidad a la elección de `eps` y `min_samples`.
  - Los puntos de borde alcanzables por dos clústeres distintos pueden cambiar de asignación según el orden de los datos.
  - Pierde eficacia en espacios de muy alta dimensión por la degradación de las distancias euclídeas.
- **Casos de uso comunes:** detección de anomalías y filtrado de ruido, análisis de datos geoespaciales y trayectorias (con métricas como *great-circle distance*), y segmentación de regiones complejas en visión artificial.

### 5.4. Gaussian Mixture Models (GMM)
- **Mecanismo de funcionamiento:** modelo probabilístico generativo de agrupamiento suave (**soft clustering**) que asume que los datos proceden de una combinación finita de distribuciones gaussianas multivariadas. En lugar de asignar cada punto a un único grupo de forma rígida, realiza una **asignación probabilística** (responsabilidades) que cuantifica la probabilidad de que cada observación haya sido generada por cada componente. Sus parámetros (pesos, medias y matrices de covarianza) se estiman iterativamente con el algoritmo **Expectation-Maximization (EM)**:
  - **Paso E (*Expectation*):** calcula las probabilidades posteriores de pertenencia de cada dato a cada gaussiana.
  - **Paso M (*Maximization*):** actualiza medias, pesos y matrices de covarianza para maximizar la log-verosimilitud.
  
  Generaliza a K-Means al permitir covarianzas *spherical*, *diag*, *tied* o *full* (modelando elipsoides con orientación y tamaño flexibles).
- **Ventajas:**
  - **Asignación probabilística (*soft clustering*):** captura incertidumbre y solapamiento natural entre grupos.
  - Modela clústeres elípticos de distintas formas, tamaños y orientaciones gracias a las matrices de covarianza.
  - Permite seleccionar el número de componentes y el tipo de covarianza de forma fundamentada mediante **BIC/AIC** (o inferirlo automáticamente con la variante bayesiana *BayesianGaussianMixture*).
- **Desventajas:**
  - Riesgo de **singularidades matemáticas** en matrices de covarianza si una componente tiene muy pocas muestras (requiere regularización).
  - Asume que las distribuciones subyacentes son aproximadamente gaussianas; puede desajustarse ante geometrías no gaussianas.
  - Mayor coste computacional que K-Means, especialmente en alta dimensión con covarianza *full*.
  - Converge a mínimos locales según la inicialización de sus centros.
- **Casos de uso comunes:** estimación de densidad y generación sintética de muestras, segmentación de perfiles o contenidos con solapamiento natural (intereses híbridos) y detección probabilística de anomalías (observaciones con densidad conjunta muy baja).

---

### 5.5. Tabla comparativa resumen

| Algoritmo | Enfoque y asignación | Hiperparámetros principales | ¿Requiere $K$ a priori? | Formas de clúster | Manejo de *outliers* | Escalabilidad típica | Casos de uso destacados |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **K-Means** | Particional por centroides (*hard*) | `n_clusters` ($K$), inicialización (*k-means++*) | **Sí** | Convexas / esféricas de varianza similar | Bajo (distorsionan centroides) | **Muy alta** — $O(n)$ por iteración (*MiniBatch*) | Segmentación de clientes, compresión de imágenes, minería de texto |
| **Jerárquico Aglomerativo** | Jerárquico *bottom-up* (*hard* por corte) | `linkage` (*Ward, complete, average, single*), métrica de distancia, conectividad | **No** *(se elige al cortar el dendrograma)* | Globulares (*Ward/Complete*) o no globulares (*Single*, con riesgo de *chaining*) | Bajo–moderado (sensible en *single linkage*) | **Baja–media** — $O(n^2)$ sin conectividad | Bioinformática/filogenética, cohortes clínicas, *feature agglomeration* |
| **DBSCAN** | Basado en densidad (*hard* + ruido) | `eps` ($\varepsilon$), `min_samples` ($MinPts$), métrica de distancia | **No** | **Arbitrarias**, no convexas, concéntricas | **Excelente** (etiqueta ruido como `-1`) | **Media–alta** — $O(n \log n)$ con índices espaciales | Detección de anomalías, datos geoespaciales, visión artificial |
| **GMM** | Probabilístico generativo (*soft*) | `n_components`, `covariance_type` (*full, tied, diag, spherical*) | **Sí** *(orientable con BIC/AIC o variante bayesiana)* | Elipsoides con orientación y tamaño flexibles | Moderado (modelable vía baja densidad) | **Media** (costoso en alta dimensión con `full`) | Estimación de densidad, segmentación difusa solapada, anomalías probabilísticas |

---

## 6. Referencias

Fuentes técnicas oficiales consultadas y sintetizadas mediante NotebookLM:

- scikit-learn Documentation — [2.3. Clustering](https://scikit-learn.org/stable/modules/clustering.html)
- scikit-learn Documentation — [2.1. Gaussian mixture models](https://scikit-learn.org/stable/modules/mixture.html)
- scikit-learn Documentation — [Selecting the number of clusters with silhouette analysis on KMeans clustering](https://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_silhouette_analysis.html)
- scikit-learn Documentation — [Demo of DBSCAN clustering algorithm](https://scikit-learn.org/stable/auto_examples/cluster/plot_dbscan.html)
- scikit-learn Documentation — [Gaussian Mixture Model Selection (BIC)](https://scikit-learn.org/stable/auto_examples/mixture/plot_gmm_selection.html)
- Google for Developers (ML Crash Course) — [Supervised Learning](https://developers.google.com/machine-learning/intro-to-ml/supervised)
- Google for Developers (ML Crash Course) — [What is clustering?](https://developers.google.com/machine-learning/clustering/overview)
- Google for Developers (ML Crash Course) — [Clustering algorithms](https://developers.google.com/machine-learning/clustering/clustering-algorithms)
- IBM Think — [What Is Unsupervised Learning?](https://www.ibm.com/think/topics/unsupervised-learning)
- IBM Think — [What is clustering?](https://www.ibm.com/think/topics/clustering)
- IBM Think — [What is k-means clustering?](https://www.ibm.com/think/topics/k-means-clustering)
- IBM Think — [What is Hierarchical Clustering?](https://www.ibm.com/think/topics/hierarchical-clustering)
- Wikipedia — [DBSCAN](https://en.wikipedia.org/wiki/DBSCAN)

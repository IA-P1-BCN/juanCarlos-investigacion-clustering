# 📓 Log de aprendizaje — Taller de Clustering

Diario de lo aprendido en cada fase del [roadmap](learn_roadmap.md). En cada fase:

- **Lo aprendido:** las ideas clave.
- **Preguntas de control:** mis respuestas, con su resultado (✅ bien, 🟡 a medias, ❌ mal) y la respuesta completa.
- **Mis preguntas:** las dudas que planteé por el camino.

---

## 🍄 Fase 01 · Comprensión del problema y de los datos

**Lo aprendido**
- El dataset tiene **8124 setas × 23 columnas**, todas de **texto** (letras-código), y `isnull()` dice **0 nulos**.
- Es un problema **no supervisado**: buscamos grupos sin decirle al modelo la respuesta.

**Preguntas de control**

| Pregunta | Mi respuesta | | Respuesta completa |
|---|---|---|---|
| ¿Supervisado o no supervisado? | «Es no supervisado» | ✅ | Agrupamos sin usar la etiqueta para entrenar. |
| ¿Para qué sirve aquí la etiqueta `class`? | «La guardamos para poder comprobar después nuestro acierto» | ✅ | Solo para **validar** al final (ARI/NMI), nunca para entrenar. |

---

## 🍄 Fase 02 · Preparación de los datos

**Lo aprendido**
- **Hay que buscar los problemas de forma sistemática.** Se miran los valores únicos de **todas** las columnas y se cuentan los `'?'` en todo el DataFrame.
  - Solo `stalk-root` tiene `'?'`: **2480 veces**. Los sustituimos por la **moda** (`'b'`).
- `veil-type` tiene un **solo valor**, así que no distingue nada y se quita.
- **One-Hot** (`get_dummies`): **115 columnas** de 0/1. Luego **train/test**: 5443 / 2681 filas.

**Preguntas de control**

| Pregunta | Mi respuesta | | Respuesta completa |
|---|---|---|---|
| ¿Por qué `isnull()` no vio los `'?'`? | «Los `?` no son nulos, son strings, mala conversión» | ✅ | Es un **nulo encubierto**: para pandas `'?'` es un texto válido. |
| ¿Por qué One-Hot? | «Porque los modelos usan números y porque evitamos cualquier orden» | ✅ | Si pasamos las letras a 1, 2, 3…, el modelo creería que hay un orden que no existe. |

**Mis preguntas**
- **«¿Por qué sabes que `stalk-root` tiene valores raros? ¿Quién te lo indica?»**
  → Lo sabía por el enunciado y por la documentación del dataset (UCI). En un proyecto real nadie te lo dice. Por eso añadimos la **búsqueda sistemática** en todas las columnas. Consultar la documentación también forma parte del EDA.
- **`NameError: name 'pd' is not defined`**
  → No se había ejecutado la celda plegada de las fases anteriores. Hay que usar **Run All** (añadimos el aviso ▶️ en cada fase plegada).

---

## 🍄 Fase 03 · Exploración y reducción de dimensionalidad

**Lo aprendido**
- **PCA 2D:** PC1 + PC2 guardan solo el **29,6 %** de la varianza, pero ya se ven zonas separadas.
- **Una componente principal es un eje nuevo** que mezcla **las 115 columnas** con pesos.
  - Los pesos más grandes de PC1 son `ring-type_p` +0,29, `bruises_t` +0,27 y `bruises_f` −0,27.
  - A la derecha de PC1 hay un **84 % de comestibles**; a la izquierda, un **95 % de venenosas**. PC1 significa algo así como «cuánto se parece a una seta comestible», y PCA lo encontró **sin ver la etiqueta**.
- **Random Forest = el techo.** Acierta un **100 %**, frente al **51,4 %** de un modelo tonto. La información para separar las setas está en los datos.
- Con **8 componentes** el Random Forest ya acierta el 100 %. Guardar el 95 % de la varianza necesita 40: guardar información no es lo mismo que guardar lo que separa las clases.
- **t-SNE** solo sirve para **visualizar**.

**Preguntas de control**

| Pregunta | Mi respuesta | | Respuesta completa |
|---|---|---|---|
| ¿Qué es una componente principal? | «PCA, resumir variables en pocas» | 🟡 | Eso es PCA. Una **componente** es **un eje nuevo**, mezcla de todas las columnas, en la dirección donde los datos más se diferencian. |
| ¿Por qué t-SNE solo sirve para visualizar? | «Porque no es concluyente» | 🟡 | Solo respeta quién es vecino de quién. El tamaño de las nubes y la distancia entre ellas no significan nada, el resultado cambia con `perplexity` y la semilla, y **no tiene `transform`** para datos nuevos. |
| *Extra:* ¿para qué el Random Forest? | «Para ver dónde llega la reducción del PCA, cuando consigue los mismos resultados que supervisado» | ✅ | Es la **línea base o techo**: demuestra que hay información (1,000 frente a 0,514) y cuántas componentes bastan. |
| ¿Qué representa el eje X (PC1)? ¿Es una columna del CSV? | «Es la columna con más datos» | ❌ | No es una columna: es una **receta que mezcla las 115**. Las 115 tienen peso. |
| Si en t-SNE dos nubes salen muy lejos, ¿son muy distintas? | «No, porque solo que no son vecinos» | ✅ | Las distancias grandes no se respetan. |
| Una seta con `ring-type_p` y `bruises_t`, ¿cae a la derecha o a la izquierda? | «Derecha» | ✅ | Los dos pesos son positivos. |
| ¿Qué significado le pondrías a PC1? | «Más calidad» | 🟡 | Ese es el significado del ejemplo de las películas. En las setas, PC1 ≈ «cuánto se parece a una comestible» (84 % comestibles a la derecha). |

**Mis preguntas**
- **«Sé más concreto con el ejemplo del segundo libro (películas).»**
  → El libro aprende 2 números por película con **100.000 notas** (943 usuarios y 1.682 películas) y aplica PCA. Las 25 películas con PC1 más alto están todas muy bien valoradas y las 25 más bajas, mal valoradas: PC1 ≈ «cómo de buena es la película». El significado lo pone una persona al mirar los extremos.
- **«¿Dónde está el dibujo del codo en t-SNE?»**
  → En las diapositivas de t-SNE no hay ningún codo. El **codo** aparece en la fase 04, para elegir k en K-Means.

---

## 🍄 Fase 04 · Modelado

**Lo aprendido**
- **`X_red`** = PCA a 10 componentes sobre todo `X`.
- **K-Means**
  - Reparte las setas alrededor de k centros.
  - La **silueta** sube de 0,26 (k = 2) a 0,48 (k = 7) y el **codo no es claro**: las métricas son **pistas**.
  - **k = 2 lo decide la pregunta** (¿comestible o venenosa?).
- **Aglomerativo:** construye un árbol (dendrograma) que se corta a la altura que quieras.
- **GMM:** da **probabilidades** por grupo. Solo 34 setas tienen duda (ningún grupo pasa del 90 %).
- **DBSCAN**
  - Con distancia euclídea es todo o nada: 130 trocitos con `eps = 0.5`, 1 solo grupo con `eps = 3`.
  - Con **Jaccard** el número de grupos baja poco a poco: con `eps = 0.4` salen 5 grupos casi sin ruido.

**Preguntas de control**

| Pregunta | Mi respuesta | | Respuesta completa |
|---|---|---|---|
| ¿Inercia o silueta? ¿Cuál sirve para comparar k? | «Inercia mide la distancia fuera dentro del grupo y silueta dentro del grupo» | ❌ | Al revés. La **inercia** mira **solo dentro** (distancia a su propio centro) y **siempre baja** al subir k. La **silueta** compara **mi grupo con el vecino**, y por eso sirve para comparar k. |
| ¿Qué controlan `eps` y `min_samples`? | «`min_samples` los grupos, `eps` la distancia del grupo al centro» | 🟡 | DBSCAN no tiene centro ni se le dice el número de grupos. **`eps`** = radio de vecindad alrededor de cada punto. **`min_samples`** = vecinos necesarios para ser **núcleo**. El resto es **ruido (−1)**. |
| Si eligiéramos k por la inercia más baja, ¿qué k saldría? | «k = N» | ✅ | Con k = N la inercia vale 0. En nuestra tabla saldría k = 8, el mayor que probamos: más grupos siempre «mejora» la inercia. |
| ¿Por qué un `eps` pequeño da 130 grupos y 690 de ruido? | «Porque hay muchos valores juntos en zonas alejadas» | 🟡 | Con un radio corto caben pocos vecinos. Solo las zonas muy apretadas llegan a 10 vecinos, y cada una forma su grupito. El resto es ruido. |

---

## 🍄 Fase 05 · Evaluación

**Lo aprendido**
- **Métricas internas** (silueta ↑, Davies-Bouldin ↓, Calinski-Harabasz ↑): miden la **forma** de los grupos y no usan la etiqueta.
- **Métricas externas** (ARI, NMI): comparan con la **realidad**. Solo se pueden usar si hay etiqueta.
- **K-Means k = 2:** ARI = **0,617** y NMI = **0,566**. Aglomerativo y GMM salen casi igual.
- **DBSCAN euclídea** tiene la **mejor silueta (0,357)** y el **peor ARI (0,374)**: grupos bonitos no son lo mismo que grupos útiles. Jaccard dio más ARI (0,443), pero ⚠️ **corregido en la fase 06**: la mejora venía de no usar PCA, no de Jaccard.
- **El ARI mira quién va con quién, no los nombres de los grupos.** Con los nombres al revés da lo mismo (0,617) y un reparto al azar da 0.

**Preguntas de control**

| Pregunta | Mi respuesta | | Respuesta completa |
|---|---|---|---|
| ¿Qué mide el ARI? ¿Por qué no basta un % de aciertos? | «Comprobar la realidad, si aciertan los grupos» | 🟡 | Falta el porqué: el número del cluster es un **nombre arbitrario**. El ARI compara **parejas** y está **ajustado al azar** (azar = 0). |
| ¿Davies-Bouldin, alto o bajo? ¿Por qué DBSCAN euclídea gana en silueta y pierde en ARI? | «Davies bajo, alto Calinski. DBSCAN euclídea: grupos bien formados, pero no tienen por qué ser grupos acertados» | ✅ | Las métricas internas miden forma, no si los grupos responden a la pregunta. |
| Un compañero obtiene los clusters al revés. ¿Qué ARI le sale? | «ARI bajo, porque no cuadran los grupos» | ❌ | **El mismo (0,617)**: hace los mismos grupos con otros nombres. |
| Otro compañero pone 0 1 0 1. ¿ARI alto o bajo? | «Alto, 01 y 01 son una pareja seguida» | ❌ | **Bajo (−0,5).** El ARI no mira el orden de las filas: este compañero junta {A, C} y {B, D}, que mezclan comestibles y venenosas. |
| ¿Por qué el compañero 3 saca menos de 0 con un 50 % de aciertos? | «Las parejas están dispersas… está desagrupada, casi como desordenada» | ✅ | Rompe todas las parejas reales: es **peor que el azar**. Su 50 % es casualidad de los nombres. |

**Mis preguntas**
- **«Añade tú el ejemplo, así lo vemos.»**
  → Añadimos al notebook la celda del ejemplo de juguete. Resultado:
  - Tú: **100 %** de aciertos y ARI **1,00**.
  - Compañero 2 (nombres al revés): **0 %** y ARI **1,00**.
  - Compañero 3 (0 1 0 1): **50 %** y ARI **−0,50**.
  - **El % de aciertos engaña en los dos sentidos; el ARI no.**

---

## 🍄 Fase 06 · Interpretación

**Lo aprendido**
- **Isolation Forest** hace cortes al azar hasta dejar cada punto solo, y lo raro se aísla con **menos cortes**. Con `contamination = 0.05` encontró **407 setas (5 %)**.
  - El 80 % de las raras son comestibles, con combinaciones poco comunes: tallo naranja (47 % frente a 0 % en el resto) o crecen entre hojas (50 % frente a 8 %).
  - **Raro no es lo mismo que error.**
- **Corrección de la fase 05**
  - Cada seta tiene **exactamente 21 unos**, así que Jaccard y la euclídea sobre el one-hot completo dan **los mismos grupos** (mismo ARI, 0,443).
  - La mejora venía de **no reducir con PCA**.
  - Lección: **al comparar, cambia una sola cosa cada vez**.
- **Jaccard ignora los ceros compartidos.** Gana cuando un 0 significa *ausencia* (cestas de la compra, intereses).
  - Con la euclídea, «solo pan» frente a «solo leche» queda a 1,41, igual que dos compras grandes parecidas.
  - Con Jaccard, la primera pareja queda a 1,0 (nada en común) y la segunda a 0,4.

**Preguntas de control**

| Pregunta | Mi respuesta | | Respuesta completa |
|---|---|---|---|
| ¿Por qué Jaccard va mejor con 0/1? ¿Por qué en setas da igual? | «Puedes agrupar más fácilmente; son las dos versiones de la comparación, compartir o diferenciar» | 🟡 | Falta la clave: **ignora los ceros compartidos**. En setas son equivalentes porque todas tienen 21 unos. |
| ¿Qué es una anomalía? ¿Hay que borrar las 407? | «Es un dato alejado de grupos, no implica que esté mal, puede ser algo real pero poco frecuente» | ✅ | Hay que **mirarla** antes de borrarla: puede ser un error, un fraude o algo real y raro. |
| Cestas: ¿qué cuenta la euclídea como «parecido» entre A (pan) y B (leche)? | «Solo que comparten los ceros. ¿Qué pasaría con solo café, o cualquier otro único?» | ✅ | Para la euclídea, todos los clientes de un solo producto quedan a 1,41 entre sí, aunque no compartan nada. |
| ¿Por qué ignorar los ceros tiene sentido en cestas? | «Porque cada producto tiene un valor intrínseco, no es un "rasgo" como en las setas» | ✅ | En una cesta, un 0 es **ausencia**. En una seta, un 0 en `olor_f` **informa**: tiene **otro** olor. |
| Si comparten 16 de 21, ¿en cuántas se diferencian? | «En 5» | ✅ | 21 − 16 = 5. |
| ¿Por qué en setas «compartir» y «diferenciar» dan lo mismo? | «Porque son rasgos únicos, no son valores, entonces son autoexcluyentes» | ✅ | Siempre hay 21 unos, así que comparten + se diferencian = 21. Si sabes una cifra, sabes la otra. |

**Mis preguntas**
- **«Redefine las preguntas con más contexto.»**
  → Rehicimos las preguntas con la tabla de las cestas y el ejemplo del one-hot del olor, para poder contestar sin mirar el notebook.

---

## 🍄 Conclusiones de Setas

| Pregunta | Respuesta |
|---|---|
| ¿Hay información para separar comestibles y venenosas? | **Sí**: Random Forest acierta el 100 % |
| ¿Se separan solas, sin etiqueta? | **En buena parte**: K-Means k = 2 → ARI ≈ 0,62 · NMI ≈ 0,57 |
| ¿Las métricas internas eligen bien? | **No solas**: la mejor silueta tuvo el peor ARI |
| ¿Anomalías? | ≈ 5 %, poco comunes pero reales |

---

## 💳 Fase 07 · Comprensión del problema y de los datos (Tarjetas)

**Lo aprendido**
- Hay **8950 clientes × 18 columnas**, todas **numéricas** salvo `CUST_ID`. **No hay etiqueta**: se valida con métricas internas y mirando si los grupos tienen sentido.
- **`CUST_ID`** tiene **8950 valores distintos**, uno por cliente: es una **matrícula**.
  - Dice *quién* es el cliente, no *cómo* usa la tarjeta.
  - Convertido en número **metería ruido**: C10001 y C10002 quedarían «vecinos» solo por ir seguidos, y su escala de miles se comería la distancia.
- **Escalas muy distintas:** las frecuencias van de 0 a 1 y `CREDIT_LIMIT` llega a 30.000.
- **Colas largas:** en `CASH_ADVANCE` la mediana es 0 y la media, 979.
- **Nulos:** `CREDIT_LIMIT` (1) y `MINIMUM_PAYMENTS` (313).
- **Búsqueda sistemática de valores imposibles:** 0 negativos y **8 clientes con `CASH_ADVANCE_FREQUENCY` > 1**. Todos llevan menos de 12 meses como clientes.

**Preguntas de control**

| Pregunta | Mi respuesta | | Respuesta completa |
|---|---|---|---|
| ¿Qué cambia frente a Setas? | «No tengo la "solución", y de datos string a datos numéricos» | ✅ | Además: hay que **rellenar los nulos y escalar**, y validar con métricas internas. |
| ¿Por qué `CUST_ID` no sirve? | «Tiene 5 valores, no define nada» | 🟡 | No define nada, correcto. Pero tiene **8950 valores distintos**: los 5 eran las filas de `.head()`. |
| *(Aclaración)* | «Me refería a que tiene cinco tipos, pero no nos da ningún dato, aunque hubiera 1000, ¿no?» | ✅ | El problema no es cuántos valores tiene, sino **qué significan**: un ID es un nombre elegido al azar. |
| ¿Qué haría K-Means con el ID convertido en número? | «Nada, serían siempre números diferentes» | 🟡 | No aporta nada **y además hace daño**: agruparía por orden de alta y separaría a clientes idénticos. **Hay que quitarlo.** |

---

## 💳 Fase 08 · Preparación de los datos (Tarjetas)

**Lo aprendido**
- Quitamos `CUST_ID` → quedan 8950 × 17. **Recortamos a 1** (`clip`) las 8 frecuencias imposibles, para no perder clientes.
- **Nulos → mediana:** en `MINIMUM_PAYMENTS` la media es 864 y la mediana 312. Unos pocos extremos (hasta 76.406) tiran de la media.
- **Colas largas** en todas las variables de dinero (asimetría hasta 13,9). Hay que mirar el histograma, no solo `describe()`.
- **`StandardScaler`** deja todas las variables con media 0 y desviación 1.
  - Midiendo 2000 parejas de clientes, sin escalar `CREDIT_LIMIT` aporta el **39,8 %** de la distancia y 9 variables aportan **0,0 %**.
  - Después de escalar, todas aportan entre el 2 % y el 9 %.

**Preguntas de control**

| Pregunta | Mi respuesta | | Respuesta completa |
|---|---|---|---|
| ¿Por qué la mediana y no la media? | «La mediana no se ve afectada por valores extremos» | ✅ | Es el valor del medio: describe mejor a un cliente típico (312 frente a 864). |
| ¿Qué pasa en K-Means sin escalar? | «Los grupos salen muy juntos» | ❌ | El problema es **qué variables deciden**: casi solo el dinero (el límite de crédito, 40 %). Las frecuencias se ignoran. |
| Mismo `CREDIT_LIMIT`, uno compra siempre y otro nunca: sin escalar, ¿parecidos o distintos? | «Parecidos, y uno gasta mucho más que el otro, mejor cliente» | ✅ | La frecuencia (0–1) no pesa nada frente a los miles. Matiz: la frecuencia mide **cada cuánto** compra, no **cuánto** gasta. |
| ¿Deberían ir al mismo grupo? | «No. Como no se equilibró el peso de cada columna, se da importancia a columnas que no la tienen tanto y se le niega a otras» | ✅ | Sin escalar, el peso depende de la **unidad**, no de la importancia. Escalar hace que todas empiecen con el mismo peso. |

**Mis preguntas**
- **«Prueba otra vez nlm.»**
  → Tras el login añadimos 3 recuadros de los libros:
  - Mediana: 434 en California; 200 amigos suben la media de 7,33 a 7,82 y la mediana se queda en 6.
  - Colas largas: el logaritmo las encoge.
  - Escalar: pulgadas frente a centímetros cambia los vecinos.

---

## 💳 Fase 09 · Exploración (Tarjetas)

**Lo aprendido**
- **Scree plot:** PC1 guarda el 27 % y PC2 el 20 %. Para el **80 %** hacen falta **7 de 17** componentes, y no hay codo claro.
- **Pesos:** **PC1 = «cuánto compra»** (`PURCHASES` 0,41, `PURCHASES_TRX` 0,39…) y **PC2 = «cuánto tira de efectivo»** (`CASH_ADVANCE` 0,44, `BALANCE` 0,40…).
- **PCA 2D:** sale **una nube continua**, densa cerca del origen y con brazos hacia compras y hacia efectivo. **No hay islas.**
  - Los clientes varían **poco a poco**. Las setas son especies con rasgos «en paquete».
  - Segmentar será **cortar la nube en zonas**, y las métricas internas saldrán bajas.

**Preguntas de control**

| Pregunta | Mi respuesta | | Respuesta completa |
|---|---|---|---|
| ¿Por qué no se ven grupos claros (y en las setas sí)? | «Porque no hay tantos factores para diferenciar (características)» | 🟡 | No es por el número de columnas: los clientes varían **de forma continua** y las setas son especies con rasgos que van juntos. |
| ¿Dónde cae un cliente que compra mucho y casi no saca efectivo? | «Abajo a la derecha» | ✅ | PC1 alto y PC2 bajo. |
| ¿`TENURE` (0,08 en PC1) participa? ¿Importa? | «No importa mucho» | ✅ | **Participa** (en PCA participan todas), pero apenas mueve el eje. |
| ¿Por qué «varían poco a poco» lo explica mejor? | «No hay ítems que se diferencien, son ítems progresivos, más difícil de agrupar; por eso el gráfico es una bola con brazos largos» | ✅ | Exacto. |

**Mis preguntas**
- **«¿Cómo decidimos PC1 y PC2? ¿Cogemos los datos, aplicamos un x/y y las columnas que salen de ese grupo forman PC1, y lo mismo para y?»**
  → Casi. PCA **no reparte las columnas en grupos**: **todas participan en PC1 y en PC2**, cada una con un peso. Por ejemplo, `CREDIT_LIMIT` pesa 0,21 en PC1 y 0,24 en PC2.
  - **PC1** es la dirección en la que los clientes **más se diferencian**.
  - **PC2** es la siguiente, **perpendicular** a PC1.
  - El **nombre** («compras», «efectivo») lo ponemos nosotros, mirando los pesos más grandes.

---

## 💳 Fase 10 · Modelado (Tarjetas)

**Lo aprendido**
- Sin etiqueta, **k se elige con la silueta y con el sentido de negocio**.
  - Silueta máxima en **k = 3** (0,241). Es baja porque los datos son una nube continua.
  - Con k ≥ 5 aparece un grupo de **86 clientes extremos**, que no sirve para una campaña.
- **K-Means k = 3:** 68,3 % / 17,9 % / 13,8 %.
- **Aglomerativo:** sale parecido, pero no idéntico.
- **GMM:** reparte muy distinto (3410 / 2934 / 2606), porque sus campanas se adaptan a las colas largas. **Sin etiqueta no hay árbitro.**
- **DBSCAN** sobre el PCA 2D: siempre sale un grupo gigante. Con `eps = 1.0`, **1 grupo + 81 de ruido**. Necesita **huecos**, y la nube no los tiene.
- **K-Means siempre da los k grupos que le pidas, existan o no.**

**Preguntas de control**

| Pregunta | Mi respuesta | | Respuesta completa |
|---|---|---|---|
| ¿Cuándo DBSCAN en vez de K-Means? | «Cuando en el PCA 2D hay grupos separados; si no, no lo ve» | 🟡 | Cuando hay grupos **separados por huecos**, **formas raras** (lunas, anillos), quieres **detectar ruido** o **no sabes k**. El PCA 2D solo es donde lo probamos. |
| ¿Por qué no k = 7? | «Porque k = 3 tiene más inercia y más silueta, y tendríamos muchos grupos. ¿Existen tantos grupos o nos estaríamos desviando?» | 🟡 | La silueta y los grupos pequeños (86) son buenas razones. La **inercia no**, porque siempre baja al subir k. |
| GPS de taxis con zonas concurridas separadas por calles vacías: ¿K-Means o DBSCAN? | «DBSCAN, porque hay esas calles de separación… aunque sean concurridas hay una separación geográfica, que corresponde a los puntos libres de la gráfica» | ✅ | Las calles vacías son los **huecos** de baja densidad. Además, DBSCAN sigue formas raras y marca las recogidas sueltas como ruido. |

**Mis preguntas**
- **«¿Existen tantos grupos o nos estaríamos desviando?»**
  → Nos desviaríamos. K-Means corta la nube en los k trozos que le pidas. Un grupo «existe» si tiene **buena silueta**, un **tamaño útil** y una **interpretación de negocio**.
- **«Reintenta nlm.»**
  → Añadimos 3 recuadros de los libros:
  - K-Means corta California en 10 zonas y prefiere grupos de tamaño parecido.
  - GMM y sus formas de campana.
  - DBSCAN falla sin huecos; la maldición de la dimensión.

---

## 💳 Fase 11 · Evaluación (Tarjetas)

**Lo aprendido**
- Sin etiqueta solo hay **métricas internas**:

  | Modelo | Silueta ↑ | Davies-Bouldin ↓ | Calinski ↑ |
  |---|---|---|---|
  | **K-Means** | **0,241** | **1,597** | **1606** |
  | Aglomerativo | 0,169 | 1,82 | 1289 |
  | GMM | 0,094 | 2,995 | 816 |
  | DBSCAN | 0,719 ⚠️ | 1,306 | 760 |

- **Trampa de DBSCAN:** su silueta es alta porque solo separa 81 puntos raros de un bloque con el 99 % de los clientes (8869). No segmenta nada.
- **El ARI sin etiqueta** sirve para comparar dos repartos cualesquiera:
  - **Algoritmo contra algoritmo:** K-Means–Aglomerativo 0,36; K-Means–GMM 0,07.
  - **Semilla contra semilla** (estabilidad):
    - K-Means [1, 1, 1, 1, 0,98].
    - GMM [1, 0,98, **0,8**, 1, 1]. Con 0,8, **635 clientes cambian de segmento**.
- **Silueta por segmento** (diagrama de cuchillos):

  | Segmento | Silueta media | Puntos negativos |
  |---|---|---|
  | 0 | 0,09 | 29 % |
  | 1 | 0,335 | 0 % |
  | 2 | 0,04 | 42 % |

  El segmento 1 está bien formado; los segmentos 0 y 2 se solapan.
- **t-SNE** solo sirve para **ver**:
  - Cada color ocupa su zona, aunque los bordes se tocan.
  - No mide distancias reales.

**Preguntas de control**

| Pregunta | Mi respuesta | | Respuesta completa |
|---|---|---|---|
| ¿Por qué no se puede calcular el ARI como en las setas? ¿Para qué lo usamos entonces? | «El ARI es con datos categorizados, aka la solución, y aquí no los tenemos» | 🟡 | No hay etiqueta real. Aun así, el ARI compara **dos repartos cualesquiera**: algoritmo contra algoritmo y semilla contra semilla (estabilidad). |
| ¿Por qué la silueta de 0,719 de DBSCAN no la hace la mejor? | «La segmentación: un grupo de 81 no sirve, es ruido» | 🟡 | Los 81 son ruido, y además el **99 % cae en un solo grupo**. La silueta es alta porque mide lo lejos que están los raros, no si los grupos son útiles. |
| Si K-Means da ARI 0,3 contra sí mismo con otra semilla, ¿qué significa? | «El algoritmo es estable» | ❌ | **Inestable:** salen dos segmentaciones muy distintas, así que ninguna es fiable. Un ARI cercano a 1 indica que es estable. |
| Marketing con un grupo de 8869 y otro de 81: ¿silueta o utilidad? | «Que los grupos sirvan» | ✅ | Solo se podría hacer **una campaña**. La silueta ayuda, pero no decide sola. |
| ¿K-Means o GMM para entregar? | «K-Means, GMM demasiado bueno» | 🟡 | K-Means, porque GMM es **menos estable** (0,8 con una semilla) y tiene peores métricas internas. |
| Completa: «GMM con ARI 0,8 significa ___ y por eso ___» | «Es estable, tiene el valor más alto de ARI» | 🟡 | Eso vale para K-Means. Con GMM, **≈ 635 clientes cambian de grupo**, así que es menos fiable. |

**Mis preguntas**
- **«Reintenta nlm.»**
  → Añadimos 4 recuadros de los libros:
  - El jerárquico con unión por máximo equivale a K-Means.
  - `n_init=10` frente a los malos arranques.
  - Los diagramas de silueta para elegir k.
  - t-SNE solo para visualizar, porque rompe las formas continuas.

---

## 💳 Fase 12 · Interpretación (Tarjetas)

**Lo aprendido**
- **El cluster 0, 1 o 2 no significa nada hasta que lo describimos.** Para describirlo:
  1. Añadir la columna `cluster` al `df` **sin escalar**.
  2. Calcular la **media por cluster**.
  3. **Estandarizar entre clusters** y pintar un heatmap (rojo = por encima, azul = por debajo).
- **Entregable:**

  | Segmento | % | Rasgos | Estrategia |
  |---|---|---|---|
  | 💤 Poco activos | 68,3 | Todo bajo: saldo, límite (~3.300 €), compras | Activar: cashback, recordatorios |
  | ⚠️ Riesgo por adelantos | 17,9 | Adelantos ~3.900 €, saldo alto, casi nunca paga el total | Vigilar el impago; préstamo más barato que el adelanto |
  | 💎 VIP compradores | 13,8 | Compras ~4.300 €, 57 transacciones, más límite, paga el total | Fidelizar: puntos, más límite, premium |

- **Isolation Forest** (`contamination=0.05`) marca **448 atípicos**:
  - Por segmento: 281 VIP, 160 de riesgo y solo 7 poco activos.
  - Medianas frente a los normales: compras 4.900 € frente a 330 €; límite 9.500 € frente a 3.000 €.
- De los **81 de ruido de DBSCAN**, **80** también son atípicos para Isolation Forest. Dos métodos distintos señalan a los mismos clientes.
- **Atípico ≠ error:** Isolation Forest dice «raro»; el **porqué** sale de mirar al cliente.

**Preguntas de control**

| Pregunta | Mi respuesta | | Respuesta completa |
|---|---|---|---|
| Presupuesto para una sola campaña: ¿qué segmento? | «Fidelización clientes VIP, dinero PC1» | ✅ | Los VIP concentran el dinero (brazo de PC1). Elegir **riesgo** también sería válido con su motivo. |
| Cliente con compras de 30.000 € y límite de 30.000 €: ¿error, fraude o VIP? ¿Cómo averiguarlo? | «Mirar DBSCAN» | 🟡 | DBSCAN solo repite que está lejos. Hay que mirar **sus datos**: coherencia (error), pagos y antigüedad (VIP), un cambio brusco en el historial (fraude). |
| Con `PRC_FULL_PAYMENT = 1` y `TENURE = 12`, ¿qué es y qué harías? | «VIP» · «Trato VIP» | ✅ | Gran cliente fiel. **No bloquearlo**: subirle el límite, darle un gestor, y apartarlo del cálculo de medias del segmento. |

**Mis preguntas**
- (Ninguna nueva.) Recuadros de los libros:
  - Los clusters no se etiquetan solos.
  - Segmentos de un blog (40 % / 20 %).
  - Isolation Forest para **fraude con tarjetas**.
  - La cuenta de prueba olvidada (error).

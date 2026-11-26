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

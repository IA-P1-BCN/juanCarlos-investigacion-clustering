# AGENTS.md — Clustering: Investigación y Taller Práctico

## Doble Objetivo del Repositorio
1. **Objetivo 1 — Investigación teórica (`README.md`):** Guía en español con **simplicidad máxima**, visual y pensada para **alumnos que empiezan desde cero**, cubriendo con rigor los 5 puntos de `scratch/specs.MD`.
2. **Objetivo 2 — Seguimiento del Taller Práctico (`docs/workshop/`):** Implementación y resolución progresiva de los dos notebooks de ML No Supervisado descritos en `docs/workshop/README.md`:
   - **Parte 1 (`docs/workshop/workshop-clustering-Mushrooms.ipynb`):** datos categóricos con etiqueta (`class`) reservada *solo para validar* (EDA, nulos `'?'`, `veil-type`, One-Hot, PCA/t-SNE, Random Forest baseline, K-Means/Aglomerativo/GMM/DBSCAN con Jaccard, ARI/NMI e Isolation Forest).
   - **Parte 2 (`docs/workshop/workshop-clustering-creditcard.ipynb`):** datos numéricos *sin etiqueta* (imputación por mediana, `StandardScaler`, PCA, K-Means/Aglomerativo/GMM/DBSCAN, métricas internas, t-SNE, interpretación de segmentos en heatmap e Isolation Forest).

## Entorno Python y Datos (Objetivo 2)
- **Usar `uv` siempre:** Gestionar dependencias, entornos y ejecución exclusivamente con `uv` (`uv sync`, `uv add`, `uv run ...`). Nunca usar `pip install` global.
- **Datasets como GitHub Release Assets (`data-v1`):** `mushrooms.csv` y `credit_card.csv` no se versionan en Git (`docs/workshop/data/` está en `.gitignore`). Descargarlos localmente con `uv run python docs/workshop/download_data.py`.
- **Seguimiento por tasklist:** Trabajar en orden (Parte 1 → Parte 2), validando cada notebook ejecutable de arriba abajo sin errores.

## Flujo de Investigación (NotebookLM como capa RAG vía `nlm`)
- **NotebookLM-first (ahorro de tokens):** Carga siempre cualquier recurso nuevo (documentación oficial, artículos visuales, PDFs o **vídeos de YouTube**) en el cuaderno de NotebookLM mediante `nlm source add`. No cargues PDFs extensos, páginas enteras ni transcripciones en la ventana de contexto del agente: consulta siempre hacia NotebookLM y sintetiza solo lo esencial.
- **Consultas atómicas:** Lanza una consulta por cada punto del enunciado y guarda las salidas únicamente en `scratch/` (ignorado en Git).
- **Rigor técnico simple:** Usa palabras claras y directas sin confundir conceptos clave (inercia vs. silueta, `eps`/`min_samples` en DBSCAN, asignación probabilística en GMM).

> **Disclaimer — Límites de fuentes en NotebookLM (cuotas de Google):**
> - **Cuenta gratuita (*Free*):** hasta **50 fuentes por cuaderno** (máx. 100 cuadernos).
> - **Google AI Plus:** hasta **100 fuentes por cuaderno**.
> - **Google AI Pro (*Gemini Pro AI*):** hasta **300 fuentes por cuaderno**.
> - **Por fuente individual:** hasta 500.000 palabras o 200 MB (archivos locales).
>
> *(Cuotas orientativas sujetas a cambios de Google. Mantener el cuaderno por debajo de 50 fuentes permite que cualquier alumno con cuenta gratuita pueda clonarlo).*

## Estilo Pedagógico y Visual (`README.md`)
- **Índice obligatorio alineado a `scratch/specs.MD`:** Incluir siempre antes del apartado 1 un **índice navegable con enlaces ancla** que refleje 1 a 1 las 5 preguntas del enunciado (más Referencias), para que alumnos y evaluadores ubiquen cada respuesta al instante.
- **Simplicidad máxima (alumnos desde cero):** Priorizar **solo lo esencial**. Evitar párrafos largos, jerga innecesaria y badges superfluos (dejar solo los badges útiles de NotebookLM).
- **Imagen o esquema en cada apartado:** Incluir imágenes didácticas propias en `assets/` (verificadas visualmente) y, cuando aporte claridad de flujo, diagramas **Mermaid** muy simples y coloreados.
- **Vídeos con timestamps exactos:** Enlazar los vídeos de YouTube siempre con **timestamps reales verificados (`&t=...s`)** directos al minuto donde se explica cada concepto.
- **Formato limpio en GitHub:** Usar **negritas**, *cursivas*, tablas muy cortas y alertas nativas (`[!NOTE]`, `[!TIP]`, `[!WARNING]`) con moderación.

## Reglas del Repositorio
- Guarda borradores, scripts auxiliares (generación de imágenes / re-login) y salidas de `nlm` únicamente en `scratch/` (ignorado en Git).
- Las imágenes finales usadas en `README.md` se guardan en `assets/`.
- Los datasets del taller se descargan en `docs/workshop/data/` (ignorado en Git) desde la GitHub Release `data-v1`.
- No hagas `git commit` ni `git push` sin confirmación previa.

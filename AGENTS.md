# AGENTS.md — Tarea: Algoritmos de Clustering

## Objetivo
Generar un `README.md` en español con **simplicidad máxima**, visual y pensado para **alumnos que empiezan desde cero**, cubriendo con rigor pero **sin sobrecarga cognitiva** los 5 puntos del ejercicio de Clustering.

## Flujo de Investigación (NotebookLM como capa RAG vía `nlm`)
- **NotebookLM-first (ahorro de tokens):** Carga siempre cualquier recurso nuevo (documentación oficial, artículos visuales, PDFs o **vídeos de YouTube**) en el cuaderno de NotebookLM mediante `nlm source add`. No cargues PDFs extensos, páginas enteras ni transcripciones en la ventana de contexto del agente: consulta siempre hacia NotebookLM y sintetiza solo lo esencial.
- **Consultas atómicas:** Lanza una consulta por cada punto del enunciado y guarda las salidas únicamente en `docs/` (ignorado en Git).
- **Rigor técnico simple:** Usa palabras claras y directas sin confundir conceptos clave (inercia vs. silueta, `eps`/`min_samples` en DBSCAN, asignación probabilística en GMM).

> **Disclaimer — Límites de fuentes en NotebookLM (cuotas de Google):**
> - **Cuenta gratuita (*Free*):** hasta **50 fuentes por cuaderno** (máx. 100 cuadernos).
> - **Google AI Plus:** hasta **100 fuentes por cuaderno**.
> - **Google AI Pro (*Gemini Pro AI*):** hasta **300 fuentes por cuaderno**.
> - **Por fuente individual:** hasta 500.000 palabras o 200 MB (archivos locales).
>
> *(Cuotas orientativas sujetas a cambios de Google. Mantener el cuaderno por debajo de 50 fuentes permite que cualquier alumno con cuenta gratuita pueda clonarlo).*

## Estilo Pedagógico y Visual (`README.md`)
- **Simplicidad máxima (alumnos desde cero):** Priorizar **solo lo esencial**. Evitar párrafos largos, jerga innecesaria y badges superfluos (dejar solo los badges útiles de NotebookLM).
- **Imagen o esquema en cada apartado:** Incluir imágenes didácticas propias en `assets/` (verificadas visualmente) y, cuando aporte claridad de flujo, diagramas **Mermaid** muy simples y coloreados.
- **Vídeos con timestamps exactos:** Enlazar los vídeos de YouTube siempre con **timestamps reales verificados (`&t=...s`)** directos al minuto donde se explica cada concepto.
- **Formato limpio en GitHub:** Usar **negritas**, *cursivas*, tablas muy cortas y alertas nativas (`[!NOTE]`, `[!TIP]`, `[!WARNING]`) con moderación.

## Entregable (`README.md`)
Debe responder de forma breve y clara a los 5 apartados del enunciado:
1. Aprendizaje no supervisado vs. supervisado y propósito del clustering.
2. Clustering particional (centroides) vs. jerárquico (con 1 algoritmo de cada).
3. Clustering basado en densidad (DBSCAN) y diferencias frente a los anteriores.
4. Importancia de elegir $K$/hiperparámetros y 2 métricas de evaluación (codo y silueta).
5. **K-Means, Jerárquico Aglomerativo, DBSCAN y GMM** (cómo funciona, ventajas, desventajas y cuándo usarlo) + tabla resumen.

## Reglas del Repositorio
- Guarda borradores, scripts auxiliares (generación de imágenes / re-login) y salidas de `nlm` únicamente en `docs/` (ignorado en Git).
- Las imágenes finales usadas en `README.md` se guardan en `assets/`.
- No hagas `git commit` ni `git push` sin confirmación previa.

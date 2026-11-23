# AGENTS.md — Tarea: Algoritmos de Clustering

## Objetivo
Generar un `README.md` técnico, **conciso y visual** en español, pensado para **alumnos que empiezan desde cero**, que responda con rigor a los 5 puntos del ejercicio de Clustering del bootcamp.

## Flujo de Investigación (NotebookLM como capa RAG vía `nlm`)
- **NotebookLM-first (ahorro de tokens):** Carga siempre cualquier recurso nuevo (documentación oficial, artículos visuales, PDFs o **vídeos de YouTube**) en el cuaderno de NotebookLM mediante `nlm source add`. No uses el servidor MCP completo ni cargues PDFs extensos, páginas enteras o transcripciones en la ventana de contexto del agente: consulta siempre hacia NotebookLM y sintetiza solo lo necesario.
- **Consultas atómicas:** Lanza una consulta por cada punto del enunciado y guarda las salidas únicamente en `docs/` (ignorado en Git).
- **Rigor técnico:** Respeta los conceptos devueltos por las fuentes. No inventes datos ni confundas métricas (inercia vs. silueta, `eps`/`min_samples` en DBSCAN, asignación probabilística en GMM).

> **Disclaimer — Límites de fuentes en NotebookLM (cuotas de Google):**
> - **Cuenta gratuita (*Free*):** hasta **50 fuentes por cuaderno** (máx. 100 cuadernos).
> - **Google AI Plus:** hasta **100 fuentes por cuaderno**.
> - **Google AI Pro (*Gemini Pro AI*):** hasta **300 fuentes por cuaderno**.
> - **Por fuente individual:** hasta 500.000 palabras o 200 MB (archivos locales).
>
> *(Cuotas orientativas sujetas a cambios de Google. Curar las fuentes y eliminar duplicados para optimizar el cupo y permitir que cualquier alumno con cuenta gratuita pueda clonar el cuaderno si se mantiene por debajo de 50 fuentes).*

## Estilo Pedagógico y Visual (`README.md`)
- **Audiencia inicial (desde cero):** Redacción concisa, directa y escaneable. Destacar **solo lo más crítico e importante** de esta primera fase; evitar bloques de texto extensos.
- **Prioridad visual en cada apartado:** Integrar directamente dentro de cada sección recursos gráficos útiles (simuladores interactivos, artículos con GIFs y vídeos explicativos paso a paso) y diagramas **Mermaid** con nodos coloreados cuando el concepto sea un flujo, árbol o clasificación.
- **Formato enriquecido compatible con GitHub Markdown:** Usar **negritas**, *cursivas*, tablas compactas, badges de color (`shields.io`) y alertas nativas con color (`[!NOTE]`, `[!TIP]`, `[!IMPORTANT]`, `[!WARNING]`) para resaltar ideas clave y advertencias.

## Entregable (`README.md`)
Debe cubrir los 5 apartados del enunciado:
1. Aprendizaje no supervisado vs. supervisado y propósito del clustering.
2. Clustering particional (centroides) vs. jerárquico (con 1 algoritmo de cada).
3. Clustering basado en densidad (DBSCAN) y diferencias frente a los anteriores.
4. Elección de hiperparámetros/clusters y mínimo 2 métricas de evaluación (codo, silueta).
5. Fichas concisas de **K-Means, Jerárquico Aglomerativo, DBSCAN y GMM** (mecanismo, ventajas, desventajas y casos de uso) resumidas en bloques uniformes y tabla comparativa.

## Reglas del Repositorio
- Guarda borradores, scripts auxiliares de login y salidas de `nlm` únicamente en `docs/` (ignorado en Git).
- No hagas `git commit` ni `git push` sin confirmación previa.

# AGENTS.md — Tarea: Algoritmos de Clustering

## Objetivo
Generar un `README.md` técnico, claro y bien estructurado en español que responda a los 5 puntos del ejercicio de Clustering del bootcamp.

## Flujo de Investigación (Opción A: CLI `nlm` + Skill)
- **Ahorro de contexto:** Usa la skill de NotebookLM y comandos `nlm` por terminal para consultar las fuentes del cuaderno. No uses el servidor MCP completo ni leas PDFs extensos directamente en el contexto del IDE.
- **Consultas atómicas:** Lanza una consulta por cada punto del enunciado y sintetiza solo lo necesario antes de redactar.
- **Rigor técnico:** Cita y respeta los conceptos devueltos por las fuentes. No inventes datos ni confundas métricas (ej. inercia vs. silueta, `eps`/`min_samples` en DBSCAN, asignación probabilística en GMM).

## Entregable (`README.md`)
Debe cubrir los 5 apartados del enunciado:
1. Aprendizaje no supervisado vs. supervisado y propósito del clustering.
2. Clustering particional (centroides) vs. jerárquico (con 1 algoritmo de cada).
3. Clustering basado en densidad (DBSCAN) y diferencias frente a los anteriores.
4. Elección de hiperparámetros/clusters y mínimo 2 métricas de evaluación (codo, silueta).
5. Fichas de **K-Means, Jerárquico Aglomerativo, DBSCAN y GMM** (mecanismo, ventajas, desventajas y casos de uso) resumidas en una tabla comparativa o bloques uniformes.

## Reglas del Repositorio
- Guarda borradores o salidas de `nlm` únicamente en `docs/` (ignorado en Git).
- No hagas `git commit` ni `git push` sin confirmación previa.

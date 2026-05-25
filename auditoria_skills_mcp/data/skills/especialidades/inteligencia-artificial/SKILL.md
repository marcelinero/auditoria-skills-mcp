---
name: auditoria-inteligencia-artificial
description: Auditar sistemas de inteligencia artificial — gobernanza, ciclo de vida, datos, modelos, despliegue, monitoreo y cumplimiento conforme a ISO/IEC 42001, NIST AI RMF y EU AI Act. Activar siempre que se hable de auditoría de IA, AI audit, algorithmic audit, inteligencia artificial, machine learning, ML, deep learning, modelos predictivos, GenAI, LLM, sesgo algorítmico, fairness, explicabilidad, AI governance, MLOps, model risk management, ISO 42001, NIST AI RMF, EU AI Act, sistemas de alto riesgo, model cards, datasheets, validación de modelo, drift, hallucination.
---

# Auditoría de inteligencia artificial y algoritmos

## Propósito

La auditoría de IA evalúa el gobierno y los controles sobre sistemas de inteligencia artificial: desde la decisión de usarlos, pasando por los datos, el desarrollo del modelo, su despliegue y su monitoreo, hasta su retiro. Verifica responsabilidad, transparencia, equidad, robustez, seguridad y cumplimiento regulatorio.

Es una especialidad emergente con marco regulatorio (EU AI Act) y estándares de gestión (ISO/IEC 42001) recientes.

## Cuándo activar esta SKILL

- Auditorías sobre sistemas de IA específicos (modelo de scoring crediticio, sistema de detección de fraude, chatbot, GenAI).
- Auditorías sobre el programa general de IA y su gobernanza.
- Pre-deployment review de modelos de alto riesgo.
- Cumplimiento con EU AI Act u otra regulación.
- Cuando el usuario menciona modelo, algoritmo, IA, ML, sesgo, dataset, training, inferencia.

## Marco de referencia

- **ISO/IEC 42001:2023** — Sistemas de gestión de IA (AIMS).
- **NIST AI Risk Management Framework (AI RMF 1.0)** — funciones Govern, Map, Measure, Manage.
- **EU AI Act** — clasificación por riesgo (inaceptable, alto, limitado, mínimo) y obligaciones.
- **ISO/IEC 23894** — Guía de gestión del riesgo de IA.
- **ISO/IEC 23053** — Marco para sistemas de IA con ML.
- **ISO/IEC TR 24028** — Confianza en IA.
- **ISO/IEC 24029** — Robustez de redes neuronales.
- **OECD AI Principles**.
- **UNESCO Recommendation on the Ethics of AI**.
- **OWASP Top 10 for LLM Applications**.
- **MITRE ATLAS** — Adversarial Threat Landscape for AI Systems.
- **Reguladores sectoriales**: SR 11-7 (Fed Reserve, model risk), normativa local de seguros, salud, banca.

## Conceptos fundamentales

### Niveles de riesgo (EU AI Act)

- **Riesgo inaceptable**: prohibidos (puntuación social, manipulación cognitiva, identificación biométrica masiva con excepciones).
- **Alto riesgo**: sujetos a obligaciones estrictas — IA en empleo, educación, infraestructura crítica, justicia, migración, salud, etc.
- **Riesgo limitado**: obligaciones de transparencia (deep fakes, chatbots).
- **Riesgo mínimo**: sin obligación específica.

Identificar la clasificación es el primer paso de la auditoría.

### Dimensiones de evaluación

- **Validez y confiabilidad**: el sistema hace lo que debe hacer.
- **Seguridad**: no causa daño físico o psicológico.
- **Resiliencia y robustez**: tolera condiciones adversas, ataques.
- **Explicabilidad e interpretabilidad**: las decisiones se pueden justificar.
- **Privacidad**: respeta datos personales.
- **Equidad**: no discrimina indebidamente.
- **Trazabilidad**: el ciclo de vida está documentado.
- **Responsabilidad (accountability)**: hay responsables identificables.

### Riesgos específicos de IA

- **Sesgo en datos** (histórico, representación, medición).
- **Sesgo en modelo** (objetivo de optimización, hyperparámetros).
- **Drift**: el modelo se degrada porque cambian los datos del mundo real.
- **Adversarial attacks**: entradas diseñadas para engañar al modelo.
- **Data poisoning**: contaminación del dataset de entrenamiento.
- **Model inversion / membership inference**: extraer información del dataset.
- **Hallucination** (GenAI): generación confiada de información falsa.
- **Prompt injection** (LLMs): manipulación de la instrucción para alterar comportamiento.
- **Overreliance**: usuarios confían más de lo que el sistema garantiza.
- **Concentration / vendor lock-in**: dependencia de pocos proveedores de modelos foundation.

## Proceso

### Fase 1 — Inventario y clasificación

1. Solicitar/levantar inventario completo de sistemas de IA en uso o desarrollo.
2. Clasificar cada sistema por:
   - Caso de uso.
   - Tipo de modelo (regla, ML clásico, deep learning, foundation model, GenAI).
   - Nivel de riesgo (EU AI Act u otra clasificación).
   - Datos usados (PII, datos sensibles, datos sintéticos).
   - Decisiones que automatiza (asiste, recomienda, decide).
   - Personas afectadas (clientes, empleados, ciudadanos).
3. Identificar el responsable de cada sistema.

### Fase 2 — Evaluación de la gobernanza de IA

- ¿Existe una política de IA aprobada?
- Comité de IA / AI Council con autoridad.
- Marco ético y principios.
- Roles: AI lead, model risk officer, ethics committee.
- Proceso de aprobación de nuevos sistemas (gates antes de desarrollo, antes de producción).
- Capacitación.
- Vinculación con riesgo, cumplimiento, jurídica, privacidad, seguridad.

### Fase 3 — Pruebas por sistema (ciclo de vida)

#### A. Datos

- Origen y consentimiento.
- Calidad: completitud, exactitud, frescura.
- Sesgos: representación de grupos, balance de clases, etiquetado.
- Privacidad: minimización, anonimización, base legal.
- Linaje (data lineage): trazabilidad hasta la fuente.
- Versionado del dataset.
- Documentación tipo **Datasheet for Datasets**.

#### B. Modelo

- Objetivo del modelo claro y alineado con el objetivo de negocio.
- Selección de algoritmo justificada.
- Splits de entrenamiento, validación, test sin contaminación.
- Métricas elegidas adecuadas al uso (accuracy, precision, recall, F1, AUC, calibración).
- Métricas de fairness por subgrupos sensibles (demographic parity, equalized odds, etc.).
- Hyperparámetros documentados.
- Versionado del modelo (MLflow, registry).
- Documentación tipo **Model Card**: propósito, alcance, métricas, limitaciones, datos de entrenamiento, advertencias.
- Validación independiente (segunda línea o externa para alto riesgo).

#### C. Despliegue

- Pruebas pre-despliegue: shadow mode, A/B test.
- Configuración segura: claves, endpoints, autenticación.
- Controles de acceso al modelo (¿quién puede invocarlo, modificarlo, descargarlo?).
- Logs de inferencia.
- Capacidad de rollback.
- Plan de comunicación a usuarios afectados.

#### D. Monitoreo y operación

- Monitoreo de desempeño en producción.
- Detección de drift (concept drift, data drift).
- Monitoreo de fairness en producción.
- Alertas y umbrales.
- Procedimiento de respuesta cuando el modelo se degrada.
- Reentrenamiento: frecuencia, controles.
- Reporte a stakeholders.

#### E. Uso humano

- Diseño de la interfaz: cómo se presenta la salida del modelo al usuario.
- Mecanismo de override humano para decisiones críticas.
- Información al usuario sobre que está interactuando con IA (transparencia).
- Mecanismo de feedback y reclamación.
- Capacitación de usuarios sobre limitaciones del sistema.

#### F. Retiro

- Criterios para retirar un modelo.
- Procedimiento de retiro y comunicación.
- Conservación de datos y modelo para auditabilidad posterior.

### Fase 4 — Pruebas específicas por tipo de sistema

#### Sistemas de decisión automatizada (high stakes)
- Posibilidad de explicación específica para cada decisión (especialmente bajo GDPR Art. 22 / EU AI Act).
- Recurso humano para impugnación.
- Pruebas de robustez con casos límite.

#### LLM y GenAI
- Pruebas de alucinaciones (factualidad).
- Pruebas de prompt injection.
- Filtros de salida (toxicidad, PII, datos confidenciales).
- Acuerdos con proveedor: derecho a auditar, dónde se procesan los datos, si se usan para entrenar.
- Limitaciones de uso documentadas para usuarios finales.
- RAG: validar fuentes, control de acceso a documentos sensibles.
- Costos y rate limits.

#### Modelos en industrias reguladas
- Cumplimiento con SR 11-7 (banca EE. UU.) o equivalente.
- Documentación model risk management.
- Validación independiente periódica.

### Fase 5 — Pruebas de seguridad de IA

Aplicar **MITRE ATLAS** y **OWASP LLM Top 10**:

- Adversarial robustness (perturbaciones).
- Data poisoning detection.
- Model extraction.
- Membership inference.
- Prompt injection (directa, indirecta).
- Insecure output handling.
- Supply chain (dependencias en modelos pre-entrenados, datasets).

### Fase 6 — Cumplimiento regulatorio

- Mapeo del sistema a obligaciones EU AI Act (si aplica).
- Documentación técnica requerida para sistemas de alto riesgo.
- Registro en base de datos UE (alto riesgo).
- DPIA (Data Protection Impact Assessment) cuando hay datos personales.
- Conformity assessment requerido.
- Notificación de incidentes graves.

## Outputs esperados

1. Inventario clasificado de sistemas de IA.
2. Evaluación de la gobernanza de IA.
3. Por sistema auditado: revisión del ciclo de vida con hallazgos por fase.
4. Resultados de pruebas técnicas (fairness, robustez, drift, seguridad adversarial).
5. Mapeo de cumplimiento con marco aplicable (ISO 42001, NIST AI RMF, EU AI Act).
6. Hallazgos y plan de acción.

## Banderas rojas

- "Black box" sin documentación: no se sabe qué datos, qué algoritmo, quién lo desarrolló.
- Modelo en producción sin métricas en monitoreo.
- Métricas agregadas excelentes pero no desagregadas por subgrupos.
- Decisiones automáticas sobre personas sin override humano.
- Datasets reutilizados de proyectos anteriores sin revalidar relevancia y consentimiento.
- Modelos foundation usados con datos sensibles sin acuerdos sobre uso de datos por el proveedor.
- "El modelo no discrimina" sin pruebas de fairness por grupos protegidos.
- Reentrenamientos automáticos sin control humano (riesgo de feedback loops).
- Sin plan de qué hacer si el modelo falla o se degrada.
- LLMs en uso interno con datos confidenciales pegados en servicios públicos sin control.
- Sin clasificación EU AI Act cuando la organización opera en UE.
- Vendor único como dependencia crítica sin plan de salida.

## Buenas prácticas

- **Tratar el modelo como activo**: con dueño, ciclo de vida, retiro, documentación.
- **Documentación viva**: model cards, datasheets, registros, todo versionado.
- **Validación independiente** para alto riesgo: el equipo que construye no es el que valida.
- **Métricas desagregadas** por subgrupos sensibles relevantes.
- **Humano en el bucle** para decisiones críticas, con poder real de cambio.
- **Probar sesgos en datos antes de entrenar**, no solo en el modelo después.
- **Ensayar incidentes de IA**: ¿qué hacemos si el modelo da una recomendación catastrófica?
- **Coordinarse con privacidad y ciberseguridad**: la IA cruza ambos dominios.

## Conexión con otras SKILLs

- Se complementa con `auditoria-tecnologia-informacion` (infraestructura, ITGCs).
- Se complementa con `auditoria-ciberseguridad` (amenazas adversarias).
- Se complementa con `auditoria-cumplimiento` (EU AI Act, GDPR, regulación sectorial).
- Usa fuertemente `analitica-datos` para evaluación de datasets y métricas.
- En sectores regulados, coordina con `auditoria-financiera` (model risk en banca/seguros).
- Aplica todas las SKILLs de proceso.

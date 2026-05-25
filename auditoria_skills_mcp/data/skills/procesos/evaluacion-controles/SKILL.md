---
name: evaluacion-controles
description: Identificar, documentar, evaluar el diseño y probar la efectividad operativa de controles internos en cualquier proceso o sistema. Activar siempre que se hable de controles internos, matriz de riesgos y controles, COSO, walkthrough, pruebas de diseño, pruebas de operación, control de gestión, controles clave, control compensatorio, evaluación de control interno, certificación SOX 404, o cuando se audite cualquier proceso para concluir si está adecuadamente controlado.
---

# Evaluación de controles internos

## Propósito

Esta SKILL guía la identificación, documentación y prueba de controles internos en cualquier proceso. Es la SKILL nuclear de la auditoría: prácticamente ningún engagement se completa sin aplicarla.

Aplica el marco COSO IC-IF 2013 como referencia conceptual y los enfoques de prueba estándar (walkthrough, prueba de diseño, prueba de efectividad operativa).

## Cuándo activar esta SKILL

- En cualquier engagement donde se evalúe si los controles mitigan los riesgos identificados.
- Para construir o validar matrices de riesgos y controles (RCM).
- Para certificaciones SOX 404 o equivalentes.
- Cuando el cliente pide opinión sobre la idoneidad del control interno de un proceso.
- Antes de decidir el alcance de pruebas sustantivas en auditoría financiera (a mayor confianza en controles, menor extensión sustantiva).

## Marco de referencia

- **COSO Internal Control – Integrated Framework (2013)** — los cinco componentes (ambiente, evaluación de riesgos, actividades de control, información y comunicación, monitoreo) y los 17 principios.
- **Modelo de las Tres Líneas (IIA, 2020)**.
- **NIA 315** — Identificación y evaluación de riesgos de error material.
- **NIA 330** — Respuestas del auditor a los riesgos evaluados.
- **PCAOB AS 2201** (cuando aplique SOX) — Auditoría del control interno sobre la información financiera.
- **Normas Globales de Auditoría Interna (IIA, 2025)** — Estándar 13.4 "Criterios del engagement" y Dominio V sobre desempeño del trabajo.

## Conceptos clave

### Tipos de control

- **Por naturaleza**: preventivo (evita que ocurra el riesgo), detectivo (detecta el riesgo después), correctivo (corrige consecuencias).
- **Por automatización**: manual, semi-automático (manual con apoyo de sistema), automatizado (totalmente en sistema).
- **Por nivel**: de entidad (tone at the top, código de ética), de proceso (segregación de funciones, autorizaciones), generales de TI (acceso, cambios, operaciones).
- **Por frecuencia**: continuo, diario, semanal, mensual, trimestral, anual, ad-hoc.

### Atributos de un control bien diseñado

- **Quién** lo ejecuta (rol, no persona).
- **Qué** hace exactamente.
- **Cuándo** lo ejecuta (frecuencia y trigger).
- **Cómo** evidencia la ejecución (qué deja registrado).
- **Qué riesgo mitiga** y **qué aseveración** o **qué objetivo** atiende.

Si alguno de estos cinco atributos no es claro, el control es débil por diseño.

### Riesgo, control, aseveración

En auditoría financiera, los controles se evalúan contra **aseveraciones** (existencia, integridad, exactitud, valuación, derechos y obligaciones, presentación). En auditoría operativa, contra **objetivos del proceso** (eficiencia, eficacia, cumplimiento, salvaguarda de activos, confiabilidad de información).

## Proceso

### Fase 1 — Comprender el proceso

1. Solicitar el flujograma o diagrama del proceso al auditado. Si no existe, levantarlo durante el walkthrough.
2. Identificar los **puntos clave de riesgo** (where things can go wrong): autorizaciones, cálculos, captura de información, interfaces, salidas a terceros, registros contables.
3. Para cada punto de riesgo, identificar el control esperado.

### Fase 2 — Documentar la matriz de riesgos y controles (RCM)

Cada fila de la RCM debe contener:

| Campo | Descripción |
|---|---|
| ID | Identificador único del control |
| Riesgo | Riesgo que se mitiga |
| Aseveración / objetivo | A qué responde el control |
| Descripción del control | Qué hace (verbo + objeto + criterio) |
| Quién | Rol que lo ejecuta |
| Frecuencia | Cuándo se ejecuta |
| Naturaleza | Preventivo / detectivo / correctivo |
| Tipo | Manual / automatizado / semi |
| Evidencia | Qué deja registrado |
| Es clave | Sí/no (los controles clave son los que se prueban) |
| Resultado prueba diseño | Eficaz / no eficaz |
| Resultado prueba operación | Eficaz / no eficaz |

### Fase 3 — Walkthrough

Un walkthrough es seguir una transacción de principio a fin del proceso para confirmar que la RCM refleja la realidad.

Pasos:
1. Seleccionar 1–3 transacciones reales (no inventadas).
2. Pedir al ejecutor del proceso que la recorra paso a paso.
3. Inspeccionar la evidencia que cada control deja.
4. Hacer preguntas tipo "¿qué pasaría si…?" para detectar controles compensatorios.
5. Documentar el walkthrough con copias de la evidencia.

El walkthrough no es una prueba de operación: solo confirma diseño y existencia.

### Fase 4 — Prueba de diseño

Para cada control clave, evaluar si el diseño es adecuado para mitigar el riesgo asumiendo que se ejecuta como está descrito.

Preguntas guía:
- ¿El control responde directamente al riesgo?
- ¿La frecuencia es apropiada para el riesgo?
- ¿La persona que lo ejecuta tiene la competencia y la independencia adecuadas?
- ¿La evidencia permite verificar la ejecución posteriormente?
- ¿Existen segregación de funciones suficiente?

Concluir: **diseño eficaz** o **diseño no eficaz** (con sustento).

### Fase 5 — Prueba de efectividad operativa

Solo se hace si el diseño es eficaz. Se prueba si el control efectivamente operó durante el periodo auditado.

Procedimientos:
- Inspección de evidencia (documentos, logs, registros).
- Reejecución (recalcular, repetir el control).
- Observación (presenciar la ejecución — solo válido para el momento observado).
- Indagación + corroboración (la indagación sola nunca es suficiente).

**Tamaño de muestra orientativo (basado en frecuencia del control)**:

| Frecuencia | Muestra mínima sugerida |
|---|---|
| Anual | 1 |
| Trimestral | 2 |
| Mensual | 2–5 |
| Semanal | 5–15 |
| Diario | 20–40 |
| Múltiples veces al día | 25–60 |

Estas cifras son orientativas; ver SKILL `muestreo` para el detalle estadístico.

### Fase 6 — Concluir y agregar resultados

Para cada control: **eficaz** / **deficiente**.

Las deficiencias se clasifican por severidad:

- **Deficiencia simple**: requiere mejora pero no compromete el objetivo.
- **Deficiencia significativa**: amerita atención de la administración.
- **Debilidad material** (en SOX): existe probabilidad razonable de que un error material no sea prevenido o detectado oportunamente.

A nivel de proceso o entidad, agregar las conclusiones individuales considerando controles compensatorios.

## Outputs esperados

1. **Matriz de riesgos y controles (RCM)** completa.
2. **Documentación de walkthroughs** (con evidencia adjunta).
3. **Pruebas de diseño** documentadas en papeles de trabajo.
4. **Pruebas de operación** documentadas con muestras y resultados.
5. **Listado de deficiencias** con severidad y recomendación.
6. **Conclusión sobre el control interno** del proceso/área.

## Banderas rojas

- Controles descritos sólo como "se revisa" sin especificar qué se revisa, contra qué, ni quién.
- Misma persona ejecuta un control y autoriza la transacción que el control debe verificar (falla de segregación).
- Controles "automatizados" sin evidencia de pruebas de los controles generales de TI que los soportan.
- Controles compensatorios mencionados pero no documentados ni probados.
- Frecuencias no consistentes con el riesgo (control trimestral para un riesgo diario crítico).
- Indagación como única evidencia de la prueba.
- Período de prueba que no abarca el periodo auditado.

## Conexión con otras SKILLs

- Recibe entradas de `planeacion-basada-riesgos`.
- Usa `muestreo` para definir tamaños de muestra.
- Alimenta a `papeles-trabajo` con la RCM y resultados de pruebas.
- Las deficiencias detectadas se reportan vía `comunicacion-hallazgos`.
- Para procesos digitalizados, complementarse con `auditoria-tecnologia-informacion` (controles generales de TI).

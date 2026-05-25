---
name: seguimiento-recomendaciones
description: Monitorear la implementación de recomendaciones de auditoría, verificar el cierre efectivo de hallazgos y reportar el estado al Comité de Auditoría. Activar siempre que se hable de seguimiento, monitoreo de hallazgos, follow-up, status de recomendaciones, cierre de hallazgo, verificación de implementación, plan de acción, hallazgo abierto/cerrado, hallazgo repetitivo, dashboard de auditoría, o cuando se requiera evaluar el progreso post-informe.
---

# Seguimiento de recomendaciones

## Propósito

Una recomendación que no se implementa no agrega valor. Esta SKILL guía el proceso de seguimiento sistemático del cierre de los hallazgos, la verificación independiente de su implementación efectiva (no solo declarada), y el reporte al Comité de Auditoría.

## Cuándo activar esta SKILL

- Al cierre del engagement (definir cronograma de seguimiento).
- En cada ciclo de seguimiento (mensual, trimestral, según política).
- Cuando la administración reporta que un hallazgo ha sido implementado.
- Para preparar el reporte de hallazgos abiertos al Comité de Auditoría.
- Cuando el usuario pregunta por el estado de un hallazgo o un plan de acción.

## Marco de referencia

- **Normas Globales de Auditoría Interna (IIA, 2025)**:
  - Estándar 15.2: Confirmación de la recepción de los resultados
  - Estándar 15.3: Seguimiento del progreso
- **NIA 260** — Comunicación con responsables del gobierno corporativo (en el contexto externo).
- **Política institucional** sobre tolerancia al riesgo y aceptación de hallazgos.

## Conceptos clave

### Estados de un hallazgo

- **Abierto / pendiente**: el plan de acción aún no se ha implementado.
- **En proceso**: la administración está ejecutando el plan; aún no termina.
- **Implementado por la administración (sin verificar)**: la administración declara cierre, pero auditoría no ha confirmado.
- **Cerrado (verificado)**: auditoría verificó implementación efectiva.
- **Vencido**: la fecha comprometida pasó sin implementación.
- **Riesgo aceptado**: la administración decidió no implementar y aceptar el riesgo. Requiere autorización del nivel apropiado y documentación formal.
- **No vigente**: el hallazgo perdió relevancia (ej. el proceso fue eliminado).

### Verificación efectiva

Cerrar un hallazgo no es marcar una casilla. Implica:

1. Examinar la evidencia de la implementación (no solo escuchar el reporte).
2. Probar que el control nuevo o ajustado realmente opera.
3. Concluir que la causa raíz fue atendida.

Si la implementación es parcial o cosmética, el hallazgo permanece abierto.

## Proceso

### Paso 1 — Definir el cronograma de seguimiento

Al cierre del engagement, programar fechas de revisión por hallazgo. Recomendable:

- **Hallazgos críticos**: seguimiento mensual.
- **Hallazgos altos**: seguimiento trimestral.
- **Hallazgos medios y bajos**: seguimiento semestral o al cumplirse la fecha comprometida.

Registrar en una herramienta única (issue tracker de auditoría, base de datos, sistema GRC) con: ID, severidad, descripción, recomendación, responsable, fecha comprometida, estado.

### Paso 2 — Ciclo regular de seguimiento

En cada ciclo:
1. Revisar los hallazgos cuya fecha comprometida cae en o antes del corte.
2. Solicitar a la administración el reporte de avance con evidencia.
3. Para hallazgos reportados como implementados, ejecutar verificación.

### Paso 3 — Verificación de implementación

La verificación es un mini-engagement: tiene su propio papel de trabajo. Procedimientos típicos:

- **Inspección**: leer la nueva política, ver la nueva configuración del sistema, ver los nuevos formatos.
- **Walkthrough**: seguir una transacción que use el control nuevo.
- **Prueba operativa de muestra**: para controles ya recurrentes, prueba sobre 5–25 ejecuciones según frecuencia.
- **Recálculo o reejecución**: si el ajuste fue de cálculo o lógica.
- **Indagación + corroboración**: nunca sola.

Concluir explícitamente: implementación **efectiva**, **parcial** o **inefectiva**.

### Paso 4 — Manejo de hallazgos vencidos

Si un hallazgo está vencido:

1. Comunicar al responsable y solicitar nueva fecha con justificación.
2. Escalar al nivel superior si la demora es injustificada.
3. Reportar al Comité de Auditoría a partir de cierto umbral (ej. más de 90 días vencido o cualquier crítico vencido).
4. Si la administración decide no implementar, formalizar como **riesgo aceptado**: requiere aprobación de la instancia con autoridad para aceptar ese riesgo y queda en archivo.

### Paso 5 — Reporte al Comité de Auditoría

Indicadores típicos a reportar:

- Total de hallazgos abiertos por severidad y por antigüedad.
- Hallazgos cerrados en el periodo.
- Hallazgos vencidos con su análisis.
- Hallazgos repetitivos (mismo tema observado en auditorías anteriores).
- Riesgos aceptados con su sustento.
- Tendencias por área, proceso o tipo de control.

Visualizar idealmente con dashboard que muestre la evolución a lo largo del tiempo.

## Hallazgos repetitivos

Un hallazgo es repetitivo cuando se observa nuevamente después de haber sido reportado en un engagement anterior. Es una señal de:

- Implementación cosmética (se "cerró" sin atender la causa raíz).
- Falla en la cultura de control.
- Problema estructural que excede la responsabilidad del proceso auditado.

Los hallazgos repetitivos requieren:
- Severidad agravada.
- Análisis de causa raíz extendido.
- Reporte explícito al Comité.
- Posible escalamiento a nivel ejecutivo o de junta.

## Riesgo aceptado por la administración

Cuando la administración decide **no implementar** y aceptar el riesgo:

1. La decisión debe tomarla la instancia con autoridad de aceptar ese nivel de riesgo (alineado con la matriz de delegación y el apetito de riesgo).
2. La aceptación se documenta por escrito.
3. Auditoría evalúa si el riesgo aceptado es **inaceptable** para la organización (ej. supera el apetito o cruza líneas de cumplimiento).
4. Si auditoría considera el riesgo inaceptable, debe escalar al CEO y, si no se resuelve, al Comité de Auditoría y/o a la Junta Directiva (Estándar IIA 15.3).
5. Documentar todo: el riesgo aceptado deja un rastro.

## Dashboard de seguimiento — campos mínimos

| Campo | Descripción |
|---|---|
| ID hallazgo | Identificador único |
| Engagement origen | Auditoría que lo originó |
| Fecha emisión informe | Cuándo se reportó |
| Severidad | Crítica/Alta/Media/Baja |
| Título | Resumen corto |
| Recomendación | Texto |
| Responsable | Rol/persona |
| Fecha comprometida original | Plazo inicial |
| Fecha comprometida vigente | Plazo actual |
| Última actualización | Fecha del último reporte |
| Estado | Abierto / en proceso / implementado declarado / cerrado verificado / vencido / riesgo aceptado |
| Días abierto | Diferencia entre hoy y emisión |
| Repetitivo | Sí/No |
| Verificación auditoría | Pendiente / efectiva / parcial / inefectiva |

## Banderas rojas

- "Cerrar" hallazgos solo con confirmación verbal de la administración.
- Plazos prorrogados repetidamente sin justificación.
- Volumen elevado de hallazgos en estado "implementado declarado" sin verificar.
- Patrones por área (un proceso o líder concentra hallazgos vencidos).
- Riesgos aceptados sin trazabilidad de quién aprobó.
- Recomendaciones reformuladas en cada ciclo para evitar el etiquetado de vencido.

## Buenas prácticas

- **Verificar siempre antes de cerrar**: el cierre verificado tiene un peso distinto al "implementado por administración".
- **Vincular con el ERM corporativo**: hallazgos abiertos críticos deben aparecer en los reportes de riesgo a la junta.
- **Cerrar el ciclo con la auditoría siguiente**: cuando se vuelva a auditar el proceso, el primer paso es revisar hallazgos previos.
- **Análisis de tendencias**: agregar por causa raíz para identificar problemas estructurales.

## Conexión con otras SKILLs

- Es la continuación natural de `comunicacion-hallazgos`.
- Cuando se requiere reverificar un control, se invoca `evaluacion-controles` y `muestreo`.
- Se documenta vía `papeles-trabajo`.
- La efectividad del seguimiento es revisada en `aseguramiento-calidad`.

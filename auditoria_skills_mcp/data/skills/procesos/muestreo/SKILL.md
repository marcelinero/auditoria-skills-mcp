---
name: muestreo
description: Diseñar y ejecutar muestreo estadístico y no estadístico para pruebas de controles y pruebas sustantivas, calcular tamaños de muestra, seleccionar elementos y proyectar errores. Activar siempre que el usuario hable de muestra, tamaño de muestra, sample size, MUS, muestreo estadístico, muestreo de atributos, selección aleatoria, intervalo de muestreo, NIA 530, ISA 530, error tolerable, nivel de confianza, o cuando se necesite seleccionar transacciones para probar.
---

# Muestreo de auditoría

## Propósito

Esta SKILL permite al agente diseñar, ejecutar e interpretar muestras de auditoría conforme a NIA 530 / ISA 530, decidiendo cuándo usar muestreo estadístico vs no estadístico, calculando tamaños de muestra adecuados, y proyectando errores de la muestra a la población.

## Cuándo activar esta SKILL

- Siempre que se necesite seleccionar un subconjunto de transacciones, registros o controles para probar.
- En pruebas de operación de controles (muestreo de atributos).
- En pruebas sustantivas de saldos (MUS o estratificado).
- Cuando el usuario pregunte por tamaño de muestra, intervalo de muestreo o cómo seleccionar.

## Marco de referencia

- **NIA 530 / ISA 530** — Muestreo de auditoría.
- **NIA 500 / ISA 500** — Evidencia de auditoría.
- **AICPA Audit Sampling Guide**.
- **PCAOB AS 2315**.
- **Normas Globales de Auditoría Interna (IIA, 2025)** — Estándar 14 (desempeño del trabajo).

## Conceptos clave

### Riesgo de muestreo

Riesgo de que la conclusión de la muestra difiera de la conclusión que se obtendría examinando la población completa. Se controla con tamaños de muestra apropiados y selección imparcial.

### Riesgo no de muestreo

Errores no relacionados con el tamaño de la muestra (mala interpretación de evidencia, error en procedimiento, fatiga). Se controla con supervisión y entrenamiento.

### Población

El conjunto completo de elementos del que se extrae la muestra. Debe ser **completa** (toda la población está incluida) y **adecuada** (todos los elementos pueden ser seleccionados).

### Unidad de muestreo

El elemento individual que se prueba (factura, asiento, cliente, control ejecutado, etc.).

## Decisión inicial: estadístico o no estadístico

| Criterio | Estadístico | No estadístico |
|---|---|---|
| Permite cuantificar riesgo de muestreo | Sí | No |
| Selección | Aleatoria o sistemática | Por juicio o aleatoria |
| Tamaño de muestra | Calculado por fórmula | Por juicio |
| Proyección de errores | Matemática | Por juicio |
| Cuándo usar | Poblaciones grandes y homogéneas, evidencia robusta | Poblaciones pequeñas o donde el juicio del auditor es más eficiente |

Ambos son aceptables bajo NIA 530 si están adecuadamente diseñados.

## Tipos de muestreo

### Muestreo de atributos (pruebas de controles)

Pregunta: ¿el control opera o no opera en cada caso? Resultado binario.

**Tamaño de muestra** depende de:
- Nivel de confianza deseado (típicamente 90% o 95%).
- Tasa de desviación tolerable (TDR) — máxima desviación aceptable.
- Tasa de desviación esperada (EDR) — la que se anticipa antes de probar.

Tabla orientativa (95% confianza, EDR=0%):

| TDR | Tamaño de muestra |
|---|---|
| 2% | 149 |
| 3% | 99 |
| 4% | 74 |
| 5% | 59 |
| 7% | 42 |
| 10% | 29 |

Cuando la EDR es mayor a 0%, el tamaño aumenta. Para controles clave en SOX, el rango habitual es 25–60 según frecuencia (ver SKILL `evaluacion-controles`).

### Muestreo de variables / sustantivo

Pregunta: ¿cuál es el valor monetario del error en la población?

Subtipos:
- **MUS (Monetary Unit Sampling)** — cada unidad monetaria es una unidad de muestreo; los elementos grandes tienen mayor probabilidad de ser seleccionados. Eficiente cuando los errores se esperan por sobrestimación.
- **Muestreo estratificado clásico** — la población se divide en estratos por valor o naturaleza y se muestrea cada estrato. Útil cuando hay elementos clave y otros pequeños.
- **Selección por valor monetario** — los elementos sobre cierto umbral se examinan al 100%, y el resto se muestrea.

### Muestreo no estadístico común

- **Selección por juicio**: el auditor escoge elementos por relevancia (mayores valores, transacciones con partes relacionadas, registros recientes, etc.).
- **Selección dirigida**: para probar un riesgo específico, no para concluir sobre la población.
- **Examen al 100%** de elementos clave + muestra del resto.

## Selección de la muestra

Métodos válidos:
1. **Aleatorio simple** — números aleatorios, cada elemento misma probabilidad.
2. **Sistemático** — intervalo fijo (= población / tamaño muestra). Cuidar que el intervalo no coincida con un patrón.
3. **Estratificado** — submuestras dentro de cada estrato.
4. **Por bloques** — solo si está bien justificado (poco recomendado, riesgo alto).
5. **Por juicio** — válido en muestreo no estadístico.

Documentar siempre: criterio de selección, parámetros, semilla aleatoria si aplica, lista de elementos seleccionados.

## Proceso

### Paso 1 — Definir el objetivo de la prueba

¿Qué quiere concluir el auditor? (ej. "el control de aprobación de pagos opera consistentemente"). El objetivo determina si es muestreo de atributos o variables.

### Paso 2 — Definir la población

- Listar la fuente (archivo, sistema, módulo, periodo).
- Validar que está completa: cuadrar contra mayor, totales o reportes oficiales.
- Excluir elementos no relevantes (ej. anulaciones con contrarregistro), documentando.

### Paso 3 — Determinar el tamaño de la muestra

Para muestreo estadístico, usar tablas o calculadoras (Excel con fórmulas binomiales/Poisson, software como ACL/IDEA, Python con `scipy.stats`).

Variables de entrada típicas:
- Confianza
- Error tolerable
- Error esperado
- Tamaño de población (si <10.000)

Documentar la fórmula o tabla utilizada.

### Paso 4 — Seleccionar la muestra

Ejecutar el método elegido. Si es aleatorio, fijar y registrar la semilla. Producir una lista numerada de elementos seleccionados con su identificador único.

### Paso 5 — Aplicar procedimientos a cada elemento

Para cada ítem, ejecutar el procedimiento (inspección, recálculo, confirmación, etc.) y documentar resultado: conforme / desviación / inconcluso.

Si un elemento no se puede examinar:
- Si hay sustituto adecuado, usarlo y documentar.
- Si no, considerarlo como desviación o como limitación al alcance.

### Paso 6 — Evaluar resultados y proyectar errores

**Para muestreo de atributos**:
- Tasa de desviación de la muestra = desviaciones / tamaño muestra.
- Comparar con TDR. Si supera, el control no es eficaz.
- Considerar el límite superior de desviación (con la tabla correspondiente).

**Para muestreo de variables**:
- Calcular error proyectado = (error muestra / valor muestra) × valor población, o usar el método específico de MUS.
- Comparar con materialidad.
- Considerar si los errores son sistemáticos (el mismo origen se repite) — en ese caso investigar la causa, no solo proyectar.

### Paso 7 — Concluir

Concluir si el objetivo de la prueba se cumple. Si no, ampliar muestra, aplicar procedimientos alternativos, o reportar la limitación.

## Outputs esperados

1. **Memorando de muestreo**: objetivo, población, método, tamaño, criterios.
2. **Listado de elementos seleccionados** con sus identificadores.
3. **Resultados de la prueba** elemento por elemento.
4. **Cálculo de proyección** de errores.
5. **Conclusión** sobre el objetivo de la prueba.

## Banderas rojas

- Muestra "aleatoria" sin método documentado (sospecha de selección sesgada).
- Población definida después de seleccionar la muestra.
- Tamaño de muestra muy pequeño justificado solo por "criterio profesional" sin más sustento.
- Sustitución libre de elementos no encontrados sin reglas claras.
- Ignorar errores cualitativos (ej. fraude detectado en un elemento) por estar dentro del rango cuantitativo aceptable.
- Proyección automática sin analizar la naturaleza de los errores.

## Buenas prácticas

- Cuando aparezca un error inesperado en la muestra, **no** asumir que es aislado. Investigar la causa raíz antes de proyectar.
- Documentar la **semilla aleatoria** o el algoritmo de selección para que el trabajo sea reproducible.
- Para poblaciones muy heterogéneas, estratificar siempre.
- Considerar siempre el examen 100% de elementos clave (top values, partes relacionadas, ajustes manuales del último día del mes, transacciones por encima de un umbral).
- Combinar muestreo con analítica de datos (ver SKILL `analitica-datos`): la analítica puede examinar el 100% de la población en muchos casos y volver innecesario el muestreo.

## Conexión con otras SKILLs

- Es invocada desde `evaluacion-controles` (muestras para pruebas de operación) y desde varias especialidades (financiera, operativa, cumplimiento).
- Su alternativa moderna es `analitica-datos` — siempre considerarla primero.
- Los resultados se documentan vía `papeles-trabajo`.

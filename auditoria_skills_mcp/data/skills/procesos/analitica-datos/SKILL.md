---
name: analitica-datos
description: Aplicar técnicas de análisis de datos en pruebas de auditoría — ACL, IDEA, SQL, Python, R — para procesar poblaciones completas, detectar anomalías, ejecutar reglas de negocio y producir evidencia objetiva. Activar siempre que se hable de analítica, data analytics, ACL, IDEA, scripting de auditoría, prueba al 100% de la población, queries, cruces, anomalías, outliers, reglas de detección, ETL, pruebas masivas, análisis de transacciones, examen extenso, CAATs, Computer Assisted Audit Techniques, big data en auditoría.
---

# Analítica de datos para auditoría

## Propósito

La analítica de datos transforma la auditoría: en lugar de muestrear, se examina el 100% de la población; en lugar de inspeccionar visualmente, se aplican reglas; en lugar de esperar al cierre, se monitorea continuamente. Esta SKILL guía la aplicación rigurosa de técnicas de analítica en pruebas de auditoría.

Cuando es viable, la analítica debe **preferirse sobre el muestreo**. El muestreo solo se justifica cuando la analítica no puede ejecutarse (datos no disponibles, calidad insuficiente, costo prohibitivo).

## Cuándo activar esta SKILL

- Cuando exista población digital extraíble del sistema.
- Para pruebas que se beneficien de cobertura 100% (validación de integridad, detección de outliers, cruces entre tablas).
- Para auditoría continua y monitoreo continuo.
- Cuando el usuario pregunte por SQL, Python, ACL/IDEA, dashboards, scripts, automatización de pruebas.

## Marco de referencia

- **GTAG 16: Data Analysis Technologies** (IIA).
- **GTAG 3: Continuous Auditing** (IIA).
- **ITAF — IT Audit Framework** (ISACA).
- **Normas Globales de Auditoría Interna (IIA, 2025)** — Estándar 14 (desempeño del trabajo).
- **NIA 500** — Evidencia (la analítica es una técnica de obtención de evidencia).
- **AICPA Audit Data Standards (ADS)** — formatos comunes para datos contables.

## Tipos de procedimientos analíticos

### 1. Validación de integridad

Verificar completitud y consistencia de los datos:
- Cuadre con totales del sistema (control totals).
- Verificación de continuidad (números de documento secuenciales sin saltos).
- Detección de duplicados.
- Validación de referencias cruzadas (claves foráneas).
- Comparación con periodos anteriores.

### 2. Aplicación de reglas de negocio

Probar el cumplimiento de políticas o lógica esperada:
- Pagos sobre umbral aprobados solo por roles autorizados.
- Asientos con cargos y abonos que cuadran.
- Fechas dentro del periodo correcto.
- Códigos contables válidos.
- Combinaciones prohibidas (ej. mismo proveedor con misma factura registrada dos veces).

### 3. Detección de anomalías y outliers

Identificar valores fuera de patrón:
- Análisis de Benford para detectar manipulación numérica.
- Z-score, percentiles, IQR para outliers cuantitativos.
- Frecuencias inusuales (proveedores con muchas facturas justo bajo el umbral de aprobación).
- Patrones de fechas (transacciones siempre el último día del mes / fin de semana).

### 4. Cruces entre fuentes

Identificar inconsistencias entre sistemas:
- Empleados activos en nómina vs cargos en sistema de RH.
- Proveedores en maestros vs lista de empleados (posibles partes relacionadas no declaradas).
- Compras vs recepciones vs pagos (cuadre del ciclo).
- Inventario contable vs físico.

### 5. Análisis predictivo y aprendizaje automático

- Modelos de scoring de riesgo de fraude.
- Clustering para agrupar transacciones similares.
- Series de tiempo para detectar quiebres de tendencia.

Para auditoría estos modelos no reemplazan el juicio: identifican candidatos para revisión humana.

## Proceso

### Paso 1 — Definir el objetivo analítico

Antes de tocar datos, escribir claramente:
- ¿Qué pregunta quiere responderse?
- ¿Qué evidencia produciría una respuesta?
- ¿Qué decisión depende del resultado?

Ejemplo bueno: "Identificar facturas duplicadas registradas en cuentas por pagar durante 2025."

Ejemplo malo: "Analizar las cuentas por pagar."

### Paso 2 — Comprender la fuente de datos

- Solicitar al área de TI o al dueño del sistema:
  - Diccionario de datos.
  - Esquema de tablas relevantes.
  - Reglas de validación implementadas en el sistema.
  - Acuerdos de extracción y formato.
- Documentar: sistema fuente, módulo, tablas, periodo, criterios de filtro.

### Paso 3 — Extraer y validar datos

1. Definir el método de extracción (export del sistema, query directa, archivo plano, API).
2. Validar la **completitud** de la extracción contra totales oficiales (mayor general, reportes administrados).
3. Validar la **consistencia** (totales, número de registros, fechas mínima/máxima).
4. Documentar el método y los controles de extracción aplicados.

**Nunca confiar en una extracción sin reconciliar.**

### Paso 4 — Preparar los datos (ETL)

- Limpieza: tipos de dato, formatos, valores faltantes, encoding.
- Normalización: estandarizar nombres de proveedores, códigos, fechas.
- Enriquecimiento: agregar dimensiones (ej. categoría del proveedor, tipo de gasto).
- Documentar todas las transformaciones (en un script reproducible).

### Paso 5 — Diseñar y ejecutar la prueba

Para cada test:
1. Documentar la hipótesis o regla.
2. Escribir el código (SQL, Python, R, ACL, IDEA) de forma legible y comentada.
3. Ejecutar y obtener resultado.
4. Validar el resultado: ¿la cifra tiene sentido? Hacer cuadres rápidos.
5. Guardar el output (CSV, base, dashboard) referenciando el papel de trabajo.

### Paso 6 — Investigar candidatos identificados

La analítica produce **candidatos**, no hallazgos. Cada candidato debe ser:
- Examinado individualmente o por muestra.
- Confirmado con evidencia adicional antes de elevarlo a hallazgo.
- Discutido con la administración para entender el contexto antes de concluir.

Falsos positivos son normales; documentar la depuración.

### Paso 7 — Documentar y conservar

Cada análisis debe quedar como papel de trabajo con:
- Objetivo y criterio.
- Fuente de datos y método de extracción.
- Validación de completitud.
- Script (versionado).
- Parámetros y semilla aleatoria si aplica.
- Output bruto y output depurado.
- Conclusión.

Si el análisis se va a reutilizar, dejar el script en repositorio versionado.

## Herramientas comunes

| Herramienta | Fortaleza | Cuándo elegirla |
|---|---|---|
| **ACL / Galvanize HighBond** | Auditoría especializada, log de transformaciones | Cuando la organización ya la usa, requisito de trazabilidad |
| **IDEA (CaseWare)** | Auditoría especializada, fácil para auditores | Equipos con perfil contable/financiero |
| **SQL** | Universal en bases de datos | Datos en RDBMS, queries complejas |
| **Python (pandas, numpy)** | Flexibilidad total, ML, visualización | Análisis avanzado, modelos predictivos, big data |
| **R** | Estadística profunda | Pruebas estadísticas formales, Benford, regresión |
| **Power BI / Tableau** | Visualización y dashboarding | Reporte continuo a Comité, KPIs |
| **Excel + Power Query** | Disponibilidad universal | Análisis pequeños o medianos |

## Pruebas analíticas recurrentes (catálogo)

### Compras y cuentas por pagar
- Facturas duplicadas (mismo proveedor + mismo monto + fecha cercana).
- Pagos sin orden de compra correspondiente.
- Pagos a proveedores no en maestro (one-time vendors).
- Justo bajo umbrales de aprobación.
- Pagos con dirección o cuenta bancaria coincidente con empleados.
- Modificaciones a datos maestros de proveedores antes de pagos.

### Nómina
- Empleados duplicados (mismo número de identificación).
- Empleados con sueldo > X desviaciones del promedio del cargo.
- Pagos a empleados terminados.
- Cuentas bancarias compartidas entre empleados.
- Horas extra que superan límites legales.

### Ingresos y cuentas por cobrar
- Notas crédito sobre umbral o frecuencia inusual.
- Ventas el último día del periodo (corte/cutoff).
- Descuentos fuera de política.
- Saldos antiguos no provisionados.

### Asientos manuales (Journal entry testing)
- Asientos en cuentas inusuales.
- Asientos al final del mes/trimestre/año.
- Asientos por usuarios sin perfil contable.
- Asientos con descripción nula o genérica.
- Asientos con montos redondos sospechosos.

### Inventario
- Movimientos negativos.
- Costos unitarios fuera de rango.
- Recepciones sin orden de compra.
- Conciliaciones físicas vs sistema con diferencias > umbral.

### Tarjetas de crédito corporativas
- Compras en categorías personales.
- Compras en fines de semana o feriados.
- Compras justo bajo el umbral de aprobación.
- Mismos vendor + mismo día + mismo monto.

### Análisis de Benford
- Aplicable a montos monetarios mayores a 0 con suficiente volumen y rango.
- Comparar primer dígito (y segundo dígito) contra distribución esperada.
- Desviaciones significativas son **indicadores**, no pruebas de fraude.

## Auditoría continua y monitoreo continuo

- **Auditoría continua**: ejecución automatizada, recurrente y programada de procedimientos por parte de auditoría interna.
- **Monitoreo continuo**: ejecución similar pero por parte de la administración.

Beneficios: detección temprana, cobertura amplia, eficiencia.

Requisitos:
- Acceso recurrente a datos (idealmente vía replica de solo lectura).
- Reglas estables y mantenidas.
- Proceso claro de manejo de excepciones.
- Indicadores en dashboard.

Ver SKILL `auditoria-continua` para más detalle.

## Banderas rojas

- "Confiar" en una extracción sin validar completitud.
- Falsos positivos no documentados (al final no se puede explicar el resultado).
- Scripts no versionados ni comentados — irreproducibles.
- Hallazgos basados solo en analítica sin investigación de casos.
- Modelos de ML opacos cuyas decisiones no se pueden explicar.
- Datos sensibles manejados sin enmascaramiento ni controles de acceso.
- Análisis sin documentar la fuente exacta y el periodo.

## Buenas prácticas

- **Empezar simple**: una buena query SQL gana a un modelo complejo en la mayoría de casos.
- **Controlar versiones** con Git u equivalente.
- **Documentar con notebooks** (Jupyter, R Markdown) que mezclan código, comentarios y output.
- **Reusar bibliotecas** internas: cada test que se construya debería ser componente del próximo engagement similar.
- **Validar resultados con la administración** antes de incluirlos en el informe — descartar falsos positivos sustenta credibilidad.
- **Seguridad de datos**: enmascarar PII, usar entornos seguros, minimizar copia de datos.

## Conexión con otras SKILLs

- Es una alternativa o complemento del `muestreo`.
- Se documenta vía `papeles-trabajo` (script + parámetros + output).
- Es la base de `auditoria-continua`.
- Aplica directamente en `auditoria-financiera` (asientos, cuentas), `auditoria-forense` (red flags), `auditoria-tecnologia-informacion` (logs, accesos), `auditoria-cumplimiento` (transacciones bajo regulación).
- En cualquier especialidad debe considerarse antes de elegir muestreo manual.

---
name: auditoria-continua
description: Diseñar, implementar y operar capacidades de auditoría continua y monitoreo continuo, con ejecución automatizada y recurrente de procedimientos analíticos sobre poblaciones completas para detección temprana y cobertura amplia. Activar siempre que se hable de auditoría continua, continuous auditing, continuous monitoring, monitoreo continuo, GTAG 3, automatización de pruebas, dashboard de auditoría, alertas de auditoría, KRI, key risk indicators, frecuencia, real-time auditing, near-real-time, scripts recurrentes, plataforma analítica de auditoría.
---

# Auditoría continua y monitoreo continuo

## Propósito

La auditoría continua y el monitoreo continuo trasladan el aseguramiento de un evento puntual periódico a un proceso recurrente y automatizado. Permiten detección temprana de problemas, cobertura del 100% de transacciones críticas y mayor eficiencia en el uso del tiempo de auditores.

Esta SKILL guía el diseño, implementación y operación de capacidades de auditoría continua sostenibles.

## Cuándo activar esta SKILL

- Diseño de un programa de auditoría continua.
- Adición de nuevos casos de uso a un programa existente.
- Operación recurrente de monitores de auditoría continua.
- Cuando el usuario menciona dashboards, alertas, monitoreo automatizado, KRIs.

## Marco de referencia

- **GTAG 3 — Continuous Auditing: Coordinating Continuous Auditing and Monitoring to Provide Continuous Assurance** (IIA).
- **GTAG 16 — Data Analysis Technologies** (IIA).
- **AICPA — Audit Data Analytics y Continuous Auditing**.
- **ISACA — Continuous Auditing/Continuous Monitoring**.
- **Normas Globales de Auditoría Interna (IIA, 2025)** — Estándar 14 (desempeño del trabajo).

## Conceptos fundamentales

### Auditoría continua vs Monitoreo continuo

| Dimensión | Auditoría continua | Monitoreo continuo |
|---|---|---|
| Quién la opera | Auditoría interna | Administración |
| Propósito | Aseguramiento independiente | Gestión y control |
| Frecuencia | Recurrente (diaria, semanal, mensual) | Recurrente |
| Alcance típico | Procesos clave, transacciones materiales | Procesos del área que monitorea |
| Output | Indicadores, alertas, candidatos a investigar | Dashboards de gestión, alertas operacionales |

Cuando el monitoreo continuo de la administración es maduro y confiable, auditoría continua puede **apoyarse en él** y reducir su propio esfuerzo, aplicando un enfoque tipo "audit by exception".

### Modelo de madurez

Niveles típicos:
1. **Ad-hoc**: scripts puntuales por engagement.
2. **Repetible**: scripts reutilizables entre engagements.
3. **Automatizado**: ejecución programada con alertas.
4. **Integrado**: dashboards en vivo, integración con plataformas GRC.
5. **Predictivo**: ML, anticipación de riesgos.

Avanzar nivel a nivel — no saltar etapas.

### KRIs vs KPIs

- **KPI** (Key Performance Indicator): mide desempeño.
- **KRI** (Key Risk Indicator): mide la exposición o materialización de un riesgo.

Auditoría continua se centra en KRIs y en signos tempranos de pérdida de control.

## Casos de uso clásicos

### Procesos transaccionales

- Pagos sin orden de compra correspondiente.
- Facturas duplicadas.
- Pagos a proveedores nuevos en periodo corto.
- Transacciones bajo umbrales de aprobación.
- Asientos manuales en cuentas inusuales o por usuarios sin perfil contable.
- Notas crédito sobre umbral de aprobación.

### Accesos y configuraciones

- Cuentas con privilegios elevados sin justificación.
- Cuentas inactivas sin deshabilitar.
- Conflictos de segregación de funciones (SoD) en ERP.
- Accesos a producción fuera de horario laboral.
- Cambios a datos maestros (proveedores, empleados) seguidos por transacciones.

### Cambios de TI

- Cambios sin aprobación documentada.
- Cambios de emergencia frecuentes.
- Migración a producción por personas no autorizadas.

### Continuidad y operaciones

- Backups fallidos.
- Jobs batch fallidos sin reproceso.
- Tickets críticos abiertos por más del SLA.

### Cumplimiento

- Reportes regulatorios próximos a vencer.
- Vencimientos de licencias, permisos, contratos.
- Coincidencias con listas de sanciones.

### Recursos humanos / nómina

- Empleados duplicados.
- Pagos a empleados terminados.
- Cuentas bancarias compartidas.
- Horas extra excesivas.

## Proceso de implementación

### Paso 1 — Estrategia y priorización

1. Identificar procesos críticos por riesgo y por volumen.
2. Identificar dónde el muestreo periódico no es eficaz.
3. Identificar qué datos están disponibles o lo estarán.
4. Construir un roadmap de casos de uso priorizados.
5. Definir capacidades requeridas (analistas, infraestructura, datos).

### Paso 2 — Definición del caso de uso

Para cada caso de uso:
- **Riesgo o pregunta** que aborda.
- **Regla(s) de detección** específicas y testables.
- **Fuente de datos** y frecuencia de actualización.
- **Frecuencia de ejecución** (real time, daily, weekly).
- **Umbrales** de alerta.
- **Manejo de excepciones** (quién las recibe, cómo se cierran).
- **Métricas de éxito** del caso (precision, recall esperados).

### Paso 3 — Diseño técnico

- **Arquitectura de datos**: replica de solo lectura, lake, ETL.
- **Herramienta de ejecución**: Python, R, ACL, IDEA, plataformas GRC.
- **Plataforma de visualización**: Power BI, Tableau, herramientas nativas.
- **Plataforma de gestión de excepciones**: ServiceNow, Jira, herramientas GRC.
- **Seguridad**: enmascaramiento de PII, accesos, logs.

### Paso 4 — Construcción

- Versionar código (Git).
- Pruebas unitarias del código analítico.
- Pruebas con datos históricos (¿la regla habría detectado eventos pasados conocidos?).
- Pruebas con datos sintéticos para falsos positivos/negativos esperados.
- Documentación: diccionario de datos, lógica de la regla, supuestos.

### Paso 5 — Despliegue piloto

- Ejecutar en paralelo con monitoreo periódico tradicional.
- Comparar resultados.
- Ajustar umbrales y reglas.
- Validar con la administración los falsos positivos.

### Paso 6 — Operación y triage

Cuando una alerta se dispara:
1. Triage automático (descartar duplicados conocidos, etc.).
2. Asignación a analista.
3. Investigación: contactar al ejecutor del proceso, revisar evidencia.
4. Conclusión:
   - **Cierre falso positivo** con justificación.
   - **Excepción aceptable** documentada.
   - **Hallazgo** que se eleva a engagement formal.
5. Documentación de cada alerta tratada.

### Paso 7 — Mantenimiento continuo

- Monitoreo de la calidad de las reglas (precision/recall).
- Ajuste de umbrales según volumen y materialidad.
- Adaptación a cambios en el negocio (nuevo sistema, nuevos procesos).
- Retiro de casos obsoletos.
- Adición de nuevos casos.

### Paso 8 — Reporte al Comité

- Dashboard al Comité con tendencias, alertas críticas, hallazgos detectados por monitoreo continuo.
- KRIs evolucionando en el tiempo.
- Brechas conocidas en cobertura.
- Plan de adición de nuevos casos.

## KRIs comunes en programas de auditoría continua

| Categoría | KRI ejemplo |
|---|---|
| Compras | Volumen de pagos a proveedores nuevos / mes |
| Compras | % facturas pagadas sin orden de compra |
| Tesorería | Conciliaciones bancarias con partidas >30 días |
| Nómina | Empleados pagados después de fecha de terminación |
| TI – Accesos | Cuentas privilegiadas activas vs justificadas |
| TI – Cambios | % cambios de emergencia / total cambios |
| Cumplimiento | Días para reporte regulatorio próximo a vencer |
| Cumplimiento | Coincidencias en listas de sanciones |
| ESG | Días sin medición de fuente fija con monitoreo continuo regulatorio |
| Forense | Volumen y antigüedad de denuncias en línea ética |
| Operaciones | OEE / FTY semanal por planta |

## Banderas rojas (en el programa de auditoría continua mismo)

- Reglas con tasa de falsos positivos >50% sin afinarse — desgastan al equipo y se dejan de revisar.
- Alertas críticas sin investigarse durante semanas.
- Dashboard que se mira pero sobre el que no se actúa.
- Datos provenientes de extracciones manuales no automatizadas (insostenible).
- Casos de uso que se construyeron una vez y no se mantienen tras cambios del negocio.
- Reglas que ya no aplican porque el control cambió pero nadie actualizó la regla.
- Auditoría continua que duplica el monitoreo continuo de la administración sin coordinarse.
- Sin clasificación de severidad — todas las alertas tratadas igual.

## Buenas prácticas

- **Empezar pequeño y demostrar valor**: 5 casos bien hechos valen más que 50 mediocres.
- **Integrar con la administración**: el monitoreo continuo de la administración es aliado, no competencia.
- **Diseñar para sostenibilidad**: si depende de una persona, no es un programa.
- **Versionar todo**: reglas, datos, parámetros.
- **Medir el programa**: precision, recall, casos detectados por el programa, ahorro estimado.
- **Iterar constantemente**: ningún programa es estático.
- **Comunicar valor en lenguaje del negocio**: prevenidos vs detectados, pesos ahorrados, riesgos contenidos.
- **Cuidar la calidad de los datos**: una mala extracción produce resultados engañosos sistemáticamente.
- **Privacidad y proporcionalidad**: el monitoreo continuo no es excusa para vigilancia desmedida.

## Conexión con otras SKILLs

- Es la operacionalización de `analitica-datos` a escala recurrente.
- Reemplaza progresivamente el `muestreo` periódico cuando la cobertura 100% es viable.
- Alimenta a `seguimiento-recomendaciones` (verificación de implementación de controles puede ser continua).
- Provee KRIs que alimentan `aseguramiento-calidad` y la `planeacion-basada-riesgos` (reasignar capacidad cuando un proceso muestra deterioro).
- Aplica transversalmente a las especialidades — cada una tiene casos de uso típicos.
- Las alertas críticas pueden gatillar engagements ad hoc (financiera, forense, ciberseguridad, etc.).

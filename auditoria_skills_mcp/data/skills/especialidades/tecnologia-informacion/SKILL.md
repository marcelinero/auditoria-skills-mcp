---
name: auditoria-tecnologia-informacion
description: Auditar el gobierno de TI, los controles generales de TI (ITGCs) y los controles automatizados de aplicación, evaluar la gestión de cambios, accesos lógicos, operaciones, continuidad y seguridad tecnológica conforme a COBIT, ITAF, GTAGs e ISO 27001. Activar siempre que se hable de auditoría de TI, IT audit, controles generales de TI, ITGC, COBIT, gobierno de TI, gestión de accesos, gestión de cambios, gestión de operaciones, computación en la nube, SaaS auditoría, BCP, DRP, continuidad de negocio, virtualización, ERP, SAP, Oracle, integraciones, interfaces, batch jobs, base de datos auditoría.
---

# Auditoría de tecnologías de información

## Propósito

La auditoría de TI evalúa el gobierno y los controles sobre la infraestructura, aplicaciones y datos que soportan a la organización. Es prerrequisito para confiar en cualquier control automatizado: si los controles generales de TI no operan, los controles de aplicación que dependen de ellos pierden confiabilidad.

## Cuándo activar esta SKILL

- Auditorías específicas de áreas de TI (operaciones, desarrollo, infraestructura, seguridad).
- Como complemento de auditoría financiera (ITGCs para fiabilidad de los sistemas que producen los EE.FF.).
- Auditorías de implementaciones y migraciones (ERP, SaaS, nube).
- Auditorías de BCP/DRP, gestión de incidentes.
- Auditorías de gestión de proveedores tecnológicos y contratos.

## Marco de referencia

- **COBIT 2019** (ISACA) — gobierno y gestión de TI empresarial.
- **ITAF — Information Technology Assurance Framework** (ISACA).
- **GTAGs — Global Technology Audit Guides** (IIA): especialmente
  - GTAG 1: Information Technology Risk and Controls
  - GTAG 8: Auditing Application Controls
  - GTAG 14: Auditing User-Developed Applications
  - GTAG sobre nube, ciberseguridad, identidad
- **ISO/IEC 27001 e ISO/IEC 27002** — gestión de seguridad de la información (ver también SKILL `auditoria-ciberseguridad`).
- **ISO/IEC 20000** — gestión de servicios de TI.
- **ITIL 4** — buenas prácticas de gestión de servicios.
- **NIST SP 800-53** — controles de seguridad y privacidad (sector público EE. UU., referencia global).
- **CSA CCM** — Cloud Controls Matrix.

## Estructura típica de los Controles Generales de TI (ITGCs)

Los ITGCs son controles a nivel de entidad/infraestructura sobre los que descansan los controles de aplicación. Áreas:

### 1. Gestión de accesos lógicos (Access Management)
- Provisión y baja oportuna de cuentas (joiners, movers, leavers).
- Roles y perfiles basados en menor privilegio.
- Segregación de funciones (SoD) en aplicaciones críticas.
- Autenticación robusta (MFA donde aplica).
- Gestión de cuentas privilegiadas (PAM).
- Revisión periódica de accesos (recertificación).
- Logs de acceso y de actividad.

### 2. Gestión de cambios (Change Management)
- Solicitud, aprobación, desarrollo, prueba y migración a producción.
- Segregación entre desarrollo, pruebas y producción.
- Cambios de emergencia con revisión post-implementación.
- Control de versiones del código.
- Aprobación independiente del migrador.

### 3. Gestión de operaciones (IT Operations)
- Programación y monitoreo de procesos batch.
- Gestión de copias de respaldo (frecuencia, ubicación, prueba de restauración).
- Gestión de incidentes y problemas.
- Monitoreo de capacidad y desempeño.
- Gestión de la configuración (CMDB).

### 4. Continuidad del negocio y recuperación ante desastres
- BIA (Business Impact Analysis).
- BCP (Business Continuity Plan) y DRP (Disaster Recovery Plan).
- RTO / RPO definidos por aplicación crítica.
- Pruebas regulares (mesa, paralelo, full).
- Sitios alternos.

### 5. Seguridad física de centros de datos
- Control de acceso físico.
- Energía y refrigeración redundantes.
- Detección y supresión de fuego.
- Monitoreo 24/7.

### 6. Gestión de terceros y nube
- Due diligence en contratación.
- Cláusulas de seguridad, auditabilidad, derecho a auditar.
- Reportes SOC 1 / SOC 2 / ISAE 3402 del proveedor.
- Modelo de responsabilidad compartida en nube (IaaS/PaaS/SaaS).
- Gestión de identidad federada y APIs.

## Controles de aplicación

Por aplicación crítica, evaluar:

- **Validaciones de entrada**: tipos de dato, rangos, obligatoriedad, integridad referencial.
- **Cálculos automatizados**: fórmulas, redondeos, conversiones de moneda.
- **Interfaces**: integridad y completitud de datos transferidos entre sistemas.
- **Salidas**: reportes generados, exportaciones, archivos a terceros.
- **Pistas de auditoría**: logs de transacciones y cambios.
- **Configuración funcional**: parámetros que afectan el comportamiento del proceso.

Para cada control automatizado, probar:
1. **Diseño**: revisar la configuración o código.
2. **Operación efectiva**: la prueba se basa típicamente en **una sola transacción bien diseñada** porque el comportamiento es determinístico — si el control general de cambios opera, el control opera consistentemente.

## Proceso

### Fase 1 — Comprensión del entorno tecnológico

1. Inventario de aplicaciones críticas para los procesos auditados.
2. Inventario de bases de datos, sistemas operativos, redes, hipervisores.
3. Identificación de proveedores de nube y servicios SaaS.
4. Diagrama de arquitectura y flujos de información.
5. Identificación de procesos de TI (desarrollo, operaciones, soporte).
6. Identificación de marcos adoptados por la organización (ITIL, ISO, NIST).

### Fase 2 — Evaluación del gobierno de TI

- Comité de TI / Steering Committee.
- Estrategia de TI alineada con estrategia del negocio.
- Presupuesto y portafolio de inversión.
- KPIs de TI.
- Gestión de riesgos de TI.

Usar COBIT 2019 como referencia: 40 objetivos de gobierno y gestión.

### Fase 3 — Pruebas de ITGCs

Para cada área (accesos, cambios, operaciones, continuidad):

1. Levantar y documentar el proceso.
2. Identificar controles clave.
3. Walkthrough.
4. Pruebas de diseño.
5. Pruebas de operación (muestras de cambios, accesos, jobs, etc.).
6. Conclusión por área.

#### Pruebas típicas de accesos

- Listado completo de usuarios activos vs RR.HH. activos (detectar cuentas huérfanas).
- Usuarios con privilegios elevados — revisar justificación.
- Usuarios inactivos no deshabilitados.
- Cuentas genéricas / compartidas.
- Recertificaciones del periodo: muestra y revisión de soporte.
- Conflictos SoD en perfiles del ERP.

#### Pruebas típicas de cambios

- Listado completo de cambios al periodo.
- Muestra de cambios: validar solicitud, aprobación, desarrollo, prueba, migración.
- Cambios de emergencia con revisión post.
- Acceso a producción: sólo migradores autorizados.

#### Pruebas típicas de operaciones

- Muestra de procesos batch: programación, ejecución, errores, reproceso.
- Backups: muestra y prueba de restauración (al menos una).
- Incidentes críticos: muestra de incidentes y validación de cierre.

#### Pruebas típicas de continuidad

- Existencia y vigencia del BCP/DRP.
- Última prueba ejecutada (resultados y plan de mejora).
- Cobertura del BIA respecto a procesos críticos.
- Validación de RTO/RPO contra aplicaciones reales.

### Fase 4 — Auditoría de la nube y SaaS

Aspectos específicos:

- Modelo de responsabilidad compartida claro y entendido.
- Configuraciones nativas (CSPM): IAM, redes, almacenamiento público, encriptación.
- Reportes SOC 2 Tipo II de proveedores críticos.
- Gestión de claves (BYOK / KMS).
- Localización de datos y soberanía.
- Respaldo de datos en SaaS (no asumir que el proveedor los protege para todos los escenarios).
- Plan de salida (data portability).

Frameworks útiles: CSA CCM, AWS/Azure/GCP Well-Architected, CIS Benchmarks.

### Fase 5 — Conclusión y dependencia con auditoría financiera

Si la auditoría financiera planea confiar en controles automatizados:
- Los ITGCs deben ser eficaces durante todo el periodo.
- Si los ITGCs son deficientes, los controles automatizados pierden confiabilidad y se debe ampliar las pruebas sustantivas.

## Outputs esperados

1. Inventario tecnológico documentado.
2. Matriz de ITGCs con resultados.
3. Pruebas de cambios, accesos, operaciones, continuidad.
4. Listado de configuraciones críticas evaluadas.
5. Hallazgos de TI con causa raíz e impacto en el negocio.
6. Conclusión sobre la confiabilidad de los sistemas que soportan procesos auditables.

## Banderas rojas

- Cuentas con privilegios elevados sin justificación o sin recertificación.
- Cuentas genéricas usadas por humanos.
- Migrador a producción que también desarrolla.
- Backups sin pruebas de restauración.
- BCP/DRP nunca probado o desactualizado.
- Aplicaciones críticas sin propietario funcional definido.
- "Shadow IT" — aplicaciones desarrolladas por usuarios sin gobierno.
- Configuraciones por defecto de proveedores nunca endurecidas.
- Logs no retenidos lo suficiente o sin protección contra modificación.
- Proveedores cloud sin SOC 2 ni equivalente.

## Buenas prácticas

- **Combinar pruebas técnicas con pruebas de proceso**: ver evidencia en el sistema, no solo políticas escritas.
- **Usar herramientas de extracción** directa de configuraciones (CIS-CAT, Tenable, Nessus, herramientas nativas de cloud).
- **Apoyarse en logs**: los logs cuentan la verdad de lo que pasó.
- **No confiar ciegamente en SOC 2**: leer el reporte completo, validar excepciones, complementary user entity controls (CUECs).
- **Mantenerse actualizado**: la tecnología cambia rápido — el auditor debe formarse continuamente en cloud, contenedores, APIs, IA, etc.

## Conexión con otras SKILLs

- Es la base técnica que soporta `auditoria-financiera` (ICFR), `auditoria-cumplimiento`, `auditoria-operativa` cuando hay sistemas.
- Se complementa intensamente con `auditoria-ciberseguridad` (foco en amenazas) y con `auditoria-inteligencia-artificial`.
- Usa fuertemente `analitica-datos` (logs, configuraciones, listados de usuarios).
- Aplica todas las SKILLs de proceso.

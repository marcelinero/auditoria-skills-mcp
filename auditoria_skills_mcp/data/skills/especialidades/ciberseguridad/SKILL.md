---
name: auditoria-ciberseguridad
description: Evaluar la postura de ciberseguridad de la organización aplicando NIST CSF 2.0, ISO 27001/27002 y CIS Controls — gobernanza de seguridad, identificación, protección, detección, respuesta y recuperación. Activar siempre que se hable de ciberseguridad, cybersecurity audit, NIST CSF, ISO 27001, ISO 27002, CIS Controls, MITRE ATT&CK, SIEM, SOC, EDR, DLP, IAM, MFA, gestión de vulnerabilidades, pentest, red team, ransomware, phishing, NIS 2, zero trust, gestión de identidades, respuesta a incidentes, IR, threat hunting, breach.
---

# Auditoría de ciberseguridad

## Propósito

La auditoría de ciberseguridad evalúa si la organización entiende, gestiona y reduce sus riesgos cibernéticos a un nivel aceptable. Va más allá de los controles generales de TI clásicos: incluye amenazas activas, vectores de ataque, capacidades de detección y respuesta, y resiliencia ante incidentes.

## Cuándo activar esta SKILL

- Auditorías específicas de ciberseguridad o del programa completo.
- Evaluaciones de madurez con NIST CSF 2.0, ISO 27001, CIS Controls.
- Después de incidentes: revisión post-incidente.
- Para certificaciones (ISO 27001) o cumplimiento (NIS 2, regulación sectorial).
- Cuando el usuario menciona ataque, brecha, vulnerabilidad, ransomware, IDS, SIEM, IR.

## Marco de referencia

- **NIST Cybersecurity Framework 2.0** — funciones: Govern, Identify, Protect, Detect, Respond, Recover.
- **ISO/IEC 27001** — Sistema de gestión de seguridad de la información (SGSI).
- **ISO/IEC 27002** — Código de práctica para controles de seguridad.
- **ISO/IEC 27005** — Gestión de riesgos de seguridad de la información.
- **ISO/IEC 27017 / 27018** — Seguridad y privacidad en nube.
- **ISO/IEC 27035** — Gestión de incidentes.
- **CIS Critical Security Controls v8** — 18 controles priorizados.
- **MITRE ATT&CK** — taxonomía de tácticas, técnicas y procedimientos de adversarios.
- **NIST SP 800-53** — controles para sistemas federales (referencia global).
- **NIST SP 800-61** — guía de manejo de incidentes.
- **NIS 2 Directive** (UE) — ciberseguridad de entidades esenciales e importantes.
- **PCI-DSS v4** — pagos.
- **CSA Cloud Controls Matrix**.
- **OWASP Top 10** — riesgos de aplicaciones web.

## Conceptos fundamentales

### Funciones del NIST CSF 2.0

1. **Govern (GV)** — gobernanza de ciberseguridad: estrategia, roles, políticas, gestión del riesgo, supervisión.
2. **Identify (ID)** — comprensión: activos, riesgos, dependencias.
3. **Protect (PR)** — controles preventivos: identidad, datos, plataformas, capacitación.
4. **Detect (DE)** — capacidades de detección: monitoreo continuo, análisis.
5. **Respond (RS)** — respuesta a incidentes: planeación, comunicación, contención, mitigación.
6. **Recover (RC)** — recuperación: recuperación de operaciones y comunicación.

### Triada CIA + +

- **Confidencialidad** (C), **Integridad** (I), **Disponibilidad** (A) — base clásica.
- Adicionalmente: **Autenticidad**, **No repudio**, **Trazabilidad**, **Privacidad**.

### Modelo de defensa en profundidad

Capas: perímetro de red → segmentación interna → host (EDR) → aplicación → datos → identidad. La falla de una capa no debe comprometer el sistema; cada capa eleva el costo del ataque.

### Zero Trust

"Nunca confiar, siempre verificar". Asumir que la red es hostil; verificar identidad y postura del dispositivo en cada acceso. Microsegmentación. Acceso por menor privilegio y justo a tiempo.

### Cyber Kill Chain / MITRE ATT&CK

Modelos para entender el ciclo del ataque y mapear controles a las técnicas que mitigan.

## Proceso

### Fase 1 — Comprensión del contexto cibernético

1. Inventario de activos críticos: datos, sistemas, identidades, terceros.
2. Comprensión del panorama de amenazas: industria, geografía, casos recientes.
3. Identificación de actores potenciales (cibercrimen, hacktivismo, estado-nación, insider).
4. Identificación de superficies de ataque: perimetral, aplicaciones, supply chain, factor humano.
5. Mapeo regulatorio aplicable.

### Fase 2 — Evaluación del gobierno de ciberseguridad (Govern)

- Estrategia de ciberseguridad documentada y aprobada.
- CISO con autoridad, recursos y reporte adecuado (no bajo el CIO en organizaciones maduras).
- Comité de ciberseguridad o equivalente.
- Apetito de riesgo cibernético.
- Política de seguridad de la información.
- Reporte a junta y comité de auditoría — frecuencia, contenido.
- Presupuesto y benchmarks.

### Fase 3 — Identificación (Identify)

- Inventario de activos (HW, SW, datos, identidades) — completo y actualizado.
- Clasificación de información.
- Mapa de cadena de valor y dependencias críticas.
- Evaluación de riesgos (ISO 27005 o equivalente).
- Gestión de terceros: due diligence, contratos, monitoreo.

### Fase 4 — Protección (Protect)

#### Identidad y acceso (IAM)
- MFA (multifactor) en todos los servicios críticos y para usuarios privilegiados — validar cobertura real.
- Gestión de cuentas privilegiadas (PAM): bóveda de credenciales, sesiones registradas, acceso just-in-time.
- Federación, SSO con políticas de acceso condicional.
- Joiners/Movers/Leavers — pruebas de oportunidad.
- Recertificación de accesos.
- Cuentas de servicio: inventario, rotación de credenciales, mínimo privilegio.

#### Datos
- Clasificación + DLP (Data Loss Prevention).
- Encriptación en reposo y en tránsito.
- Gestión de claves (KMS, HSM).
- Mascaramiento en ambientes no productivos.

#### Endpoints y servidores
- EDR/XDR desplegado.
- Hardening (CIS Benchmarks).
- Parches: validar SLA por criticidad.
- Antivirus actualizado.
- Restricciones de USB y software no aprobado.

#### Red
- Segmentación.
- Firewalls, IPS, WAF.
- Filtrado de DNS y proxy web.
- Inspección de tráfico cifrado en puntos críticos.
- Acceso remoto: VPN moderna o ZTNA.
- Inalámbrico: WPA3, redes segregadas.

#### Aplicaciones
- SDLC seguro: revisión de código, SAST, DAST, dependencias (SCA).
- Pruebas de penetración pre-producción.
- Hardening de configuración.
- Gestión de secretos (no hardcodeados).

#### Concientización
- Capacitación obligatoria.
- Simulaciones de phishing.
- Métricas: clic rate, reporte rate.
- Cultura de reporte sin estigma.

### Fase 5 — Detección (Detect)

- SIEM con casos de uso definidos (alineados con MITRE ATT&CK).
- SOC 24/7 o servicio gestionado (MSSP) con SLA.
- Cobertura de fuentes de log: endpoints, red, identidad, nube, aplicaciones.
- Retención de logs adecuada.
- Threat intelligence integrada.
- Threat hunting proactivo.
- Métricas: MTTD (mean time to detect), false positives.

### Fase 6 — Respuesta (Respond)

- Plan de respuesta a incidentes documentado y aprobado.
- Equipo CSIRT con roles y suplencias.
- Playbooks por tipo de incidente (ransomware, phishing, DDoS, brecha de datos).
- Comunicación: interna, junta, regulador, autoridad, clientes, prensa.
- Coordinación con asesoría legal y aseguradora.
- Ejercicios (table-top) anuales mínimo.
- Métricas: MTTR, contenidos, recurrentes.

### Fase 7 — Recuperación (Recover)

- BCP/DRP integrado con respuesta cibernética.
- Backups inmutables y aislados (offline o air-gapped) — críticos contra ransomware.
- Pruebas de restauración periódicas.
- RTO/RPO por sistema crítico.
- Lecciones aprendidas formalizadas.

### Fase 8 — Pruebas técnicas complementarias

- **Vulnerability assessment**: scans regulares (interno, externo, web).
- **Penetration testing**: anual mínimo, scoping claro.
- **Red team**: ejercicios adversariales contra controles y SOC.
- **Purple team**: cooperación red+blue para mejorar detección.
- **Auditoría de configuración** con CIS-CAT o equivalente.
- **Phishing simulado** con tasas medibles.

### Fase 9 — Métricas y madurez

Calificar contra NIST CSF 2.0 niveles (Tier 1: parcial → Tier 4: adaptativo) o contra perfil objetivo definido por la organización.

KPIs típicos:
- % activos con EDR / con parche al día.
- Cobertura MFA.
- Tiempos MTTD / MTTR.
- Cuentas privilegiadas activas vs justificadas.
- % de empleados que reportaron phishing simulado.
- Número de incidentes por severidad.
- Edad media de vulnerabilidades críticas abiertas.

## Outputs esperados

1. Inventario de activos críticos y mapa de amenazas.
2. Evaluación de madurez por función NIST CSF.
3. Resultados de pruebas técnicas (vuln scan, pentest, configuración).
4. Pruebas de operación de controles clave.
5. Hallazgos priorizados por riesgo cibernético cuantificado (impacto × probabilidad).
6. Plan de tratamiento.

## Banderas rojas

- CISO sin autoridad, recursos o reporte adecuado.
- Inventario de activos incompleto o desactualizado.
- MFA "implementado" pero con excepciones masivas.
- Cuentas privilegiadas compartidas o sin recertificación.
- Vulnerabilidades críticas abiertas más de lo que su SLA permite.
- Logs no retenidos o no centralizados.
- Plan de respuesta sin probar nunca en table-top.
- Backups en línea sin copia inmutable u offline.
- Concientización con tasas de clic en phishing simulado >20% sin mejora.
- Proveedores críticos sin SOC 2 / ISO 27001 ni cláusulas de seguridad en contrato.
- Configuraciones cloud expuestas (S3 públicos, security groups abiertos a 0.0.0.0/0).
- Servicios expuestos a Internet con autenticación débil o sin MFA.
- Después de un incidente, no se actualiza el plan ni se documentan lecciones.

## Buenas prácticas

- **Verificar evidencia técnica, no solo políticas**: una política sin configuración no protege.
- **Usar herramientas de validación independientes**: scans, herramientas de postura cloud (CSPM), CIS-CAT.
- **Mapear controles a MITRE ATT&CK**: esto da claridad sobre qué amenazas se cubren y cuáles no.
- **Integrar con `auditoria-tecnologia-informacion`**: los ITGCs son la base; ciberseguridad agrega capa adversaria.
- **No confundir certificaciones con seguridad**: ISO 27001 prueba que existe un sistema de gestión, no que sea efectivo.
- **Comunicar en lenguaje del riesgo**: la junta entiende impacto financiero, no CVSS.

## Conexión con otras SKILLs

- Se monta sobre `auditoria-tecnologia-informacion` y la complementa con foco adversarial.
- Coordina con `auditoria-cumplimiento` para regulación (NIS 2, GDPR, sectorial).
- Usa fuertemente `analitica-datos` para análisis de logs.
- Para investigaciones post-incidente, coordina con `auditoria-forense`.
- Aplica todas las SKILLs de proceso.

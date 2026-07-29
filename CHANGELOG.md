# Changelog

Todos los cambios relevantes de este proyecto se documentan aquí.

El formato sigue [Keep a Changelog](https://keepachangelog.com/es/1.0.0/) y el versionado sigue [Semantic Versioning](https://semver.org/lang/es/).

---

## [Unreleased]

---

## [2.2.3] — 2026-07-29

### Cambiado
- Revisión de vigencia normativa de los marcos citados en 8 SKILLs (v2.2.0/2.2.1 cubrió el ciclo anterior; este release cierra los gaps sustantivos surgidos desde entonces, con alcance acotado a contenido normativo nuevo o cambiado):
  - `auditoria-ciberseguridad`: **OWASP Top 10:2025** (publicado nov. 2025, reordena categorías e incorpora "Software Supply Chain Failures" y "Mishandling of Exceptional Conditions"); se agrega el **IIA Cybersecurity Topical Requirement** (obligatorio desde el 5-feb-2026).
  - `auditoria-inteligencia-artificial`: calendario del EU AI Act precisado — el Digital Omnibus (acuerdo del 7-may-2026) diferencia sistemas standalone de Alto Riesgo del Anexo III (2-dic-2027) de sistemas embebidos en producto (2-ago-2028); se agrega el **NIST AI RMF Generative AI Profile (NIST AI 600-1)**, ausente hasta ahora pese a ser el marco más relevante para auditorías de IA generativa.
  - `auditoria-esg-sostenibilidad`: confirmado que la Comisión Europea **adoptó el 3-jul-2026 el acto delegado final con los ESRS simplificados** (antes descrito como pendiente); se agregan las **enmiendas del ISSB a IFRS S2** sobre emisiones financiadas (vigentes desde periodos que inicien en 2027); nota del GHG Protocol actualizada con el Phase 1 Progress Update (31-mar-2026).
  - `auditoria-ambiental`: se agrega la misma nota de revisión en curso del **GHG Protocol**, ausente hasta ahora pese a que el estándar es un marco anclado del SKILL (inconsistencia con `auditoria-esg-sostenibilidad`).
  - `auditoria-tecnologia-informacion` y `analitica-datos`: **ITAF actualizado a su 5ª edición** (ISACA, feb. 2026), que reemplaza la de 2020.
  - `auditoria-gestion-desempeno`: **UK Corporate Governance Code** especificado a la edición 2024 (Provisión 29, declaración de efectividad de controles materiales, operativa desde 1-ene-2026); **GAO Yellow Book** especificado a la revisión 2024 (cambio de "quality control" a "quality management", vigente desde 15-dic-2025).
  - `auditoria-cumplimiento` y `auditoria-forense`: se agregan los **IIA Topical Requirements** de Terceros (vigente desde 15-sep-2026) y Anticorrupción (en consulta pública, aún no vigente); nota de **ISO 37301 en revisión** (ISO cerró revisión el 5-jun-2026); `auditoria-cumplimiento` alinea "PCI-DSS" a **PCI-DSS v4.0.1** por consistencia con `auditoria-ciberseguridad`.
- `catalog.json` actualizado a la versión **1.2.0**; corregida inconsistencia en `auditoria-gestion-desempeno` (el campo `frameworks` decía "ISO 37000" sin año, el cuerpo del SKILL ya decía "ISO 37000:2021").

### Seguridad
- Endurecimiento del repositorio y del pipeline (2026-07-06): rulesets de protección para `main` (PR obligatorio, sin force-push) y tags `v*` (inmutables); alertas y actualizaciones de seguridad de Dependabot habilitadas; `publish.yml` reducido a `contents: read` y `mcp-publisher` fijado a v1.7.9. Sin impacto en el paquete publicado.
- Documentación corregida: se elimina la instrucción `uvx auditoria-skills-mcp --version` del README (el entrypoint no soporta ese flag; queda en backlog implementarlo).

---

## [2.2.2] — 2026-07-06

### Corregido
- **El pipeline de publicación pisaba las SKILLs de este repo** con una copia clonada de `marcelinero/auditoria-skills` (desactualizado desde mayo 2026) justo antes del build. Por eso los paquetes 2.2.0 y 2.2.1 publicados en PyPI **no incluyen** las actualizaciones de marcos normativos anunciadas en este CHANGELOG (verificado descargando el wheel 2.2.1: `auditoria-cumplimiento` aún referencia ISO 37001 sin la revisión :2025). El paso de sincronización fue eliminado; a partir de ahora se publica exactamente lo commiteado aquí. Se requiere un release de contenido (2.2.2) para corregir lo publicado.

### Cambiado
- Este repositorio pasa a ser la **fuente canónica del catálogo de SKILLs** (antes documentada en `marcelinero/auditoria-skills`). README actualizado: badges, sección "SKILLs catalog" y enlace de licencia apuntan ahora a este repo.
- `Homepage` en `pyproject.toml` apunta a este repositorio.

### Agregado
- Archivo `LICENSE` con el texto oficial de CC BY-SA 4.0.

---

## [2.2.1] — 2026-07-01

### Corregido
- `auditoria-forense`: la referencia a **ISO 37001** en "Marco de referencia" no citaba la revisión vigente; actualizada a **ISO 37001:2025** para quedar consistente con `auditoria-cumplimiento`.

---

## [2.2.0] — 2026-07-01

### Cambiado
- Revisión general de marcos normativos anclados en los SKILLs para reflejar actualizaciones ocurridas desde su redacción original:
  - `auditoria-ciberseguridad`: CIS Controls v8 → **v8.1** (junio 2024); ISO/IEC 27001/27002 especificados como **:2022** (el periodo de transición de la versión 2013 venció en octubre de 2025); PCI-DSS actualizado a **v4.0.1**.
  - `auditoria-cumplimiento`: ISO 37001 actualizado a la revisión **:2025** (reemplaza 2016; nuevas subcláusulas de cambio climático y conflictos de interés; transición hasta feb. 2027).
  - `auditoria-esg-sostenibilidad`: nota sobre el estatus de **TCFD** (disuelto en 2023, incorporado en ISSB) y **SASB** (mantenido por el ISSB); añadida actualización sobre el **Paquete Ómnibus I** de la UE (Stop-the-Clock, alcance de CSRD/ESRS reducido a empresas >1.000 empleados y >€450M, normas ESRS revisadas esperadas a mediados de 2026 aplicables desde FY2027); nota sobre revisiones en curso del **GHG Protocol** (publicación no esperada antes de 2027).
  - `auditoria-inteligencia-artificial`: calendario de aplicación del **EU AI Act** actualizado, incluyendo el aplazamiento del plazo para sistemas de alto riesgo del Anexo III (agosto 2026 → diciembre 2027) bajo el "Digital Omnibus".
  - `auditoria-tecnologia-informacion`: referencias a GTAGs numerados (GTAG 1, 8, 14) reemplazadas por la serie temática vigente del IIA (2024-2025); ISO/IEC 27001/27002 especificados como **:2022**.
  - `auditoria-calidad`: nota sobre la revisión **ISO 9001:2026** (en etapa FDIS, publicación esperada septiembre 2026).
  - `catalog.json` actualizado a la versión 1.1.0 para reflejar los cambios anteriores en los metadatos de `frameworks`.

---

## [2.1.0] — 2026-05-31

### Cambiado
- Interfaz MCP (nombres de tools, descripciones, mensajes de error) migrada al inglés para compatibilidad con el MCP Registry oficial.
- README reescrito en formato bilingüe (español/inglés): quickstart, personalización y ciclo de vida de los SKILLs.
- Descripción en `server.json` acortada a ≤ 100 caracteres (límite del MCP Registry).

### CI/CD
- Pipeline de publicación usa GitHub OIDC — sin tokens almacenados.
- `uv publish` con flag `--skip-existing` para tolerar versiones duplicadas en PyPI.
- Paso de MCP Registry continúa aunque PyPI falle por versión ya publicada.

---

## [2.0.0] — 2026-05-01

### Añadido
- Primera publicación en PyPI como paquete instalable (`uvx auditoria-skills-mcp`).
- 20 SKILLs de auditoría interna en español, ancladas a marcos globales:
  - **8 SKILLs de proceso:** planeación, evaluación de controles, muestreo, papeles de trabajo, comunicación de hallazgos, seguimiento de recomendaciones, aseguramiento de calidad, analítica de datos.
  - **12 SKILLs de especialidad:** financiera, operativa, TI, forense, cumplimiento, ESG/sostenibilidad, ciberseguridad, inteligencia artificial, calidad, ambiental, gestión de desempeño, auditoría continua.
- Herramientas MCP: `list_skills`, `get_skill`, `search_skills`.
- `server.json` para registro en `registry.modelcontextprotocol.io`.
- CI/CD con workflows de validación y publicación automática en PyPI y MCP Registry.

---

## Tipos de cambio

| Tipo | Descripción |
|------|-------------|
| **Añadido** | Nueva funcionalidad o nuevos SKILLs |
| **Cambiado** | Cambios en funcionalidad existente o actualización de marcos |
| **Corregido** | Corrección de errores o inconsistencias |
| **Eliminado** | Funcionalidad o contenido removido |
| **CI/CD** | Cambios en pipelines de integración/despliegue |

[2.2.2]: https://github.com/marcelinero/auditoria-skills-mcp/compare/v2.2.1...v2.2.2
[2.2.1]: https://github.com/marcelinero/auditoria-skills-mcp/compare/v2.2.0...v2.2.1
[2.2.0]: https://github.com/marcelinero/auditoria-skills-mcp/compare/v2.1.0...v2.2.0
[2.1.0]: https://github.com/marcelinero/auditoria-skills-mcp/compare/v2.0.0...v2.1.0
[2.0.0]: https://github.com/marcelinero/auditoria-skills-mcp/releases/tag/v2.0.0

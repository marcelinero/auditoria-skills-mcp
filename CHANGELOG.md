# Changelog

Todos los cambios relevantes de este proyecto se documentan aquí.

El formato sigue [Keep a Changelog](https://keepachangelog.com/es/1.0.0/) y el versionado sigue [Semantic Versioning](https://semver.org/lang/es/).

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

[2.1.0]: https://github.com/marcelinero/auditoria-skills-mcp/compare/v2.0.0...v2.1.0
[2.0.0]: https://github.com/marcelinero/auditoria-skills-mcp/releases/tag/v2.0.0

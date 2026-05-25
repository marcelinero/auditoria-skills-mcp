# auditoria-skills-mcp

> mcp-name: io.github.marcelinero/auditoria-skills

Servidor [Model Context Protocol (MCP)](https://modelcontextprotocol.io) con **20 SKILLs de auditoría interna**, ancladas a normas globales (IIA, COSO, NIST, ISO, IFRS, COBIT, ACFE).

Instalable en un solo comando — sin clonar repositorios ni gestionar rutas.

[![PyPI](https://img.shields.io/pypi/v/auditoria-skills-mcp.svg)](https://pypi.org/project/auditoria-skills-mcp/)
[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg)](https://github.com/marcelinero/auditoria-skills/blob/main/LICENSE)
[![SKILLs](https://img.shields.io/badge/SKILLs-20-brightgreen.svg)](https://github.com/marcelinero/auditoria-skills)

---

## Instalación rápida

### Claude Desktop

Agregá esto a `claude_desktop_config.json`:

- **macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows:** `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "auditoria-skills": {
      "command": "uvx",
      "args": ["auditoria-skills-mcp"]
    }
  }
}
```

Reiniciá Claude Desktop. Sin clonar repos, sin rutas absolutas.

### Claude Code (CLI)

```bash
claude mcp add auditoria-skills -- uvx auditoria-skills-mcp
```

### Requisito: `uv`

```bash
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

---

## Herramientas disponibles

| Herramienta | Descripción |
| --- | --- |
| `listar_skills` | Lista las 20 SKILLs con tipo, categoría y marcos normativos |
| `obtener_skill` | Carga el contenido completo de una SKILL por nombre |
| `buscar_skills` | Filtra por tipo (`proceso`/`especialidad`) y/o marco (ISO, NIST, IIA…) |

---

## SKILLs incluidas

### Procesos transversales (8)

| SKILL | Estándares ancla |
| --- | --- |
| `planeacion-basada-riesgos` | IIA, COSO ERM, ISO 31000 |
| `evaluacion-controles` | COSO IC-IF, IIA, SOX 404 |
| `muestreo` | NIA/ISA 530, AICPA |
| `papeles-trabajo` | NIA/ISA 230, IIA |
| `comunicacion-hallazgos` | IIA Standards |
| `seguimiento-recomendaciones` | IIA Standards |
| `aseguramiento-calidad` | IIA, IIA QA Manual |
| `analitica-datos` | GTAG 16, ISACA |

### Especialidades (12)

| SKILL | Estándares ancla |
| --- | --- |
| `auditoria-financiera` | NIA/ISA, NIIF/IFRS, SOX, COSO IC-IF |
| `auditoria-operativa` | IIA, ISO 9001, INTOSAI |
| `auditoria-tecnologia-informacion` | COBIT 2019, ITAF, ISO 27001 |
| `auditoria-forense` | ACFE, NIA 240, FATF |
| `auditoria-cumplimiento` | ISO 37301, ISO 37001 |
| `auditoria-esg-sostenibilidad` | ISSB IFRS S1/S2, GRI, TCFD, SASB |
| `auditoria-ciberseguridad` | NIST CSF 2.0, ISO 27001/27002, CIS |
| `auditoria-inteligencia-artificial` | ISO/IEC 42001, NIST AI RMF, EU AI Act |
| `auditoria-calidad` | ISO 9001, ISO 19011 |
| `auditoria-ambiental` | ISO 14001, ISO 14064, GHG Protocol |
| `auditoria-gestion-desempeno` | IIA, INTOSAI ISSAI, COSO ERM |
| `auditoria-continua` | GTAG 3, AICPA, ISACA |

---

## Ejemplos de uso

```text
Cargá la SKILL auditoria-ciberseguridad y ayudame a planear
una auditoría basada en NIST CSF 2.0.
```

```text
¿Qué SKILLs del catálogo aplican a normas ISO?
```

```text
Voy a hacer una auditoría de cumplimiento de ISO 37301.
Cargá las SKILLs relevantes y construí el plan de engagement.
```

---

## Repositorio de contenido

Las SKILLs viven en el repositorio principal:
**[github.com/marcelinero/auditoria-skills](https://github.com/marcelinero/auditoria-skills)**

Contribuciones, nuevas SKILLs e issues → ese repositorio.

---

## Licencia

[CC BY-SA 4.0](https://github.com/marcelinero/auditoria-skills/blob/main/LICENSE)

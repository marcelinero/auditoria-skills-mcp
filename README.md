# auditoria-skills-mcp

> mcp-name: io.github.marcelinero/auditoria-skills

[Model Context Protocol (MCP)](https://modelcontextprotocol.io) server exposing **20 internal-audit SKILLs** grounded in globally accepted standards (IIA, COSO, NIST, ISO, IFRS, COBIT, ACFE). SKILLs are written in Spanish — the working language of the target audience.

Zero-install — one command, no repo cloning, no path configuration.

[![PyPI](https://img.shields.io/pypi/v/auditoria-skills-mcp.svg)](https://pypi.org/project/auditoria-skills-mcp/)
[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg)](https://github.com/marcelinero/auditoria-skills/blob/main/LICENSE)
[![SKILLs](https://img.shields.io/badge/SKILLs-20-brightgreen.svg)](https://github.com/marcelinero/auditoria-skills)

---

## Quickstart

### Claude Desktop

Add to `claude_desktop_config.json`:

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

Restart Claude Desktop. No repo cloning, no absolute paths.

### Claude Code (CLI)

```bash
claude mcp add auditoria-skills -- uvx auditoria-skills-mcp
```

### Prerequisite: `uv`

```bash
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

---

## Available tools

| Tool | Description |
| --- | --- |
| `list_skills` | List all 20 SKILLs with type, category, and anchor standards |
| `get_skill` | Load the full content of a SKILL by name |
| `search_skills` | Filter by type (`proceso`/`especialidad`) and/or framework (ISO, NIST, IIA…) |

---

## Included SKILLs

### Process SKILLs — cross-cutting (8)

| SKILL | Anchor standards |
| --- | --- |
| `planeacion-basada-riesgos` | IIA, COSO ERM, ISO 31000 |
| `evaluacion-controles` | COSO IC-IF, IIA, SOX 404 |
| `muestreo` | NIA/ISA 530, AICPA |
| `papeles-trabajo` | NIA/ISA 230, IIA |
| `comunicacion-hallazgos` | IIA Standards |
| `seguimiento-recomendaciones` | IIA Standards |
| `aseguramiento-calidad` | IIA, IIA QA Manual |
| `analitica-datos` | GTAG 16, ISACA |

### Specialty SKILLs — by domain (12)

| SKILL | Anchor standards |
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

## Usage examples

```text
Load the auditoria-ciberseguridad SKILL and help me plan
an audit based on NIST CSF 2.0.
```

```text
Which SKILLs in the catalog apply to ISO standards?
```

```text
I'm doing a compliance audit for ISO 37301.
Load the relevant SKILLs and build the engagement plan.
```

---

## Content repository

SKILLs live in the main repository:
**[github.com/marcelinero/auditoria-skills](https://github.com/marcelinero/auditoria-skills)**

Contributions, new SKILLs, and issues → that repository.

---

## Acerca de / About

> **Español:** Servidor MCP con 20 SKILLs de auditoría interna redactadas en español neutro, ancladas a normas globales (IIA, COSO, NIST, ISO, IFRS, COBIT, ACFE). Cubre procesos transversales (planeación, muestreo, papeles de trabajo) y especialidades (financiera, TI, forense, ESG, ciberseguridad, IA y más).

---

## License

[CC BY-SA 4.0](https://github.com/marcelinero/auditoria-skills/blob/main/LICENSE)

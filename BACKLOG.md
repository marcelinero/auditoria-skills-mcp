# Backlog — auditoria-skills-mcp

> Hoja de ruta del proyecto. Cada release cuenta una sola historia: las capacidades se liberan de forma paulatina para que el usuario las adopte a su conveniencia. Los items se mueven de sección a medida que se ejecutan.
>
> Última actualización: 2026-07-07.

---

## En curso — v2.3.0: Capa de agente (kit sin código)

Rama: `feat/agent-layer` · Plan detallado aprobado (sesión Claude Code 2026-07-06).

**Objetivo:** que un auditor use un "agente auditor" en sus auditorías locales con Claude Desktop o Claude Code, sin escribir código: el kit son un system prompt, un set de evals y una guía de instalación. El MCP existente provee la metodología (las 20 SKILLs).

| # | Item | Estado |
|---|------|--------|
| 0 | Actualizar `feat/agent-layer` desde `main` (v2.2.2) — fast-forward limpio | Pendiente |
| 1 | `agent/system-prompt.md` — identidad de auditor senior, límites no negociables (no firma, no acepta riesgos, escala fraude), uso de las 3 tools MCP, política de activación de skills, orquestación multi-skill (pipeline del engagement), estado del engagement, formato de papeles de trabajo, escalamiento y ambigüedad | Pendiente |
| 2 | `agent/evals.json` — 14 evals en 6 categorías (3 single-skill-clear, 3 multi-skill-composition, 2 escalation-required, 2 near-miss, 2 ambiguous-scope, 2 engagement-state) | Pendiente |
| 3 | `agent/claude-code/auditor-interno.md` — subagente listo para copiar a `.claude/agents/` (contenido duplicado del system prompt; fuente de verdad: `agent/system-prompt.md`) | Pendiente |
| 4 | `agent/README.md` — guía del kit: instalación en Claude Desktop (Proyecto + MCP) y Claude Code, cómo correr evals en simulación (PO-5), limitaciones y descargo | Pendiente |
| 5 | Docs: sección "Agent kit" en README raíz, CHANGELOG `[2.3.0]`, corregir comandos v2.2.0 residuales en PO-1 de CLAUDE.md | Pendiente |
| 6 | Verificación: JSON válido + 14 evals corridos en simulación sin caer en failure modes + smoke test con el MCP real | Pendiente |
| 7 | Release: bump 2.2.2 → 2.3.0 (pyproject + server.json ×2), PR a `main`, tag `v2.3.0` (publica automático), GitHub release | Pendiente |

---

## Pendiente de seguridad (requiere acción del owner)

- **Trusted Publishing en PyPI**: configurar en pypi.org (*Manage project → Publishing*) el publisher OIDC apuntando a `marcelinero/auditoria-skills-mcp` / `publish.yml`; después ajustar `uv publish` en el workflow y **eliminar el secret `PYPI_TOKEN`** (token de larga vida, último riesgo alto abierto de la auditoría de seguridad del 2026-07-06).

## Próximo — v2.4.0 (candidatos, sin comprometer)

- **CLI con Claude Agent SDK** (`auditoria-agent`): agente ejecutable desde terminal con el MCP conectado; memoria de engagement y papeles de trabajo persistidos en disco. Requiere API key de Anthropic del usuario. *(Decisión de v2.3.0: postergado para mantener el release enfocado.)*
- **Harness automatizado de evals**: script que corre `agent/evals.json` contra la API real y verifica skills activadas y outputs; reemplaza/complementa la simulación manual cuando el set crezca. *(Decisión de v2.3.0: postergado; la simulación manual basta para iterar el prompt.)*
- **Ampliar el set de evals** con base en lo aprendido usando el agente en auditorías reales (meta: ≥3 por categoría).

## Ideas / deuda técnica (sin versión asignada)

- **Alinear versiones internas divergentes**: el servidor MCP reporta la versión del `catalog.json` (1.1.0), `__init__.py` dice 2.1.0 y el paquete va en 2.2.2. Decidir una sola fuente (probablemente la de pyproject) y derivar las demás.
- **Índice propio del catálogo** (`auditoria_skills_mcp/data/skills/README.md`): opcional; hoy el índice vive en las tablas del README raíz y PO-3 ya apunta ahí.
- **Implementar flag `--version` en el entrypoint**: el server ignora argumentos; la instrucción se retiró del README (2026-07-07) hasta que exista el flag.
- **Excluir `CLAUDE.md`/`BACKLOG.md` del sdist** si se prefiere un tarball limpio (`[tool.hatch.build.targets.sdist] exclude`). Hoy viajan como bonus inofensivo.
- **v3.0.0 (visión)**: el agente pasa a ser la interfaz principal del producto (reservado en CLAUDE.md).

---

## Hecho

- **Endurecimiento de seguridad (2026-07-06/07)** — Rulesets `protect-main` (PR obligatorio, sin force-push) y `protect-release-tags` (tags `v*` inmutables); Dependabot alerts + security updates habilitados; `publish.yml` con `contents: read` y `mcp-publisher` fijado a v1.7.9; auditoría sin secretos en árbol ni historial.
- **v2.2.2 (2026-07-06)** — Consolidación: este repo es la fuente canónica del catálogo; eliminado el paso del pipeline que pisaba las SKILLs con el repo `auditoria-skills` (bug que hizo que 2.2.0/2.2.1 publicaran contenido viejo); LICENSE CC BY-SA 4.0 agregada; CLAUDE.md versionado; repo `auditoria-skills` deprecado y archivado en GitHub.
- **v2.2.0 / v2.2.1 (2026-07-01)** — Actualización de marcos normativos en las SKILLs (ISO 37001:2025, CIS v8.1, EU AI Act, ESRS post-Ómnibus, etc.). *Nota: llegaron a PyPI recién con 2.2.2 por el bug del pipeline.*
- **v2.1.0 (2026-05-31)** — Interfaz MCP en inglés, README bilingüe, publicación vía OIDC.

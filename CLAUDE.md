# CLAUDE.md — Instrucciones del proyecto para Claude Code

> Este archivo se carga automáticamente al inicio de cada sesión de Claude Code en este repo. Define el contexto del proyecto, las convenciones y los procedimientos operativos estándar.

---

## Contexto del proyecto

Este repositorio contiene un **MCP de auditoría interna** con un catálogo de **20 SKILLs** organizadas en dos dimensiones (procesos transversales + especialidades). Para v2.3.0 se planea incorporar una **capa de agente** que orqueste las SKILLs y el MCP para ejecutar trabajos de auditoría end-to-end (rama `feat/agent-layer`).

Está publicado en PyPI, instalable con `uvx` o `pip`, y registrado en el portal oficial de MCP de Anthropic.

**Este repo es la fuente canónica del catálogo de SKILLs** desde v2.2.2. El repo `marcelinero/auditoria-skills` (catálogo original) está deprecado; el pipeline de publicación ya NO sincroniza desde él — se publica exactamente lo commiteado aquí.

## Estructura del repo

```
├── auditoria_skills_mcp/     # Paquete Python publicado (servidor MCP)
│   ├── server.py             # Servidor MCP (tools: list/get/search skills)
│   └── data/
│       ├── catalog.json      # Metadatos de las 20 SKILLs
│       └── skills/           # 20 SKILL.md (8 procesos + 12 especialidades)
│           ├── procesos/
│           └── especialidades/
├── agent/                    # Capa de agente (PLANEADA, rama feat/agent-layer, rumbo a v2.3.0)
│   ├── system-prompt.md      # System prompt del agente auditor
│   ├── evals.json            # Set inicial de evals para iteración
│   └── README.md             # Guía de uso del kit
├── .github/workflows/        # CI: validate.yml (PRs) + publish.yml (tags v*)
├── server.json               # Manifiesto del MCP Registry (versión debe coincidir con pyproject)
├── pyproject.toml            # Empaquetado (hatchling); versión del paquete
├── CHANGELOG.md              # Registro de cambios por versión
├── BACKLOG.md                # Hoja de ruta: en curso, próximos releases, ideas, hecho
├── CONTRIBUTING.md           # Guía de contribución (niveles canónico/local/comunitario)
├── LICENSE                   # CC BY-SA 4.0
├── README.md                 # Documentación principal (se renderiza en PyPI)
└── CLAUDE.md                 # Este archivo
```

Al taggear `v*` el workflow `publish.yml` construye y publica automáticamente a PyPI y al MCP Registry. La versión vive en **tres lugares** que deben coincidir: `pyproject.toml` y `server.json` (campos `version` y `packages[0].version`).

## Al inicio de cada sesión

Lee estos archivos antes de actuar sobre el proyecto:

1. `README.md` — resumen actualizado del proyecto
2. `CHANGELOG.md` — últimos cambios
3. `BACKLOG.md` — qué está en curso y qué sigue
4. `agent/system-prompt.md` — comportamiento esperado del agente (cuando exista)
5. Estado de git: rama activa, working tree limpio o no, últimos commits

## Convenciones de versionado

- **SemVer estricto**: MAJOR.MINOR.PATCH
- **MAJOR**: cambios que rompen compatibilidad con versiones anteriores
- **MINOR**: features nuevas retrocompatibles
- **PATCH**: bugfixes retrocompatibles
- Estado actual: **v2.2.2**
- Próxima versión objetivo: **v2.3.0** (agrega capa de agente, no rompe nada de v2.2.x)
- Reservar **v3.0.0** para el momento en que el agente pase a ser la interfaz principal

Pre-releases usan sufijo tipo `-beta.1`, `-rc.1`.

## Convenciones de ramas

- `main` — siempre desplegable; protegida por ruleset (`protect-main`): el push directo y el force-push están bloqueados a nivel de GitHub, todo entra por PR. Los tags `v*` son inmutables (`protect-release-tags`).
- `feat/<nombre>` — nueva funcionalidad
- `fix/<nombre>` — bugfix
- `chore/<nombre>` — mantenimiento sin efecto funcional
- `docs/<nombre>` — solo documentación

Todo cambio material entra a `main` vía Pull Request.

## Convenciones de commits

Formato tipo Conventional Commits:

```
<tipo>(<scope opcional>): <descripción corta>

<cuerpo opcional>
```

Tipos: `feat`, `fix`, `docs`, `chore`, `refactor`, `test`, `perf`.

Ejemplo: `feat(agent): add system prompt and initial eval set`

## No negociables

- **Nunca pushees directamente a `main`.** Todo cambio pasa por rama + PR.
- **Nunca commitees secretos** (API keys, tokens, credenciales). Si detectas uno, detén el proceso y avisa.
- **Siempre actualiza `CHANGELOG.md`** cuando hagas un cambio material.
- **Siempre taggea después de merge a main** para releases.
- **Nunca modifiques archivos en `auditoria_skills_mcp/data/skills/` sin autorización explícita del usuario.** Las skills son la fuente de verdad metodológica y el usuario es su curador.
- **Antes de correr comandos destructivos** (`git reset --hard`, `git push --force`, `rm -rf`), confirma con el usuario.

---

## Procedimientos operativos estándar

### PO-1: Cortar el release v2.3.0 (capa de agente)

Objetivo: llevar el trabajo actual del agente a `main` y publicar v2.3.0.

Precondiciones:
- El trabajo del agente vive en rama `feat/agent-layer` (o similar)
- Los evals corren en verde
- `CHANGELOG.md` refleja los cambios

Pasos:

1. Verificar estado limpio en la rama de trabajo:
   ```bash
   git status
   ```
2. Confirmar con el usuario que el agente cumple criterios de release (evals, docs, README actualizado).
3. Actualizar `CHANGELOG.md` con sección `## [2.3.0] - YYYY-MM-DD` que describa: capa de agente añadida (system prompt, evals, README del kit), sin cambios rompedores en MCP ni skills.
4. Llevar la rama a `main` vía PR (el push directo está bloqueado por ruleset):
   ```bash
   gh pr create --base main --head feat/agent-layer --title "feat(agent): agent layer for v2.3.0"
   gh pr merge --merge
   ```
5. Taggear desde `main` actualizado:
   ```bash
   git checkout main && git pull origin main
   git tag -a v2.3.0 -m "v2.3.0 — Agent layer added (non-breaking)"
   git push origin v2.3.0
   ```
6. Crear release en GitHub apuntando al tag:
   ```bash
   gh release create v2.3.0 --title "v2.3.0 — Agent layer" --notes-from-tag
   ```
7. Reportar al usuario: link del release, resumen de lo publicado.

### PO-2: Crear nueva rama de feature

1. Verificar estado limpio en `main`.
2. Crear rama:
   ```bash
   git checkout main
   git pull origin main
   git checkout -b feat/<nombre>
   git push -u origin feat/<nombre>
   ```
3. Reportar al usuario que la rama existe local y remotamente.

### PO-3: Agregar una skill nueva

1. Confirmar con el usuario: nombre de la skill, categoría (proceso o especialidad).
2. Crear carpeta en `auditoria_skills_mcp/data/skills/<categoria>/<nombre>/`.
3. Crear `SKILL.md` con el frontmatter YAML estándar (`name`, `description`) y la estructura del catálogo (Propósito, Cuándo activar, Marco de referencia, Proceso, Outputs, Banderas rojas, Buenas prácticas, Conexión con otras SKILLs).
4. Registrar la skill en `auditoria_skills_mcp/data/catalog.json` (name, type, category/domain, path, frameworks) — el servidor solo sirve lo que está en el catálogo.
5. Actualizar las tablas de SKILLs del `README.md` raíz.
6. Actualizar `CLAUDE.md` si la nueva skill implica cambios en procedimientos.
7. Sugerir al usuario agregar al menos 2 evals nuevos en `agent/evals.json` que activen la nueva skill.

### PO-4: Agregar o modificar un eval

1. Leer `agent/evals.json`.
2. Confirmar con el usuario el prompt, la categoría (`single-skill-clear`, `multi-skill-composition`, `escalation-required`, `near-miss`, `ambiguous-scope`, `engagement-state`), skills esperadas, outputs esperados y failure modes.
3. Insertar el eval respetando la estructura JSON.
4. Validar que el JSON es válido:
   ```bash
   python -m json.tool agent/evals.json > /dev/null && echo "JSON válido"
   ```

### PO-5: Ejecutar un eval en modo simulación

1. Cargar mentalmente el system prompt (`agent/system-prompt.md`) y las skills relevantes.
2. Recibir el prompt del eval como si fuera del auditor humano.
3. Reportar al usuario:
   - Qué skills se habrían activado y por qué
   - Qué output se habría producido (esbozo)
   - Si se cumplen los `expected_outputs` del eval
   - Si se cae en algún `failure_mode`
4. Sugerir ajustes al system prompt o a las descriptions de las skills si el eval fallaría.

### PO-6: Bugfix en producción (hotfix)

Si el usuario reporta un bug en la versión publicada actual (ver "Estado actual" arriba):

1. `git checkout -b fix/<nombre> <tag de la versión publicada>`
2. Aplicar fix, commitear.
3. Tag: `v2.1.1` (o el siguiente patch disponible).
4. Merge back a `main` para no perder el fix.

---

## Lo que NO debes hacer sin permiso explícito

- Modificar archivos en `auditoria_skills_mcp/data/skills/` (el usuario es su curador).
- Publicar a PyPI (`twine upload`, `uv publish`, etc.).
- Hacer force push a cualquier rama.
- Cambiar la configuración del MCP publicado.
- Emitir tags fuera del esquema definido.
- Modificar `CLAUDE.md` sin proponerlo primero al usuario.

---

## Sobre el agente en sí

Cuando trabajes sobre `agent/`, ten presente que este agente es el que orquestará las 20 skills en tiempo de ejecución. Es distinto de ti (Claude Code trabajando sobre el repo). Tu trabajo aquí es de **infraestructura**: construir el system prompt, los evals, el harness, la integración con el MCP.

El agente en tiempo de ejecución tendrá su propio `system-prompt.md` que le da personalidad de auditor y define sus límites (no firmar informes, no aceptar riesgos por la organización, escalar fraude, etc.). Esos límites son del agente-auditor, no tuyos.

---

## Contacto y decisiones

- Owner del repo: administrador único (el usuario en esta sesión).
- Modelo de contribución: PRs bienvenidos para skills ligeras; cambios estructurales requieren issue previo.
- Idioma de trabajo: español para skills y docs; inglés para código y commit messages es aceptable.

---

*Última actualización de este archivo: 2026-07-07 — refresco general de documentación: rutas reales del repo, PO-1 apuntando a v2.3.0, protección de `main` y tags por rulesets, y BACKLOG.md incorporado al flujo de trabajo.*

"""
auditoria-skills-mcp
Servidor MCP con las 20 SKILLs de auditoría interna.
Uso: uvx auditoria-skills-mcp
"""

import asyncio
import json
from pathlib import Path

from mcp.server import NotificationOptions, Server
from mcp.server.models import InitializationOptions
from mcp.server.stdio import stdio_server
import mcp.types as types

# ── Paths ──────────────────────────────────────────────────────────────────────
DATA_DIR = Path(__file__).parent / "data"
CATALOG_PATH = DATA_DIR / "catalog.json"

try:
    with open(CATALOG_PATH, encoding="utf-8") as _f:
        CATALOG: dict = json.load(_f)
except FileNotFoundError:
    raise SystemExit(f"catalog.json no encontrado en {DATA_DIR}") from None
except json.JSONDecodeError as e:
    raise SystemExit(f"catalog.json tiene formato inválido: {e}") from None

SKILLS: list[dict] = CATALOG["skills"]

# ── Server ─────────────────────────────────────────────────────────────────────
server = Server("auditoria-skills")


@server.list_tools()
async def handle_list_tools() -> list[types.Tool]:
    return [
        types.Tool(
            name="listar_skills",
            description=(
                "Lista todas las SKILLs de auditoría disponibles con sus metadatos: "
                "nombre, tipo (proceso/especialidad), categoría o dominio, y marcos normativos ancla."
            ),
            inputSchema={"type": "object", "properties": {}, "required": []},
        ),
        types.Tool(
            name="obtener_skill",
            description=(
                "Obtiene el contenido completo de una SKILL de auditoría por su nombre exacto. "
                "Devuelve las instrucciones, el proceso paso a paso, los outputs esperados y las "
                "buenas prácticas definidas en esa SKILL."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "nombre": {
                        "type": "string",
                        "description": (
                            "Nombre exacto de la SKILL. Ejemplos: 'planeacion-basada-riesgos', "
                            "'auditoria-ciberseguridad', 'evaluacion-controles'. "
                            "Usar listar_skills para ver todos los nombres disponibles."
                        ),
                    }
                },
                "required": ["nombre"],
            },
        ),
        types.Tool(
            name="buscar_skills",
            description=(
                "Filtra el catálogo de SKILLs por tipo, categoría o marco normativo. "
                "Útil para encontrar qué SKILLs aplican a un dominio o norma específica."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "tipo": {
                        "type": "string",
                        "enum": ["proceso", "especialidad"],
                        "description": (
                            "'proceso' para SKILLs transversales (planeación, muestreo, papeles de trabajo…), "
                            "'especialidad' para SKILLs por dominio (financiera, TI, forense, ESG…)."
                        ),
                    },
                    "marco": {
                        "type": "string",
                        "description": (
                            "Texto a buscar dentro de los marcos normativos ancla. "
                            "Ejemplos: 'ISO', 'NIST', 'IIA', 'COSO', 'SOX', 'IFRS', 'COBIT', 'ACFE'."
                        ),
                    },
                },
                "required": [],
            },
        ),
    ]


@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict | None
) -> list[types.TextContent]:
    arguments = arguments or {}

    # ── listar_skills ──────────────────────────────────────────────────────────
    if name == "listar_skills":
        procesos = [s for s in SKILLS if s["type"] == "proceso"]
        especialidades = [s for s in SKILLS if s["type"] == "especialidad"]

        lines: list[str] = [
            f"# SKILLs disponibles — auditoria-skills v{CATALOG['version']}",
            f"Total: {len(SKILLS)} SKILLs ({len(procesos)} procesos · {len(especialidades)} especialidades)",
            "",
            "## SKILLs de proceso (transversales)",
        ]
        for s in procesos:
            cat = s.get("category", "—")
            fw = " · ".join(s.get("frameworks", []))
            lines.append(f"- **{s['name']}**  [categoría: {cat}]")
            lines.append(f"  Marcos: {fw}")

        lines += ["", "## SKILLs de especialidad"]
        for s in especialidades:
            domain = s.get("domain", "—")
            fw = " · ".join(s.get("frameworks", []))
            lines.append(f"- **{s['name']}**  [dominio: {domain}]")
            lines.append(f"  Marcos: {fw}")

        lines += [
            "",
            "---",
            "Usa `obtener_skill` con el nombre exacto para cargar el contenido completo de cualquier SKILL.",
            "Usa `buscar_skills` con filtros de tipo o marco para acotar la búsqueda.",
        ]
        return [types.TextContent(type="text", text="\n".join(lines))]

    # ── obtener_skill ──────────────────────────────────────────────────────────
    elif name == "obtener_skill":
        nombre = (arguments.get("nombre") or "").strip()
        skill = next((s for s in SKILLS if s["name"] == nombre), None)

        if not skill:
            available = "\n".join(f"  - {s['name']}" for s in SKILLS)
            return [
                types.TextContent(
                    type="text",
                    text=(
                        f"SKILL '{nombre}' no encontrada.\n\n"
                        f"Nombres válidos:\n{available}"
                    ),
                )
            ]

        skill_path = (DATA_DIR / skill["path"]).resolve()
        if not skill_path.is_relative_to(DATA_DIR.resolve()):
            return [
                types.TextContent(
                    type="text",
                    text="Ruta de SKILL fuera del paquete — entrada rechazada.",
                )
            ]
        if not skill_path.exists():
            return [
                types.TextContent(
                    type="text",
                    text=f"Archivo de SKILL no encontrado: {skill['path']}",
                )
            ]

        content = skill_path.read_text(encoding="utf-8")
        header = (
            f"<!-- SKILL: {skill['name']} | tipo: {skill['type']} | "
            f"marcos: {', '.join(skill.get('frameworks', []))} -->\n\n"
        )
        return [types.TextContent(type="text", text=header + content)]

    # ── buscar_skills ──────────────────────────────────────────────────────────
    elif name == "buscar_skills":
        tipo = arguments.get("tipo")
        marco = (arguments.get("marco") or "").strip().lower()

        results = SKILLS
        if tipo:
            results = [s for s in results if s["type"] == tipo]
        if marco:
            results = [
                s for s in results
                if any(marco in fw.lower() for fw in s.get("frameworks", []))
            ]

        if not results:
            return [
                types.TextContent(
                    type="text",
                    text="No se encontraron SKILLs con los filtros indicados. Intentá con `listar_skills` para ver todas.",
                )
            ]

        lines = [f"# Resultados — {len(results)} SKILL(s) encontrada(s)", ""]
        for s in results:
            cat = s.get("category") or s.get("domain", "—")
            fw = " · ".join(s.get("frameworks", []))
            lines.append(f"- **{s['name']}** [{s['type']} / {cat}]")
            lines.append(f"  Marcos: {fw}")

        lines += [
            "",
            "Usá `obtener_skill` con cualquiera de estos nombres para cargar su contenido completo.",
        ]
        return [types.TextContent(type="text", text="\n".join(lines))]

    else:
        return [
            types.TextContent(type="text", text=f"Herramienta desconocida: '{name}'.")
        ]


# ── Entry points ───────────────────────────────────────────────────────────────
async def main() -> None:
    async with stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            InitializationOptions(
                server_name="auditoria-skills",
                server_version=CATALOG.get("version", "2.0.0"),
                capabilities=server.get_capabilities(
                    notification_options=NotificationOptions(),
                    experimental_capabilities={},
                ),
            ),
        )


def main_sync() -> None:
    asyncio.run(main())


if __name__ == "__main__":
    main_sync()

"""
auditoria-skills-mcp
MCP server exposing 20 internal-audit SKILLs grounded in global standards.
Usage: uvx auditoria-skills-mcp
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
    raise SystemExit(f"catalog.json not found in {DATA_DIR}") from None
except json.JSONDecodeError as e:
    raise SystemExit(f"catalog.json has invalid format: {e}") from None

SKILLS: list[dict] = CATALOG["skills"]

# ── Server ─────────────────────────────────────────────────────────────────────
server = Server("auditoria-skills")


@server.list_tools()
async def handle_list_tools() -> list[types.Tool]:
    return [
        types.Tool(
            name="list_skills",
            description=(
                "List all available audit SKILLs with their metadata: "
                "name, type (process/specialty), category or domain, and anchor standards."
            ),
            inputSchema={"type": "object", "properties": {}, "required": []},
        ),
        types.Tool(
            name="get_skill",
            description=(
                "Get the full content of an audit SKILL by its exact name. "
                "Returns the instructions, step-by-step process, expected outputs, and "
                "best practices defined in that SKILL."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "description": (
                            "Exact SKILL name. Examples: 'planeacion-basada-riesgos', "
                            "'auditoria-ciberseguridad', 'evaluacion-controles'. "
                            "Use list_skills to see all available names."
                        ),
                    }
                },
                "required": ["name"],
            },
        ),
        types.Tool(
            name="search_skills",
            description=(
                "Filter the SKILL catalog by type, category, or regulatory framework. "
                "Useful for finding which SKILLs apply to a specific domain or standard."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "type": {
                        "type": "string",
                        "enum": ["proceso", "especialidad"],
                        "description": (
                            "'proceso' for cross-cutting SKILLs (planning, sampling, working papers…), "
                            "'especialidad' for domain SKILLs (financial, IT, forensic, ESG…)."
                        ),
                    },
                    "framework": {
                        "type": "string",
                        "description": (
                            "Text to search within anchor regulatory frameworks. "
                            "Examples: 'ISO', 'NIST', 'IIA', 'COSO', 'SOX', 'IFRS', 'COBIT', 'ACFE'."
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

    # ── list_skills ────────────────────────────────────────────────────────────
    if name == "list_skills":
        procesos = [s for s in SKILLS if s["type"] == "proceso"]
        especialidades = [s for s in SKILLS if s["type"] == "especialidad"]

        lines: list[str] = [
            f"# Available SKILLs — auditoria-skills v{CATALOG['version']}",
            f"Total: {len(SKILLS)} SKILLs ({len(procesos)} process · {len(especialidades)} specialty)",
            "",
            "## Process SKILLs (cross-cutting)",
        ]
        for s in procesos:
            cat = s.get("category", "—")
            fw = " · ".join(s.get("frameworks", []))
            lines.append(f"- **{s['name']}**  [category: {cat}]")
            lines.append(f"  Frameworks: {fw}")

        lines += ["", "## Specialty SKILLs"]
        for s in especialidades:
            domain = s.get("domain", "—")
            fw = " · ".join(s.get("frameworks", []))
            lines.append(f"- **{s['name']}**  [domain: {domain}]")
            lines.append(f"  Frameworks: {fw}")

        lines += [
            "",
            "---",
            "Use `get_skill` with the exact name to load the full content of any SKILL.",
            "Use `search_skills` with type or framework filters to narrow the search.",
        ]
        return [types.TextContent(type="text", text="\n".join(lines))]

    # ── get_skill ──────────────────────────────────────────────────────────────
    elif name == "get_skill":
        skill_name = (arguments.get("name") or "").strip()
        skill = next((s for s in SKILLS if s["name"] == skill_name), None)

        if not skill:
            available = "\n".join(f"  - {s['name']}" for s in SKILLS)
            return [
                types.TextContent(
                    type="text",
                    text=(
                        f"SKILL '{skill_name}' not found.\n\n"
                        f"Valid names:\n{available}"
                    ),
                )
            ]

        skill_path = (DATA_DIR / skill["path"]).resolve()
        if not skill_path.is_relative_to(DATA_DIR.resolve()):
            return [
                types.TextContent(
                    type="text",
                    text="SKILL path is outside the package — request rejected.",
                )
            ]
        if not skill_path.exists():
            return [
                types.TextContent(
                    type="text",
                    text=f"SKILL file not found: {skill['path']}",
                )
            ]

        content = skill_path.read_text(encoding="utf-8")
        header = (
            f"<!-- SKILL: {skill['name']} | type: {skill['type']} | "
            f"frameworks: {', '.join(skill.get('frameworks', []))} -->\n\n"
        )
        return [types.TextContent(type="text", text=header + content)]

    # ── search_skills ──────────────────────────────────────────────────────────
    elif name == "search_skills":
        skill_type = arguments.get("type")
        framework = (arguments.get("framework") or "").strip().lower()

        results = SKILLS
        if skill_type:
            results = [s for s in results if s["type"] == skill_type]
        if framework:
            results = [
                s for s in results
                if any(framework in fw.lower() for fw in s.get("frameworks", []))
            ]

        if not results:
            return [
                types.TextContent(
                    type="text",
                    text="No SKILLs found with the given filters. Try `list_skills` to see all available SKILLs.",
                )
            ]

        lines = [f"# Results — {len(results)} SKILL(s) found", ""]
        for s in results:
            cat = s.get("category") or s.get("domain", "—")
            fw = " · ".join(s.get("frameworks", []))
            lines.append(f"- **{s['name']}** [{s['type']} / {cat}]")
            lines.append(f"  Frameworks: {fw}")

        lines += [
            "",
            "Use `get_skill` with any of these names to load its full content.",
        ]
        return [types.TextContent(type="text", text="\n".join(lines))]

    else:
        return [
            types.TextContent(type="text", text=f"Unknown tool: '{name}'.")
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

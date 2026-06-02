# Contribuir a auditoria-skills-mcp

Bienvenido. Este documento explica cómo evolucionan los SKILLs en tres niveles: canónico, local y comunitario.

---

## Niveles de evolución

### 1️⃣ Versión canónica (oficial, centralizada)

Cuando un marco de referencia se revisa (COSO, NIST, IIA, ISO, etc.), el mantendedor actualiza el SKILL correspondiente y lo publica en PyPI. Esto garantiza:

- **Fidelidad al estándar**: cambios sincronizados con la versión oficial del marco.
- **Actualización centralizada**: todos los auditores reciben la versión mejorada automáticamente.
- **Trazabilidad**: queda registrado en qué versión y por qué cambió.

**Flujo:**
```
Revisión de COSO/NIST/ISO → Mantendedor ajusta SKILL → PR aprobado → Publicación PyPI
```

### 2️⃣ Adaptación local (descentralizado, sin tocar lo común)

Como los SKILLs son Markdown + YAML, cada auditor puede:

- **Clonar o hacer fork** del repositorio.
- **Ajustar los SKILLs** a su contexto local:
  - Matriz de controles interna.
  - Procedimientos específicos de la entidad.
  - Referencias locales (normativa local, políticas internas).
  - Casos de uso propios.
- **Ejecutar localmente** sin cambiar la versión comunitaria.

**No requiere PR ni aprobación.** Es tu copia, tu responsabilidad.

**Flujo:**
```
Fork repo → Clona localmente → Edita ./data/skills/xxx/SKILL.md → Ejecuta: uv run python -m auditoria_skills_mcp
```

### 3️⃣ Mejora compartida (comunidad, después de validar)

Si mejoras algo que es **genérico y reutilizable** (no específico de tu entidad), puedes proponer incorporarlo al estándar:

- **Abre un Pull Request** describiendo:
  - Qué mejoró y por qué.
  - Qué marco o estándar lo justifica.
  - Si es adaptable a otros contextos o solo a uno.
- **Revisión del mantendedor**:
  - ¿Es realmente genérico?
  - ¿Está alineado con los marcos de referencia?
  - ¿Mejora la calidad sin añadir complejidad innecesaria?
- **Si se aprueba**: se fusiona a `main`, se incrementa la versión y se publica en PyPI.

**Criterios de aceptación para una mejora comunitaria:**
- Mejora de **contenido** (claridad, completitud, precisión del marco).
- Fixes de **errores** (typos, inconsistencias, referencias rotas).
- Nuevos SKILLs alineados con estándares reconocidos.
- Mejoras de **formato** o **UX** que beneficien a todos.

**No aceptamos** cambios muy específicos de un contexto, opiniones sin respaldo normativo, o reordenamientos sin justificación.

---

## Cómo hacer un Pull Request

### Preparación

1. **Fork y clona:**
   ```bash
   git clone https://github.com/tu-usuario/auditoria-skills-mcp.git
   cd auditoria-skills-mcp
   git checkout -b feature/mejora-xxx
   ```

2. **Instala dependencias:**
   ```bash
   uv sync
   ```

3. **Edita el/los SKILL.md** en `./auditoria_skills_mcp/data/skills/`.

4. **Prueba localmente:**
   ```bash
   uv run python -m auditoria_skills_mcp
   ```

### Abre el PR

**Título:** Describe brevemente la mejora (ej: `Actualizar ISO 14001 en auditoria-ambiental`).

**Descripción:**
```markdown
## Descripción
Qué cambió y por qué.

## Justificación
Qué marco, estándar o best practice lo respalda.

## Impacto
¿Es un cambio local o genérico? ¿Beneficia a otros auditores?

## Checklist
- [ ] Cambios son genéricos, no locales.
- [ ] Referencia normativa citada correctamente.
- [ ] Probado localmente.
```

---

## Estructura del SKILL

Cada SKILL es un archivo `SKILL.md` con este patrón:

```yaml
---
name: auditoria-xxx
description: Una línea breve de cuándo activar.
---

# Título del SKILL

## Propósito
Qué evalúa y por qué importa.

## Cuándo activar esta SKILL
Triggers, palabras clave, contextos.

## Marco de referencia
Estándares aplicables con citas.

## Procedimiento
Pasos, entregables, best practices.
```

**Reglas:**
- **Frontmatter YAML**: `name`, `description`.
- **Markdown limpio**: encabezados H2/H3 clara jerarquía.
- **Referencias normativas**: citas completas (ISO xxxx:yyyy, etc.).
- **Ejemplos concretos**: casos de uso auditables.
- **Idioma**: español.

---

## Versionado

- **Version canónica** → `pyproject.toml` y `server.json`.
- **Changelog**: registra qué SKILL cambió en cada versión (si aplica).
- **Tags Git**: marcas por versión (v2.1.0, v2.2.0, etc.).

Cuando un PR se aprueba, la versión se incrementa antes de publicar en PyPI.

---

## Preguntas frecuentes

### ¿Puedo adaptar los SKILLs sin hacer PR?
**Sí.** Clona/fork, ajusta, ejecuta localmente. No hay restricción.

### ¿Cuándo debo hacer PR?
Cuando la mejora es **genérica y beneficia a otros auditores**, no solo a tu contexto.

### ¿Cómo sé si es genérico?
Si aplica a múltiples entidades, industrias o geographies. Si es específico de tu país, política interna o matriz local → mantén en tu fork.

### ¿Quién revisa los PRs?
El mantendedor (@marcelinero). Los criterios están arriba.

### ¿Qué pasa si mi PR se rechaza?
Nada malo. Puedes mantenerlo en tu fork adaptado, o ajustarlo y reenviarlo. Feedback constructivo.

---

## Código de conducta

- Sé respetuoso.
- Cita estándares, no opiniones.
- Asume buena intención.
- Enfócate en mejorar la auditoría interna.

---

**Gracias por contribuir.** Los 20 SKILLs mejoran porque auditores como tú los usan, adaptan y perfeccionan.

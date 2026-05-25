---
name: papeles-trabajo
description: Documentar la evidencia y las conclusiones del trabajo de auditoría de manera que un revisor experimentado pueda reconstruir el trabajo realizado y llegar a las mismas conclusiones. Activar siempre que se hable de papeles de trabajo, working papers, documentación de auditoría, archivo de auditoría, evidencia documental, índice de papeles, referenciación cruzada, soporte de hallazgo, traza de auditoría, custody, custodia de evidencia, NIA 230, ISA 230, o cuando se documente cualquier procedimiento ejecutado.
---

# Papeles de trabajo y documentación de auditoría

## Propósito

Un papel de trabajo es el registro escrito que evidencia: qué se hizo, cuándo, quién, con qué evidencia, qué se concluyó. Es la columna vertebral de la calidad de la auditoría: si no está documentado, no se hizo.

Esta SKILL guía al agente para producir papeles de trabajo que cumplan el criterio fundamental: **un auditor experimentado y ajeno al engagement debe poder, leyendo solo los papeles, reconstruir el trabajo y llegar a la misma conclusión**.

## Cuándo activar esta SKILL

- De forma transversal y continua durante todo el engagement.
- Cada vez que se ejecute un procedimiento, se obtenga evidencia o se concluya algo.
- Al cerrar el archivo del engagement.
- Cuando un revisor pide "el papel de trabajo de…".

## Marco de referencia

- **NIA 230 / ISA 230** — Documentación de auditoría.
- **PCAOB AS 1215** — Audit Documentation.
- **Normas Globales de Auditoría Interna (IIA, 2025)** — Estándar 14.6 "Documentación del engagement".
- **Política institucional de retención** de la organización.

## Atributos de un buen papel de trabajo

Cada papel de trabajo debe contener al menos:

| Elemento | Descripción |
|---|---|
| Encabezado | Cliente / entidad, engagement, año, periodo cubierto |
| Título | Qué procedimiento documenta (ej. "Prueba de operación – control de aprobación de pagos") |
| Objetivo | Qué se quiere probar y por qué |
| Procedimiento | Qué se hizo paso a paso |
| Población y muestra | Cómo se seleccionaron los ítems |
| Evidencia | Documentos, capturas, archivos, referencias |
| Resultados | Hallazgos elemento por elemento |
| Conclusión | Si el objetivo se cumple |
| Excepciones / observaciones | Limitaciones, ajustes, supuestos |
| Preparado por / fecha | Quién y cuándo |
| Revisado por / fecha | Revisor y cuándo |
| Referenciación cruzada | Conexión con otros papeles (índice) |

## Estructura del archivo

### Archivo permanente (Permanent file)

Información que se mantiene de un periodo a otro y se actualiza cuando cambia:
- Acuerdos contractuales y societarios.
- Estructura organizacional, organigramas.
- Políticas y procedimientos clave.
- Historial de auditorías previas.
- Mapas de procesos.
- Listado de sistemas críticos.

### Archivo corriente (Current file)

Información específica del periodo auditado:
- Memorando de planeación.
- Programa de trabajo.
- Matriz de riesgos y controles.
- Pruebas de diseño y operación.
- Pruebas sustantivas.
- Resúmenes de entrevistas.
- Borradores y versión final del informe.
- Comunicaciones con la administración.
- Hallazgos y planes de acción.

### Indexación

Usar un sistema de referencias estable (ej. letras por área + números por subnivel). Cada papel debe tener un código único y referenciar los papeles relacionados.

Ejemplo de esquema:

```
A   – Planeación y administración
B   – Control interno general
C   – Pruebas de procesos
   C-1   Compras
      C-1.1   RCM compras
      C-1.2   Walkthrough compras
      C-1.3   Pruebas de operación compras
D   – Pruebas sustantivas
E   – Hallazgos
F   – Informe final
G   – Comunicaciones
```

## Reglas de oro

### 1. Nada de "se revisó"

"Se revisaron las facturas y todo está bien" no es papel de trabajo. Debe especificar: qué facturas, contra qué, qué se verificó, qué se concluyó por cada una.

### 2. Cada conclusión debe tener evidencia adjunta o referenciada

No basta con afirmar; debe mostrarse. Adjuntar copia de la evidencia (PDF, captura, exportación) o referenciarla con ubicación verificable.

### 3. Trazabilidad bidireccional

Cualquier número en el informe debe poder rastrearse hasta el papel de trabajo que lo soporta, y al revés, todo papel de trabajo debe conectarse con el objetivo del engagement.

### 4. Evidencia electrónica con integridad

Si la evidencia es un archivo, registrar:
- Nombre del archivo.
- Fecha y hora de obtención.
- Origen (sistema, persona que entregó).
- Hash (SHA-256 recomendado) si la integridad es crítica.
- Para auditoría forense, ver SKILL `auditoria-forense` para custodia formal.

### 5. Diferenciar hechos de opiniones

Los hechos se documentan; las opiniones del auditor se identifican como tales ("a juicio del equipo…").

### 6. Tiempos y oportunidad

NIA 230 exige que la documentación final se complete dentro de un plazo razonable después de la fecha del informe (típicamente 60 días). Cualquier ajuste posterior debe quedar etiquetado y firmado por separado.

### 7. Confidencialidad

Los papeles de trabajo son confidenciales y propiedad del auditor (o de la función). No se entregan al auditado salvo procedimiento formal.

## Estándares de redacción

- **Lenguaje claro, objetivo y específico**. Nada de adjetivos calificativos sin sustento ("excelente", "muy malo").
- **Verbos en pasado** para procedimientos ejecutados ("se inspeccionó", "se recalculó").
- **Cifras con decimales y unidades coherentes**.
- **Fuentes y períodos explícitos** en cada cifra.
- **Anglicismos solo cuando son término técnico aceptado** (walkthrough, sampling, etc.).

## Plantilla mínima de papel de trabajo

```
Engagement: [Nombre]                       Ref: [Código del papel]
Periodo: [Fechas]                          Fecha preparación: [aaaa-mm-dd]
Preparado por: [Nombre / rol]              Revisado por: [Nombre / rol]
Fecha revisión: [aaaa-mm-dd]

OBJETIVO
[Qué se busca probar]

PROCEDIMIENTO EJECUTADO
[Pasos detallados]

POBLACIÓN Y MUESTRA
[Origen, total, tamaño muestra, método selección, ref. SKILL muestreo]

RESULTADOS
[Tabla o detalle por ítem]

EXCEPCIONES / OBSERVACIONES
[Limitaciones, ajustes, supuestos]

CONCLUSIÓN
[Si el objetivo se cumple, qué riesgo queda, recomendación si aplica]

REFERENCIAS CRUZADAS
[Otros papeles relacionados]

ANEXOS
[Listado de evidencia adjunta]
```

## Banderas rojas

- Papel sin revisor o con revisor que no firmó.
- Conclusiones que no se desprenden de la evidencia documentada.
- Evidencia mencionada pero no adjunta ni referenciada.
- Cifras inconsistentes entre papeles que deberían cuadrar.
- Anotaciones a mano sobre papeles ya finalizados.
- Cambios al archivo después del cierre formal sin etiquetado.
- "Confiamos en la administración" como sustento de una conclusión.
- Papeles muy genéricos que podrían pegarse en cualquier engagement.

## Buenas prácticas para entornos digitales

- Usar una herramienta de auditoría (TeamMate+, AuditBoard, Pentana, Workiva, MS SharePoint configurado, etc.) que dé control de versiones, firma electrónica e indexación automática.
- Mantener nomenclatura de archivos consistente: `[ref]_[titulo]_v[n].xlsx`.
- Para papeles producidos por scripts (Python, R, SQL), guardar el script junto con el output y registrar parámetros y semillas.
- Para extractos de bases de datos, documentar la consulta exacta y la conexión utilizada.
- Bloquear edición del archivo final una vez aprobado.

## Conexión con otras SKILLs

- Recibe información de **todas** las demás SKILLs de proceso y especialidad.
- Es la fuente principal del archivo que `aseguramiento-calidad` revisa.
- Sustenta los hallazgos que `comunicacion-hallazgos` formaliza.
- Las pistas y muestras de `analitica-datos` deben quedar guardadas como papeles con su query, parámetros y output.

---
name: auditoria-forense
description: Investigar fraude, conducta indebida y conducta ilícita aplicando técnicas forenses, preservando cadena de custodia y produciendo evidencia útil para procesos disciplinarios o legales. Activar siempre que se hable de auditoría forense, fraude, fraud examination, investigación interna, integrity investigation, conflicto de interés, soborno, corrupción, lavado de activos, denuncia, whistleblower, hotline, ACFE, CFE, NIA 240, GAFI, FATF, due diligence de integridad, evidencia digital, peritaje, cadena de custodia.
---

# Auditoría forense

## Propósito

La auditoría forense investiga indicios de fraude, corrupción, conflicto de interés, lavado de activos y otras conductas ilícitas o impropias, con un estándar de evidencia más alto que la auditoría regular y con foco en **utilidad legal** de los hallazgos. Sus productos pueden alimentar decisiones disciplinarias, demandas civiles o procesos penales.

Esta SKILL guía la conducción de investigaciones forenses preservando la cadena de custodia, la confidencialidad y los derechos de los involucrados.

## Cuándo activar esta SKILL

- Cuando hay denuncia interna o externa (línea ética, whistleblower).
- Cuando emergen indicios de fraude durante una auditoría regular.
- Cuando la administración o el Comité solicitan investigar una situación.
- Para due diligence de integridad sobre terceros (M&A, vendor due diligence).
- En cumplimiento antisoborno (ISO 37001) y antilavado.

## Marco de referencia

- **ACFE — Association of Certified Fraud Examiners**:
  - Fraud Examiners Manual.
  - Code of Professional Standards.
  - Report to the Nations (datos globales sobre fraude).
- **NIA 240** — Responsabilidades del auditor en relación con el fraude.
- **GAFI / FATF** — Recomendaciones contra lavado de activos y financiación del terrorismo.
- **ISO 37001:2025** — Sistemas de gestión antisoborno.
- **ISO 37301** — Sistemas de gestión de cumplimiento.
- **OCDE Convención Anticohecho** y guías relacionadas.
- **FCPA (EE. UU.) y UK Bribery Act** — leyes antisoborno con alcance extraterritorial.
- **Wolfsberg Principles** (sector financiero).
- **ISO/IEC 27037** — manejo de evidencia digital.

## Conceptos fundamentales

### Triángulo del fraude (Cressey)

Tres elementos que típicamente coexisten:
1. **Presión / incentivo**: deudas, expectativas, metas, vicios.
2. **Oportunidad**: debilidad de control que permite el acto.
3. **Racionalización**: justificación interna ("me lo merezco", "lo voy a devolver").

### Diamante del fraude (Wolfe & Hermanson)

Suma una cuarta arista:
4. **Capacidad / capability**: la habilidad para ejecutarlo.

### Tipologías ACFE

Tres grandes categorías:
- **Apropiación indebida de activos** (asset misappropriation): efectivo, inventario, datos.
- **Corrupción**: soborno, conflicto de interés, gratificaciones, extorsión económica.
- **Estados financieros fraudulentos**: manipulación de ingresos, pasivos, gastos, revelaciones.

### Estándar de prueba

A diferencia de la auditoría regular (razonabilidad), la forense tiende al estándar de la prueba más exigente del foro al que pueda llegar el caso:
- **Procedimientos disciplinarios internos**: estándar interno (típicamente "preponderancia de la evidencia").
- **Procedimientos civiles**: preponderancia.
- **Procedimientos penales**: "más allá de duda razonable" (la auditoría apoya a la fiscalía pero no concluye penalmente).

## Principios rectores

### 1. Confidencialidad estricta
Información de la investigación se comparte solo con el círculo autorizado (sponsor, asesor legal, equipo). Filtraciones pueden invalidar la investigación.

### 2. Imparcialidad
El investigador no es juez ni parte. Investiga hechos, no busca confirmar hipótesis. Documenta tanto evidencia que apoya como evidencia que refuta la hipótesis.

### 3. Cadena de custodia
Toda evidencia recolectada debe tener trazabilidad ininterrumpida: quién la recolectó, cuándo, dónde, cómo se almacenó, quién accedió. Una ruptura puede hacer la evidencia inadmisible.

### 4. Privilegio legal
Cuando aplica (sobre todo en jurisdicciones con privilegio abogado-cliente), conducir la investigación bajo dirección legal puede proteger los productos del trabajo. Coordinar con asesoría jurídica desde el inicio.

### 5. Derechos de los involucrados
Respetar derechos a no autoincriminarse, a representación, a la dignidad. La organización no es autoridad penal.

### 6. Privacidad y protección de datos
Las medidas de investigación deben ser proporcionales y conforme a normativa de privacidad (GDPR, leyes locales). Documentar el sustento legal de las medidas.

## Proceso

### Fase 1 — Recepción y triage

1. Recepción del reporte (línea ética, hallazgo de auditoría, denuncia formal).
2. Triage inicial: ¿hay indicios suficientes para investigación formal? ¿Es un asunto disciplinario menor o investigación seria?
3. Definir patrocinador (sponsor) — típicamente Comité de Auditoría, Ética o Junta Directiva en asuntos sensibles.
4. Conformar equipo (auditores forenses, abogados, especialistas TI, RR. HH. cuando aplique).
5. Definir alcance preliminar y plan de investigación.
6. Acordar protocolos: comunicaciones, custodia, escalamiento.

### Fase 2 — Aseguramiento de evidencia

Antes que las personas se enteren de la investigación:

- **Hold legal / preservación de información**: bloquear destrucción de correos, documentos, sistemas.
- **Imágenes forenses** de dispositivos relevantes (cuando jurídicamente procede): laptops, móviles, servidores. Usar herramientas con verificación de hash (EnCase, FTK, X-Ways).
- **Preservación de logs** (correo, SIEM, CCTV, accesos físicos, red).
- **Aseguramiento de documentos físicos**.

Cada pieza se cataloga: identificador único, fuente, fecha/hora, hash si aplica, custodio.

### Fase 3 — Investigación documental y digital

- Análisis de correo electrónico y mensajería (con proporcionalidad y base legal).
- Análisis de sistemas transaccionales: ver SKILL `analitica-datos` para pruebas como Benford, duplicados, partes relacionadas, transacciones bajo umbral, asientos manuales.
- Análisis de cuentas bancarias y movimientos (cuando hay autorización).
- Análisis de relaciones (sociales, societarias, contractuales) — fuentes públicas, registros mercantiles, listas de sanciones (OFAC, ONU, UE), bases de PEPs.
- Análisis de patrones temporales (transacciones a horas o fechas anómalas).

### Fase 4 — Entrevistas

Las entrevistas son herramienta central. Tipos:

- **Informativas**: a personas con conocimiento del proceso o contexto.
- **De corroboración**: para confirmar evidencia ya identificada.
- **Admisión** (de los presuntos involucrados): se realizan al final, con la mayor evidencia posible ya en mano.

Preparación:
- Plan de entrevista por entrevistado.
- Línea de preguntas (de las generales a las específicas).
- Documentos a presentar (mostrar, no entregar).
- Acta detallada o grabación con consentimiento documentado.

Durante:
- Tono profesional, no acusatorio.
- Preguntas abiertas primero, cerradas después.
- Permitir silencios.
- Observar lenguaje no verbal sin sobreinterpretar.
- Documentar afirmaciones, evasivas, contradicciones.
- Cierre: ¿quiere agregar algo? ¿hay alguien más que deba entrevistarse?

Después:
- Acta firmada idealmente por el entrevistado (si rehúsa, dejar constancia).
- Identificar nuevas líneas de investigación.

### Fase 5 — Análisis y conclusiones

1. Reconstrucción de los hechos con línea de tiempo.
2. Identificación de personas involucradas con evidencia específica para cada una.
3. Cuantificación del impacto (financiero, operativo, reputacional).
4. Identificación de fallas de control que permitieron el acto.
5. Tipificación: qué política/norma/ley se infringió.
6. Conclusiones — solo lo que la evidencia sustenta.

### Fase 6 — Informe forense

Más riguroso que un informe de auditoría regular. Estructura:

```
1. Resumen ejecutivo
2. Antecedentes y origen del caso
3. Alcance y limitaciones
4. Metodología empleada
5. Reconstrucción de los hechos (línea de tiempo)
6. Evidencia documentada (listada y referenciada)
7. Cuantificación del impacto
8. Análisis del control interno y fallas que permitieron los hechos
9. Conclusiones por persona/entidad y por hecho
10. Recomendaciones (control, disciplinarias, legales — sin invadir competencia)
11. Anexos (catálogo de evidencia con cadena de custodia)
```

El informe debe escribirse asumiendo que será leído por abogados, jueces o reguladores.

### Fase 7 — Acciones derivadas

El sponsor (no el investigador) decide:
- Acciones disciplinarias.
- Acciones civiles para recuperación.
- Reporte a autoridades (cuando hay obligación legal o decisión).
- Reportes a reguladores (UAF/FIU, supervisores).
- Comunicación interna y externa (manejo reputacional).

El investigador apoya con evidencia y contexto, pero no decide.

### Fase 8 — Lecciones aprendidas y mejoras de control

Toda investigación debe terminar con un análisis de causa raíz a nivel de control:
- ¿Qué controles fallaron?
- ¿Qué señales se ignoraron?
- ¿Qué cambios estructurales evitarían recurrencia?

## Investigación sobre terceros (vendor due diligence de integridad)

Para terceros críticos (proveedores, distribuidores, agentes, socios M&A):
- Validar identidad y existencia legal.
- Beneficiarios reales (UBO).
- Cruce con listas de sanciones, PEPs, adverse media.
- Análisis de antecedentes judiciales y reguladores.
- Conflictos de interés con empleados.
- Reputación en su mercado.
- Capacidad operativa real.

Documentar el riesgo y la decisión final.

## Banderas rojas comunes

### En personas
- Cambios de estilo de vida no explicados por ingresos.
- Resistencia a tomar vacaciones o rotar funciones.
- Control desproporcionado sobre un proceso (única persona que sabe).
- Ostentación o, por el contrario, problemas financieros conocidos.
- Vínculos no declarados con proveedores o clientes.
- Acceso a sistemas o documentos fuera de su rol.

### En transacciones
- Patrones consistentemente bajo umbrales de aprobación.
- Mismos actores en aprobaciones y revisiones.
- Documentación incompleta o repetitiva.
- Cancelaciones y notas crédito frecuentes.
- Pagos a entidades en jurisdicciones de alto riesgo.
- Variaciones inusuales en cuentas que cierran el periodo.

### En sistemas
- Logs alterados o desactivados.
- Accesos privilegiados usados a horas inusuales.
- Cambios de datos maestros antes de transacciones grandes.
- Conexiones desde geografías no esperadas.

## Banderas rojas en la conducción de la investigación

- Investigadores presionados a "concluir rápido" antes de evidencia suficiente.
- Acceso a información restringido por las personas que aparentemente serían el objeto.
- Cambio de sponsor en medio de la investigación.
- Filtraciones a la prensa o redes durante la investigación.
- Destrucción de evidencia durante la investigación.

## Conexión con otras SKILLs

- Usa intensamente `analitica-datos` para detectar patrones.
- Las pruebas se documentan vía `papeles-trabajo` con custodia reforzada.
- Coordinar con `auditoria-cumplimiento` (lavado, antisoborno, conflictos de interés).
- Coordinar con `auditoria-tecnologia-informacion` para preservar evidencia digital.
- El informe forense se rige por estándares más exigentes que `comunicacion-hallazgos` regular.

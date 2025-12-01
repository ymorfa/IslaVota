# Guía de Contribución

Gracias por tu interés en contribuir a este proyecto.
Nuestro objetivo es crear una plataforma segura, transparente y confiable; por ello seguimos un flujo de trabajo estricto y auditable. Cualquier aporte es bienvenido siempre que respete estas pautas.

---

## 📌 Principios Generales

* Toda contribución pasa por **Pull Request (PR)**.
* No se permiten **commits directos** a `main`.
* Toda discusión técnica queda registrada en **issues** o PRs.
* Priorizamos cambios pequeños, revisables y con propósito claro.
* Código seguro, documentado y probado.

---

## 🛠️ Flujo de Contribución

1. **Fork** del repositorio.

2. Crear una rama descriptiva a partir de `main`:

   ```bash
   git checkout -b feature/nombre-claramente-descriptivo
   ```

3. Realizar cambios y asegurarse de que:

   * El código compila.
   * Se ejecutan los tests.
   * Se cumplen los linters/formatters.

4. Crear un **Pull Request** hacia `main`.

5. Responder comentarios de revisión.

6. El PR será fusionado cuando:

   * Al menos un revisor lo apruebe.
   * Todos los checks pasen.
   * No existan conflictos.

---

## ✨ Estándares de Código

* Mantén el código **simple, claro y legible**.
* Sigue las convenciones del proyecto:

  * Python → PEP8, nombres descriptivos, typing cuando sea posible.
  * HTML/CSS/JS → semántico, limpio, evitando duplicaciones.
* Todas las funciones y módulos nuevos deben incluir:

  * Docstring breve.
  * Explicación de parámetros y valor de retorno.
* Evitar dependencias innecesarias.
* Antes de enviar un PR, pasa los linters correspondientes:

  ```bash
  black .
  flake8 .
  ```

---

## 🧪 Tests

Las contribuciones deben incluir pruebas cuando aplique:

* Nuevas funcionalidades → tests nuevos.
* Corrección de bugs → test que reproduzca el bug + fix.
* Mantenemos una suite de pruebas que debe correr correctamente antes del PR.

Ejecuta:

```bash
pytest
```

---

## 📄 Estilo de Commits

Usamos un estilo semántico y claro:

```
feat: agrega validación de identidad
fix: corrige error en login
docs: actualiza readme
chore: tareas menores o mantenimiento
refactor: reestructura código sin cambiar funcionalidad
test: añade o actualiza pruebas
```

Recomendado (opcional): **commits firmados (GPG)** para mayor trazabilidad.

---

## 🧵 Pull Requests

Tu PR debe incluir:

* **Descripción clara** del cambio.
* **Motivación**: qué problema resuelve o qué funcionalidad añade.
* Si aplica, capturas o ejemplos de antes vs después.
* Checklist breve:

  ```text
  - [ ] El código compila
  - [ ] Tests ejecutan correctamente
  - [ ] No rompo funcionalidad existente
  - [ ] Documenté los cambios necesarios
  ```

Los PRs grandes deben dividirse en PRs pequeños si es posible.

---

## 🐞 Reporte de Errores (Issues)

Para reportar bugs, usa este formato:

1. Título claro.
2. Pasos para reproducir.
3. Comportamiento esperado.
4. Logs o screenshots cuando sea posible.
5. Entorno (OS, versión de Python, navegador, etc.).

---

## 🔐 Seguridad

Si encuentras una vulnerabilidad:

* **No abras un issue público.**
* Envíala por correo a: **islavota@gmail.com**
* La revisaremos y responderemos con prioridad.

---

## 📦 Dependencias

* Evita agregar dependencias sin justificación.
* Si propones una nueva dependencia debes explicar:

  * por qué es necesaria,
  * alternativas evaluadas,
  * impacto en seguridad y tamaño del proyecto.

---

## 🤝 Código de Conducta

Este proyecto sigue el **Código de Conducta del Contribuyente** incluido en `CODE_OF_CONDUCT.md`.
Participar implica aceptar y respetar sus reglas.

---

## 🙏 Gracias

Apreciamos el tiempo y el esfuerzo de cada contribución.
Tu ayuda hace que este proyecto sea más sólido, accesible y confiable para todos.

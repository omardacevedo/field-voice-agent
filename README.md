# field-voice-agent

# Proyecto Integrador: Agente de Voz Conversacional (Backend)

## 1. Descripción del Proyecto
Este proyecto consiste en el desarrollo de un agente de voz conversacional en Python. El sistema está diseñado con una arquitectura orientada a servicios para manejar flujos de voz en tiempo real, integrando las siguientes etapas: Captura (Micrófono) → Transcripción (Speech-to-Text) → Procesamiento (LLM) → Síntesis (Text-to-Speech).

## 2. Client Brief
**Objetivo:** Construir un agente de voz conversacional mínimo en Python puro utilizando `asyncio` para comprender la arquitectura de sistemas de agentes en tiempo real (tipo Pipecat/LiveKit).
**Requerimientos:**
* Implementar un loop asíncrono para el manejo de audio y texto.
* Garantizar una baja latencia en la cadena de procesamiento.
* Mantener una estructura modular que permita intercambiar proveedores de STT/LLM/TTS.

## 3. Workflow con Claude Code
El desarrollo sigue un flujo de trabajo profesional de **Agente AFK (Away From Keyboard)**:
1. **Definición de Tareas:** Creación de Issues en GitHub con criterios de aceptación claros.
2. **Desarrollo Iterativo:** Generación de código modular mediante Claude Code para implementar funcionalidades atómicas.
3. **Validación:** Ejecución de pruebas locales, validación de endpoints mediante Swagger UI y commits atómicos vinculados a Issues.
4. **Sincronización:** Gestión de repositorio remoto mediante Git con historial trazable.

## 4. Tecnologías Utilizadas
* **Lenguaje:** Python 3.12
* **Concurrencia:** `asyncio`
* **Framework API:** Django Ninja (para la capa de control)
* **Validación:** Pydantic v2
* **Seguridad:** JWT (Bearer Tokens)

## 5. Componentes del Proyecto
* **Backend:** Arquitectura modular basada en apps de Django.
* **Frontend:** Documentación interactiva mediante **Swagger UI** (disponible en `/api/v1/docs`) y panel de administración para gestión de estados del sistema.

## 6. Configuración Inicial
1. Clonar el repositorio.
2. Crear entorno virtual: `python -m venv venv`
3. Instalar dependencias: `pip install -r requirements/base.txt`
4. Ejecutar servidor: `python manage.py runserver`

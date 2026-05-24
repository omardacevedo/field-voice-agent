# Reporte de Control Arquitectónico (Mid-Sprint Review)

**Punto de evaluación:** Antes de iniciar la Integración de STT/LLM (Issue #4)
**Componente bajo análisis:** Acoplamiento de servicios externos en la API de Django Ninja.

## Diagnóstico Inicial
Al ejecutar el análisis de la arquitectura, se detectó un riesgo de "lógica dispersa". Si acoplamos las llamadas directas a las APIs de Inteligencia Artificial (Claude/Gemini/Groq) directamente dentro de los endpoints (rutas) de Django Ninja, el código se volverá rígido, difícil de testear y altamente vulnerable a fallos de red.

## Propuestas de los Sub-Agentes 

*   **Sub-Agente A (Enfoque Monolítico Directo):** Sugiere implementar las peticiones HTTP a la IA directamente en los controladores de la API. 
    *   *Pro:* Rápido de programar. 
    *   *Contra:* Bloquea el hilo principal de Django, genera latencia inaceptable para el usuario y acopla fuertemente el sistema a un solo proveedor de IA.
*   **Sub-Agente B (Enfoque Event-Driven con Celery):** Sugiere delegar todo el procesamiento a colas de mensajes usando RabbitMQ/Redis y Celery. 
    *   *Pro:* Máxima escalabilidad y tolerancia a fallos. 
    *   *Contra:* "Sobreingeniería" para el estado actual del MVP; requiere levantar más contenedores y aumenta drásticamente la complejidad operativa inicial.
*   **Sub-Agente C (Enfoque Service Layer + Strategy Pattern):** Sugiere crear una capa intermedia (`services/ai_service.py`) basada en clases abstractas que defina contratos estrictos para STT y LLM.
    *   *Pro:* Permite cambiar de proveedor de IA (ej. de Claude a Gemini) modificando solo una variable de entorno. Mantiene los endpoints limpios. 
    *   *Contra:* Requiere un esfuerzo inicial de diseño de interfaces en Python.

## Solución Híbrida Implementada
El comité (Tech Lead + IA) ha decidido implementar una versión optimizada de la propuesta del **Sub-Agente C**, pero utilizando soporte de concurrencia nativa (`asyncio` / `ASGI` de Django) en lugar de hilos tradicionales. 

**Justificación técnica:** 
Esta decisión nos da la flexibilidad de inyectar dependencias (cambiar de IA sin romper la app) y evita bloquear las peticiones de los técnicos de campo en terrenos con mala conexión. Se pospone la complejidad de RabbitMQ/Celery (Sub-Agente B) hasta que el sistema requiera procesar más de 100 reportes simultáneos, mitigando la deuda técnica temprana de forma inteligente.
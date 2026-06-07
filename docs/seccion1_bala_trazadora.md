# Sección 1: La Bala Trazadora (Tracer Bullet) y el Enrutamiento de las Skills

En el desarrollo del ecosistema **Field-Voice-Agent**, el equipo de ingeniería enfrentó un desafío clásico de los sistemas modernos basados en Inteligencia Artificial: la alta incertidumbre en las fronteras de integración. Diseñar un sistema reactivo y robusto requería mitigar riesgos antes de que la acumulación de código boilerplate oscureciera los cuellos de botella arquitectónicos.

## 1. El Árbol de Diseño Finito e Hipótesis Iniciales
Antes de escribir la primera línea de código, la exploración inicial mediante el desglose del *árbol de diseño* (Product Requirement Document desglosado hacia Historias de Usuario) nos obligó a confrontar nuestras asunciones originales. 

* **Asunción Inicial Errada:** Originalmente se asumía que el sistema debía procesar los flujos de audio de los técnicos agrícolas mediante un esquema puramente síncrono en Django, delegando la extracción de entidades de forma bloqueante o implementando de inmediato una infraestructura pesada basada en colas distribuídas (Celery + RabbitMQ).
* **Refinamiento de Hipótesis:** Gracias a la auditoría preliminar de dependencias y de riesgos operacionales, determinamos que el mayor peligro residía en la latencia de red en zonas rurales y el acoplamiento con las APIs externas de LLMs (proveedores externos). Añadir Celery en el día uno representaría una introducción prematura de complejidad operativa (sobreingeniería). En su lugar, el árbol de diseño se refinó para explotar las capacidades **ASGI asíncronas de Django 5.2** emparejadas con un enrutamiento ágil a través de **Django Ninja**.

## 2. Definición de nuestra Bala Trazadora (Tracer Bullet)
En lugar de construir el software de forma horizontal tradicional (crear toda la base de datos primero, luego todas las vistas y al final la integración), aplicamos el concepto de **Bala Trazadora**: una porción vertical ultradelgada del sistema que atraviesa todas las capas de la arquitectura (API, Capa de Servicio y Persistencia) para validar el flujo extremo a extremo (E2E).

En *Field-Voice-Agent*, nuestra Bala Trazadora fue la combinación secuencial de los **Issues #1 al #4**, culminando con el esqueleto funcional del endpoint `/process-voice/` y el módulo abstracto `VoiceAgentService`.

### ¿Por qué esta fue nuestra bala trazadora?
Porque forzar el flujo completo desde la ruta de entrada hasta la simulación estructurada de la IA mitigó los tres riesgos más altos del proyecto simultáneamente:

1.  **Validación del Entorno Híbrido (Persistencia):** Confirmó que el mapeo ORM de los modelos base (`ServiceReport`, `ConversationTurns`) operaba sin fricciones tanto en el fallback local de desarrollo (SQLite) como en el entorno de producción Cloud (PostgreSQL en Railway), unificado bajo el setup estructural de la app en el Issue #1 y #2.
2.  **Mitigación de Bloqueos de Hilo:** Al implementar el endpoint con `async def` utilizando el motor ASGI en Django Ninja (Issue #3), demostramos que la aplicación podía sostener conexiones concurrentes de múltiples técnicos sin congelar el hilo principal mientras espera la resolución de procesos pesados de audio.
3.  **Desacoplamiento de Proveedores de IA:** La creación de la interfaz abstracta `VoiceAgentService` inyectando un comportamiento de proveedor simulado (*Mock*) demostró que la API puede interactuar con contratos de datos estrictos (JSON estructurado con locación, materiales y observaciones) sin depender financieramente ni técnicamente de la estabilidad o costo de un proveedor externo (Claude/Gemini) en fases tempranas.

## 3. Feedback Temprano obtenido
Gracias a este disparo vertical de la arquitectura, pudimos validar que un técnico en campo puede enviar una carga útil simulada y recibir una respuesta JSON estructurada con un tiempo de respuesta óptimo en la capa del servidor. El esqueleto arquitectónico quedó completamente verificado y "en verde", permitiendo que los sprints posteriores se enfoquen puramente en la lógica interna del negocio sin temor a que los cimientos de la integración fallen.
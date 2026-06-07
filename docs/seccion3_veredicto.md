# Sección 3: El Veredicto Retrospectivo de los Sub-Agentes

En la fase intermedia del proyecto, la ejecución de la skill de simulación arquitectónica (`/improve-codebase-architecture`) nos obligó a detener la "Programación Táctica" (escribir código rápido solo para cerrar tickets) y adoptar una mentalidad de "Programación Estratégica" (invertir tiempo en el diseño para acelerar el futuro), conceptos fuertemente defendidos por John Ousterhout.

## 1. El Impacto en la Velocidad de Desarrollo
Durante el Punto de Control, tres sub-agentes propusieron vías distintas para la integración de la IA:
* **A:** Monolito directo (rápido pero frágil).
* **B:** Arquitectura Orientada a Eventos con Celery (escalable pero con alta sobrecarga inicial).
* **C:** Patrón Strategy con soporte asíncrono ASGI.

Decidimos implementar una solución híbrida basada en el **Sub-Agente C**. A corto plazo, esto redujo nuestra velocidad de desarrollo, ya que tuvimos que invertir tiempo en abstraer la clase `VoiceAgentService` en lugar de simplemente programar el endpoint de una vez. Sin embargo, en la segunda mitad del sprint, **la velocidad se multiplicó exponencialmente**. Al momento de enlazar el endpoint final (`/process-voice/`), el desarrollador (humano o agente) solo tuvo que instanciar la clase y llamar a un método. El acoplamiento suelto permitió paralelizar el trabajo.

## 2. Elasticidad frente al Cambio y "Change Amplification"
Ousterhout define la **Amplificación de Cambios (Change Amplification)** como un síntoma de mal diseño arquitectónico, donde un cambio conceptual simple requiere modificaciones en múltiples lugares del código.

**El Veredicto Final:**
Nuestra arquitectura demostró tener un "buen gusto arquitectónico" y ser altamente elástica. Al finalizar los últimos issues, no sufrimos de *Change Amplification*. 

Si el día de mañana el cliente solicita cambiar el motor de IA de Claude a Gemini, la modificación requiere cambiar exactamente **una sola línea de código** (la instanciación del proveedor en el constructor del servicio), dejando intactos los enrutadores, los validadores HTTP, y los modelos de base de datos. La decisión de encapsular la complejidad de la IA detrás de una interfaz profunda demostró ser la inversión técnica más rentable de todo el ciclo de desarrollo de *Agricola Sender*.
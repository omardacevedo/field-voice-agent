# Client Brief: FieldVoice Agent

## 1. Definición del Problema
Los técnicos de campo (instaladores/mantenimiento) pierden hasta un 20% de su jornada laboral documentando reportes administrativos tras cada intervención. El uso de interfaces táctiles en entornos hostiles es ineficiente, propenso a errores y genera fatiga administrativa.

## 2. Propuesta de Solución
Un agente de voz conversacional (FieldVoice) que utiliza LLMs para transcribir, estructurar y sincronizar reportes de servicio en tiempo real, integrado directamente con el backend del sistema de gestión (Django/PostgreSQL).

## 3. Requerimientos Técnicos
- Backend: Python (Django) con arquitectura asíncrona (`asyncio`).
- Base de Datos: PostgreSQL.
- Flujo de Audio: Integración de servicios STT/TTS.
- Despliegue: CI/CD integrado con Railway.

## 4. Metodología de Desarrollo
Este proyecto se desarrolla bajo el flujo de "Agente AFK", utilizando Claude Code para la generación, refactorización y despliegue iterativo de componentes.
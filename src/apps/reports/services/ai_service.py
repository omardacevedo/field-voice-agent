# src/apps/reports/services/ai_service.py

class VoiceAgentService:
    """
    Capa de abstracción para el Agente de Voz.
    Implementa el patrón Strategy para la IA.
    """
    def __init__(self, provider="mock"):
        self.provider = provider

    async def process_audio_to_json(self, audio_data) -> dict:
        """
        Simula la recepción de audio, la transcripción (STT) y la extracción de datos (LLM).
        Retorna un JSON estructurado listo para la base de datos.
        """
        mock_response = {
            "status": "success",
            "extracted_data": {
                "location": "Sector Norte - Lote 4",
                "materials_used": [{"name": "Fertilizante NPK", "quantity": "5 litros"}],
                "observations": "Se detectó leve plaga de pulgón, aplicar tratamiento mañana."
            }
        }
        return mock_response
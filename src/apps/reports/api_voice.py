# src/apps/reports/api_voice.py
from ninja import Router
from .services.ai_service import VoiceAgentService

router = Router()
ai_agent = VoiceAgentService()

@router.post("/process-voice/")
async def process_voice_report(request):
    """
    Endpoint que recibe el reporte de voz del técnico.
    Delega el procesamiento al ai_service sin bloquear el hilo principal.
    """
    audio_dummy = "audio_bytes_simulados"
    
    # Procesamiento asíncrono
    result = await ai_agent.process_audio_to_json(audio_dummy)
    
    return {"message": "Reporte de voz procesado correctamente", "data": result}
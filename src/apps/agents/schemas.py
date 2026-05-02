import uuid
from datetime import datetime
from typing import Optional
from ninja import Schema


class ConversationTurnIn(Schema):
    role: str
    transcription: str
    audio_url: str = ""
    extracted_data: Optional[dict] = None
    token_count: Optional[int] = None
    duration_ms: Optional[int] = None


class ConversationTurnOut(Schema):
    id: uuid.UUID
    turn_index: int
    role: str
    transcription: str
    audio_url: str
    extracted_data: Optional[dict] = None
    token_count: Optional[int] = None
    duration_ms: Optional[int] = None
    created_at: datetime


class AgentSessionIn(Schema):
    report_id: uuid.UUID
    model_used: str = "claude-sonnet-4-6"


class AgentSessionPatch(Schema):
    status: Optional[str] = None
    ended_at: Optional[datetime] = None


class AgentSessionOut(Schema):
    id: uuid.UUID
    report_id: uuid.UUID
    status: str
    model_used: str
    total_turns: int
    started_at: datetime
    ended_at: Optional[datetime] = None


class AgentSessionDetail(AgentSessionOut):
    turns: list[ConversationTurnOut]

    @staticmethod
    def resolve_turns(obj) -> list:
        return list(obj.turns.order_by("turn_index"))

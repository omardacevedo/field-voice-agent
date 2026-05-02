import uuid
from ninja import Router
from ninja_jwt.authentication import JWTAuth
from django.db.models import F
from django.shortcuts import get_object_or_404

from apps.reports.models import ServiceReport
from .models import AgentSession, ConversationTurn
from .schemas import (
    AgentSessionIn,
    AgentSessionOut,
    AgentSessionDetail,
    AgentSessionPatch,
    ConversationTurnIn,
    ConversationTurnOut,
)

router = Router()


@router.post("/", auth=JWTAuth(), response={201: AgentSessionOut})
def create_session(request, payload: AgentSessionIn):
    report = get_object_or_404(
        ServiceReport, id=payload.report_id, technician=request.auth
    )
    session = AgentSession.objects.create(
        report=report,
        technician=request.auth,
        model_used=payload.model_used,
    )
    return 201, session


@router.get("/{session_id}", auth=JWTAuth(), response=AgentSessionDetail)
def get_session(request, session_id: uuid.UUID):
    return get_object_or_404(
        AgentSession.objects.prefetch_related("turns"),
        id=session_id,
        technician=request.auth,
    )


@router.patch("/{session_id}", auth=JWTAuth(), response=AgentSessionOut)
def patch_session(request, session_id: uuid.UUID, payload: AgentSessionPatch):
    session = get_object_or_404(
        AgentSession, id=session_id, technician=request.auth
    )
    for attr, value in payload.model_dump(exclude_unset=True).items():
        setattr(session, attr, value)
    session.save()
    return session


@router.post("/{session_id}/turns", auth=JWTAuth(), response={201: ConversationTurnOut})
def add_turn(request, session_id: uuid.UUID, payload: ConversationTurnIn):
    session = get_object_or_404(
        AgentSession, id=session_id, technician=request.auth, status="ACTIVE"
    )
    next_index = session.turns.count()
    turn = ConversationTurn.objects.create(
        session=session,
        turn_index=next_index,
        **payload.model_dump(),
    )
    AgentSession.objects.filter(id=session.id).update(total_turns=F("total_turns") + 1)
    return 201, turn


@router.get("/{session_id}/turns", auth=JWTAuth(), response=list[ConversationTurnOut])
def list_turns(request, session_id: uuid.UUID):
    session = get_object_or_404(AgentSession, id=session_id, technician=request.auth)
    return list(session.turns.order_by("turn_index"))

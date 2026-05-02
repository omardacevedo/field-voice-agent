import uuid
from django.conf import settings
from django.db import models


class AgentSession(models.Model):
    class Status(models.TextChoices):
        ACTIVE = "ACTIVE", "Activa"
        COMPLETED = "COMPLETED", "Completada"
        FAILED = "FAILED", "Fallida"
        ABORTED = "ABORTED", "Abortada"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    report = models.ForeignKey(
        "reports.ServiceReport",
        on_delete=models.CASCADE,
        related_name="sessions",
    )
    technician = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="agent_sessions",
    )
    status = models.CharField(
        max_length=20, choices=Status.choices, default=Status.ACTIVE
    )
    model_used = models.CharField(max_length=100, default="claude-sonnet-4-6")
    total_turns = models.PositiveIntegerField(default=0)
    started_at = models.DateTimeField(auto_now_add=True)
    ended_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ["-started_at"]
        verbose_name = "agent session"
        verbose_name_plural = "agent sessions"

    def __str__(self):
        return f"Session {self.id} — {self.report.work_order}"


class ConversationTurn(models.Model):
    class Role(models.TextChoices):
        USER = "user", "Usuario"
        ASSISTANT = "assistant", "Asistente"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    session = models.ForeignKey(
        AgentSession,
        on_delete=models.CASCADE,
        related_name="turns",
    )
    turn_index = models.PositiveIntegerField()
    role = models.CharField(max_length=20, choices=Role.choices)
    transcription = models.TextField()
    audio_url = models.URLField(blank=True)
    extracted_data = models.JSONField(null=True, blank=True)
    token_count = models.PositiveIntegerField(null=True, blank=True)
    duration_ms = models.PositiveIntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["session", "turn_index"]
        unique_together = [("session", "turn_index")]
        verbose_name = "conversation turn"
        verbose_name_plural = "conversation turns"

    def __str__(self):
        return f"Turn {self.turn_index} ({self.role}) — {self.session_id}"

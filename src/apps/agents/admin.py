from django.contrib import admin
from .models import AgentSession, ConversationTurn


class ConversationTurnInline(admin.TabularInline):
    model = ConversationTurn
    extra = 0
    readonly_fields = ["id", "created_at"]
    fields = ["turn_index", "role", "transcription", "token_count", "duration_ms", "created_at"]


@admin.register(AgentSession)
class AgentSessionAdmin(admin.ModelAdmin):
    list_display = ["id", "report", "technician", "status", "model_used", "total_turns", "started_at"]
    list_filter = ["status", "model_used"]
    search_fields = ["report__work_order", "technician__email"]
    readonly_fields = ["id", "started_at"]
    inlines = [ConversationTurnInline]


@admin.register(ConversationTurn)
class ConversationTurnAdmin(admin.ModelAdmin):
    list_display = ["id", "session", "turn_index", "role", "token_count", "created_at"]
    list_filter = ["role"]
    search_fields = ["session__report__work_order"]
    readonly_fields = ["id", "created_at"]

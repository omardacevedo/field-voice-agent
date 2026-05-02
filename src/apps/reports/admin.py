from django.contrib import admin
from .models import ServiceReport


@admin.register(ServiceReport)
class ServiceReportAdmin(admin.ModelAdmin):
    list_display = ["work_order", "client_name", "technician", "status", "intervention_type", "created_at"]
    list_filter = ["status", "intervention_type"]
    search_fields = ["work_order", "client_name", "technician__email"]
    readonly_fields = ["id", "created_at", "updated_at"]
    ordering = ["-created_at"]
    fieldsets = (
        (None, {"fields": ("id", "technician", "status", "work_order")}),
        ("Intervención", {"fields": ("client_name", "intervention_type", "location", "description")}),
        ("Materiales y observaciones", {"fields": ("materials_used", "observations")}),
        ("Tiempos", {"fields": ("started_at", "completed_at", "created_at", "updated_at")}),
    )

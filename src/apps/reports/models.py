import uuid
from django.conf import settings
from django.db import models


class ServiceReport(models.Model):
    class Status(models.TextChoices):
        DRAFT = "DRAFT", "Borrador"
        IN_PROGRESS = "IN_PROGRESS", "En progreso"
        COMPLETED = "COMPLETED", "Completado"
        SYNCED = "SYNCED", "Sincronizado"

    class InterventionType(models.TextChoices):
        INSTALLATION = "INSTALLATION", "Instalación"
        MAINTENANCE = "MAINTENANCE", "Mantenimiento"
        REPAIR = "REPAIR", "Reparación"
        INSPECTION = "INSPECTION", "Inspección"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    technician = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="reports",
    )
    status = models.CharField(
        max_length=20, choices=Status.choices, default=Status.DRAFT
    )
    work_order = models.CharField(max_length=100, unique=True, db_index=True)
    client_name = models.CharField(max_length=200)
    intervention_type = models.CharField(max_length=20, choices=InterventionType.choices)
    location = models.JSONField(default=dict)
    description = models.TextField(blank=True)
    materials_used = models.JSONField(default=list)
    observations = models.TextField(blank=True)
    started_at = models.DateTimeField(null=True, blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "service report"
        verbose_name_plural = "service reports"

    def __str__(self):
        return f"{self.work_order} — {self.client_name}"

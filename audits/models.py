from django.conf import settings
from django.db import models

from core.models import TimeStampedModel


class AuditLog(TimeStampedModel):
    event_type = models.CharField(max_length=100)
    actor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="audit_logs",
    )
    metadata = models.JSONField(default=dict, blank=True)
    prev_hash = models.CharField(max_length=255, blank=True)
    curr_hash = models.CharField(max_length=255)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return f"{self.event_type} at {self.created_at}"

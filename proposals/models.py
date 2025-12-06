from django.conf import settings
from django.db import models

from core.models import TimeStampedModel


class Initiative(TimeStampedModel):
    STATUS_CHOICES = [
        ("draft", "Borrador"),
        ("review", "En revisión"),
        ("published", "Publicada"),
        ("closed", "Cerrada"),
    ]

    promoter = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="initiatives",
    )
    title = models.CharField(max_length=255)
    summary = models.TextField()
    content = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="draft")
    starts_at = models.DateTimeField(null=True, blank=True)
    ends_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title


class SupportSignature(TimeStampedModel):
    initiative = models.ForeignKey(
        Initiative,
        on_delete=models.CASCADE,
        related_name="support_signatures",
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="support_signatures",
    )
    comment = models.TextField(blank=True)

    class Meta:
        unique_together = ("initiative", "user")

    def __str__(self):
        return f"{self.user.email} -> {self.initiative.title}"

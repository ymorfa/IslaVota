from django.conf import settings
from django.db import models

from core.models import TimeStampedModel


class NotificationTemplate(TimeStampedModel):
    CHANNEL_CHOICES = [
        ("email", "Email"),
        ("sms", "SMS"),
        ("push", "Push"),
    ]

    code = models.CharField(max_length=100, unique=True)
    channel = models.CharField(max_length=20, choices=CHANNEL_CHOICES)
    subject = models.CharField(max_length=255, blank=True)
    body = models.TextField()

    def __str__(self):
        return f"{self.code} ({self.channel})"


class Notification(TimeStampedModel):
    STATUS_CHOICES = [
        ("queued", "En cola"),
        ("sent", "Enviada"),
        ("failed", "Falló"),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="notifications",
    )
    template = models.ForeignKey(
        NotificationTemplate,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="notifications",
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="queued")
    destination = models.CharField(max_length=255)
    payload = models.JSONField(default=dict, blank=True)
    sent_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.email} - {self.status}"

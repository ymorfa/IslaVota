from django.conf import settings
from django.db import models

from core.models import TimeStampedModel
from identity.models import IdentityProfile


class VerificationAttempt(TimeStampedModel):
    METHODS = [
        ("document", "Documento"),
        ("biometric", "Biométrico"),
        ("manual", "Manual"),
    ]
    STATUSES = [
        ("pending", "Pendiente"),
        ("approved", "Aprobado"),
        ("rejected", "Rechazado"),
    ]

    profile = models.ForeignKey(
        IdentityProfile,
        on_delete=models.CASCADE,
        related_name="verification_attempts",
    )
    method = models.CharField(max_length=20, choices=METHODS)
    status = models.CharField(max_length=20, choices=STATUSES, default="pending")
    score = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    notes = models.TextField(blank=True)
    reviewed_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="reviewed_verifications",
    )

    def __str__(self):
        return f"{self.profile.user.email} - {self.method} ({self.status})"


class DeviceFingerprint(TimeStampedModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="device_fingerprints",
    )
    device_hash = models.CharField(max_length=255)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.user.email} - {self.device_hash}"

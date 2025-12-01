from django.conf import settings
from django.db import models

from core.models import TimeStampedModel


class IdentityProfile(TimeStampedModel):
    STATUS_CHOICES = [
        ("pending", "Pendiente"),
        ("verified", "Verificado"),
        ("rejected", "Rechazado"),
    ]

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="identity_profile",
    )
    full_name = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")

    def __str__(self):
        return f"{self.user.email} ({self.status})"


class IdentityDocument(TimeStampedModel):
    DOCUMENT_TYPES = [
        ("ci", "Carnet de Identidad"),
        ("passport", "Pasaporte"),
    ]

    profile = models.ForeignKey(
        IdentityProfile,
        on_delete=models.CASCADE,
        related_name="documents",
    )
    doc_type = models.CharField(max_length=20, choices=DOCUMENT_TYPES)
    number = models.CharField(max_length=50)
    file_hash = models.CharField(max_length=255)
    status = models.CharField(max_length=20, default="submitted")
    issued_at = models.DateField(null=True, blank=True)
    expires_at = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.doc_type} - {self.number}"


class BiometricSample(TimeStampedModel):
    SAMPLE_TYPES = [
        ("face", "Rostro"),
        ("iris", "Iris"),
    ]

    profile = models.ForeignKey(
        IdentityProfile,
        on_delete=models.CASCADE,
        related_name="biometric_samples",
    )
    sample_type = models.CharField(max_length=20, choices=SAMPLE_TYPES)
    storage_url = models.CharField(max_length=255)
    match_score = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.sample_type} sample for {self.profile.user.email}"

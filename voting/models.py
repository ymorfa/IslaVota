from django.conf import settings
from django.db import models

from core.models import TimeStampedModel
from proposals.models import Initiative


class Ballot(TimeStampedModel):
    initiative = models.OneToOneField(
        Initiative,
        on_delete=models.CASCADE,
        related_name="ballot",
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    published_at = models.DateTimeField(null=True, blank=True)
    closed_at = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Vote(TimeStampedModel):
    ballot = models.ForeignKey(
        Ballot,
        on_delete=models.CASCADE,
        related_name="votes",
    )
    voter = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="votes",
    )
    payload_ciphertext = models.TextField()
    audit_hash = models.CharField(max_length=255)

    class Meta:
        unique_together = ("ballot", "voter")

    def __str__(self):
        return f"Vote {self.id} for {self.ballot.title}"

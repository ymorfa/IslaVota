from rest_framework import serializers

from audits.models import AuditLog


class AuditLogSerializer(serializers.ModelSerializer):
    actor_email = serializers.ReadOnlyField(source="actor.email")

    class Meta:
        model = AuditLog
        fields = [
            "id",
            "event_type",
            "actor",
            "actor_email",
            "metadata",
            "prev_hash",
            "curr_hash",
            "created_at",
        ]
        read_only_fields = ["event_type", "actor", "metadata", "prev_hash", "curr_hash", "created_at"]

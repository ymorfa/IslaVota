from rest_framework import serializers

from proposals.models import Initiative, SupportSignature


class InitiativeSerializer(serializers.ModelSerializer):
    promoter_email = serializers.ReadOnlyField(source="promoter.email")

    class Meta:
        model = Initiative
        fields = [
            "id",
            "title",
            "summary",
            "content",
            "status",
            "starts_at",
            "ends_at",
            "promoter",
            "promoter_email",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["status", "promoter", "promoter_email", "created_at", "updated_at"]


class SupportSignatureSerializer(serializers.ModelSerializer):
    user_email = serializers.ReadOnlyField(source="user.email")

    class Meta:
        model = SupportSignature
        fields = ["id", "initiative", "user", "user_email", "comment", "created_at"]
        read_only_fields = ["user", "user_email", "created_at"]

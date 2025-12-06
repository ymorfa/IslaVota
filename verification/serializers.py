from rest_framework import serializers

from verification.models import DeviceFingerprint, VerificationAttempt


class VerificationAttemptSerializer(serializers.ModelSerializer):
    class Meta:
        model = VerificationAttempt
        fields = [
            "id",
            "profile",
            "method",
            "status",
            "score",
            "notes",
            "reviewed_by",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["status", "reviewed_by", "created_at", "updated_at"]


class DeviceFingerprintSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceFingerprint
        fields = ["id", "device_hash", "ip_address", "user_agent", "created_at"]
        read_only_fields = ["ip_address", "user_agent", "created_at"]

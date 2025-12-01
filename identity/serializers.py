from rest_framework import serializers

from identity.models import BiometricSample, IdentityDocument, IdentityProfile


class IdentityDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = IdentityDocument
        fields = ["id", "doc_type", "number", "file_hash", "status", "issued_at", "expires_at", "created_at"]
        read_only_fields = ["status", "created_at"]


class BiometricSampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = BiometricSample
        fields = ["id", "sample_type", "storage_url", "match_score", "created_at"]
        read_only_fields = ["match_score", "created_at"]


class IdentityProfileSerializer(serializers.ModelSerializer):
    documents = IdentityDocumentSerializer(many=True, read_only=True)
    biometric_samples = BiometricSampleSerializer(many=True, read_only=True)

    class Meta:
        model = IdentityProfile
        fields = [
            "id",
            "full_name",
            "country",
            "status",
            "documents",
            "biometric_samples",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["status", "created_at", "updated_at"]

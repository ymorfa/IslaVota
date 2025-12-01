from rest_framework import serializers

from voting.models import Ballot, Vote


class BallotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ballot
        fields = [
            "id",
            "initiative",
            "title",
            "description",
            "published_at",
            "closed_at",
            "is_active",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["created_at", "updated_at"]


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ["id", "ballot", "voter", "payload_ciphertext", "audit_hash", "created_at"]
        read_only_fields = ["voter", "created_at"]

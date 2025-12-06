from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "name", "is_verified", "is_active", "created_at", "updated_at"]
        read_only_fields = ["is_verified", "is_active", "created_at", "updated_at"]

from rest_framework import serializers

from notifications.models import Notification, NotificationTemplate


class NotificationTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationTemplate
        fields = ["id", "code", "channel", "subject", "body", "created_at", "updated_at"]
        read_only_fields = ["created_at", "updated_at"]


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = [
            "id",
            "user",
            "template",
            "status",
            "destination",
            "payload",
            "sent_at",
            "created_at",
        ]
        read_only_fields = ["user", "status", "sent_at", "created_at"]

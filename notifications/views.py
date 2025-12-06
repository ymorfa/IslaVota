from rest_framework import permissions, viewsets

from notifications.models import Notification, NotificationTemplate
from notifications.serializers import NotificationSerializer, NotificationTemplateSerializer


class NotificationTemplateViewSet(viewsets.ModelViewSet):
    serializer_class = NotificationTemplateSerializer
    queryset = NotificationTemplate.objects.all().order_by("-created_at")
    permission_classes = [permissions.IsAdminUser]


class NotificationViewSet(viewsets.ModelViewSet):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        qs = Notification.objects.select_related("user", "template").order_by("-created_at")
        if self.request.user.is_staff:
            return qs
        return qs.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

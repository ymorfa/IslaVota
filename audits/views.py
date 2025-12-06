from rest_framework import permissions, viewsets

from audits.models import AuditLog
from audits.serializers import AuditLogSerializer


class AuditLogViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = AuditLogSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        qs = AuditLog.objects.select_related("actor")
        if self.request.user.is_staff:
            return qs
        return qs.filter(actor=self.request.user)

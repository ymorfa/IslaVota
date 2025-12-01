from django.db.models import Q
from rest_framework import permissions, viewsets

from proposals.models import Initiative, SupportSignature
from proposals.serializers import InitiativeSerializer, SupportSignatureSerializer


class InitiativeViewSet(viewsets.ModelViewSet):
    serializer_class = InitiativeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        qs = Initiative.objects.select_related("promoter").order_by("-created_at")
        if self.request.user.is_staff:
            return qs
        return qs.filter(Q(status="published") | Q(promoter=self.request.user))

    def perform_create(self, serializer):
        serializer.save(promoter=self.request.user, status="review")


class SupportSignatureViewSet(viewsets.ModelViewSet):
    serializer_class = SupportSignatureSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        qs = SupportSignature.objects.select_related("initiative", "user")
        if self.request.user.is_staff:
            return qs
        return qs.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

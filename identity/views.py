from rest_framework import permissions, viewsets
from rest_framework.exceptions import ValidationError

from identity.models import BiometricSample, IdentityDocument, IdentityProfile
from identity.serializers import (
    BiometricSampleSerializer,
    IdentityDocumentSerializer,
    IdentityProfileSerializer,
)


class IdentityProfileViewSet(viewsets.ModelViewSet):
    serializer_class = IdentityProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        qs = IdentityProfile.objects.select_related("user")
        if self.request.user.is_staff:
            return qs
        return qs.filter(user=self.request.user)

    def perform_create(self, serializer):
        if IdentityProfile.objects.filter(user=self.request.user).exists():
            raise ValidationError("El perfil de identidad ya existe.")
        serializer.save(user=self.request.user)


class IdentityDocumentViewSet(viewsets.ModelViewSet):
    serializer_class = IdentityDocumentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        qs = IdentityDocument.objects.select_related("profile__user")
        if self.request.user.is_staff:
            return qs
        return qs.filter(profile__user=self.request.user)

    def perform_create(self, serializer):
        profile = IdentityProfile.objects.filter(user=self.request.user).first()
        if not profile:
            raise ValidationError("Crea primero un perfil de identidad.")
        serializer.save(profile=profile)


class BiometricSampleViewSet(viewsets.ModelViewSet):
    serializer_class = BiometricSampleSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        qs = BiometricSample.objects.select_related("profile__user")
        if self.request.user.is_staff:
            return qs
        return qs.filter(profile__user=self.request.user)

    def perform_create(self, serializer):
        profile = IdentityProfile.objects.filter(user=self.request.user).first()
        if not profile:
            raise ValidationError("Crea primero un perfil de identidad.")
        serializer.save(profile=profile)

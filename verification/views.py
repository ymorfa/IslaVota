from rest_framework import permissions, viewsets
from rest_framework.exceptions import PermissionDenied

from identity.models import IdentityProfile
from verification.models import DeviceFingerprint, VerificationAttempt
from verification.serializers import DeviceFingerprintSerializer, VerificationAttemptSerializer


class VerificationAttemptViewSet(viewsets.ModelViewSet):
    serializer_class = VerificationAttemptSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        qs = VerificationAttempt.objects.select_related("profile__user", "reviewed_by")
        if self.request.user.is_staff:
            return qs
        return qs.filter(profile__user=self.request.user)

    def perform_create(self, serializer):
        profile_id = self.request.data.get("profile")
        if not profile_id:
            raise PermissionDenied("Debes indicar el perfil a verificar.")
        profile = IdentityProfile.objects.filter(id=profile_id).first()
        if not profile or (profile.user != self.request.user and not self.request.user.is_staff):
            raise PermissionDenied("No puedes crear verificaciones para otro usuario.")
        serializer.save(profile=profile)


class DeviceFingerprintViewSet(viewsets.ModelViewSet):
    serializer_class = DeviceFingerprintSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        qs = DeviceFingerprint.objects.select_related("user")
        if self.request.user.is_staff:
            return qs
        return qs.filter(user=self.request.user)

    def perform_create(self, serializer):
        ip_address = self.request.META.get("REMOTE_ADDR")
        user_agent = self.request.META.get("HTTP_USER_AGENT", "")
        serializer.save(user=self.request.user, ip_address=ip_address, user_agent=user_agent)

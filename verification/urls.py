from django.urls import include, path
from rest_framework.routers import DefaultRouter

from verification.views import DeviceFingerprintViewSet, VerificationAttemptViewSet

router = DefaultRouter()
router.register("attempts", VerificationAttemptViewSet, basename="verification-attempt")
router.register("devices", DeviceFingerprintViewSet, basename="verification-device")

urlpatterns = [
    path("", include(router.urls)),
]

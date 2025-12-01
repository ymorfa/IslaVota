from django.urls import include, path
from rest_framework.routers import DefaultRouter

from identity.views import BiometricSampleViewSet, IdentityDocumentViewSet, IdentityProfileViewSet

router = DefaultRouter()
router.register("profiles", IdentityProfileViewSet, basename="identity-profile")
router.register("documents", IdentityDocumentViewSet, basename="identity-document")
router.register("biometrics", BiometricSampleViewSet, basename="identity-biometric")

urlpatterns = [
    path("", include(router.urls)),
]

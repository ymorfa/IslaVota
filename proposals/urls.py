from django.urls import include, path
from rest_framework.routers import DefaultRouter

from proposals.views import InitiativeViewSet, SupportSignatureViewSet

router = DefaultRouter()
router.register("initiatives", InitiativeViewSet, basename="initiative")
router.register("signatures", SupportSignatureViewSet, basename="support-signature")

urlpatterns = [
    path("", include(router.urls)),
]

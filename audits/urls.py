from django.urls import include, path
from rest_framework.routers import DefaultRouter

from audits.views import AuditLogViewSet

router = DefaultRouter()
router.register("logs", AuditLogViewSet, basename="audit-log")

urlpatterns = [
    path("", include(router.urls)),
]

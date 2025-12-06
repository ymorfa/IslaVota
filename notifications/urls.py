from django.urls import include, path
from rest_framework.routers import DefaultRouter

from notifications.views import NotificationTemplateViewSet, NotificationViewSet

router = DefaultRouter()
router.register("templates", NotificationTemplateViewSet, basename="notification-template")
router.register("notifications", NotificationViewSet, basename="notification")

urlpatterns = [
    path("", include(router.urls)),
]

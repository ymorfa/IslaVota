from django.urls import include, path
from rest_framework.routers import DefaultRouter

from users.views import MeView, UserViewSet

router = DefaultRouter()
router.register("users", UserViewSet, basename="user")

urlpatterns = [
    path("", include(router.urls)),
    path("me/", MeView.as_view(), name="me"),
]

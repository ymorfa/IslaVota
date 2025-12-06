from django.urls import path

from core.views import HealthcheckView

urlpatterns = [
    path("health/", HealthcheckView.as_view(), name="healthcheck"),
]

from django.urls import include, path
from rest_framework.routers import DefaultRouter

from voting.views import BallotViewSet, VoteViewSet

router = DefaultRouter()
router.register("ballots", BallotViewSet, basename="ballot")
router.register("votes", VoteViewSet, basename="vote")

urlpatterns = [
    path("", include(router.urls)),
]

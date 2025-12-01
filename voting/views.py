from rest_framework import permissions, viewsets
from rest_framework.exceptions import PermissionDenied

from proposals.models import Initiative
from voting.models import Ballot, Vote
from voting.serializers import BallotSerializer, VoteSerializer


class BallotViewSet(viewsets.ModelViewSet):
    serializer_class = BallotSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        qs = Ballot.objects.select_related("initiative")
        if self.request.user.is_staff:
            return qs
        return qs.filter(is_active=True)

    def perform_create(self, serializer):
        initiative_id = self.request.data.get("initiative")
        initiative = Initiative.objects.filter(id=initiative_id).first()
        if not initiative:
            raise PermissionDenied("Iniciativa no encontrada.")
        if initiative.promoter != self.request.user and not self.request.user.is_staff:
            raise PermissionDenied("Solo el promotor o administradores pueden crear boletas.")
        serializer.save()


class VoteViewSet(viewsets.ModelViewSet):
    serializer_class = VoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        qs = Vote.objects.select_related("ballot", "voter")
        if self.request.user.is_staff:
            return qs
        return qs.filter(voter=self.request.user)

    def perform_create(self, serializer):
        ballot_id = self.request.data.get("ballot")
        ballot = Ballot.objects.filter(id=ballot_id).first()
        if not ballot or not ballot.is_active:
            raise PermissionDenied("La boleta no está activa.")
        serializer.save(voter=self.request.user)

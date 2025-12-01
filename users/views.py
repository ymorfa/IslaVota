from rest_framework import permissions, viewsets
from rest_framework.generics import RetrieveUpdateAPIView

from users.models import User
from users.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """Gestión básica de usuarios (solo administradores)."""

    queryset = User.objects.all().order_by("-created_at")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]


class MeView(RetrieveUpdateAPIView):
    """Permite al usuario ver/actualizar su propio perfil."""

    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

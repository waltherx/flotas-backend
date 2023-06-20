from rest_framework import viewsets
from .serializer import UserSerializer
from django.contrib.auth.models import User

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    """def perform_create(self, serializer):
        usuario = serializer.save()
        usuario.set_password(usuario.password)
        usuario.save()"""
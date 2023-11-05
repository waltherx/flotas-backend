from rest_framework import viewsets
from .serializer import UserSerializer
from rest_framework.decorators import action
from django.contrib.auth.models import User
from rest_framework.response import Response

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=True, methods=['GET'])
    def users(self, request, pk=None):
        product = self.get_object()
        users = product.reviews.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    """def perform_create(self, serializer):
        usuario = serializer.save()
        usuario.set_password(usuario.password)
        usuario.save()"""
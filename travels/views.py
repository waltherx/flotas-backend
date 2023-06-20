from rest_framework import viewsets
from .serializer import CiudadSerializer, RutaSerializer, ViajeSerializer
from .models import Ruta, Ciudad, Viaje


class CiudadView(viewsets.ModelViewSet):
    serializer_class = CiudadSerializer
    queryset = Ciudad.objects.all()


class RutaView(viewsets.ModelViewSet):
    serializer_class = RutaSerializer
    queryset = Ruta.objects.all()


class ViajeView(viewsets.ModelViewSet):
    serializer_class = ViajeSerializer
    queryset = Viaje.objects.all()

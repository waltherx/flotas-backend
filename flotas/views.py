from rest_framework import viewsets
from .serializer import (
    MarcaSerializer,
    FlotaSerializer,
    AsientoSerializer,
    DisenioSerializer,
)
from .models import Marca, Flota, Asiento, Disenio


class MarcaView(viewsets.ModelViewSet):
    serializer_class = MarcaSerializer
    queryset = Marca.objects.all()


class FlotaView(viewsets.ModelViewSet):
    serializer_class = FlotaSerializer
    queryset = Flota.objects.all()


class AsientoView(viewsets.ModelViewSet):
    serializer_class = AsientoSerializer
    queryset = Asiento.objects.all()


class DisenioView(viewsets.ModelViewSet):
    serializer_class = DisenioSerializer
    queryset = Disenio.objects.all()

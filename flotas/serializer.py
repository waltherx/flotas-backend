from rest_framework import serializers
from .models import Marca, Flota,Asiento,Disenio


class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = "__all__"

class FlotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flota
        fields = "__all__"

class AsientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asiento
        fields = "__all__"

class DisenioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disenio
        fields = "__all__"
import graphene
from graphene_django import DjangoObjectType
from .models import Ciudad, Viaje, Ruta
from transporte.models import Flota, Marca


class CiudadesType(DjangoObjectType):
    class Meta:
        model = Ciudad
        fields = ("id", "nombre", "descripcion")


class RutasType(DjangoObjectType):
    class Meta:
        model = Ruta
        fields = "__all__"


class ViajesType(DjangoObjectType):
    class Meta:
        model = Viaje
        fields = "__all__"


class FlotasType(DjangoObjectType):
    class Meta:
        model = Flota
        fields = "__all__"


class MarcasType(DjangoObjectType):
    class Meta:
        model = Marca
        fields = "__all__"


class Query(graphene.ObjectType):
    ciudades = graphene.List(CiudadesType)
    ciudad = graphene.Field(CiudadesType, id=graphene.ID())

    rutas = graphene.List(RutasType)
    ruta = graphene.Field(RutasType, id=graphene.ID())

    viajes = graphene.List(ViajesType)
    viaje = graphene.Field(ViajesType, id=graphene.ID())

    def resolve_ciudades(root, info):
        return Ciudad.objects.all()

    def resolve_ciudad(root, info, id):
        return Ciudad.objects.get(id=id)

    def resolve_rutas(root, info):
        return Ruta.objects.all()

    def resolve_ruta(root, info, id):
        return Ruta.objects.get(id=id)

    def resolve_viajes(root, info):
        return Viaje.objects.all()

    def resolve_viaje(root, info, id):
        return Viaje.objects.get(id=id)


schema = graphene.Schema(query=Query)

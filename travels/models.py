from flotas.models import Flota
from django.db import models


class Ciudad(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    latidud = models.DecimalField(max_digits=12, decimal_places=8)
    longitud = models.DecimalField(max_digits=12, decimal_places=8)

    def __str__(self) -> str:
        return f"Ciudad -> {self.nombre}"


class Ruta(models.Model):
    nombre = models.CharField(max_length=200)
    distancia = models.DecimalField(max_digits=12, decimal_places=2)
    origen = models.ForeignKey(Ciudad, on_delete=models.DO_NOTHING, related_name='rutas_origen')
    destino = models.ForeignKey(Ciudad, on_delete=models.DO_NOTHING, related_name='rutas_destino')

    def __str__(self) -> str:
        return f"Ruta -> {self.nombre}"


class Viaje(models.Model):
    llegada = models.DateTimeField("hora de llegada")
    salida = models.DateTimeField("hora de salida")
    flota = models.ForeignKey(Flota, on_delete=models.DO_NOTHING)
    ruta = models.ForeignKey(Ruta, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return f"Viaje : {self.flota} , Ruta : {self.ruta}"

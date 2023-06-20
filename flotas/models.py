from django.db import models


class Marca(models.Model):
    fabricante = models.CharField(max_length=100)
    modelo = models.CharField(max_length=200)
    tipo = models.CharField(max_length=100)
    anio = models.IntegerField()

    def __str__(self) -> str:
        return f"Marca : {self.modelo}"


class Flota(models.Model):
    placa = models.CharField(max_length=20)
    capacidad = models.IntegerField(default=0)
    marca = models.ForeignKey(Marca, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return f"Flota {self.placa}, marca {self.marca}"


class Asiento(models.Model):
    numero = models.IntegerField()
    flota = models.ForeignKey(Flota, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return f"Asiento : {self.flota.placa}, nro : {self.numero}"


class Disenio(models.Model):
    distribucion = models.JSONField()
    flota = models.ForeignKey(Flota, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return f"{self.distribucion}"

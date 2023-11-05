from django.contrib import admin
from .models import Asiento, Flota, Marca, Disenio

admin.site.register(Marca)
admin.site.register(Flota)
admin.site.register(Asiento)
admin.site.register(Disenio)
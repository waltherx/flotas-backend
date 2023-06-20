from django.contrib import admin
from .models import Ruta, Viaje, Ciudad


admin.site.register(Ciudad)
admin.site.register(Viaje)
admin.site.register(Ruta)

from django.urls import include, path
from rest_framework import routers

from flotas import views

router = routers.DefaultRouter()
router.register("flotas", views.FlotaView)
router.register("marcas", views.MarcaView)
router.register("asientos", views.AsientoView)
router.register("disenios", views.DisenioView)

urlpatterns = [
    path("/", include(router.urls)),
]
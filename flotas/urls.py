from django.urls import include, path
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from flotas import views

router = routers.DefaultRouter()
router.register("flota", views.FlotaView)
router.register("marca", views.MarcaView)
router.register("asiento", views.AsientoView)
router.register("disenio", views.DisenioView)


urlpatterns = [
    path("v1/api/", include(router.urls)),
    path("docs/", include_docs_urls(title="Flotas API")),
]

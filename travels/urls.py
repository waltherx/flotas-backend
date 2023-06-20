from django.urls import include, path
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from travels import views

router = routers.DefaultRouter()
router.register("ciudad", views.CiudadView)
router.register("ruta", views.RutaView)
router.register("viaje", views.ViajeView)


urlpatterns = [
    path("v1/api/", include(router.urls)),
    path("docs/", include_docs_urls(title="Rutas API")),
]

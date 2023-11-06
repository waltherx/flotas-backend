from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path
from rest_framework import permissions
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="transporte API",
        default_version="v0.1",
        description="Aqui nada mas",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="mddx@gg.cc"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/transporte", include("transporte.urls")),
    path("api/itinerario", include("itinerario.urls")),
    path("api/auth", include("auth.urls")),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path("graphql", csrf_exempt(GraphQLView.as_view(graphiql=True))),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

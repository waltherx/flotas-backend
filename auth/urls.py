from django.urls import path, include
from auth import views
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls

router = DefaultRouter()

router.register(r"api", views.UserView)

urlpatterns = [
    path("/", include(router.urls)),
]

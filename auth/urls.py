from django.urls import path, include
from auth import views
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path("/login", views.UserViewSet.as_view({'get': 'users'}), name="users"),
]

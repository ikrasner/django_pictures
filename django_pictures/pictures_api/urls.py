from django.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import ImagesViewSet

v1_router = DefaultRouter()
v1_router.register("image", ImagesViewSet)

urlpatterns = [
    path("v1/", include(v1_router.urls)),
]

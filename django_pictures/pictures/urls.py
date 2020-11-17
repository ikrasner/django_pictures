from django.urls import path

from . import views


urlpatterns = [
    path("", views.image_view, name="image_view"),
    path("<int:image_pk>/remove/", views.image_remove, name="image_remove"),
    path("upload/", views.image_upload, name="image_upload"),
]

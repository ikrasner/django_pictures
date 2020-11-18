from django.shortcuts import redirect
from django.shortcuts import render

from .forms import PictureUpload
from .models import Image


def image_remove(request, image_pk):
    image = Image.objects.get(pk=image_pk)
    image.delete()
    return redirect("image_view")


def image_upload(request):
    images = request.FILES.getlist("picture_upload")
    for img in images:
        Image(image=img).save()
    return redirect("image_view")


def image_view(request):
    form = PictureUpload()
    uploaded_images = Image.objects.all()
    return render(request, "index.html", {"form": form, "images": uploaded_images})

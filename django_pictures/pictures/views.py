from django.core.paginator import Paginator
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
    # TODO add pagination
    form = PictureUpload()
    uploaded_images = Image.objects.all()

    paginator = Paginator(uploaded_images, 16)
    page_number = request.GET.get("page")
    page = paginator.get_page(page_number)
    # if request.method != 'POST':
    #     return render(
    #     request,
    #     "index.html", {"form": form, "images": page})
    return render(
        request, "index.html", {"form": form, "images": page, "paginator": paginator}
    )

from pictures.models import Image
from pictures_api.serializers import ImageSerializer
from rest_framework import mixins
from rest_framework import viewsets


class ImagesViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = ImageSerializer
    queryset = Image.objects.all()

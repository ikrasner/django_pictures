from pictures.models import Image
from rest_framework import serializers
from sorl.thumbnail import get_thumbnail


class ImageSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField("get_image_url")
    thumbnail_url = serializers.SerializerMethodField("get_thumbnail_url")
    height = serializers.SerializerMethodField("get_image_height")
    width = serializers.SerializerMethodField("get_image_width")
    size = serializers.SerializerMethodField("get_file_size")

    def get_image_height(self, instance):
        return instance.image.height

    def get_image_width(self, instance):
        return instance.image.width

    def get_image_url(self, instance):
        return instance.image.url

    def get_thumbnail_url(self, instance):
        return get_thumbnail(instance.image, "100x100", crop="center", upscale=True).url

    def get_file_size(self, instance):
        return instance.image.size

    class Meta:
        fields = ("id", "image_url", "thumbnail_url", "height", "width", "size")
        model = Image

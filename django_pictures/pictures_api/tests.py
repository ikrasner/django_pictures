from io import BytesIO

from django.core.files import File
from django.test import TestCase
from pictures import models
from pictures.models import Image
from PIL import Image as PILImage
from rest_framework.reverse import reverse
from rest_framework.test import APIClient


class TestImagesApi(TestCase):
    @classmethod
    def setUp(self):
        image_1_w = 10
        image_1_h = 15
        self.image_1 = models.Image(
            image=self.generate_image_file(name="image_1", size=(image_1_w, image_1_h)),
        )

        self.image_1.save()

        image_2_w = 44
        image_2_h = 14
        self.image_2 = models.Image(
            image=self.generate_image_file(name="image_2", size=(image_2_w, image_2_h)),
        )

        self.image_2.save()

    @staticmethod
    def generate_image_file(
        name="image.jpeg", ext="jpeg", size=(50, 50), color=(256, 0, 0)
    ):
        file_obj = BytesIO()
        image = PILImage.new("RGB", size=size, color=color)
        image.save(file_obj, ext)
        file_obj.seek(0)
        return File(file_obj, name=name)

    def test_get_image_by_id(self):
        client = APIClient()
        image_id = self.image_1.id
        response = client.get(reverse("image-detail", args=[image_id]), format="json")
        actual_image = response.json()
        assert actual_image["height"] == type(self).image_1.image.height
        assert actual_image["width"] == type(self).image_1.image.width
        assert actual_image["size"] == type(self).image_1.image.size

    def test_get_images_list(self):
        client = APIClient()
        response = client.get(reverse("image-list"), format="json")
        actual_image_list = response.json()
        assert len(actual_image_list) == Image.objects.count()

    def test_delete_image_by_id(self):
        client = APIClient()
        image_id = self.image_1.pk

        assert Image.objects.filter(pk=image_id).exists()
        client.delete(reverse("image-detail", args=[image_id]), format="json")
        assert not Image.objects.filter(pk=image_id).exists()

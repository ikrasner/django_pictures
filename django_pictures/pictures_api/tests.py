from io import BytesIO

from django.core.files import File
from django.test import TestCase
from pictures import models
from pictures.models import Image
from PIL import Image as PILImage
from rest_framework.reverse import reverse
from rest_framework.test import APIClient


class TestApi(TestCase):
    @classmethod
    def setUpClass(cls):
        super(TestApi, cls).setUpClass()
        cls.image_1_w = 10
        cls.image_1_h = 15
        cls.image_1 = models.Image(
            image=cls.generate_image_file(
                name="image_1", size=(cls.image_1_w, cls.image_1_h)
            ),
        )

        cls.image_1.save()

        cls.image_2_w = 10
        cls.image_2_h = 15
        cls.image_2 = models.Image(
            image=cls.generate_image_file(
                name="image_2", size=(cls.image_2_w, cls.image_2_h)
            ),
        )

        cls.image_2.save()

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
        image_id = 1
        response = client.get(reverse("image-detail", args=[image_id]), format="json")
        actual_image = response.json()
        assert actual_image["height"] == type(self).image_1_h
        assert actual_image["width"] == type(self).image_1_w

    def test_get_images_list(self):
        client = APIClient()
        response = client.get(reverse("image-list"), format="json")
        actual_image_list = response.json()
        assert len(actual_image_list) == Image.objects.count()

    def test_delete_image_by_id(self):
        ...
        # client = APIClient()
        # response = client.get(reverse("image-remove"), format="json")
        # actual_image_list = response.json()
        # print(actual_image_list)
        # assert len(actual_image_list) == Image.objects.count()

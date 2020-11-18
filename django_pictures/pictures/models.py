from django.db import models
from django.dispatch import receiver
from sorl.thumbnail import delete
from sorl.thumbnail import ImageField


class Image(models.Model):
    image = ImageField(upload_to="pictures/", blank=True, null=True)


@receiver(models.signals.post_delete, sender=Image)
def delete_file(sender, instance: Image, *args, **kwargs):
    delete(instance.image, delete_file=True)

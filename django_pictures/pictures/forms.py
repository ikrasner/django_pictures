from django.forms import ClearableFileInput
from django.forms import Form
from django.forms import ImageField


class PictureUpload(Form):
    picture_upload = ImageField(
        label="Select pictures", widget=ClearableFileInput(attrs={"multiple": True})
    )

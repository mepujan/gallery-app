from django.forms import ModelForm
from .models import Gallery


class GalleryForm(ModelForm):
    class Meta:
        model = Gallery
        fields = ("title", "image")

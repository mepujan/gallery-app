from django.db import models
from django.core.validators import FileExtensionValidator


class Gallery(models.Model):
    title = models.CharField(max_length=20, blank=True)
    image = models.ImageField(upload_to='images', validators=[
                              FileExtensionValidator(['png', 'jpg', 'jpeg'])])

    def __str__(self) -> str:
        return str(self.pk)

    class Meta:
        verbose_name_plural = "Galleries"

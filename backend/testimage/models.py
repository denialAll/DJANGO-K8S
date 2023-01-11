from django.db import models

# Create your models here.

class Image(models.Model):

    image = models.ImageField(upload_to="display_picture", blank=True)
    name = models.CharField(max_length=156, default="John Doe")
from distutils.command.upload import upload
from unicodedata import category
from django.db import models

# Create your models here.
class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    image = models.ImageField(upload_to="image/", null=True)

    def __str__(self):
        return self.name

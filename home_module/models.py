from pyexpat import model
from turtle import title
from django.db import models

# Create your models here.

class Wallpaper(models.Model):
    title = models.CharField(max_length=30)
    sub_title = models.CharField(max_length=35, null=True)
    image = models.ImageField(upload_to='wallpapers')

    def __str__(self):
        return self.title

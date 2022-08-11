from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    email_activation_code = models.CharField(max_length=70, verbose_name="Activate code")
    is_active = models.BooleanField(verbose_name='Active', default=False)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.get_username()
from django.db import models

# Create your models here.

class Contact(models.Model):
    subject = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    email = models.EmailField()
    message = models.TextField()
    created_date = models.DateField(auto_now_add=True, null=True)

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return self.subject
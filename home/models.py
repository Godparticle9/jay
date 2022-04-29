import email
from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    address=models.CharField(max_length=30)
    phone=models.CharField(max_length=30)
    city=models.CharField(max_length=30)

    def __str__(self):
        return self.name +"-"+self.email
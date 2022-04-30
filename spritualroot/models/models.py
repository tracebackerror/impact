from django.db import models

# Create your models here.
class ContactForm(models.Model):
    name = models.CharField(max_length=50)
    email =models.EmailField(max_length=70)
    phone = models.CharField(max_length=10)
    comments = models.CharField(max_length=200)
from django.db import models

# Create your models here.

class BioData(models.Model):
    name = models.CharField(max_length=200)
    email_address = models.EmailField()


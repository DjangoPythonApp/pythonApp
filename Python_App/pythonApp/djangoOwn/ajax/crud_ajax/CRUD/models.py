from django.db import models

# Create your models here.
class User(models.Model):
    name:str = models.CharField(max_length=200)
    email:str = models.EmailField()
    password:str = models.CharField()

    
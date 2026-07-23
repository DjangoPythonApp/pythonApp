from django.db import models

# Create your models here.
class GeneralModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField()
    age = models.IntegerField()

    def __str__(self):
        return self.name
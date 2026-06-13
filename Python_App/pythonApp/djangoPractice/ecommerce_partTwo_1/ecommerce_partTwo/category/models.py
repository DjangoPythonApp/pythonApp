from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    number = models.IntegerField()
    selected_quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.name
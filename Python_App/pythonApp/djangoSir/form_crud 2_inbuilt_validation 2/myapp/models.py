from django.db import models
from django.core.validators import RegexValidator, MinValueValidator

class Product(models.Model):

    name = models.CharField(
        max_length=100,
        validators=[
            RegexValidator(
                regex=r'^[A-Za-z ]+$',
                message='Name can contain only letters and spaces.'
            )
        ]
    )

    price = models.FloatField(
        validators=[
            MinValueValidator(
                0.01,
                message='Price must be greater than 0.'
            )
        ]
    )

    description = models.TextField(
        validators=[
            RegexValidator(
                regex=r'^[A-Za-z0-9 ,.!?-]+$',
                message='Description contains invalid characters.'
            )
        ]
    )

    def __str__(self):
        return self.name
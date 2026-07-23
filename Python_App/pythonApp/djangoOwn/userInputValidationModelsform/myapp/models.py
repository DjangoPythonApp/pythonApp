from django.db import models
from django.core.validators import MinValueValidator, RegexValidator

class Product(models.Model):
    name = models.CharField(max_length=100,
            validators=[
                RegexValidator(
                    regex=r'^[A-Za-z ]+$',
                    message='Name must contain only letters and spaces.',
                )
            ])




    price = models.FloatField(
       validators=[
            MinValueValidator(0.01, 
                message='Price must be greater than zero.')
        ]
    )


    description = models.TextField(
        max_length=200,
        validators=[
            RegexValidator(
                regex=r'^[A-Za-z0-9 .,!?]+$',
                message='Description can only contain letters, numbers, and basic punctuation.'
            )
        ]
    )

    def __str__(self):
        return self.name

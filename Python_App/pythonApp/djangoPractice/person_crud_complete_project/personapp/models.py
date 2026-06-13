from django.db import models

class Person(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    address=models.TextField()
    course_enrolled=models.CharField(max_length=100)
    image=models.ImageField(upload_to='persons/')

    def __str__(self):
        return self.name

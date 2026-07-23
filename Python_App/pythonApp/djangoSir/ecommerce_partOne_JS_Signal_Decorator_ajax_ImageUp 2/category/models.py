from django.db import models
from django.utils.timezone import localtime

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="category/", blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.description} - {self.image}"
    


class AuditLog(models.Model):
    action = models.CharField(max_length=50)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        local_time = localtime(self.created_at)
        formatted_time = local_time.strftime("%d-%m-%Y %I:%M %p")
        return f"{self.action} - {formatted_time}"
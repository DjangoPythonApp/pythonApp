from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Category, AuditLog


# A signal allows Django to notify another function when an event occurs.
# pre_save, post_save, pre_delete, post_delete

# CREATE + UPDATE
@receiver(post_save, sender=Category)
def category_saved(sender, instance, created, **kwargs):
    if created:
        AuditLog.objects.create(
            action="CREATE",
            message=f"Category '{instance.name}' created"
        )
    else:
        AuditLog.objects.create(
            action="UPDATE",
            message=f"Category '{instance.name}' updated"
        )


# DELETE
@receiver(post_delete, sender=Category)
def category_deleted(sender, instance, **kwargs):
    AuditLog.objects.create(
        action="DELETE",
        message=f"Category '{instance.name}' deleted"
    )
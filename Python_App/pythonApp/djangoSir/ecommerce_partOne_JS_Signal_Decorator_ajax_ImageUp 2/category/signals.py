from django.db.models.signals import pre_save, post_save, post_delete
from django.dispatch import receiver
from .models import Category, AuditLog
import os


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



@receiver(pre_save, sender=Category)
def delete_old_image(sender, instance, **kwargs):
    if not instance.pk:
        return

    try:
        old_instance = Category.objects.get(pk=instance.pk)
    except Category.DoesNotExist:
        return

    old_image = old_instance.image
    new_image = instance.image

    if old_image and old_image != new_image:
        if os.path.isfile(old_image.path):
            os.remove(old_image.path)


@receiver(post_delete, sender=Category)
def delete_category_image(sender, instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)
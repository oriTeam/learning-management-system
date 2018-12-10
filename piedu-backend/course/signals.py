from django.db.models.signals import post_save, post_delete, pre_delete, pre_save
from django.dispatch import receiver
from .models import Class

@receiver([post_save, ], sender = Class)
def update_name_code(sender, instance, **kwargs):
    instance.update_name_and_code()
    # pass
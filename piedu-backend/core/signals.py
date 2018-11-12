from django.db.models.signals import post_save, post_delete, pre_delete, pre_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission

User = get_user_model()

# from django.conf import settings
# User = settings.AUTH_USER_MODEL

@receiver([post_save, ], sender=User)
def update_role_from_attr(sender, instance, **kwargs):
    instance.update_user_role()

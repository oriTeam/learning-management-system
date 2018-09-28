from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _


class User(AbstractUser):
    code = models.CharField(max_length=15, unique=True, null=True, verbose_name=_('Code'))
    avatar = models.ImageField(null=True, blank=True, verbose_name=_('Avatar'))
    phone_number = models.CharField(max_length=20, null=True, blank=True, verbose_name=_('Phone Number'))
    unit = models.TextField(blank=True, null=True)
    role = models.CharField(max_length=2)



# Create your models here.

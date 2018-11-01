from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _


class User(AbstractUser):
    code = models.CharField(max_length=15, unique=True, null=True, verbose_name=_('Code'))
    avatar = models.ImageField(null=True, blank=True, verbose_name=_('Avatar'))
    phone_number = models.CharField(max_length=20, null=True, blank=True, verbose_name=_('Phone Number'))
    gender = models.BooleanField(null=True, verbose_name=_('Gender'))
    unit = models.CharField(max_length=20,blank=True, null=True, verbose_name=_('Unit'))
    role = models.CharField(max_length=2, verbose_name=_("User's role"))
    # 0. Student account
    # 1. Lecturer account
    # 2. Admin account

    class Meta:
        db_table = 'user'
        ordering = ['id']
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        user = ''
        if self.role == '0':
            user = 'Student'
        elif self.role == '1':
            user = 'Lecturer'
        elif self.role == '2':
            user = 'Admin'
        return "{}: {}".format(user, self.username)
    def parse_data(self):
        data={
        "id" : self.id,
        "code" : self.code,
        "avatar" : self.avatar,
        "phone_number" : self.phone_number,
        "gender" : self.phone_number,
        "unit" : self.unit,
        "role" : self.role
        }
        return data
    def is_Admin(self):
        return True if self.role == '2' else False
    def is_Student(self):
        return True if self.role == '0' else False
    def is_Lecturer(self):
        return True if self.role =='1' else False
# Create your models here.

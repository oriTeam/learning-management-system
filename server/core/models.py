from django.db import models, connection
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _
from django.contrib.auth.models import Group, Permission
# from guardian.shortcuts import assign_perm

class User(AbstractUser):
    code = models.CharField(max_length=15, unique=True, null=True, verbose_name=_('Code'))
    avatar = models.ImageField(null=True, blank=True, verbose_name=_('Avatar'))
    phone_number = models.CharField(max_length=20, null=True, blank=True, verbose_name=_('Phone Number'))
    gender = models.BooleanField(default=True, verbose_name=_('Gender'))
    unit = models.CharField(max_length=20, blank=True, null=True, verbose_name=_('Unit'))
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, related_name='group')
    # groups = models.ManyToManyField(Group, related_name='groups')

    class Meta:
        db_table = 'user'
        ordering = ['id']
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        user_group = ''
        if 'student' in self.group.name:
            user = 'Student'
        elif 'lecturer' in self.group.name:
            user = 'Lecturer'
        elif 'admin' in self.group.name:
            user = 'Admin'
        return "{}: {}".format(user, self.username)

    def parse_data(self):
        data = {
            "id": self.id,
            "code": self.code,
            # "avatar" : self.avatar,
            "phone_number": self.phone_number,
            "gender": self.phone_number,
            "unit": self.unit,
            "group": self.group.name
        }
        return data

    def is_admin(self):
        return True if 'admin' in self.group.name else False

    def is_student(self):
        return True if 'student' in self.group.name else False

    def is_lecturer(self):
        return True if 'lecturer' in self.group.name else False

    def update_user_role(self):
        if self.is_admin():
            if not self.is_superuser:
                self.is_staff = True
                self.is_superuser = True
                self.save()

        elif self.is_lecturer():
            if not self.is_staff or self.is_superuser:
                self.is_staff = True
                self.is_superuser = False
                self.save()

        elif self.is_student():
            if self.is_staff or self.is_superuser:
                self.is_staff = False
                self.is_superuser = False
                self.save()


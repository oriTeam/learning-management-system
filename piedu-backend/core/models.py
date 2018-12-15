from django.db import models, connection
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _
from django.contrib.auth.models import Group, Permission
# from guardian.shortcuts import assign_perm
from django.conf import settings
import os

GENDER_CHOICES = (
    (_('Male'), _('Male')),
    (_('Female'), _('Female')),
    (_('Other'), _('Other'))
)

class User(AbstractUser):
    code = models.CharField(max_length=15, unique=True, null=True, verbose_name=_('Code'))
    avatar = models.ImageField(null=True, blank=True, verbose_name=_('Avatar'))
    phone_number = models.CharField(max_length=20, null=True, blank=True, verbose_name=_('Phone Number'))
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, null=True, blank=True, verbose_name=_('Gender'))
    unit = models.CharField(max_length=20, blank=True, null=True, verbose_name=_('Unit'))
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, related_name='users_set')
    birthday = models.DateField(null=True, blank=True, verbose_name=_('Birthday'))
    address = models.TextField(null=True, blank=True, verbose_name=_('Address'))
    # groups = models.ManyToManyField(Group, related_name='groups')

    class Meta:
        db_table = 'user'
        ordering = ['id']
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        user_group = ''
        if self.is_student():
            user_group = 'Student'
        elif self.is_lecturer():
            user_group = 'Lecturer'
        elif self.is_admin():
            user_group = 'Admin'
        return "{}: {}".format(user_group, self.username)

    def save(self):
        # Save the provided password in hashed format
        user = super(User, self)
        user.set_password(self.password)
        user.save()
        return user
        
    def get_name_and_id(self):
        data ={
            "id" : self.id,
            "name" : self.fullname(),
        }
        return data
    def parse_data(self):
        avatar_url = settings.MEDIA_URL + "908312.png"
        # print(self.avatar == "")
        if self.avatar != "" :
            avatar_url= self.avatar 

        data = {
            "id": self.id,
            "code": self.code,
            "avatar" : avatar_url,
            "phone_number": self.phone_number,
            "gender": self.phone_number,
            "unit": self.unit,
            "group": self.group.name,
            "fullname": self.fullname(),
        }
        return data

    def parse_basic_info(self):
        avatar_url = settings.MEDIA_URL + "908312.png"
        if self.avatar != "":
            avatar_url = self.avatar
        data = {
            "id": self.id,
            "code": self.code,
            "fullname": self.fullname(),
            "username": self.username,
            "gender": self.gender,
            "phone_number": self.phone_number,
            "personal_page": '',
        }
        return data

    def fullname(self):
        if self.last_name and self.first_name:
            return self.last_name + " " + self.first_name
        else:
            return "Chưa cập nhật"

    def is_admin(self):
        return True if 'admin' in str(self.group) else False

    def is_student(self):
        return True if 'student' in str(self.group) else False

    def is_lecturer(self):
        return True if 'lecturer' in str(self.group) else False

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


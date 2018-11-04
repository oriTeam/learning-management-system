from django.db import models, connection
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _
from django.contrib.auth.models import Group, Permission


class User(AbstractUser):
    code = models.CharField(max_length=15, unique=True, null=True, verbose_name=_('Code'))
    avatar = models.ImageField(null=True, blank=True, verbose_name=_('Avatar'))
    phone_number = models.CharField(max_length=20, null=True, blank=True, verbose_name=_('Phone Number'))
    gender = models.BooleanField(default=True, verbose_name=_('Gender'))
    unit = models.CharField(max_length=20, blank=True, null=True, verbose_name=_('Unit'))
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
        data = {
            "id": self.id,
            "code": self.code,
            # "avatar" : self.avatar,
            "phone_number": self.phone_number,
            "gender": self.phone_number,
            "unit": self.unit,
            "role": self.role
        }
        return data

    def is_Admin(self):
        return True if self.role == '2' else False

    def is_Student(self):
        return True if self.role == '0' else False

    def is_Lecturer(self):
        return True if self.role == '1' else False

    def update_user_role(self):
        if self.role == '2':
            if not self.is_superuser:
                user = User.objects.get(pk=self.id)
                user.is_staff = True
                user.is_admin = True
                user.is_superuser = True
                user.save()
        else:
            if self.is_superuser:
                user = User.objects.get(pk=self.id)
                user.is_staff = False
                user.is_admin = False
                user.is_superuser = False
                user.save()
    def remove_user_from_group(self):
        for group in Group.objects.all():
            group.user_set.remove(self)

    def update_user_group(self):
        user_group = 'user_groups'
        with connection.cursor() as cursor:
            cursor.execute('INSERT INTO {0} SET user_id = {1}, group_id = {2}'.format(
                user_group, self.id, '3')
            )





        # self.groups.clear()
        # group = Group.objects.get(pk=3)
        # group.user_set.add(self)



        # group = Group.objects.get(pk=3)
        # group.user_set.add(User.objects.get(pk=self.id))
        # group.save()
        # # if self.role == '2':
        #     user = User.objects.get(pk=self.id)
        #     group = Group.objects.get(name='admin_group')
        #     group.user_set.add(user)
        #             # user.save()
        #     print(user.groups.all())
        #             # group.save()
        #
        # elif self.role == '1':
        #     try:
        #         group = Group.objects.get(name='lecturer_group')
        #     except Group.DoesNotExist:
        #         print("Lectuter Group Does Not Exist")
        #     else:
        #         if self not in group.user_set.all():
        #             self.groups.clear()
        #             group.user_set.add(self)
        # elif self.role == '0':
        #     try:
        #         group = Group.objects.get(name='student_group')
        #     except Group.DoesNotExist:
        #         print("Student Group Does Not Exist")
        #     else:
        #         if self not in group.user_set.all():
        #             self.groups.clear()
        #             group.user_set.add(self)
        # # pass




# Create your models here.

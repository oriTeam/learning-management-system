from django.conf import settings
from django.db import models
from django.utils.translation import gettext as _

from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from core.models import User


class CourseCategory(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Course Category"))

    class Meta:
        db_table = 'course_category'
        ordering = ['id']
        verbose_name = _("Catergory")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return "Category : {}".format(self.name)

    def parse_data(self):
        data = {
            "id": self.id,
            "name": self.name
        }
        return data


class Subject(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Subject"))
    avatar = models.ImageField(null=True, verbose_name=_('Avatar'))
    code = models.CharField(max_length=25, null=True, verbose_name=_("Code"))
    category = models.ForeignKey(CourseCategory, null=True, on_delete=models.CASCADE, related_name='subjects_set',
                                 verbose_name=_("Course Category"))

    class Meta:
        db_table = 'subject'
        ordering = ['id']
        verbose_name = _("Subject")
        verbose_name_plural = _("Subjects")

    def __str__(self):
        return "Subject : {}".format(self.name)


class Class(models.Model):
    code = models.CharField(max_length=25, blank=True, null=True, verbose_name=_("Code"))
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name=_("Name"))
    description = models.TextField(null=True, verbose_name=_('Description'))
    time_start = models.DateTimeField(verbose_name=_("Start time"))
    time_end = models.DateTimeField(verbose_name=_("End time"))
    subject = models.ForeignKey(Subject, null=True, on_delete=models.CASCADE,related_name='classes_set', verbose_name=_('Subject'))
    students = models.ManyToManyField('core.User', through='ClassStudent')
    class Meta:
        db_table = 'class'
        ordering = ["id"]
        verbose_name = _("Class")
        verbose_name_plural = _("Classes")

    def __str__(self):
        return "Class : {0}".format(self.name)

    def update_name_and_code(self):
        code = str(self.subject.code) + " " + str(self.id)
        name = str(self.subject.name) + " " + code
        if self.name != name or self.code != code:
            self.code = code
            self.name = name
            self.save()


    def parse_basic_info(self):
        data = {
            "id": self.id,
            "code": self.code,
            "name": self.name,
            "subject": self.subject.name,
            "students": len(self.students_set.all())
        }
        return data
    def parse_info_and_username(self):
        data = self.parse_basic_info()
        
        data.update({
            "avatar_path": self.subject.avatar.url,
            "description": self.description
        })

        class_lecturer = ClassLecturer.objects.filter(own_class__id = self.id).select_related("lecturer")
        username = [item.lecturer.fullname() for item in class_lecturer]
        data.update({
            "lecturer" : username
        })
        return data

    def parse_basic_info_for_class(self):
        data = {
            "id": self.id,
            "code": self.code,
            "name": self.name,
            "subject": self.subject.name,
            "students": [item.parse_data() for item in students],
        }
        return data
    def parse_info(self):
        data = self.parse_basic_info()
        data.update({
            "avatar_path": self.subject.avatar.url,
            "description": self.description
        })
        return data

    def parse_full_info(self):
        data = self.parse_info()
        data.update({
            "time_start": str(self.time_start),
            "time_end": str(self.time_end),
            "description": self.description
        })
        return data
    

class Schedule(models.Model):
    own_class = models.ForeignKey(Class, on_delete=models.CASCADE, null=True, related_name='schedules_set',
                                  verbose_name=_('Class'))
    day_of_week = models.CharField(max_length=3, verbose_name=_('Day Of Week'))
    session_start = models.CharField(max_length=3, null=True, verbose_name=_('Start Session'))
    session_end = models.CharField(max_length=3, null=True, verbose_name=_('End Session'))

    class Meta:
        db_table = 'schedule'
        ordering = ['id']
        verbose_name = _('Schedule')
        verbose_name_plural = _("Schedules")

    def __str__(self):
        return "Class: {} | Start Session: {} | End Session: {}".format(self.own_class.name, self.session_start, self.session_end)

    def parse_data(self):
        data = {
            "id": self.id,
            "class_id": self.own_class.id,
            "day_of_week": self.day_of_week,
            "session_start":self.session_start,
            "session_end" : self.session_end, 
        }
        return data


class ClassLecturer(models.Model):
    own_class = models.ForeignKey(Class, on_delete=models.CASCADE, null=True, related_name='lecturers_set', verbose_name=_("Class"))
    lecturer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True,
                                 related_name='own_classes_set', verbose_name=_("Lecturer"))

    class Meta:
        db_table = 'class_lecturer'
        ordering = ["id"]
        verbose_name = _("Class - Lecturer")
        verbose_name_plural = _("Classes - Lecturers")

    def __str__(self):
        return "Class : {} | Lecturer : {}".format(self.own_class.name, self.lecturer.username)


class ClassStudent(models.Model):
    own_class = models.ForeignKey(Class, on_delete=models.CASCADE,null=True, related_name='students_set', verbose_name=_("Class"))
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True, related_name='classes_set', verbose_name=_("Student"))

    class Meta:
        db_table = 'class_student'
        ordering = ["id"]
        verbose_name = _("Class - Student")
        verbose_name_plural = _("Classes - Students")

    def __str__(self):
        return "Class : {} | User : {}".format(self.own_class.name, self.student.username)


class EnrollRequest(models.Model):
    own_class = models.ForeignKey(Class, on_delete=models.CASCADE, null=True, related_name='wait_students_set', verbose_name=_('Class'))
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True,
                                related_name='wait_classes_set', verbose_name=_('Student'))

    class Meta:
        db_table = 'enroll_request'
        ordering = ['id']
        verbose_name = _('Enroll Request')
        verbose_name_plural = _('Enroll Requests')

    def __str__(self):
        return "Class: {} | Student: {}".format(self.own_class.name, self.own_class.name)

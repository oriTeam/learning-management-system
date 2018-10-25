from django.db import models
from django.utils.translation import gettext as _
from django.conf import settings

# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Course's Name"))

    class Meta:
        db_table = 'courses'
        ordering = ['id']
        verbose_name = _("Course")
        verbose_name_plural = _("Courses")

    def __str__(self):
        return "courses_name : {}".format(self.course_name)


class Class(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Class's Name"))
    description = models.TextField(null=True, verbose_name=_('Description'))
    time_start = models.DateTimeField(verbose_name=_("Class's start time"))
    time_end = models.DateTimeField(verbose_name=_("Class's end time"))
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name=_("Course"))

    class Meta:
        db_table = 'class'
        ordering = ["id"]
        verbose_name = _("Class")
        verbose_name_plural = _("Classes")

    def __str__(self):
        return "Course : {} | Class : {}".format(self.course_id.name, self.name)


class Schedule(models.Model):
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE, verbose_name=_('Class'))
    day_of_week = models.CharField(max_length=5, verbose_name=_('Day Of Week'))
    encoded_session = models.CharField(max_length=20, verbose_name=_('Encoded Session'))

    class Meta:
        db_table = 'schedule'
        ordering = ['id']
        verbose_name = _('Schedule')

    def __str__(self):
        return "Class: {} | Encoded Session: {}".format(self.class_id.name, self.encoded_session)


class ClassLecturer(models.Model):
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE, verbose_name=_("Class"))
    lecturer_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_("User"))

    class Meta:
        db_table = 'class_lecturer'
        ordering = ["id"]
        verbose_name = _("Class - Lecturer")
        verbose_name_plural = _("Classes - Lecturers")

    def __str__(self):
        return "Class : {} | Lecturer : {}".format(self.class_id.name, self.lecturer_id.username)


class ClassStudent(models.Model):
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE, verbose_name=_("Class"))
    student_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_("Student"))

    class Meta:
        db_table = 'class_student'
        ordering = ["id"]
        verbose_name = _("Class - Student")
        verbose_name_plural = _("Classes - Students")

    def __str__(self):
        return "Class : {} | User : {}".format(self.class_id.name, self.user_id.code)


class EnrollRequest(models.Model):
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE, verbose_name=_('Class'))
    student_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_('Student'))

    class Meta:
        db_table = 'enroll_request'
        ordering = ['id']
        verbose_name = _('Enroll Request')
        verbose_name_plural = _('Enroll Requests')

    def __str__(self):
        return "Class: {} | Student: {}".format(self.class_id.name, self.class_id.name)

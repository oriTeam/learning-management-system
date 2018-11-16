from django.db import models
from django.utils.translation import gettext as _
from django.conf import settings


# Create your models here.

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
    category = models.ForeignKey(CourseCategory, null=True, on_delete=models.CASCADE,related_name='classes_set', \
                                                                                                   verbose_name=_("Course Category"))
    class Meta:
        db_table = 'subject'
        ordering = ['id']
        verbose_name = _("Subject")
        verbose_name_plural = _("Subjects")

    def __str__(self):
        return "Subject : {}".format(self.name)


class Class(models.Model):
    code = models.CharField(max_length=25, unique=True, default='', verbose_name=_("Class's Code"))
    name = models.CharField(max_length=255, verbose_name=_("Class's Name"))
    description = models.TextField(null=True, verbose_name=_('Description'))
    time_start = models.DateTimeField(verbose_name=_("Class's start time"))
    time_end = models.DateTimeField(verbose_name=_("Class's end time"))
    subject = models.ForeignKey(Subject, null=True, on_delete=models.CASCADE,related_name='classes_set', verbose_name=_('Subject'))

    class Meta:
        db_table = 'class'
        ordering = ["id"]
        verbose_name = _("Class")
        verbose_name_plural = _("Classes")

    def __str__(self):
        return "Class : {0} {1}".format(self.name, self.code)

    def parse_basic_info(self):
        data = {
            "id": self.id,
            "code": self.code,
            "name": self.name,
            "subject": self.subject.name,
            "students": len(self.students_set.all())
        }
        return data

    def parse_info(self):
        data = self.parse_basic_info()
        data.update({
            # "cat": self.subject.name,
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
    own_class = models.ForeignKey(Class, on_delete=models.CASCADE, null=True, related_name='schedules_set', verbose_name=_('Class'))
    day_of_week = models.CharField(max_length=5, verbose_name=_('Day Of Week'))
    # encoded_session = models.CharField(max_length=20, verbose_name=_('Encoded Session'))
    session_start = models.CharField(max_length=2, null=True, verbose_name=_('Session Start'))
    session_end = models.CharField(max_length=2, null=True, verbose_name=_('Session End'))

    class Meta:
        db_table = 'schedule'
        ordering = ['id']
        verbose_name = _('Schedule')

    def __str__(self):
        return "Class: {} | Encoded Session: {}".format(self.class_id.name, self.encoded_session)

    def parse_data(self):
        data = {
            "id": self.id,
            "class_id": self.class_id,
            "day_of_week": self.day_of_week,
            "encoded_session": self.encoded_session
        }
        return data


class ClassLecturer(models.Model):
    own_class = models.ForeignKey(Class, on_delete=models.CASCADE, null=True, related_name='lecturers_set', verbose_name=_("Class"))
    lecturer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, related_name='own_classes_set', verbose_name=_("User"))

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
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, related_name='wait_classes_set', verbose_name=_('Student'))

    class Meta:
        db_table = 'enroll_request'
        ordering = ['id']
        verbose_name = _('Enroll Request')
        verbose_name_plural = _('Enroll Requests')

    def __str__(self):
        return "Class: {} | Student: {}".format(self.own_class.name, self.own_class.name)

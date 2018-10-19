from django.db import models
from django.utils.translation import gettext as _
from django.conf import settings
from syllabus.models import Syllabus,Material

# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length= 255,verbose_name= _("Course's Name"))

    class Meta :
        db_table = 'courses'
        ordering = ['id']
        verbose_name = _("Course")
        verbose_name_plural = _("Courses")
    def __str__(self):
        return "courses_name : {}".format(self.course_name)

class Class(models.Model):
    name = models.CharField(max_length =255, verbose_name=_("Class's Name"))
    time_start = models.DateTimeField(verbose_name = _("Class's start time"))
    time_end = models.DateTimeField(verbose_name= _("Class's end time"))
    course_id = models.ForeignKey(Course,on_delete = models.CASCADE , verbose_name=_("Course"))
    class Meta:
        db_table = 'class'
        ordering =["id"]
        verbose_name = _("Class")
        verbose_name_plural = _("Classes")
    def __str__(self):
        return "Course : {} | Class : {}".format(self.course_id.name,self.name)


class ClassUser(models.Model):
    class_id = models.ForeignKey(Class,on_delete = models.CASCADE , verbose_name=_("Class"))
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, verbose_name=_("User"))

    class Meta:
        db_table = 'class_user'
        ordering = ["id"]
        verbose_name = _("Class - User")
        verbose_name_plural = _("Classes - Users")
    def __str__(self):
        return "Class : {} | User : {}".format(self.class_id.name,self.user_id.code)
class ClassSyllabus(models.Model):
    class_id = models.ForeignKey(Class,on_delete= models.CASCADE,verbose_name = _("Class"))
    syllabus_id = models.ForeignKey(Syllabus,on_delete = models.CASCADE,verbose_name= _("Syllabus"))

    class Meta:
        db_table = 'class_syllabus'
        ordering = ["id"]
        verbose_name = _("Class - Syllasbus")
        verbose_name_plural = _("Classes - Syllabus")
    def __str__(self):
        return "Class : {} | Syllabus : {}".format(self.class_id.name,self.syllabus_id.name)



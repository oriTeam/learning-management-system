from django.db import models
from django.utils.translation import gettext as _
from django.conf import settings
from document.models import Document
from faculty.models import Faculty
from semester.models import Semester

# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=80, verbose_name=_("Course's Title"))
    course_code = models.CharField(max_length=20, verbose_name=_("Course's Code"))
    avatar = models.ImageField(verbose_name=_("Course's Avatar"))
    description = models.TextField(null=True, verbose_name=_("Course's Description"))
    course_type = models.CharField(max_length=10, verbose_name=_("Course's Type"))
    # 0. Opened for everyone.
    # 1. Student enroll and teacher accepted
    # 2. Teacher add only.

    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, null=True, verbose_name=_("Faculty"))
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, null=True, verbose_name=_("Semester"))

    # author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='course_set', verbose_name=_('Author'))

    class Meta:
        db_table = 'course'
        ordering = ["id"]
        verbose_name = _("Course")
        verbose_name_plural = _("Courses")

    def __str__(self):
        return self.title



class CourseLecturer(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name=_("Course"))
    lecturer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_("Lecturer"))

    class Meta:
        db_table = 'course_lecturer'
        ordering = ['id']
        verbose_name = _("Course - Lecturer")
        verbose_name_plural = _("Courses - Lecturers")

    def __str__(self):
        return "Course: {} | Lecturer: {}".format(self.course.title, self.lecturer.code)

class CourseStudent(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name=_("Course"))
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_("Student"))

    class Meta:
        db_table = 'course_student'
        ordering = ['id']
        verbose_name = _("Course - Student")
        verbose_name_plural = _("Courses - Students")

    def __str__(self):
        return "Course: {} | Student: {}".format(self.course.title, self.student.code)


class CourseDocument(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name=_("Course"))
    document = models.ForeignKey(Document, on_delete=models.CASCADE, verbose_name=_("Document"))

    class Meta:
        db_table = 'course_document'
        ordering = ['id']
        verbose_name = _("Course - Document")
        verbose_name_plural = _("Courses - Documents")

    def __str__(self):
        return "Course: {} | Document: {}".format(self.course.title, self.document.name)

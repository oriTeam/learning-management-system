from django.contrib import admin

from .models import Course, CourseDocument, CourseLecturer, CourseStudent

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'course_code', 'course_type')

@admin.register(CourseStudent)
class CourseStudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'course', 'student')

@admin.register(CourseDocument)
class CourseDocumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'course', 'document')

@admin.register(CourseLecturer)
class CourseLecturerAdmin(admin.ModelAdmin):
    list_display = ('id', 'course', 'lecturer')
# Register your models here.

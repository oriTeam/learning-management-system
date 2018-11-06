from django.contrib import admin
from .models import CourseCategory, Class, ClassLecturer, ClassStudent, EnrollRequest, Schedule, Subject

# Register your models here.

@admin.register(CourseCategory)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Subject)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'avatar')

@admin.register(Class)
class ClasAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'time_start', 'time_end')

@admin.register(ClassStudent)
class ClassStudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'class_id', 'student_id')

@admin.register(ClassLecturer)
class ClassLecturerAdmin(admin.ModelAdmin):
    list_display = ('id', 'class_id', 'lecturer_id')

@admin.register(EnrollRequest)
class EnrollRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'class_id', 'student_id')

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('id', 'class_id', 'day_of_week', 'encoded_session')

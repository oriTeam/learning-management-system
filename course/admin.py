from django.contrib import admin
from .models import Course, Class, ClassLecturer, ClassStudent, EnrollRequest, Schedule

# Register your models here.

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Class)
class ClasAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'course_id', 'time_start', 'time_end')

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

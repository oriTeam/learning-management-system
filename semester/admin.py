from django.contrib import admin

from .models import Semester

@admin.register(Semester)
class SemesterAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'semester_code')
# Register your models here.

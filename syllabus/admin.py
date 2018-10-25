from django.contrib import admin
from .models import Syllabus, Material, SyllabusTemplate, ClassSyllabus
# Register your models here.

@admin.register(Syllabus)
class SyllsbusAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'class_id', 'week', 'content')

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'material_type', 'syllabus_id', 'file')

@admin.register(ClassSyllabus)
class ClassSyllabusAdmin(admin.ModelAdmin):
    list_display = ('id', 'class_id', 'syllabus_id')

@admin.register(SyllabusTemplate)
class SyllabusTemplateAdmin(admin.ModelAdmin):
    list_display = ('id', 'class_id')


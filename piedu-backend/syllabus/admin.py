from django.contrib import admin
from .models import Syllabus, Material, SyllabusTemplate


@admin.register(Syllabus)
class SyllsbusAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'own_class', 'week', 'content')


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'material_type', 'syllabus', 'file')


@admin.register(SyllabusTemplate)
class SyllabusTemplateAdmin(admin.ModelAdmin):
    list_display = ('id', 'own_class')

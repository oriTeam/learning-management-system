from django.contrib import admin

from .models import Document

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type', 'content')
# Register your models here.

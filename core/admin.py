from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# admin.site.register(User, UserAdmin)
# Register your models here.
from .forms import UserForm

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
	form = UserForm
	list_display = ()


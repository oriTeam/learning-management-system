from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

from django.contrib.auth.admin import UserAdmin
# admin.site.register(CustomUserModel, UserAdmin)
# from guardian.admin import GuardedModelAdmin


# admin.site.register(User, UserAdmin)
# Register your models here.
from .forms import UserForm

@admin.register(User)
# class UserAdmin(GuardedModelAdmin):
class UserAdmin(admin.ModelAdmin):
	form = UserForm
	list_display = ('id', 'username', 'code', 'unit', 'group')

# class AuthorAdmin(GuardedModelAdmin):
#     pass
#
# admin.site.register(, AuthorAdmin)
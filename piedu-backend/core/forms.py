from django import forms
from django.core.exceptions import ValidationError

from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = []

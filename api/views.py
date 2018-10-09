from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import login as auth, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


# Create your views here.
def login(request):
    form = AuthenticationForm(None, request.POST)
    if request.method == "POST" and request.user.is_anonymous:
        if form.is_valid():
            auth(request, form.get_user())
            return JsonResponse({'success' : True})
    errors = form.errors.get_json_data()
    return JsonResponse(errors)

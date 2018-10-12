from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'userpage/user-page.html')
def login(request):
    return render(request, 'mainpage/login.html')
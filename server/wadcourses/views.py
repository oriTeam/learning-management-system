from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'mainpage/index.html')
def login(request):
    return render(request, 'mainpage/login.html')
def my_course(request):
    return render(request, 'mainpage/my-course.html')
def all_course(request):
    return render(request, 'mainpage/all-course.html')
def contact(request):
    return render(request, 'mainpage/contact.html')
def help(request):
    return render(request, 'mainpage/help.html')
def user(request):
    return render(request,'userpage/user-page.html')
def inner_course(request):
    return render(request,'mainpage/inner-course.html')
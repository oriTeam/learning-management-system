from course.models import CourseCategory
from course.models import Subject
from django.shortcuts import render

# Create your views here.
def index(request):
    categories = CourseCategory.objects.all()
    return render(request, 'mainpage/index.html', {'categories': categories})

def login(request):
    return render(request, 'mainpage/login.html')

def my_course(request):
    if request.user.is_authenticated:
        return render(request, 'mainpage/my-class.html')
    else:
        return render(request, 'mainpage/login.html')

def all_course(request):
    if request.user.is_authenticated:
        subjects = Subject.objects.all()
        return render(request, 'mainpage/all-class.html', {'subjects': subjects})
    else:
        return render(request, 'mainpage/login.html')

def contact(request):

    return render(request, 'mainpage/contact.html')

def help(request):
    return render(request, 'mainpage/help.html')

def user(request):
    if request.user.is_authenticated:
        return render(request,'userpage/user-page.html')
    else:
        return render(request, 'mainpage/login.html')

def inner_course(request):
    if request.user.is_authenticated:
        return render(request, 'mainpage/inner-class.html')
    else:
        return render(request, 'mainpage/login.html')

# FOR TEST
def new_class(request):
    return render(request, 'mainpage/new-class.html')

def app(request):
    return render(request, 'basepage/mainbase.html')
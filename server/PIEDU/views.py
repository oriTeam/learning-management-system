from django.shortcuts import render
from course.models import CourseCategory
from course.models import Subject
# Create your views here.
def index(request):
    categories = CourseCategory.objects.all()
    print(categories)
    return render(request, 'mainpage/index.html', {'categories': categories})
def login(request):
    return render(request, 'mainpage/login.html')
def my_course(request):
    return render(request, 'mainpage/my-class.html')
def all_course(request):
    subjects = Subject.objects.all()
    print(subjects)
    return render(request, 'mainpage/all-class.html', {'subjects': subjects})
def contact(request):
    return render(request, 'mainpage/contact.html')
def help(request):
    return render(request, 'mainpage/help.html')
def user(request):
    return render(request,'userpage/user-page.html')
def inner_course(request):
    return render(request, 'mainpage/inner-class.html')
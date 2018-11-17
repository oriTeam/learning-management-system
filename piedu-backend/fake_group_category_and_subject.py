import sys
import os
import django
from random import randint, choice
import datetime
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "PIEDU.settings")
django.setup()
User = get_user_model()
from course.models import CourseCategory, Subject, Class, Schedule, ClassLecturer, ClassStudent, EnrollRequest
from syllabus.models import Syllabus, SyllabusTemplate
from django.contrib.auth.models import Group, Permission

groups = ['admin_group', 'lecturer_group', 'student_group']

categories = ['CNTT', 'Ngoại Ngữ', 'Toán', 'Chính trị', 'Vật lý', 'Điện tử viễn thông', 'Cơ học kỹ thuật & tự động hóa',
              'Vật lý kỹ thuật & CN Nano']

subjects = [{"name": "Quản lý dự án phần mềm "},
            {"name": "Xử lý ảnh "},
            {"name": "Thị giác máy "},
            {"name": "Cơ sở dữ liệu "},
            {"name": "Nguyên lý hệ điều hành "},
            {"name": "An toàn và an ninh mạng "},
            {"name": "Xác suất thống kê "},
            {"name": "Cấu trúc dữ liệu và giải thuật "},
            {"name": "An ninh phần mềm "},
            {"name": "Đồ họa máy tính "},
            {"name": "Lập trình hướng đối tượng "},
            {"name": "Xác suất thống kê "},
            {"name": "Tin học cơ sở 4 "},
            {"name": "Kiến trúc máy tính "},
            {"name": "Hệ quản trị CSDL "},
            {"name": "Các vấn đề hiện đại CNTT "},
            {"name": "Phân tích thiết kế HTTT  "},
            {"name": "Lập trình mạng "},
            {"name": "Mạng không dây "},
            {"name": "Tương tác người máy "},
            {"name": "Phát triển ứng dụng web "},
            {"name": "Phân tích và thiết kế thuật toán "},
            {"name": "Thiết kế giao diện người dùng "},
            {"name": "Các chủ đề hiện đại của HTTT "},
            {"name": "Phân tích đánh giá hiệu năng hệ thống máy tính "},
            {"name": "Thực hành hệ điều hành mạng "},
            {"name": "Các thiết bị mạng và môi trường truyền "},
            ]

for group in groups:
    try:
        name = group
        checker = Group.objects.filter(name=name)
        if len(checker) == 0:
            print('Creating  {0}.'.format(name))
            new_group = Group.objects.create(name=name)
            new_group.save()
            print('Group {0} successfully created.'.format(name))
        else:
            print('Group {0} has existed'.format(name))
    except:
        print('There was a problem creating the Course Category: {0}.  Error: {1}.' \
          .format(name, sys.exc_info()[1]))

print('========================================')

for category in categories:
    try:
        name = category
        checker = CourseCategory.objects.filter(name = name)
        if len(checker) == 0:
            print('Creating  {0}.'.format(category))
            course_category = CourseCategory.objects.create(name=name)
            course_category.save()
            print('Course Category {0} successfully created.'.format(category))
        else:
            print('Course Category {0} has existed'.format(category))
    except:
        print('There was a problem creating the Course Category: {0}.  Error: {1}.' \
            .format(category, sys.exc_info()[1]))

print('=======================================')

def check_subject_in_category(subject, category):
    return True if len(category.subjects_set.filter(name=subject)) != 0 else False

for subject in subjects:
    try:
        category = choice(CourseCategory.objects.all())
        if not check_subject_in_category(subject['name'], category):
            name = subject['name']
            print('Creating  {0}.'.format(name))
            new_subject = Subject.objects.create(name=name, category=category)
            new_subject.save()
            print('Subject {0} successfully created.'.format(name))
        else:
            print('Subject {0} has existed'.format(name))
    except:
        print('There was a problem creating the Subject: {0}.  Error: {1}.' \
          .format(category, sys.exc_info()[1]))
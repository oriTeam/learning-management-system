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
from course.models import Course, Class, Schedule, ClassLecturer, ClassStudent, EnrollRequest
from syllabus.models import Syllabus, SyllabusTemplate

courses = ['CNTT', 'Ngoại Ngữ', 'Toán', 'Chính trị', 'Vật lý', 'Điện tử viễn thông', 'Cơ học kỹ thuật & tự động hóa', 'Vật lý kỹ thuật & CN Nano']

classes = [{"name": "Quản lý dự án phần mềm ", "id": "INT3111 21"}, {"name": "Xử lý ảnh ", "id": "INT3404"},
           {"name": "Thị giác máy ", "id": "INT3412"}, {"name": "Cơ sở dữ liệu ", "id": "INT2207 1"},
           {"name": "Nguyên lý hệ điều hành ", "id": "INT 2206 1"},
           {"name": "An toàn và an ninh mạng ", "id": "INT3307 1"},
           {"name": "Xác suất thống kê ", "id": "MAT1101_4 5 21"},
           {"name": "Cấu trúc dữ liệu và giải thuật ", "id": "INT2203 10"},
           {"name": "An ninh phần mềm ", "id": "INT6170"}, {"name": "Đồ họa máy tính ", "id": "INT3403 3"},
           {"name": "Lập trình hướng đối tượng ", "id": "INT2204_6"}, {"name": "Xác suất thống kê ", "id": "MAT1101_2"},
           {"name": "Xác suất thống kê ", "id": "MAT1101_1"}, {"name": "Tin học cơ sở 4 ", "id": "INT1006_1"},
           {"name": "Kiến trúc máy tính ", "id": "INT2205 22"}, {"name": "Kiến trúc máy tính ", "id": "INT2205 10"},
           {"name": "Hệ quản trị CSDL ", "id": "INT 3202 1"}, {"name": "Các vấn đề hiện đại CNTT ", "id": "INT3507 3"},
           {"name": "Hệ quản trị CSDL ", "id": "INT3202 5"},
           {"name": "Phân tích thiết kế HTTT ", "id": "INT2020 2"},
           {"name": "Phân tích thiết kế HTTT  ", "id": "INT2020 1 "}, {"name": "Lập trình mạng ", "id": "INT3304 1"},
           {"name": "Mạng không dây ", "id": "INT3303 1"}, {"name": "Kiến trúc máy tính ", "id": "INT2205 6"},
           {"name": "Xác suất thống kê ", "id": "MAT1101_22"},
           {"name": "Cấu trúc dữ liệu và giải thuật ", "id": "INT2203_23"},
           {"name": "Tương tác người máy ", "id": "INT6164"}, {"name": "Lập trình hướng đối tượng ", "id": "INT2204_7"},
           {"name": "Cấu trúc dữ liệu và giải thuật ", "id": "INT2203"},
           {"name": "Quản lý dự án phần mềm  ", "id": "INT3111_1"},
           {"name": "Phát triển ứng dụng web ", "id": "INT3306_2"},
           {"name": "Cấu trúc dữ liệu và giải thuật ", "id": "INT2203_8"},
           {"name": "Cấu trúc dữ liệu và giải thuật ", "id": "INT2203_6"},
           {"name": "Cấu trúc dữ liệu và giải thuật ", "id": "INT2203_3"},
           {"name": "Lập trình hướng đối tượng ", "id": "INT2204 "},
           {"name": "Lập trình hướng đối tượng ", "id": "INT2204_22"},
           {"name": "Lập trình hướng đối tượng ", "id": "INT2204_1_23"},
           {"name": "Các vấn đề hiện đại CNTT ", "id": "INT2207_7"},
           {"name": "Cấu trúc dữ liệu và giải thuật  ", "id": "INT2203_4 "},
           {"name": "Lập trình hướng đối tượng ", "id": "INT2204_1"},
           {"name": "Lập trình hướng đối tượng ", "id": "INT2204_2 & INT2204_4"},
           {"name": "Phân tích và thiết kế thuật toán ", "id": "INT3513_22"},
           {"name": "Phân tích và thiết kế thuật toán ", "id": "INT3513_21"},
           {"name": "Tin học cơ sở 4 ", "id": "INT1006_8"}, {"name": "Tin học cơ sở 4 ", "id": "INT1006_6"},
           {"name": "Tin học cơ sở 4 ", "id": "INT1006_5"}, {"name": "Tin học cơ sở 4 ", "id": "INT1006_2"},
           {"name": "Cấu trúc dữ liệu và giải thuật ", "id": "INT2203_21"},
           {"name": "Quản lý dự án phần mềm ", "id": "INT3111_20"},
           {"name": "Thiết kế giao diện người dùng ", "id": "INT3115"}, {"name": "Tin học cơ sở 4 ", "id": "INT1006_3"},
           {"name": "Các chủ đề hiện đại của HTTT ", "id": "INT3220"},
           {"name": "Phân tích đánh giá hiệu năng hệ thống máy tính ", "id": "INT3216"},
           {"name": "Thực hành hệ điều hành mạng ", "id": "INT3301"},
           {"name": "Các thiết bị mạng và môi trường truyền ", "id": "INT3318"},
           {"name": "Cấu trúc dữ liệu và giải thuật ", "id": "INT2203_2"},
           {"name": "Cấu trúc dữ liệu và giải thuật ", "id": "INT2203_7"},
           {"name": "Kiến trúc máy tính ", "id": "INT2205_9"}, {"name": "Kiến trúc máy tính ", "id": "INT2205_3"},
           {"name": "Kiến trúc máy tính ", "id": "INT2205 11"}, {"name": "Đồ họa máy tính ", "id": "INT3403 1"}]

start = ['2018-01-02', '2018-02-01', '2018-03-14', '2018-04-01', '2018-02-15', '2018-01-11', '2018-04-01',
         '2018-01-31', ]

end = ['2019-01-02', '2019-02-01', '2019-03-14', '2019-04-01', '2019-02-15', '2019-01-11', '2019-04-01', '2019-01-31', ]

while True:
    course_id = input("Course can fake: ")
    if course_id.isdigit():
        course = int(course_id)
        # class_num = int(class_num)
        break

for course in courses:
    try:
        name = course
        check_course = Course.objects.filter(name = course)
        if len(check_course) == 0:
            print('Creating  {0}.'.format(course))
            course = Course.objects.create(name=course)
            course.save()
            print('User {0} successfully created.'.format(course))
        else:
            print('Course {0} has existed'.format(course))
    except:
        print('There was a problem creating the user: {0}.  Error: {1}.' \
            .format(course, sys.exc_info()[1]))

def get_random_student():
    students_id = []
    students_queryset = User.objects.filter(group__name__contains='student')

    for student in students_queryset:
        students_id.append(student.id)
    random_student_id = choice(students_id)
    return random_student_id

def get_random_lecturer():
    lecturers_id = []
    lecturer_queryset = User.objects.filter(group__name__contains='lecturer')

    for lecturer in lecturer_queryset:
        lecturers_id.append(lecturer.id)
    random_lecturer_id = choice(lecturers_id)
    return random_lecturer_id

for _class in classes:
    try:
        start_date = choice(start)
        end_date = choice(end)
        course = Course.objects.get(pk=course_id)
        class_ = Class.objects.create(code=_class['id'], name=_class['name'], description="", time_start=start_date,
                                      time_end=end_date, course_id=course)
        class_.save()
        print('Class {0} successfully created in {1}'.format(_class['name'], course))

        for i in range(0, 2):
            lecturer_id = get_random_lecturer();
            lecturer = User.objects.get(pk=lecturer_id)
            class_lecturer = ClassLecturer.objects.filter(lecturer_id=lecturer)
            if len(class_lecturer) == 0:
                class_lecturer_ = ClassLecturer.objects.create(class_id=class_, lecturer_id=lecturer)
                class_lecturer_.save()
            print('Class {0} | Lecturer {1} successfully created'.format(_class['name'], lecturer.username))

        for i in range(0, 40):
            student_id = get_random_student();
            student = User.objects.get(pk=student_id)
            class_student = ClassStudent.objects.filter(student_id = student_id)
            if len(class_student) == 0:
                class_student_ = ClassStudent.objects.create(class_id = class_, student_id = student)
                class_student_.save()
            print('Class {0} | Student {1} successfully created'.format(_class['name'], student.username))

        for i in range(0, 15):
            title = "Tuần " + str(i + 1)
            content = "Nột dung tuần " + str(i + 1)
            f_class = class_
            week = i + 1
            syllabus = Syllabus.objects.create(title=title, content=content, class_id=f_class, week=week)
            syllabus.save()
            print('Class {0} | Syllabus {1} successfully created'.format(_class['name'], title))

        for i in range(0, 10):
            student_id = get_random_student();
            student = User.objects.get(pk=student_id)
            enroll_request = EnrollRequest.objects.filter(student_id = student_id)
            class_student = ClassStudent.objects.filter(student_id=student_id)

            if len(enroll_request) == 0:
                enroll_request_ = EnrollRequest.objects.create(class_id = class_, student_id = student)
                enroll_request_.save()
                print('Enroll Request: Class {0} | Student {1} successfully created'.format(_class['name'], student.username))

    except:
        print('There was a problem creating the class in course: {0}.  Error: {1}.' \
              .format(course, sys.exc_info()[1]))

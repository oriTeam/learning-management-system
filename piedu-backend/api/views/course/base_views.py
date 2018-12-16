import datetime

import dateutil.parser
from api.check import ClassSession
from api.functions import get_token_from_request, get_user_from_token
from api.permission import IsMyOwnOrAdmin, IsAuthenticated
from core.serializers import UserSerializerView
from course.models import CourseCategory, Class, Schedule, ClassLecturer, ClassStudent, EnrollRequest, Subject
from course.serializers import CourseCategorySerializer, SubjectSerializer, ClassSerializer
from django.db.models import Q
from django.http import JsonResponse
from django.utils import timezone
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response


@api_view(['GET'])
@permission_classes((permissions.IsAuthenticatedOrReadOnly,))
def test(request):
    id = request.GET['id']

    print(id)
    return JsonResponse({"data": id})


# """ course_category """

@api_view(['GET'])
@permission_classes((permissions.IsAuthenticatedOrReadOnly,))
def course_category_list_view(request):
    list_course_categorys = CourseCategory.objects.all()
    if len(list_course_categorys) == 0:
        data = {
            "success": False,
            "errors": "CourseCategorys are invalid"
        }
        return Response(data)
    else:

        serializer = CourseCategorySerializer(list_course_categorys, many=True)
        return Response(serializer.data)


@api_view(['GET'])
@permission_classes((permissions.IsAuthenticatedOrReadOnly,))
def course_category_detail(request, id):
    try:
        course_category = CourseCategory.objects.get(pk=id)

    except CourseCategory.DoesNotExist:
        data = {
            "success": False,
            "errors": "CourseCategory is invalid"
        }
        return Response(data)
    else:
        serializer = CourseCategorySerializer(course_category)
        return Response(serializer.data)


@api_view(['GET'])
@permission_classes((permissions.IsAuthenticatedOrReadOnly,))
def get_subject(request, id):
    all_subject = Subject.objects.filter(category__id=id)
    if len(all_subject) == 0:
        data = {
            "success": False,
            "errors": "CourseCategory is invalid"
        }
        return Response(data)
    else:

        serializer = SubjectSerializer(all_subject, many=True)
        return Response(serializer.data)


# """ subject """

@api_view(['GET'])
@permission_classes((permissions.IsAuthenticatedOrReadOnly,))
def subject_list_view(request):
    list_subjects = Subject.objects.all()
    if len(list_subjects) == 0:
        data = {
            "success": False,
            "errors": "Subjects are invalid"
        }
        return Response(data)
    else:

        serializer = SubjectSerializer(list_subjects, many=True)
        return Response(serializer.data)


@api_view(['GET'])
@permission_classes((permissions.IsAuthenticatedOrReadOnly,))
def subject_detail(request, id):
    try:
        subject = Subject.objects.get(pk=id)
    except Subject.DoesNotExist:

        data = {
            "success": False,
            "errors": "Subject is invalid"
        }
        return Response(data)
    else:
        serializer = SubjectSerializer(subject)

        return Response(serializer.data)


@api_view(['GET'])
@permission_classes((permissions.IsAuthenticatedOrReadOnly,))
def get_class(request, id):
    all_class = Class.objects.filter(subject__id=id)
    if len(all_class) == 0:
        data = {
            "success": False,
            "errors": "Subject is invalid"
        }
        return Response(data)
    else:
        serializer = ClassSerializer(all_class, many=True)
        return Response(serializer.data)


# """  class """


@api_view(['GET'])
@permission_classes((permissions.IsAuthenticatedOrReadOnly,))
def class_list_view(request):
    list_class = Class.objects.all()
    if len(list_class) == 0:
        data = {
            "success": False,
            "errors": "Class are invalid"
        }
        return Response(data)
    else:

        serializer = ClassSerializer(list_class, many=True)
        return Response(serializer.data)


@api_view(['GET'])
@permission_classes((permissions.IsAuthenticatedOrReadOnly,))
def class_detail(request, id):
    try:
        class_detail = Class.objects.prefetch_related('students').get(pk=id)
    except Class.DoesNotExist:
        data = {
            "success": False,
            "errors": "Class is invalid"
        }
        return Response(data)
    else:
        result = []
        # rs = class_detail.parse_basic_info_for_class()
        result.append(class_detail.parse_full_info())
        class_student = ClassStudent.objects.filter(own_class__id=id).select_related('student')
        students = [item.student.parse_basic_info() for item in class_student]
        class_lecturer = ClassLecturer.objects.filter(own_class__id=id)    
        result.append({"lecturer" :[item.lecturer.get_name_and_id() for item in class_lecturer]})
        result.append({"student" : students})
        schedules = Schedule.objects.filter(own_class__id =id)
        schedule = [item.parse_data() for item in schedules]
        result.append(schedule)
        
        # serializer = ClassSerializer(class_detail)
        return Response(result)
        # return Response(serializer.data)


@api_view(['GET'])
@permission_classes((IsMyOwnOrAdmin,))
def get_student(request):
    id = request.GET['class_id']
    class_students = ClassStudent.objects.select_related('student').filter(own_class__id=id)
    if len(class_students) == 0:
        data = {
            "success": False,
            "errors": "Class is invalid"
        }
        return Response(data)
    else:
        students = [class_student.student for class_student in class_students if class_student.student is not None]
        # serializer = ClassStudentSerializer(class_students,many=True)
        if len(students) == 0:
            data = {
                "success": False,
                "errors": "Class is invalid"
            }
            return Response(data)
        else:
            serializer = UserSerializerView(students, many=True)
            return Response(serializer.data)


@api_view(['GET'])
# @permission_classes((IsLecturer,IsMyOwnOrAdmin,))
@permission_classes((permissions.IsAuthenticatedOrReadOnly,))
def get_enroll_request(request, id):
    enroll_requests = EnrollRequest.objects.select_related('student').filter(own_class__id=id)
    if len(enroll_requests) == 0:
        data = {
            "success": False,
            "errors": "Class is invalid"
        }
        return Response(data)
    else:
        students = [enroll_request.student for enroll_request in enroll_requests if enroll_request.student is not None]
        if len(students) == 0:
            data = {
                "success": False,
                "errors": "Class is invalid"
            }
            return Response(data)
        else:
            student_list = [item.parse_basic_info() for item in students]
            return Response({"success": True, "students": student_list})
            # serializer = UserSerializerView(students,many = True)
            # return Response(serializer.data)


@api_view(["GET", "POST"])
@permission_classes((permissions.IsAuthenticated,))
def get_current_class(request):
    # id = request.user.id
    # try :
    #     user = User.objects.get(pk = id)
    # except User.DoesNotExist :
    #     data = {
    #             "success" : False,
    #             "errors" : "User is invalid"
    #     }
    #     return Response(data)
    # else :
    token = get_token_from_request(request)
    user = get_user_from_token(token)
    
    if user is not None:
        now = datetime.datetime.now(tz=timezone.utc)
        if user.is_lecturer():
            class_lecturers = ClassLecturer.objects.filter(lecturer__id=user.id).select_related('own_class').filter(
                own_class__time_start__lte=now, own_class__time_end__gte=now)
            if len(class_lecturers) == 0:
                data = {
                    "empty": True,
                    "message": "ClassList is empty"
                }
                return Response(data)
            else:
                all_class = [item.own_class for item in class_lecturers if item.own_class is not None]
                if len(all_class) == 0:
                    data = {
                        "success": False,
                        "errors": "Class is invalid"
                    }
                    return Response(data)
                else:
                    data = []
                    for class_queryset in all_class:
                        data.append(class_queryset.parse_info_and_username())
                    return Response(data)
                    # serializers = ClassSerializer(all_class, many=True)
                    # return Response(serializers.data)

        elif user.is_student():
            class_students = ClassStudent.objects.filter(student__id=user.id).select_related('own_class').filter(
                own_class__time_start__lte=now, own_class__time_end__gte=now)
            if len(class_students) == 0:
                data = {
                    "empty": True,
                    "message": "ClassList is empty"
                }
                return Response(data)
            else:
                all_class = [item.own_class for item in class_students if item.own_class is not None]
                if len(all_class) == 0:
                    data = {
                        "success": False,
                        "errors": "Class is invalid"
                    }
                    return Response(data)
                else:
                    data = []
                    for class_queryset in all_class:
                        data.append(class_queryset.parse_info_and_username())
                    return Response(data)
                    # serializers = ClassSerializer(all_class, many=True)
                    # return Response(serializers.data)
        else:
            return Response({"admin": "User is admin"})
    else:
        return Response({"invalid": "User is invalid"})


# @api_view(['GET'])
# def get_enroll_request(request,id):
#     enroll_requests = EnrollRequest.objects.select_related('student').filter(own_class__id = id)
#     if len(enroll_requests) == 0 :
#         data = {
#                 "success" : False,
#                 "errors" : "Class is invalid"
#         }
#         return Response(data) 
#     else :
#         students =[enroll_request.student for enroll_request in enroll_requests if enroll_request.student is not None]          
#         if len(students) == 0 :
#             data = {
#                     "success" : False,
#                     "errors" : "Class is invalid"
#             }
#             return Response(data) 
#         else :
#             serializer = UserSerializerView(students,many = True)
#             return Response(serializer.data)

@api_view(["GET", "POST"])
@permission_classes((permissions.IsAuthenticated,))
# @permission_classes((permissions.IsAuthenticatedOrReadOnly,))
def get_past_class(request):
    # id = request.user.id
    # try :
    #     user = User.objects.get(pk = id)
    # except User.DoesNotExist :
    #     data = {
    #             "success" : False,
    #             "errors" : "User is invalid"
    #     }
    #     return Response(data)
    # else :
    token = get_token_from_request(request)
    user = get_user_from_token(token)
    if user is not None:
        now = datetime.datetime.now(tz=timezone.utc)
        if user.is_lecturer():
            class_lecturers = ClassLecturer.objects.filter(lecturer__id=user.id).select_related('own_class').filter(
                own_class__time_end__lte=now)
            if len(class_lecturers) == 0:
                data = {
                    "empty": True,
                    "message": "ClassList is empty"
                }
                return Response(data)
            else:
                all_class = [item.own_class for item in class_lecturers if item.own_class is not None]
                if len(all_class) == 0:
                    data = {
                        "success": False,
                        "errors": "Class is invalid"
                    }
                    return Response(data)
                else:
                    data = []
                    for class_queryset in all_class:
                        data.append(class_queryset.parse_info_and_username())
                    return Response(data)
                    # serializers = ClassSerializer(all_class, many=True)
                    # return Response(serializers.data)
        elif user.is_student():
            class_students = ClassStudent.objects.filter(student__id=user.id).select_related('own_class').filter(
                own_class__time_end__lte=now)
            if len(class_students) == 0:
                data = {
                    "empty": True,
                    "message": "ClassList is empty"
                }
                return Response(data)
            else:
                all_class = [item.own_class for item in class_students if item.own_class is not None]

                if len(all_class) == 0:
                    data = {
                        "success": False,
                        "errors": "Class is invalid"
                    }
                    return Response(data)
                else:
                    data = []
                    for class_queryset in all_class:
                        data.append(class_queryset.parse_info_and_username())
                    return Response(data)

                    # serializers = ClassSerializer(all_class, many=True)
                    # return Response(serializers.data)
        else:
            return Response({"admin": "User is admin"})
    else:
        return Response({"invalid": "User is invalid"})


@api_view(["GET", "POST"])
@permission_classes((permissions.IsAuthenticated,))
def get_future_class(request):
    # id = request.user.id
    # try :
    #     user = User.objects.get(pk = id)
    # except User.DoesNotExist :
    #     data = {
    #             "success" : False,
    #             "errors" : "User is invalid"
    #     }
    #     return Response(data)
    # else :
    token = get_token_from_request(request)
    user = get_user_from_token(token)
    if user is not None:
        now = datetime.datetime.now(tz=timezone.utc)
        if user.is_lecturer():

            class_lecturers = ClassLecturer.objects.filter(lecturer__id=user.id).select_related('own_class').filter(
                own_class__time_start__gte=now)
            if len(class_lecturers) == 0:
                data = {
                    "empty": True,
                    "message": "ClassList is empty"
                }
                return Response(data)
            else:
                all_class = [item.own_class for item in class_lecturers if item.own_class is not None]
                if len(all_class) == 0:
                    data = {
                        "success": False,
                        "errors": "Class is invalid"
                    }
                    return Response(data)
                else:
                    data = []
                    for class_queryset in all_class:
                        data.append(class_queryset.parse_info_and_username())
                    return Response(data)
                    # serializers = ClassSerializer(all_class, many=True)
                    # return Response(serializers.data)
        elif user.is_student():
            class_students = ClassStudent.objects.filter(student__id=user.id).select_related('own_class').filter(
                own_class__time_start__gte=now)
            if len(class_students) == 0:
                data = {
                    "empty": True,
                    "message": "ClassList is empty"
                }
                return Response(data)
            else:
                all_class = [item.own_class for item in class_students if item.own_class is not None]
                if len(all_class) == 0:
                    data = {
                        "success": False,
                        "errors": "Class is invalid"
                    }
                    return Response(data)
                else:
                    data = []
                    for class_queryset in all_class:
                        data.append(class_queryset.parse_info_and_username())
                    return Response(data)

                    # serializers = ClassSerializer(all_class, many=True)
                    # return Response(serializers.data)
        else:
            return Response({"admin": "User is admin"})
    else:
        return Response({"invalid": "User is invalid"})


@api_view(['GET'])
@permission_classes((permissions.IsAuthenticated,))
def get_schedule(request):
    # id = request.user.id
    # try :
    #     user = User.objects.get(pk = id)
    # except User.DoesNotExist :
    #        data = {
    #             "success" : False,
    #             "errors" : "User is invalid"
    #     }
    #     return Response(data)
    # else :
    token = get_token_from_request(request)
    user = get_user_from_token(token)
    if user is not None:
        now = datetime.datetime.now(tz=timezone.utc)
        all_class = []
        if user.is_lecturer():
            class_lecturers = ClassLecturer.objects.filter(lecturer__id=user.id).select_related('own_class').filter(
                own_class__time_start__lte=now, own_class__time_end__gte=now)
            if len(class_lecturers) == 0:
                data = {
                    "success": False,
                    "errors": "Class is invalid"
                }
                return Response(data)
            else:
                all_class = [item.own_class for item in class_lecturers if item.own_class is not None]
                if len(all_class) == 0:
                    data = {
                        "success": False,
                        "errors": "Class is invalid"
                    }
                    return Response(data)

        elif user.is_student():
            class_students = ClassStudent.objects.filter(student__id=user.id).select_related('own_class').filter(
                own_class__time_start__lte=now, own_class__time_end__gte=now)
            if len(class_students) == 0:
                data = {
                    "success": False,
                    "errors": "Class is invalid"
                }
                return Response(data)
            else:
                all_class = [item.own_class for item in class_students if item.own_class is not None]
                if len(all_class) == 0:
                    data = {
                        "success": False,
                        "errors": "Class is invalid"
                    }
                    return Response(data)

        schedules = []
        for item in all_class:
            rs = Schedule.objects.filter(own_class__id=item.id)
            schedules.append({item.code: [schedule.parse_data() for schedule in rs]})
        if len(schedules) == 0:
            data = {
                "success": False,
                "errors": "Schedules is invalid"
            }
            return Response(data)
        else:

            return JsonResponse({"data": schedules})
    else:
        return Response({"invalid": "User is invalid"})


@api_view(['POST', 'GET'])
@permission_classes((permissions.IsAuthenticated,))
# @permission_classes((permissions.IsAuthenticatedOrReadOnly,))
def check_validate(request):
    # print(json.loads(request.body.decode('utf-8')))

    time_start = dateutil.parser.parse(request.data.get('time_start'))
    time_end = dateutil.parser.parse(request.data.get('time_end'))
    session_start = request.data.get('session_start')
    session_end = request.data.get('session_end')
    day_of_week = request.data.get('day_of_week')
    subject = Subject.objects.get(pk=request.data.get('subject'))
    description = request.data.get('description')
    if time_start > time_end:
        data = {
            "success": False,
            "errors": "Time start cannot greater than time end!"
        }
        return Response(data)
    if session_start > session_end:
        data = {
            "success": False,
            "errors": "Session start cannot greater than session end!"
        }
        return Response(data)
    token = get_token_from_request(request)
    user = get_user_from_token(token)
    if user is not None:
        now = datetime.datetime.now(tz=timezone.utc)
        # comment  2 line after when read data from post method
        # time_end = now
        # time_start = now
        all_class = []
        if user.is_lecturer():
            # class_lecturers = ClassLecturer.objects.filter(lecturer__id= id).select_related('own_class').filter(own_class__time_start__lte= now,own_class__time_end__gte=now)
            class_lecturers = ClassLecturer.objects.filter(lecturer__id=user.id).select_related('own_class').exclude(
                Q(own_class__time_start__gte=time_end) | Q(own_class__time_end__lte=time_start))
            # if len(class_lecturers) == 0:
            #     data = {
            #         "success": False,
            #         "errors": "Class is invalid"
            #     }
            #     return Response(data)
            # else:
            all_class = [item.own_class for item in class_lecturers if item.own_class is not None]
                # if len(all_class) == 0:
                #     data = {
                #         "success": False,
                #         "errors": "Class is invalid"
                #     }
                #     return Response(data)

            schedules = []
            info_all_schedule = ClassSession()
            for item in all_class:
                rs = Schedule.objects.filter(own_class__id=item.id, day_of_week=day_of_week)

                for rs_item in rs:
                    info_all_schedule.add(int(rs_item.session_start), int(rs_item.session_end))
            if info_all_schedule.add(session_start, session_end) == False:
                data = {
                    "success": False,
                    "errors": "Session is coincided!"
                }
                return Response(data)
                # print(schedules)

            new_class = Class.objects.create(description=description, time_start=time_start, time_end=time_end,
                                             subject=subject)
            new_class.save()
            new_class_lecturer = ClassLecturer.objects.create(own_class=new_class, lecturer=user)
            new_class_lecturer.save()
            new_schedule = Schedule.objects.create(own_class=new_class, day_of_week=day_of_week, session_start=
                                                    session_start, session_end=session_end)
            new_schedule.save()



            data = {
                "success": True,
                "message": "Class" + new_class.name + "have been created successfully",
                "class_id": new_class.id
            }
            return Response(data)



        elif user.is_student():
            # data = {
            #             "success" : False,
            #             "errors" : "Access denied!"
            #         }
            # return Response(data)
            class_students = ClassStudent.objects.filter(student__id=user.id).select_related('own_class').exclude(
                Q(own_class__time_start__gte=time_end) | Q(own_class__time_end__lte=time_start))
            if len(class_students) == 0:
                data = {
                    "success": False,
                    "errors": "Class is invalid"
                }
                return Response(data)
            else:
                all_class = [item.own_class for item in class_students if item.own_class is not None]
                if len(all_class) == 0:
                    data = {
                        "success": False,
                        "errors": "Class is invalid"
                    }
                    return Response(data)

            schedules = []
            info_all_schedule = ClassSession()
            for item in all_class:
                rs = Schedule.objects.filter(own_class__id=item.id, day_of_week=day_of_week)

                for rs_item in rs:
                    info_all_schedule.add(int(rs_item.session_start), int(rs_item.session_end))
            if info_all_schedule.add(session_start, session_end) == False:
                data = {
                    "success": False,
                    "code": "coincided",
                    "errors": "Session is coincided!"
                }
                return Response(data)
                # print(schedules)

            data = {
                "success": True,
                "message": "You can enroll this class"
            }
            return Response(data)


# @api_view(['GET'])
# @permission_classes((permissions.IsAuthenticatedOrReadOnly,))
# def search(request):
#     print("a")
#     # value = 3

#     value = str(request.GET.get('value'))
#     print(value)
#     if value =="1" :
#         words = split_word(request.GET.get('search'))
#         rs = []
#         for word in words :
#             classes = Class.objects.filter(name = word)
#             for item in classes :
#                 rs.append(item.parse_full_info())
#         return JsonResponse({"data" : rs})
#     elif value == "2":
#         words = split_word(request.GET.get('search'))
#         rs = []
#         for word in words :
#             lecturers = User.objects.filter(username__contains = word)
#             for item in lecturers :
#                 if (str(item.group) == "lecturer_group"):
#                     rs.append(item.parse_data())
#         return JsonResponse({"data" : rs})
#     else:
#         words = split_word(request.GET.get('search'))
#         rs = []
#         for word in words :
#             print(word)
#             students = User.objects.filter(username__contains = word)
#             for item in students :
#                 if (str(item.group) == "student_group"):
#                     rs.append(item.parse_data())
#         return JsonResponse({"data" :rs})


@api_view(['GET'])
@permission_classes((permissions.IsAuthenticatedOrReadOnly,))
def get_status(request):
    class_id = request.GET.get('own_class')
    student = request.GET.get('student')
    class_student_querysets = ClassStudent.objects.filter(Q(own_class=class_id) & Q(student=student))
    enroll_request_querysets = EnrollRequest.objects.filter(Q(own_class=class_id) & Q(student=student))
    if len(class_student_querysets) == 0 and len(enroll_request_querysets) == 0:
        return JsonResponse({'code': 0, 'message': 'Not enrolled or waiting'})
    elif len(class_student_querysets) > 0:
        return JsonResponse({'code': 1, 'message': 'Enrolled'})
    elif len(enroll_request_querysets) > 0:
        return JsonResponse({'code': 2, 'message': 'Waiting'})

from course.models import CourseCategory, Class, Schedule, ClassLecturer, ClassStudent, EnrollRequest, Subject
from core.models import User
from django.http import JsonResponse
from api.functions import string_to_boolean
from api.base import BaseManageView
import datetime
from django.utils import timezone
import json
import pytz
from rest_framework.decorators import api_view
from rest_framework.response import Response
from course.serializers import CourseCategorySerializer,SubjectSerializer,ClassSerializer,ClassStudentSerializer
from core.serializers import UserSerializer 
from django.db.models import Q



@api_view(['GET'])
def test(request,id):
    data = request.GET
    id = data.get["id"]
    print(id)

# """ course_category """

@api_view(['GET'])
def course_category_list_view(request):
    list_course_categorys = CourseCategory.objects.all()
    if len(list_course_categorys) == 0 :
        data = {
                "success" : False,
                "errors" : "CourseCategorys are invalid"
        }
        return Response(data)
    else:
        
        serializer = CourseCategorySerializer(list_course_categorys,many = True)
        return Response(serializer.data)
@api_view(['GET'])
def course_category_detail(request,id):
    try:
        course_category = CourseCategory.objects.get(pk=id)
    except CourseCategory.DoesNotExist:
        data = {
                "success" : False,
                "errors" : "CourseCategory is invalid"
        }
        return Response(data)
    else:
        serializer = CourseCategorySerializer(course_category)
        return Response(serializer.data)

@api_view(['GET'])
def get_subject(request,id):
    all_subject = Subject.objects.filter(category__id =id)
    if len(all_subject) == 0 :
        data = {
                "success" : False,
                "errors" : "CourseCategory is invalid"
        }
        return Response(data) 
    else :
            
            serializer = SubjectSerializer(all_subject,many = True)
            return Response(serializer.data)


# """ subject """

@api_view(['GET'])
def subject_list_view(request):
    list_subjects = Subject.objects.all()
    if len(list_subjects) == 0 :
        data = {
                "success" : False,
                "errors" : "Subjects are invalid"
        }
        return Response(data)
    else:
        
        serializer = SubjectSerializer(list_subjects,many = True)
        return Response(serializer.data)

@api_view(['GET'])
def subject_detail(request,id):
    try:
        subject = Subject.objects.get(pk=id)
    except Subject.DoesNotExist:
        
        data = {
                "success" : False,
                "errors" : "Subject is invalid"
        }
        return Response(data)
    else:
        serializer = SubjectSerializer(subject)
        
        return Response(serializer.data)

@api_view(['GET'])
def get_class(request,id):
    all_class = Class.objects.filter(subject__id =id)
    if len(all_class) == 0 :
        data = {
                "success" : False,
                "errors" : "Subject is invalid"
        }
        return Response(data) 
    else :       
            serializer = ClassSerializer(all_class,many = True)
            return Response(serializer.data)



# """  class """

@api_view(['GET'])
def class_list_view(request):
    list_class = Class.objects.all()
    if len(list_class) == 0 :
        data = {
                "success" : False,
                "errors" : "Class are invalid"
        }
        return Response(data)
    else:
        
        serializer = ClassSerializer(list_class,many = True)
        return Response(serializer.data)
@api_view(['GET'])
def class_detail(request,id):
    try:
        class_detail = Class.objects.get(pk=id)
    except Class.DoesNotExist:
        
        data = {
                "success" : False,
                "errors" : "Class is invalid"
        }
        return Response(data)
    else:
        serializer = ClassSerializer(class_detail)
        
        return Response(serializer.data)

@api_view(['GET'])
def get_student(request,id):
    class_students = ClassStudent.objects.select_related('student').filter(own_class__id = id)
    if len(class_students) == 0 :
        data = {
                "success" : False,
                "errors" : "Class is invalid"
        }
        return Response(data) 
    else :
        students =[class_student.student for class_student in class_students if class_student.student is not None]        
        # serializer = ClassStudentSerializer(class_students,many=True)
        if len(students) == 0 :
            data = {
                    "success" : False,
                    "errors" : "Class is invalid"
            }
            return Response(data) 
        else :
            serializer = UserSerializer(students,many = True)
            return Response(serializer.data)

@api_view(['GET'])
def get_enroll_request(request,id):
    enroll_requests = EnrollRequest.objects.select_related('student').filter(own_class__id = id)
    if len(enroll_requests) == 0 :
        data = {
                "success" : False,
                "errors" : "Class is invalid"
        }
        return Response(data) 
    else :
        students =[enroll_request.student for enroll_request in enroll_requests if enroll_request.student is not None]          
        if len(students) == 0 :
            data = {
                    "success" : False,
                    "errors" : "Class is invalid"
            }
            return Response(data) 
        else :
            serializer = UserSerializer(students,many = True)
            return Response(serializer.data)

@api_view(["GET"])
def get_current_class(request,id):
    try :
        user = User.objects.get(pk = id)
    except User.DoesNotExist :
        data = {
                "success" : False,
                "errors" : "User is invalid"
        }
        return Response(data)
    else :
        now = datetime.datetime.now(tz = timezone.utc)
        print(user.is_student)
        if user.is_lecturer() :
            
            
            class_lecturers = ClassLecturer.objects.filter(lecturer__id= id).select_related('own_class').filter(own_class__time_start__lte= now,own_class__time_end__gte=now)
            if len(class_lecturers) == 0 :
                data = {
                    "success" : False,
                    "errors" : "Class is invalid"
                }
                return Response(data) 
            else :          
                all_class = [item.own_class for item in class_lecturers if item.own_class is not None]
                if len(all_class) == 0 :
                    data = {
                        "success" : False,
                        "errors" : "Class is invalid"
                    }
                    return Response(data) 
                else :
                    serializers = ClassSerializer(all_class,many = True)
                    return Response(serializers.data)
        elif user.is_student :
            
            class_students = ClassStudent.objects.filter(student__id= id).select_related('own_class').filter(own_class__time_start__lte= now,own_class__time_end__gte=now)
            if len(class_students) == 0 :
                data = {
                    "success" : False,
                    "errors" : "Class is invalid"
                }
                return Response(data) 
            else :          
                all_class = [item.own_class for item in class_students if item.own_class is not None]
                if len(all_class) == 0 :
                    data = {
                        "success" : False,
                        "errors" : "Class is invalid"
                    }
                    return Response(data) 
                else :
                    serializers = ClassSerializer(all_class,many = True)
                    return Response(serializers.data)
@api_view(['GET'])
def get_enroll_request(request,id):
    enroll_requests = EnrollRequest.objects.select_related('student').filter(own_class__id = id)
    if len(enroll_requests) == 0 :
        data = {
                "success" : False,
                "errors" : "Class is invalid"
        }
        return Response(data) 
    else :
        students =[enroll_request.student for enroll_request in enroll_requests if enroll_request.student is not None]          
        if len(students) == 0 :
            data = {
                    "success" : False,
                    "errors" : "Class is invalid"
            }
            return Response(data) 
        else :
            serializer = UserSerializer(students,many = True)
            return Response(serializer.data)

@api_view(["GET"])
def get_past_class(request,id):
    try :
        user = User.objects.get(pk = id)
    except User.DoesNotExist :
        data = {
                "success" : False,
                "errors" : "User is invalid"
        }
        return Response(data)
    else :
        now = datetime.datetime.now(tz = timezone.utc)
        print(user.is_student)
        if user.is_lecturer() :
            
            
            class_lecturers = ClassLecturer.objects.filter(lecturer__id= id).select_related('own_class').filter(Q(own_class__time_start__gte= now) | Q( own_class__time_end__lte=now))
            if len(class_lecturers) == 0 :
                data = {
                    "success" : False,
                    "errors" : "Class is invalid"
                }
                return Response(data) 
            else :          
                all_class = [item.own_class for item in class_lecturers if item.own_class is not None]
                if len(all_class) == 0 :
                    data = {
                        "success" : False,
                        "errors" : "Class is invalid"
                    }
                    return Response(data) 
                else :
                    serializers = ClassSerializer(all_class,many = True)
                    return Response(serializers.data)
        elif user.is_student :
            
            class_students = ClassStudent.objects.filter(student__id= id).select_related('own_class').filter(own_class__time_start__lte= now,own_class__time_end__gte=now)
            if len(class_students) == 0 :
                data = {
                    "success" : False,
                    "errors" : "Class is invalid"
                }
                return Response(data) 
            else :          
                all_class = [item.own_class for item in class_students if item.own_class is not None]
                if len(all_class) == 0 :
                    data = {
                        "success" : False,
                        "errors" : "Class is invalid"
                    }
                    return Response(data) 
                else :
                    serializers = ClassSerializer(all_class,many = True)
                    return Response(serializers.data)




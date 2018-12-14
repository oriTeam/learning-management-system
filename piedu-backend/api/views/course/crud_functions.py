import datetime

from course.models import CourseCategory, Class, Schedule, ClassLecturer, ClassStudent, EnrollRequest, Subject
from course.serializers import CourseCategorySerializer
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.utils import timezone
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from api.permission import  IsAuthenticated, IsAdmin,IsLecturer,IsMyOwnOrAdmin,IsStudent,IsAdminOrLecturer

from django.contrib.auth import get_user_model
User = get_user_model()


@api_view(["GET", "POST"])
@permission_classes((IsAuthenticated,))
def get_all_class_info(request):
    data = []
    time = request.data.get("time")
    now = datetime.datetime.now(tz=timezone.utc)
    all_class=[]
    if time == "past" :
        all_class = Class.objects.filter(time_end__lte = now)
    elif time == "present" :
        all_class = Class.objects.filter(time_start__lte=now,time_end__gte = now)
    else :
        all_class = Class.objects.filter(time_start__gte=now)
    if 'page' in request.data:
        class_querysets = all_class
        paginator = Paginator(class_querysets, 12)
        page = request.data.get('page')
        try:
            class_querysets = paginator.page(page)
        except PageNotAnInteger:
            class_querysets = paginator.page(1)
        except EmptyPage:
            class_querysets = paginator.page(paginator.num_pages)
            # class_querysets = Class.objects.all()

        for class_queryset in class_querysets:
            data.append(class_queryset.parse_info_and_username())
    else:
        for classo in Class.objects.all():
            data.append({"class" : classo.name})
    # serializers = ClassInfoSerializer(class_querysets, many=True)
    return Response(data)

@api_view(["GET", "POST"])
@permission_classes((IsAdminOrLecturer, ))
def remove_class_student(request):
    if request.method == "POST":
        class_id = request.data.get('class_id')
        student_id = request.data.get('student_id')
        try:
            own_class = Class.objects.get(id=class_id)
            student = User.objects.get(id=student_id)
            class_student = ClassStudent.objects.filter(own_class=class_id, student=student_id)
        except Class.DoesNotExist:
            return Response({"success": False, "code": "classdoesnotexist"})
        except User.DoesNotExist:
            return Response({"success": False, "code": "studentdoesnotexist"})
        except ClassStudent.DoesNotExist:
            return Response({"success": False, "code": "doesnotexist"})
        else:
            class_student.delete()
            return Response({"success": True, "message": "Student have been removed from class"})
    errors = {'success': False, 'code': "failed"}
    return Response(errors)


@api_view(["GET", "POST"])
@permission_classes((IsAdminOrLecturer, ))
def add_class_student(request):
    if request.method == "POST":
        class_id = request.data.get('class_id')
        student_id = request.data.get('student_id')
        try:
            own_class = Class.objects.get(id=class_id)
            student = User.objects.get(id=student_id)
            enroll_request = EnrollRequest.objects.filter(own_class=class_id, student=student_id)
        except Class.DoesNotExist:
            return Response({"success": False, "code": "classdoesnotexist"})
        except User.DoesNotExist:
            return Response({"success": False, "code": "studentdoesnotexist"})
        except EnrollRequest.DoesNotExist:
            return Response({"success": False, "code": "doesnotexist"})
        else:
            enroll_request.delete()
            class_student = ClassStudent.objects.create(own_class=own_class, student=student)
            class_student.save()
            return Response({"success": True, "message": "Student have been added into class"})
    errors = {'success': False, 'code': "failed"}
    return Response(errors)

@api_view(["GET", "POST"])
@permission_classes((IsAdminOrLecturer, ))
def remove_enroll_request(request):
    if request.method == "POST":
        class_id = request.data.get('class_id')
        student_id = request.data.get('student_id')
        try:
            enroll_request = EnrollRequest.objects.filter(own_class=class_id, student=student_id)
        except EnrollRequest.DoesNotExist:
            return Response({"success": False, "code": "doesnotexist"})
        else:
            enroll_request.delete()
            return Response({"success": True, "message": "EnrollRequest have been removed"})
    errors = {'success': False, 'code': "failed"}
    return Response(errors)




@api_view(["GET"])
@permission_classes((permissions.AllowAny,))
def get_full_class_info(request):
    request_data = request.GET
    class_id = request_data['class']
    try:
        own_class = Class.objects.get(id=class_id)
    except Class.DoesNotExist:
        pass
    else:
        return Response(own_class.parse_full_info())

@api_view(["GET"])
@permission_classes((permissions.AllowAny,))
def get_own_class(request):
    user = request.user
    own_classes = user.classes_set.all()
    data = []
    for own_class in own_classes:
        data.append(own_class.parse_info())

    return Response(data)

def course_category_details(request, id):
    course_category = CourseCategory.objects.get(pk=id)
    serializer = CourseCategorySerializer(course_category)
    return Response(serializer.data)



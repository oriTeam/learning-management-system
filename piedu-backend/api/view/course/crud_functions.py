from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ClassInfoSerializer
from course.models import CourseCategory, Class

# @api_view(["GET"])
# def create_course_category(request):
#     serializer = CourseCategorySerializer(request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response({"sucsess": True, "message": "Course Category created"})
#     else:
#         data = {
#             "success" : False,
#             "errors" : serializer.errors
#         }
#         return Response(data)
#

@api_view(["GET"])
@permission_classes((permissions.AllowAny,))
def get_all_class_info(request):
    class_querysets = Class.objects.all()
    data = []
    for class_queryset in class_querysets:
        data.append(class_queryset.parse_info())
    # serializers = ClassInfoSerializer(class_querysets, many=True)
    return Response(data)


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


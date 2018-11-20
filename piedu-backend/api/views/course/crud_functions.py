from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from course.serializers import CourseCategorySerializer
from course.models import CourseCategory, Class

@api_view(["GET"])
@permission_classes((permissions.AllowAny,))
def get_all_class_info(request):
    data = []
    if 'page' in request.GET:
        class_querysets = Class.objects.all()
        paginator = Paginator(class_querysets, 6)
        page = request.query_params.get('page')
        try:
            class_querysets = paginator.page(page)
        except PageNotAnInteger:
            class_querysets = paginator.page(1)
        except EmptyPage:
            class_querysets = paginator.page(paginator.num_pages)
            # class_querysets = Class.objects.all()

        for class_queryset in class_querysets:
            data.append(class_queryset.parse_info())
    else:
        for classo in Class.objects.all():
            data.append({"class" : classo.name})
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

def course_category_details(request, id):
    course_category = CourseCategory.objects.get(pk=id)
    serializer = CourseCategorySerializer(course_category)
    return Response(serializer.data)



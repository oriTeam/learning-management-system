from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CourseCategorySerializer
from course.models import CourseCategory

@api_view(["GET"])
def create_course_category(request):
    serializer = CourseCategorySerializer(request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"sucsess": True, "message": "Course Category created"})
    else:
        data = {
            "success" : False,
            "errors" : serializer.errors
        }
        return Response(data)


@api_view(["GET"])
def course_category_details(request, id):
    course_category = CourseCategory.objects.get(pk=id)
    serializer = CourseCategorySerializer(course_category)
    return Response(serializer.data)

from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,)
from rest_framework import viewsets, generics, mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers
from course.models import CourseCategory, Class, Schedule, ClassLecturer, ClassStudent, EnrollRequest, Subject
from .serializers import CourseCategorySerializer, SubjectSerializer, ClassSerializer, ClassLecturerSerializer, \
    ClassStudentSerializer, EnrollRequestSerializer, ScheduleSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response



# COURSECATEGORY

class CourseCategoryCreateView(generics.CreateAPIView):
    queryset = CourseCategory.objects.all()
    serializer_class = CourseCategorySerializer

    @api_view(["GET"])
    def create_course_category(self, request):
        serializer = CourseCategorySerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"sucsess": True, "message": "Course Category created"})
        else:
            data = {
                "success": False,
                "errors": serializer.errors
            }
            return Response(data)

class CourseCategoryListView(generics.ListAPIView):
    queryset = CourseCategory.objects.all()
    serializer_class = CourseCategorySerializer


class CourseCategoryDetailView(generics.RetrieveAPIView):
    queryset = CourseCategory.objects.all()
    serializer_class = CourseCategorySerializer
    lookup_field = 'id'


class CourseCayegoryUpdateView(generics.RetrieveUpdateAPIView):
    queryset = CourseCategory.objects.all()
    serializer_class = CourseCategorySerializer
    lookup_field = 'id'


class CourseCategoryDeleteView(generics.DestroyAPIView):
    queryset = CourseCategory.objects.all()
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# class CourseCategoryDetailUpdateAPIView(viewsets.GenericViewSet,
#                                         RetrieveUpdateDestroyAPIView):
#     queryset = CourseCategory.objects.all()
#     serializer_class = CourseCategoryListSerializer
#     lookup_field = 'id'
#
# class CourseCategoryListCreateAPIView(viewsets.GenericViewSet,
#                                       ListCreateAPIView):
#     serializer_class = CourseCategoryListSerializer
#     queryset = CourseCategory.objects.all()


# SUBJECT
class SubjectDetailUpdateAPIView(viewsets.GenericViewSet, RetrieveUpdateDestroyAPIView):
    serializer_class = SubjectSerializer
    lookup_field =  'id'

class SubjectListCreateAPIView(viewsets.GenericViewSet, ListCreateAPIView):
    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()


#CLASS
class ClassDetailUpdateAPIView(viewsets.GenericViewSet, RetrieveUpdateDestroyAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    lookup_field =  'id'

class ClassListCreateAPIView(viewsets.GenericViewSet, ListCreateAPIView):
    serializer_class = ClassSerializer
    queryset = Class.objects.all()



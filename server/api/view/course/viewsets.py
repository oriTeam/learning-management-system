from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,)
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers
from course.models import CourseCategory, Class, Schedule, ClassLecturer, ClassStudent, EnrollRequest, Subject
from .serializers import CourseCategoryListSerializer, SubjectListSerializer, ClassListSerializer

# COURSECATEGORY
class CourseCategoryDetailUpdateAPIView(viewsets.GenericViewSet,
                                        RetrieveUpdateDestroyAPIView):
    queryset = CourseCategory.objects.all()
    serializer_class = CourseCategoryListSerializer
    lookup_field = 'id'

class CourseCategoryListCreateAPIView(viewsets.GenericViewSet,
                                      ListCreateAPIView):
    serializer_class = CourseCategoryListSerializer
    queryset = CourseCategory.objects.all()


# SUBJECT
class SubjectDetailUpdateAPIView(viewsets.GenericViewSet, RetrieveUpdateDestroyAPIView):
    serializer_class = SubjectListSerializer
    lookup_field =  'id'

class SubjectListCreateAPIView(viewsets.GenericViewSet, ListCreateAPIView):
    serializer_class = SubjectListSerializer
    queryset = Subject.objects.all()


#CLASS
class ClassDetailUpdateAPIView(viewsets.GenericViewSet, RetrieveUpdateDestroyAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassListSerializer
    lookup_field =  'id'

class ClassListCreateAPIView(viewsets.GenericViewSet, ListCreateAPIView):
    serializer_class = ClassListSerializer
    queryset = Class.objects.all()



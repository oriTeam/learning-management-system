from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,)
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers
from course.models import Course

class CourseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
        read_only_fields = ()

class CourseDetailUpdateAPIView(viewsets.GenericViewSet,
                              RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseListSerializer
    lookup_field = 'id'

class CourseListCreateAPIView(viewsets.GenericViewSet,
                            ListCreateAPIView):
    serializer_class = CourseListSerializer
    queryset = Course.objects.all()



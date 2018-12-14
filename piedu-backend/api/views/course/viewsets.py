
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,)
from rest_framework import viewsets, generics, mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers
from course.models import CourseCategory, Class, Schedule, ClassLecturer, ClassStudent, EnrollRequest, Subject
from course.serializers import CourseCategorySerializer, SubjectSerializer, ClassSerializer, ClassLecturerSerializer, \
    ClassStudentSerializer, EnrollRequestSerializer, ScheduleSerializer
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import permissions
from api.permission import  IsAdmin,IsLecturer,IsMyOwnOrAdmin,IsStudent,IsAdminOrLecturer



# COURSECATEGORY
class CourseCategoryCreateView(generics.CreateAPIView):
    queryset = CourseCategory.objects.all()
    serializer_class = CourseCategorySerializer
    # pagination_classes = (permissions.)

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
class SubjectCreateView(generics.CreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class SubjectListView(generics.ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

# class SubjectFromCourseListView(generics.ListAPIView):
#     queryset = Subject.objects.all()
#     serializer_class = SubjectSerializer
#     lookup_field = 'Category__id'
class SubjectDetailView(generics.RetrieveAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    lookup_field = 'id'


class SubjectUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    lookup_field = 'id'


class SubjectDeleteView(generics.DestroyAPIView):
    queryset = Subject.objects.all()
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


#CLASS
@permission_classes((IsAdminOrLecturer,))
class ClassCreateView(generics.CreateAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    
class ClassListView(generics.ListAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer


class ClassDetailView(generics.RetrieveAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    lookup_field = 'id'

@permission_classes((IsLecturer,))
class ClassUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    lookup_field = 'id'

@permission_classes((IsLecturer,))
class ClassDeleteView(generics.DestroyAPIView):
    queryset = Class.objects.all()
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# class ClassDetailUpdateAPIView(viewsets.GenericViewSet, RetrieveUpdateDestroyAPIView):
#     queryset = Class.objects.all()
#     serializer_class = ClassSerializer
#     lookup_field =  'id'
#
# class ClassListCreateAPIView(viewsets.GenericViewSet, ListCreateAPIView):
#     serializer_class = ClassSerializer
#     queryset = Class.objects.all()

##SCHEDULE

class ScheduleCreateView(generics.CreateAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer


class ScheduleListView(generics.ListAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer


class ScheduleDetailView(generics.RetrieveAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    lookup_field = 'id'


class ScheduleUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    lookup_field = 'id'


class ScheduleDeleteView(generics.DestroyAPIView):
    queryset = Schedule.objects.all()
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


##CLASSLECTURER

class ClassLecturerCreateView(generics.CreateAPIView):
    queryset = ClassLecturer.objects.all()
    serializer_class = ClassLecturerSerializer


class ClassLecturerListView(generics.ListAPIView):
    queryset = ClassLecturer.objects.all()
    serializer_class = ClassLecturerSerializer


class ClassLecturerDetailView(generics.RetrieveAPIView):
    queryset = ClassLecturer.objects.all()
    serializer_class = ClassLecturerSerializer
    lookup_field = 'id'


class ClassLecturerUpdateView(generics.RetrieveUpdateAPIView):
    queryset = ClassLecturer.objects.all()
    serializer_class = ClassLecturerSerializer
    lookup_field = 'id'


class ClassLecturerDeleteView(generics.DestroyAPIView):
    queryset = ClassLecturer.objects.all()
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


##CLASSSTUDENT
class ClassStudentCreateView(generics.CreateAPIView):
    queryset = ClassStudent.objects.all()
    serializer_class = ClassStudentSerializer


class ClassStudentListView(generics.ListAPIView):
    queryset = ClassStudent.objects.all()
    serializer_class = ClassStudentSerializer


class ClassStudentDetailView(generics.RetrieveAPIView):
    queryset = ClassStudent.objects.all()
    serializer_class = ClassStudentSerializer
    lookup_field = 'id'


class ClassStudentUpdateView(generics.RetrieveUpdateAPIView):
    queryset = ClassStudent.objects.all()
    serializer_class = ClassStudentSerializer
    lookup_field = 'id'

@permission_classes((IsLecturer,))
class ClassStudentDeleteView(generics.DestroyAPIView):
    queryset = ClassStudent.objects.all()
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


##ENROLLREQUEST
@permission_classes((permissions.IsAuthenticatedOrReadOnly,))
class EnrollRequestCreateView(generics.CreateAPIView):
    queryset = EnrollRequest.objects.all()
    serializer_class = EnrollRequestSerializer


class EnrollRequestListView(generics.ListAPIView):
    queryset = EnrollRequest.objects.all()
    serializer_class = EnrollRequestSerializer


class EnrollRequestDetailView(generics.RetrieveAPIView):
    queryset = EnrollRequest.objects.all()
    serializer_class = EnrollRequestSerializer
    lookup_field = 'id'


class EnrollRequestUpdateView(generics.RetrieveUpdateAPIView):
    queryset = EnrollRequest.objects.all()
    serializer_class = EnrollRequestSerializer
    lookup_field = 'id'


class EnrollRequestDeleteView(generics.DestroyAPIView):
    queryset = EnrollRequest.objects.all()
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
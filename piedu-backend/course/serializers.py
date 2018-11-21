from rest_framework import serializers
from course.models import CourseCategory, Class, Schedule, ClassLecturer, ClassStudent, EnrollRequest, Subject
from django.core.exceptions import ValidationError

# COURSECATEGORY
class CourseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseCategory
        fields = '__all__'
        read_only_fields = ()


# SUBJECT
class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'
        read_only_fields = ()


# CLASS
class ClassSerializer(serializers.ModelSerializer):
    def check_date(self,data):
        if data['time_start'] > data['time_end'] :
            raise serializers.ValidationError("time start must be after time end")
        return data
    class Meta:
        model = Class
        fields = '__all__'
        read_only_fields = ()
    
    


# SCHEDULE
class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'
        read_only_fields = ()


# CLASSLECTURER
class ClassLecturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassLecturer
        fields = '__all__'
        read_only_fields = ()


# CLASSSTUDENT
class ClassStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassStudent
        fields = '__all__'
        read_only_fields = ()


# ENROLLREQUEST
class EnrollRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnrollRequest
        fields = '__all__'
        read_only_fields = ()

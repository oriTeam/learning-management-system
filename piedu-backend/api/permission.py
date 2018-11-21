from rest_framework import permissions
from rest_framework.permissions import BasePermission
from course.models import Class,ClassLecturer,ClassStudent,CourseCategory,EnrollRequest,Schedule,Subject
SAFE_METHODS = ['GET', 'HEAD', 'OPTIONS']

class IsLecturer(BasePermission):
    def has_permission(self,request,view):
        if request.user.is_authenticated and request.user.is_lecturer() :
            return True
        return False

class IsStudent(BasePermission):
    def has_permission(self,request,view):
        if request.user.is_authenticated and request.user.is_student() :
            return True
        return False

class IsAdmin(BasePermission):
    def has_permission(self,request,view):
        if request.user.is_authenticated and request.user.is_admin() :
            return True
        return False
class IsMyOwnOrAdmin(BasePermission):
    def has_permission(self,request,view):
        if request.user.is_authenticated  :
            if request.user.is_admin() :
                return True
            # if request.user.group_id == 3 :
            #         class_student = ClassStudent.objects.        
        return False

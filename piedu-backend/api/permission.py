from rest_framework import permissions
from rest_framework.permissions import BasePermission
from course.models import Class,ClassLecturer,ClassStudent,CourseCategory,EnrollRequest,Schedule,Subject
SAFE_METHODS = ['GET', 'HEAD', 'OPTIONS']

from .functions import get_user_from_token, get_token_from_request


class IsAuthenticated(BasePermission):
    def has_permission(self,request,view):
        token = get_token_from_request(request)
        user = get_user_from_token(token)
        if user is not None:
            return True
        return False

class IsLecturer(BasePermission):
    def has_permission(self,request,view):
        token = get_token_from_request(request)
        user = get_user_from_token(token)
        if user is not None and user.is_lecturer():
            return True
        return False
        
class IsStudent(BasePermission):
    def has_permission(self,request,view):
        token = get_token_from_request(request)
        user = get_user_from_token(token)
        if user is not None and user.is_student() :
            return True
        return False

class IsAdmin(BasePermission):
    def has_permission(self,request,view):
        token = get_token_from_request(request)
        user = get_user_from_token(token)
        # print(user)
        print(user)
        if user is not None and user.is_admin() :
            return True
        return False

class IsAdminOrLecturer(BasePermission):
    def has_permission(self,request,view):
        token = get_token_from_request(request)
        user = get_user_from_token(token)
        if user is not None :
            if user.is_admin() or user.is_lecturer() :
                return True
        return False
        
class IsMyOwnOrAdmin(BasePermission):
    def has_permission(self,request,view):
        class_id = request.GET['class_id']
        token = get_token_from_request(request)
        user = get_user_from_token(token)
        if user is not None  :
            if user.is_admin() :
                return True
            if user.group_id == 3 :
                try :
                    class_student = ClassStudent.objects.get(student__id = user.id,own_class__id =class_id)
                except ClassStudent.DoesNotExist:
                    return False
                else : 
                    return True 
            if user.group_id == 2 :
                try :
                    class_lecturer = ClassLecturer.objects.get(lecturer__id = user.id,own_class__id =class_id)
                except ClassLecturer.DoesNotExist:
                    return False
                else : 
                    return True        
        return False

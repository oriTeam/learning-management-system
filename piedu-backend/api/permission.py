from rest_framework import permissions
from rest_framework.permissions import BasePermission
from course.models import Class,ClassLecturer,ClassStudent,CourseCategory,EnrollRequest,Schedule,Subject
SAFE_METHODS = ['GET', 'HEAD', 'OPTIONS']

class IsLecturer(BasePermission):
    def has_permission(self,request,view):
        if request.user.is_authenticated and request.user.is_lecturer() :
            return True
        # data ={
        #     "success" : False,
        #     "code"    : "Access denied"
        # }
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
            if request.user.group_id == 3 :
                try :
                    class_student = ClassStudent.objects.get(student__id = request.user.id,own_class__id =1126)
                except ClassStudent.DoesNotExist:
                    return False
                else : 
                    return True 
            if request.user.group_id == 2 :
                try :
                    class_lecturer = ClassLecturer.objects.get(lecturer__id = request.user.id,own_class__id =1126)
                except ClassLecturer.DoesNotExist:
                    return False
                else : 
                    print(request.user.id)
                    print(class_lecturer)
                    return True        
        return False

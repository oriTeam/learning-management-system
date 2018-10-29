from course.models import Course,Class,Schedule,ClassLecturer,ClassStudent,EnrollRequest
from django.http import JsonResponse
from api.functions import string_to_boolean
from api.base import BaseManageView

class Course_():
    def get_course_info(self,request):
        course_id = request.GET['course_id']
        datas = []
        course = Course.objects.filter(course_id = course_id)
        data ={}
        data["id"] = course["id"]
        data["name"] = course["name"]
        
        return JsonResponse(data)
    def get_all_courses(self):
        datas = []
        courses =Course.objects.all()
        # if courses.DoesNotExist :
        #     return JsonResponse({"success" : False ,"code" : "course does not exist"})
        # else :
        for course in courses :
            data ={}
            data["id"] = course["id"]
            data["name"] = course["name"]
            datas.append(data)
        return JsonResponse({"success": True})
    

# class Class_():
    
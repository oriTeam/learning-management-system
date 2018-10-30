from course.models import Course,Class,Schedule,ClassLecturer,ClassStudent,EnrollRequest
from django.http import JsonResponse
from api.functions import string_to_boolean
from api.base import BaseManageView

class Course_(BaseManageView):

    error_messages = {
        "Course": {
            "invalid": "This course_id is invalid",
        },
    }

    def __init__(self, *args, **kwargs):
        self.VIEWS_BY_METHOD = {
            'GET' : self.get_course_info,
        }

    def get_course_info(self, request):
        request_data =   request.GET
        course_id = request_data.get('course_id')
        data = {}
        try:
            course = Course.objects.get(pk=course_id)
        except Course.DoesNotExist:
            # return JsonResponse({"invalid": "This course_id is invalid"})
            return self.json_error(field = 'Course', code = "invalid")
        else:
            data["id"] = course.id
            data["name"] = course.name
        
        return JsonResponse(data)

    def get_all_courses(self, request):
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
    
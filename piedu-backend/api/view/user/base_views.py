from course.models import CourseCategory, Class, Schedule, ClassLecturer, ClassStudent, EnrollRequest, Subject
from core.models import User
from django.http import JsonResponse
from api.functions import string_to_boolean
from api.base import BaseManageView

class _User(BaseManageView):
    error_messages = {
       "User" : {
            "invalid" : "This user_id is invalid",
        }
    }
    def __init__(self,*args,**kwargs):
        self.self.VIEWS_BY_METHOD = {
            "GET" : self.get_user_info,
        }

    def get_user_info(self,request):
        request_data = request.GET
        user_id = request_data.get('user_id')
        try :
            user = User.objects.get(pk = user_id)
        except User.DoesNotExist:
            return self.json_error(field = "User", code = "invalid")
        else :
            return JsonResponse(user.parse_data())

from django.views import View
from django.http import JsonResponse
from api.functions import get_token_from_request, get_user_from_token,split_word
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from core.models import User
from course.models import Class




@api_view(['GET'])
@permission_classes((permissions.IsAuthenticatedOrReadOnly,))
def search(request):
    # print("a")
    # value = 3

    value = str(request.GET.get('value'))
    # print(value)
    if value =="1" :
        words = split_word(request.GET.get('search'))
        rs = []
        for word in words :
            classes = Class.objects.filter(name = word)
            for item in classes :
                rs.append(item.parse_full_info())
        return JsonResponse({"data" : rs})
    elif value == "2":
        words = split_word(request.GET.get('search'))
        rs = []
        for word in words :
            lecturers = User.objects.filter(username__contains = word)
            for item in lecturers :
                if (str(item.group) == "lecturer_group"):
                    rs.append(item.parse_data())
        return JsonResponse({"data" : rs})
    else:
        words = split_word(request.GET.get('search'))
        rs = []
        for word in words :
            print(word)
            students = User.objects.filter(username__contains = word)
            for item in students :
                if (str(item.group) == "student_group"):
                    rs.append(item.parse_data())
        return JsonResponse({"data" :rs})



class BaseManageView(View):
    """
    The base class for ManageViews
    A ManageView is a views which is used to dispatch the requests to the appropriate views
    This is done so that we can use one URL with different methods (GET, PUT, etc)
    """
    error_messages = {}
    
    def dispatch(self, request, *args, **kwargs):
        if not hasattr(self, 'VIEWS_BY_METHOD'):
            raise Exception('VIEWS_BY_METHOD static dictionary variable must be defined on a ManageView class!')
        if request.method in self.VIEWS_BY_METHOD:
            return self.VIEWS_BY_METHOD[request.method](request, *args, **kwargs)
        return JsonResponse({},status = 405)


    def json_error(self, field, code):
        default_errors = self.error_messages[field]
        errors = []
        errors.append({"code" : code, "message" : default_errors[code]})
        return JsonResponse({field : errors}, safe = False, status = 404)
    

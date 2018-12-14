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
def get_data(request):
    selected_type = request.GET['selected_type']
    print(selected_type)
    all_data = []
    if selected_type=="user":
        list_user =  User.objects.all().exclude(group__name = 'admin_group')
        for user in list_user :
            all_data.append({"id" : user.id,"name" : user.fullname()})
    elif selected_type=="class":
        list_class = Class.objects.all()
        for  classes in list_class :
            all_data.append({"id" : classes.id, "name" : classes.name })
    return Response(all_data)

@api_view(['GET'])
@permission_classes((permissions.IsAuthenticatedOrReadOnly,))
def result_search(request):
    _type = request.data.get('type')
    if _type == "user" :
        user_id = request.data.get('user_id')
        try :
            user = User.objects.get(pk = user_id)
        except User.DoesNotExist :
            return Response("User is invalid")
        else :
            return Response(user.parse_data())
    elif _type == "class":
        class_id = request.data.get('class_id')
        try :
            item = Class.objects.get(pk = class_id)
        except Class.DoesNotExist :
            return Response("Class is invalid")
        else:
            return Response(item.parse_info_and_username())
    else :
        return Response("Search failed")
    

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
    

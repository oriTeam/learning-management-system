import datetime
from django.utils import timezone
from core.models import User
from django.http import JsonResponse
from api.functions import string_to_boolean
from core.serializers import UserSerializerView
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import permissions 
import dateutil.parser
from api.functions import get_token_from_request, get_user_from_token
from api.permission import  IsAuthenticated, IsAdmin,IsLecturer,IsMyOwnOrAdmin,IsStudent,IsAdminOrLecturer
from django.contrib.auth.models import Group
from course.models import Class,ClassStudent,ClassLecturer
from django.contrib.auth import authenticate

@api_view(['GET','POST'])
@permission_classes((permissions.IsAuthenticated,))
def get_user_detail_view(request):

    token = get_token_from_request(request)
    view_user = get_user_from_token(token)
    id = request.data.get('profile_id')
    try :
        user = User.objects.get(pk=id)
    except User.DoesNotExist:
        data = {
                "success" : False,
                "errors" : "User is invalid"
        }
        return Response(data)
    else:
        if view_user is not None:
            result = user.parse_data()
            return Response({"success": True,"profile": result})
            # serializer = UserSerializerView(user)
            # return Response(serializer.data)

@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
def change_password(request):
    # try :
    #     user = User.objects.get(pk=id)
    # except User.DoesNotExist:
    #     data = {
    #             "success" : False,
    #             "errors" : "User is invalid"
    #     }
    #     return Response(data)
    # else:
    token = get_token_from_request(request)
    user = get_user_from_token(token)
    old_password = request.data.get("old_password")
    validated = authenticate(username=user.username,password=old_password)
    if validated :
        new_password = request.data.get("new_password")
        if user is not None:
            user.set_password(str(new_password))
            user.save()
        
            data = {
                    "success" : True,
                    "message" : "Done!"
            }
            return Response(data)
        else :
            data = {
                    "success" : False,
                    "message" : "User is invalid"
            }
        return Response(data)
    else :
        data ={
            "success" : False,
            "message" : "Current Password is invalid"
        }
        return Response(data)

@api_view(['GET','POST'])
@permission_classes((IsAdmin,))
def create_user(request):
    code = request.data.get("code")
    # avatar = request.data.get("avatar")
    phone_number = request.data.get("phone_number")
    gender = request.data.get("gender")
    unit = request.data.get("unit")
    group = Group.objects.get(pk=request.data.get("group"))
    address = request.data.get("address")
    birthday = dateutil.parser.parse(request.data.get("birthday"))
    first_name =request.data.get("first_name")
    last_name = request.data.get("last_name")
    password = request.data.get("password")
    username = request.data.get("username")
    try :
        new_user = User.objects.create(code= code,phone_number=phone_number,gender=gender,unit=unit,group=group,address=address,birthday=birthday,first_name=first_name,last_name=last_name,username=username)
        new_user.set_password(str(password))
        new_user.save()
    except Exception as e:
        data ={
            "success" : False,
            "message" : "Can't create"
        }
        
        return Response(data)
    else :
        data ={
            "success" : True,
            "message" : "Created"
        }
        return Response(data)

@api_view(['GET','POST'])
@permission_classes((IsMyOwnOrAdmin,))
def edit_user_info(request):
    token = get_token_from_request(request)
    user = get_user_from_token(token)
    code = request.data.get("code")
    avatar = request.data.get("avatar")
    phone_number = request.data.get("phone_number")
    gender = request.data.get("gender")
    unit = request.data.get("unit")
    address = request.data.get("address")
    birthday = dateutil.parser.parse(request.data.get("birthday"))
    first_name =request.data.get("first_name")
    last_name = request.data.get("last_name")
    username = request.data.get("username")
    try :
        user.code= code
        user.avatar = avatar
        user.phone_number = phone_number
        user.gender = gender
        user.unit = unit
        user.address = address
        user.birthday  = birthday
        user.first_name = first_name
        user.last_name= last_name
        user.username= username
        user.save()
    except :
        data ={
            "success" : False,
            "message" : "Can't edit info"
        }
        return Response(data)
    else :
        data ={
            "success" : True,
            "message" : "Edited"
        }
    
@api_view(['GET','POST'])
@permission_classes((permissions.IsAuthenticated,))
def get_class_of_user(request):
    token = get_token_from_request(request)
    user = get_user_from_token(token)
    now = datetime.datetime.now(tz=timezone.utc)
    if user is not None:
        if user.is_student():
    
            all_class = ClassStudent.objects.filter(student__id =user.id).exclude(own_class__time_start__gte=now)
            data = {
                "success" : True,
                "data"     : len(all_class)
            }
            return Response(data)
        elif user.is_lecturer():
            all_class = ClassLecturer.objects.filter(lecturer__id =user.id).exclude(own_class__time_start__gte=now)
            data = {
                "success" : True,
                "data"     : len(all_class)
            }
            return Response(data)
    else :
        data = {
                "success" : False,
                "data"     : "User is invalid"
            }
        return Response(data)



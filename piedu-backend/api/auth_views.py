from django.contrib.auth import login as auth, authenticate
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.status import HTTP_401_UNAUTHORIZED
from rest_framework.authtoken.models import Token
from django.conf import settings

@api_view(["POST"])
@permission_classes((permissions.AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    user = authenticate(username=username, password=password)
    if user:
        auth(request, user)
        token, _ = Token.objects.get_or_create(user=user)
    # return Response({"token": token.key})
        redirectTo = settings.FRONTEND_SERVER_URL
        return Response({'success' : True, 'token': token.key, "redirectTo" : redirectTo})

    print("NOT USER")
    return Response({'success': 'False', "error": "username or password is incorrect!"})


@api_view(["GET"])
@permission_classes((permissions.AllowAny,))
def is_authenticated(request):
    user = request.user
    if user.is_authenticated:
        return Response({"authenticated": True, "id": user.id, "name": user.username, "avatarPath": user.avatar.url})
    else:
        return Response({"authenticated": False})

@api_view(["GET"])
@permission_classes((permissions.AllowAny,))
def logout(request):
    request.user.auth_token.delete()
    return Response({"logout": "success"})


from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        user = token.user
        if user.avatar:
            avatarPath = user.avatar.url
        else:
            avatarPath = ''
        return Response({'token': token.key, 'user_id': token.user_id, 'email': user.email, 'avatarPath':
            avatarPath, 'group': user.group.name, "username": user.username})

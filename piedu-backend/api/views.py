from django.contrib.auth import login as auth, authenticate
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.status import HTTP_401_UNAUTHORIZED
from rest_framework.authtoken.models import Token

@api_view(["POST"])
@permission_classes((permissions.AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'success':'False',"error": "username or password is incorrect!"})
    else:
        auth(request, user)
    # token, _ = Token.objects.get_or_create(user=user)
    # return Response({"token": token.key})
    redirectTo = request.get_host()
    return Response({'success' : True, "redirectTo" : redirectTo})

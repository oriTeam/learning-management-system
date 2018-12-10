from django.http import JsonResponse
from django.db.models import Prefetch
from rest_framework.authtoken.models import Token


def string_to_boolean(value):
    if value is not None and value.lower() == 'false':
        return False
    else: 
        return True

def user_is_authenticated(token):
    try:
        token_object =  Token.objects.get(key=token)
    except Token.DoesNotExist:
        return False
    else:
        return True

def get_user_from_token(token):
    try:
        token_object =  Token.objects.get(key=token)
    except Token.DoesNotExist:
        print('Token is invalid')
        return None
    else:
        return token_object.user

def get_token_from_request(request):
    token = ''
    if request.method == 'GET':
        token = request.GET.get('token')
    else:
        token = request.data.get('token')
    return token
def split_word(string):
    word = string.split(" ")
    return word
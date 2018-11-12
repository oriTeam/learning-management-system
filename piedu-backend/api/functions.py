from django.http import JsonResponse
from django.db.models import Prefetch

def string_to_boolean(value):
    if value is not None and value.lower() == 'false':
        return False
    else: 
        return True
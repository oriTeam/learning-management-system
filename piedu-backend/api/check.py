from datetime import datetime
from django.utils import timezone
import json
import pytz
from rest_framework.response import Response


class ClassSession(object):
    def __init__(self):
        self.session = [0,0,0,0,0,0,0,0,0,0,0,0]
    def add(self,session_start=None,session_end=None):
        for i in range(session_start-1,session_end):
            if self.session[i] == 0 :
                self.session[i] = 1
            else :
                return False
        return True

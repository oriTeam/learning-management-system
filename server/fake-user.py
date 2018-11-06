import sys
import os
import django
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "PIEDU.settings")
django.setup()
User = get_user_model()
from django.contrib.auth.models import Group, Permission

while True:
    start = input("----- Start at (code) : ")
    end = input("----- End at (code) : ")
    group = input("Group id : \n"
                  "1: Admin \n"
                  "2: Lecturer \n"
                  "3: Student \n"
                  "----- Select group id: ")
    if start.isdigit() or end.isdigit():
        start = int(start)
        end = int(end)
        break

for code in range(start, end):
    try:
        email = str(code) + '@vnu.edu.vn'
        group = str(group)
        print('Creating user {0}.'.format(code))
        user = User.objects.create_user(username=str(code), email=email, group=Group.objects.get(pk=group))
        user.set_password(str(code))
        user.save()

        assert authenticate(username=str(code), password=str(code))
        print('User {0} successfully created.'.format(code))

    except:
        print('There was a problem creating the user: {0}.  Error: {1}.' \
              .format(code, sys.exc_info()[1]))

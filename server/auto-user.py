import sys
import os
import django
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "PIEDU.settings")
django.setup()
User = get_user_model()

while True:
    start = input("Start at (student' code) : ")
    end = input("End at (student' code) : ")
    role = input("Role : ")
    if start.isdigit() or end.isdigit():
        start = int(start)
        end = int(end)
        break

for code in range(start, end):
    try:
        email = str(code) + '@vnu.edu.vn'
        role = str(role)
        print('Creating user {0}.'.format(code))
        user = User.objects.create_user(username=code, email=email, role=role)
        user.set_password(code)
        user.save()

        assert authenticate(username=code, password=code)
        print('User {0} successfully created.'.format(code))

    except:
        print('There was a problem creating the user: {0}.  Error: {1}.' \
            .format(code, sys.exc_info()[1]))

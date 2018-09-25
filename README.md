# Learning Managenment System

> Hệ thống quản lý môn học 

> Sử dụng framework [Django] v2.1


## Sử dụng:
    1. Cài đặt python 3.x, pip, Django 2.1.
    
    2. Download file zip hoặc clone repo này về máy, mở cmd (terminal) tại thư mục chính (chứa file manage.py).
    
    3. Cài đặt một số package python phải dùng:
    Cách 1: AIO:
        
        $ pip install -r requirements.txt
    
    Cách 2: Cài từng package:
    
        $ pip install django-debug-toolbar

        $ pip install django-webpack-loader
        
        $ pip install django-guardian
        
        $ pip install reportlab

        $ pip install mysql-python
        
        hoặc nếu không được: 
        
        $ pip install mysqlclient
        

    4. Cài các node modules(phải cài npm trước):
        
        $ npm i -D

        $ ./node_modules/.bin/webpack
    
    5. Migrate:
        
        $ python manage.py makemigrations
        
        $ python manage.py migrate
        
    6. Và chạy thôi :)) 
        
        $ python manage.py runserver
        
## Contributors
    Updating ...
    

[Django]: <https://docs.djangoproject.com/en/2.1/>
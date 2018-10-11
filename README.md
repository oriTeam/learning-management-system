# Learning Managenment System

> Hệ thống quản lý môn học 


## Sử dụng:

  1. Cài đặt python 3.x, pip, Django 2.1.
    
  2. Download file zip hoặc clone repo này về máy, mở cmd (terminal) tại thư mục chính (chứa file manage.py).
    
  3. Cài đặt một số package python phải dùng:

    Note: Gỡ Pillow bản cũ và cài bản 5.0.0:
	
    $ pip remove Pillow

	$ pip install Pillow==5.0.0
	
  -- Cách 1: AIO:
        
        $ pip install -r requirements.txt
    
  -- Cách 2: Cài từng package:
        
        $ pip install django-mptt
        
        $ pip install django-haystack
        
        $ pip install markdown2
        
        $ pip install django-widget-tweaks
        
        $ pip install django-machina
        
        **sudo rm -rf /usr/local/lib/python3.6/dist-packages/haystack/
    
        $ pip install django-debug-toolbar

        $ pip install django-webpack-loader
        
        $ pip install django-guardian
        
        $ pip install reportlab

        $ pip install mysql-python
        
        hoặc nếu không được: 
        
        $ pip install mysqlclient
        

   
  5. Migrate:
        
    $ python manage.py makemigrations
        
    $ python manage.py migrate
        
        
  6. Và chạy thôi :)) 
        
    $ python manage.py runserver
        
## Contributors

   1. vantrong291
   2. Chikyuu
   3. tuanhah
   4. LeCongThuong
   5. lethithanhhoa
   6. bogianoithonda
   
## Công nghệ sử dụng

   1. Backend: Django, Mysql, ...
   2. Frontend: VueJs, Bootstrapv4, ...    

[Django]: <https://docs.djangoproject.com/en/2.1/>

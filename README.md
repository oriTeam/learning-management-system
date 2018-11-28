# Learning Managenment System

> Hệ thống quản lý môn học 


## Sử dụng:

  1. Cài đặt python 3.x, pip, Django 2.1.
    
  2. Download file zip hoặc clone repo này về máy, mở cmd (terminal) tại thư mục chính (chứa file manage.py).
    
  3. Cài đặt một số package python phải dùng, tại thư mục gốc:
    
    $ cd piedu-backend
    $ pip install -r requirements.txt
       
  5. Migrate:
        
    $ python manage.py makemigrations
        
    $ python manage.py migrate
  
  6. Chuyển tới thư mục frontend và setup cho frontend:
    
    $ cd ../piedu-frontend
    $ npm install        
        
  7. Và chạy thôi :)) 
       
    $ python piedu-backend/manage.py runserver
    $ cd ../piedu-frontend    
    $ npm run serve
    
## Contributors

   1. vantrong291
   2. chikyuu29198
   3. tuanhah
   4. LeCongThuong
   5. lethithanhhoa
   6. bogianoithonda
   
## Công nghệ sử dụng

   1. Backend: Django, Mysql, ...
   2. Frontend: VueJs, Bootstrapv4, ...    

[Django]: <https://docs.djangoproject.com/en/2.1/>

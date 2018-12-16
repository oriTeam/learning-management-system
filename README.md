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
    
## Contributors: 6

   1. Phạm Văn Trọng: @vantrong291
   2. Vũ Ngọc Chi: @chikyuu29198
   3. Hoàng Anh Tuấn: @tuanhah, @Ryuzaki98
   4. Lê Công Thương: @LeCongThuong
   5. Lê Thị Thanh Hoa: @lethithanhhoa
   6. Trần Hữu Tuân: @bogianoithonda
   
## Công nghệ sử dụng

   1. Backend: Django, DjangoREST, Mysql, ...
   2. Frontend: VueJs, Vuetify, Bootstrapv4, ...    

[Django]: <https://docs.djangoproject.com/en/2.1/>

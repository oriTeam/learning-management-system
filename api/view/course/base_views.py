from course.models import Course,Class,Schedule,ClassLecturer,ClassStudent,EnrollRequest
from core.models import User
from django.http import JsonResponse
from api.functions import string_to_boolean
from api.base import BaseManageView
import datetime

class Course_(BaseManageView):

    error_messages = {
        "Course": {
            "invalid": "This course_id is invalid",
        },
        "Class": {
            "invalid": "This class_id is invalid",
        }
    }

    def __init__(self, *args, **kwargs):
        self.VIEWS_BY_METHOD = {
            'GET' : self.get_course_info,
            'GET' : self.get_courses,
        }

    def get_course_info(self, request):
        request_data = request.GET
        course_id = request_data.get('course_id')
        data = {}
        try:
            course = Course.objects.get(pk=course_id)
        except Course.DoesNotExist:
            # return JsonResponse({"invalid": "This course_id is invalid"})
            return self.json_error(field = 'Course', code = "invalid")
        else:
            data = {"course" :course.parse_data()}
        
        return JsonResponse(data)

    def get_courses(self, request):
        datas = []
        courses =Course.objects.all()
        # if courses.DoesNotExist :
        #     return JsonResponse({"success" : False ,"code" : "course does not exist"})
        # else :
        for course in courses :
            data ={"course" : course.parse_data()}
            datas.append(data)
        return JsonResponse({"success": True})

    def get_course_class(self,request):
        request_data = request.GET
        course_id = request_data.get('course_id')
        all_class = Class.objects.filter(course_id = course_id)
        result=[]
        for item in all_class :
            result.append(item.parse_data())
        return JsonResponse({result})



    

class Class_(BaseManageView):
    error_messages = {
        "Class": {
            "invalid": "This class_id is invalid",
        },
        "User" : {
            "invalid" : "This user_id is invalid",
        },
        "ClassLecturer" : {
            "invalid" : "This Class_Lecturer is invalid",
        },
        "ClassStudent" : {
            "invalid" : "This Class_Student is invalid",
        }
    }

    def __init__(self, *args, **kwargs):
        self.VIEWS_BY_METHOD = {
            "GET" : self.get_all_class,
            "GET" : self.get_class_info,
            "GET" : self.get_current_class,
            "GET" : self.get_past_class,
            "GET" : self.get_student,
        }
    def get_class_info(self,request):
        request_data = request.GET
        class_id = request_data.get('class_id')
        item = Class.objects.filter(pk = class_id)
        # except item.DoesNotExist :
        if item is null :
            return self.json_error(field = "Class", code = "invalid")
        else :
            data = {"class" :item.parse_data()}
        return JsonResponse(data)
    def get_all_class(self,request):
        request_data = request.GET
        all_class = Class.objects.all()
        datas =[]
        for item in all_class:
            data = {"class" : item.parse_data()}
            datas.append(data)
        return JsonResponse({"success" :True})
    
    
        
    def get_class_from_userId(self,request):
        request_data = request.GET
        user_id = request_data.get('user_id')
        try :
            user = User.objects.get(pk = user_id)
        except User.DoesNotExist :
            return self.json_error(field = "User" , code = "invalid")
        else :
            all_class =[]
            if user.isStudent :
                class_students = ClassStudent.objects.filter(student_id= user_id)
                if len(class_students) == 0 :
                    return self.json_error(field = "ClassStudent" ,code = "invalid")
                else :
                    for class_student in class_students: 
                        class_id = class_student.class_id
                        try :
                            item = Class.objects.get(pk=class_id)
                        except Class.DoesNotExist :
                            return self.json_error(field = "Class", code = "invalid")
                        else :
                             all_class.append(item)
                
            elif user.isLecturer :
                class_lecturers = ClassLecturer.objects.filter(lecturer_id = user_id)
                if len(class_lecturers) == 0 :
                    return self.json_error(field = "ClassLecturer",code ="invalid")
                else :
                    for class_lecturer in class_lecturers:
                        class_id = class_lecturer.class_id
                        try :
                            item = Class.objects.get(pk = class_id)
                        except Class.DoesNotExist :
                            return self.json_error(field = "Class",code = "invalid")
                        else :
                            all_class.append(item)

            return all_class
    def checktime(time_start,time_end,now):
        return True if time_start <= now and time_end >= now else False
    
    def get_current_class(self,request):
        all_class = self.get_class_from_userId(request)
        now = datetime.datetime.now()
        all_current_class =[]
        for item in all_class :
            if checktime(item.time_start,item.time_end,now) :
                all_current_class.append(item.parse_data())
        return JsonResponse({all_current_class})
    def get_past_class(self,request):
        all_class = self.get_class_from_userId(request)
        now = datetime.datetime.now()
        all_past_class = []
        for item in all_class :
            if checktime(item.time_start,item.time_end,now) == False :
                all_past_class.append(item.parse_data())
        return JsonResponse({all_past_class})
    
    def get_student(self,request):
        request_data = request.GET
        class_id = request_data.get("class_id")
        class_students = ClassStudent.objects.filter(class_id = class_id)
        students=[]
        for class_student in class_students:
            try :
                student = User.objects.get(pk = class_student.student_id)
            except User.DoesNotExist:
                return json_error(field = "User",code ="invalid")
            else :
                students.append(student.parse_data())
        return JsonResponse({students})


                         

                
        
        

    
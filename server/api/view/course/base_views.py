from course.models import Course,Class,Schedule,ClassLecturer,ClassStudent,EnrollRequest
from core.models import User
from django.http import JsonResponse
from api.functions import string_to_boolean
from api.base import BaseManageView
import datetime
import json
import pytz

class _Course(BaseManageView):

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
            # 'GET' : self.get_course_info,
            'GET' : self.get_courses,
            #  'GET' : self.get_course_class,
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
            data = course.parse_data()
        
        return JsonResponse(data)

    def get_courses(self, request):
        datas = []
        courses =Course.objects.all()
        # if courses.DoesNotExist :
        #     return JsonResponse({"success" : False ,"code" : "course does not exist"})
        # else :
        for course in courses :
            data =course.parse_data()
            datas.append(data)
        return JsonResponse({"data" :datas})

    def get_course_class(self,request):
        request_data = request.GET
        course_id = request_data.get('course_id')
        all_class = Class.objects.filter(course_id = course_id)
        if len(all_class) == 0 :
            return self.json_error(field="Course",code="invalid")
        else :
            # result=[]
            
            # for item in all_class :
            #     # result.append(item.parse_data())
            #     result.append(item.parse_data())
            # result = json.dumps(result,default=str)
            result = [item.parse_data() for item in all_class]
            # result = json.dumps(result,default=str)
            
            return JsonResponse({"data " :result})



    

class _Class(BaseManageView):
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
            # "GET" : self.get_all_class,
            # "GET" : self.get_class_info,
            # "GET" : self.get_current_class,
            # "GET" : self.get_past_class,
            "GET" : self.get_student,
            # "GET" : self.get_enroll_request,
        }
    def get_class_info(self,request):
        request_data = request.GET
        class_id = request_data.get('class_id')
        try :
            item = Class.objects.get(pk=class_id)
        except Class.DoesNotExist :
            return self.json_error(field ="Class", code = "invalid")
        # if len(item) == 0:
        #     return self.json_error(field = "Class", code = "invalid")
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
        return JsonResponse({"data" : datas})
    
    
        
    def get_class_from_userId(self,request):
        request_data = request.GET
        user_id = request_data.get('user_id')
        try :
            user = User.objects.get(pk = user_id)
        except User.DoesNotExist :
            return self.json_error(field = "User" , code = "invalid")
        else :
            all_class =[]
            if user.is_student :
                class_students = ClassStudent.objects.filter(student_id= user_id)
                if len(class_students) == 0 :
                    return self.json_error(field = "ClassStudent" ,code = "invalid")
                else :
                    for class_student in class_students: 
                        class_id = class_student.class_id.id
                        try :
                            item = Class.objects.get(pk=class_id)
                        except Class.DoesNotExist :
                            return self.json_error(field = "Class", code = "invalid")
                        else :
                             all_class.append(item)
                
            elif user.is_lecturer :
                class_lecturers = ClassLecturer.objects.filter(lecturer_id = user_id)
                if len(class_lecturers) == 0 :
                    return self.json_error(field = "ClassLecturer",code ="invalid")
                else :
                    for class_lecturer in class_lecturers:
                        class_id = class_lecturer.class_id.id
                        try :
                            item = Class.objects.get(pk = class_id)
                        except Class.DoesNotExist :
                            return self.json_error(field = "Class",code = "invalid")
                        else :
                            all_class.append(item)

            return all_class
    def checktime(self,time_start,time_end,now):
        # return True if time_start <= now and time_end >= now else False
        return True if time_start.replace(tzinfo=None) <= now.replace(tzinfo=None) <= time_end.replace(tzinfo=None) else False
        # utc=pytz.UTC




    def get_current_class(self,request):
        all_class = self.get_class_from_userId(request)
        now = datetime.datetime.now()
        all_current_class =[]
        for item in all_class :
            if self.checktime(item.time_start,item.time_end,now) :
                all_current_class.append(item.parse_data())
        return JsonResponse({"data" :all_current_class})
    def get_past_class(self,request):
        all_class = self.get_class_from_userId(request)
        now = datetime.datetime.now()
        all_past_class = []
        for item in all_class :
            if self.checktime(item.time_start,item.time_end,now) == False :
                all_past_class.append(item.parse_data())
        return JsonResponse({"data" :all_past_class})
    
    def get_student(self,request):
        request_data = request.GET
        class_id = request_data.get("class_id")
        class_students = ClassStudent.objects.filter(class_id__id = class_id)
        if len(class_students) == 0 :
            return self.json_error(field="Class",code="invalid")
        else : 
            students=[]
            for class_student in class_students:
                try :
                    student = User.objects.get(pk = class_student.student_id.id)
                except User.DoesNotExist:
                    return self.json_error(field = "User",code ="invalid")
                else :
                    students.append(student.parse_data())
            return JsonResponse({"data" : students})

    def get_enroll_request(self,request):
        request_data = request.GET
        class_id = request_data.get('class_id')
        enroll_request_by_class_id =  EnrollRequest.objects.filter(class_id = class_id)
        if len(enroll_request_by_class_id) == 0 :
            return self.json_error(field= "Class", code = "invalid")
        else :
            students=[]
            for item in enroll_request_by_class_id :
                try :
                    student = User.objects.get(pk = item.student_id)
                except User.DoesNotExist :
                    return self.json_error(field = "User",code = "invalid")
                else :
                    students.append(student.parse_data())
            return JsonResponse({students})


                         

                
        
        

    
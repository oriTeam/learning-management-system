from course.models import Course,Class,Schedule,ClassLecturer,ClassStudent,EnrollRequest
from core.models import User
from syllabus.models import Material,Syllabus,SyllabusTemplate
from django.http import JsonResponse
from api.functions import string_to_boolean
from api.base import BaseManageView


class _Material(BaseManageView):
    error_messages = {
        "Class": {
            "invalid": "This class_id is invalid",
        },
        "User" : {
            "invalid" : "This user_id is invalid",
        },
        "Material" : {
            "invalid" : "This material is invalid",
        },
        "Syllabus" : {
            "invalid" : "This syllabus is invalid",
        }
    }

    def __init__(self, *args, **kwargs):
        self.VIEWS_BY_METHOD = {
            "GET" : self.get_material_info,
            "GET" : self.get_syllabus_material,   
        }
    
    def get_material_info(self,request):
        request_data = request.GET
        material_id = request_data.get("material_id")
        try :
            material = Material.objects.get(pk = material_id)
        except Material.DoesNotExist:
            return self.json_error(field="Material",code= "invalid")
        else :
            return JsonResponse(material.parse_data)
    
    
    
    def get_syllabus_material(self,request):
        request_data = request.GET
        syllabus_id = request_data.get("syllabus_id")
        all_material = Material.objects.filter(syllabus_id = syllabus_id)
        
        if len(all_material) == 0 :
            return self.json_error(field= "Syllabus",code = "invalid")
        else :
            result = []
            for item in all_material:
                result.append(item.parse_data)
            return JsonResponse({result})
    
class _Syllabus(BaseManageView):
    error_messages = {
        "Class": {
            "invalid": "This class_id is invalid",
        },
        "User" : {
            "invalid" : "This user_id is invalid",
        },
        "Material" : {
            "invalid" : "This material is invalid",
        },
        "Syllabus" : {
            "invalid" : "This syllabus is invalid",
        }
    }

    def __init__(self, *args, **kwargs):
        self.VIEWS_BY_METHOD = {
            "GET" : self.get_class_syllabus,
            
        }
    def get_class_syllabus(self,request):
        request_data = request.GET
        class_id = request_data.get("class_id")
        all_syllabus = Syllabus.objects.filter(class_id = class_id)
        if len(all_syllabus) == 0 :
            return self.json_error(field="Class",code = "invalid")
        else :
            result = []
            for item in all_syllabus:
                result.append(item.parse_data())
            return JsonResponse({result})
class _Template(BaseManageView):
    error_messages = {
        "Class": {
            "invalid": "This class_id is invalid",
        },
        "User" : {
            "invalid" : "This user_id is invalid",
        },
        "Material" : {
            "invalid" : "This material is invalid",
        },
        "Syllabus" : {
            "invalid" : "This syllabus is invalid",
        }
    }
    def __init__(self, *args, **kwargs):
        self.VIEWS_BY_METHOD = {
            "GET" : self.get_syllabus_template,
            "GET" : self.get_syllabus_template_info,
            
        }
    def get_syllabus_template(self,request):
        all_syllabus_template = SyllabusTemplate.objects.all()
        result=[]
        if len(all_syllabus_template) == 0 :
            return JsonResponse({"Sucess" : False, "Code" : "Syllabus Template is empty!"})
        else :
            for syllabus_template in all_syllabus_template :
                class_id = syllabus_template.class_id
                try :
                    item = Class.objects.get(pk = class_id)
                except Class.DoesNotExist :
                    return self.json_error(field = "Class",code = "invalid")
                else :
                    result.append(item.parse_data())
        return JsonResponse({result})
    
    def get_syllabus_template_info(self,request):
        request_data = request.GET
        syllabus_template_id = request_data.get("template_id")
        try :
            syllabus_template = SyllabusTemplate.objects.get(pk = syllabus_template_id)
        except SyllabusTemplate.DoesNotExist :
            return self.json_error(field = "SyllabusTemplate" , code = "invalid")
        else :
            class_id = syllabus_template.class_id
            all_syllabus = Syllabus.objects.filter(class_id = class_id)
            if len(all_syllabus) == 0 :
                return self.json_error(field="Class",code = "invalid")
            else :
                result = []
                for item in all_syllabus:
                    all_material_in_item = Material.objects.filter(syllabus_id = item.syllabus_id)
                    for material in all_material_in_item :
                        result.append(material.parse_data())
                return JsonResponse({result})


                    

    
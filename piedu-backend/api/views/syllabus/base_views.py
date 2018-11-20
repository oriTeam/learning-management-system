from course.models import CourseCategory, Class, Schedule, ClassLecturer, ClassStudent, EnrollRequest, Subject
from syllabus.models import Material, Syllabus, SyllabusTemplate
from django.http import JsonResponse
from api.functions import string_to_boolean
from api.base import BaseManageView
from django.conf import settings
from syllabus.serializers import MaterialSerializer,SyllabusSerializer,SyllabusTemplateSerializer
User = settings.AUTH_USER_MODEL
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def get_material_info(request,id):
    try:
        material = Material.objects.get(pk=id)
    except Material.DoesNotExist:
        data = {
                "success" : False,
                "errors" : "Material are invalid"
        }
        return Response(data)
    else:
        serializers = MaterialSerializer(material)
        return Response(serializers.data) 

@api_view(['GET'])
def get_syllabus_material(request,id):
    materials = Material.objects.filter(syllabus__id = id)
    if len(materials) == 0 :
        data = {
                "success" : False,
                "errors" : "Syllabus is invalid"
        }
        return Response(data) 
    else :
        serializers = MaterialSerializer(materials,many=True)
        return Response(serializers.data)
    
@api_view(['GET'])
def get_class_syllabus(request,id):
    all_syllabus =Syllabus.objects.filter(own_class__id = id) 
    if len(all_syllabus) == 0 :
        data = {
                "success" : False,
                "errors" : "Class is invalid"
        }
        return Response(data) 
    else :
        serializers = SyllabusSerializer(all_syllabus,many=True)
        return Response(serializers.data)                        

@api_view(['GET'])
def get_syllabus_template(request,id):
    all_syllabus = Syllabus.objects.filter(own_class__id=id)
    if len(all_syllabus) == 0:
        data = {
                "success" : False,
                "errors" : "Template is invalid"
        }
        return Response(data)
    else:
        serializers = SyllabusSerializer(all_syllabus,many=True)
        return Response(serializers.data)

@api_view(['GET'])
def get_syllabus_template(request):
    all_syllabus_template = SyllabusTemplate.objects.all()
    if len(all_syllabus_template) ==0 :
        data = {
                "success" : False,
                "errors" : "Template is invalid"
        }
    else :
        serializers = SyllabusTemplateSerializer(all_syllabus_template,many=True)
        return Response(serializers.data)


class GetSyllabusTemplate(BaseManageView):
    error_messages = {
        "Class": {
            "invalid": "This class_id is invalid",
        },
        "User": {
            "invalid": "This user_id is invalid",
        },
        "Material": {
            "invalid": "This material is invalid",
        },
        "Syllabus": {
            "invalid": "This syllabus is invalid",
        }
    }

    def __init__(self, *args, **kwargs):
        self.VIEWS_BY_METHOD = {
            "GET": self.get_syllabus_template,

        }

    def get_syllabus_template(self, request):
        all_syllabus_template = SyllabusTemplate.objects.all()
        result = []
        if len(all_syllabus_template) == 0:
            return JsonResponse({"Sucess": False, "Code": "Syllabus Template is empty!"})
        else:
            for syllabus_template in all_syllabus_template:
                class_id = syllabus_template.class_id
                try:
                    item = Class.objects.get(pk=class_id)
                except Class.DoesNotExist:
                    return self.json_error(field="Class", code="invalid")
                else:
                    result.append(item.parse_info())
        return JsonResponse({"data": result})

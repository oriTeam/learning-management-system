from course.models import CourseCategory, Class, Schedule, ClassLecturer, ClassStudent, EnrollRequest, Subject
from syllabus.models import Material, Syllabus, SyllabusTemplate
from django.http import JsonResponse
from api.functions import string_to_boolean
from api.base import BaseManageView
from django.conf import settings
from syllabus.serializers import MaterialSerializer,SyllabusSerializer,SyllabusTemplateSerializer
User = settings.AUTH_USER_MODEL
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import permissions 

@api_view(['GET'])
@permission_classes((permissions.IsAuthenticated,))
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
@permission_classes((permissions.IsAuthenticated,))
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
@permission_classes((permissions.IsAuthenticated,))
def get_class_syllabus(request,id):
    all_syllabus =Syllabus.objects.filter(own_class__id = id) 
    
    if len(all_syllabus) == 0 :
        data = {
                "success" : False,
                "errors" : "Class is invalid"
        }
        return Response(data) 
    else :
        result = []
        for syllabus in all_syllabus:
            material=[]
            materials = Material.objects.filter(syllabus__id = syllabus.id)
            
            serializers = MaterialSerializer(materials,many=True)
            material.append(serializers.data)
            data = syllabus.parse_data()
            data['materials'] = material
            result.append(data)
        return Response(result) 
			

        serializers = SyllabusSerializer(all_syllabus,many=True)
        return Response(serializers.data)                        

@api_view(['GET'])
@permission_classes((permissions.IsAuthenticated,))
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
@permission_classes((permissions.IsAuthenticatedOrReadOnly,))
def get_all_syllabus_template(request):
    all_syllabus_template = SyllabusTemplate.objects.all()
    if len(all_syllabus_template) ==0 :
        data = {
                "success" : False,
                "errors" : "Template is invalid"
        }
    else :
        serializers = SyllabusTemplateSerializer(all_syllabus_template,many=True)
        return Response(serializers.data)

@api_view(['GET','POST'])
@permission_classes((permissions.IsAuthenticatedOrReadOnly,))
def save_syllabus_template(request):
    class_id = request.data.get('class_id')
    token = get_token_from_request(request)
    user = get_user_from_token(token)
    try :
        new_class = Class.objects.get(pk = class_id)
    except Class.DoesNotExist:
        return Response("Class is invalid")
    else:
        try :
            validate = ClassLecturer.objects.get(own_class__id= class_id,lecturer__id = user.id)
        except ClassLecturer.DoesNotExist :
            return Response("Access denied!")
        else:
            new_syllabus_template = SyllabusTemplate.objects.create( own_class= new_class,lecturer =user)
            new_syllabus_template.save()
            data = {
                "success": True,
                "message": " Template have been created successfully"
            }
            return Response(data)








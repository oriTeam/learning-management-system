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
from api.permission import  IsAuthenticated, IsAdmin, IsLecturer,IsMyOwnOrAdmin,IsStudent,IsAdminOrLecturer
from django.core.files.storage import FileSystemStorage


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
    
@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
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
            # material.append(serializers.data)
            data = syllabus.parse_data()
            data['materials'] = serializers.data
            data['dialog'] = False
            data['file'] = ''
            result.append(data)
        return Response(result) 
			

        # serializers = SyllabusSerializer(all_syllabus,many=True)
        # return Response(serializers.data)

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
@permission_classes((IsLecturer,))
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
@permission_classes((IsLecturer,))
def save_syllabus_template(request):
    class_id = request.data.get('class_id')
    # token = get_token_from_request(request)
    # user = get_user_from_token(token)
    try :
        new_class = Class.objects.get(pk = class_id)
    except Class.DoesNotExist:
        return Response("Class is invalid")
    else:
        # try :
        #     validate = ClassLecturer.objects.get(own_class__id= class_id,lecturer__id = user.id)
        # except ClassLecturer.DoesNotExist :
        #     return Response("Access denied!")
        # else:
        validated = SyllabusTemplate.objects.filter(own_class__id = class_id)
        if len(validated) == 0 :
            new_syllabus_template = SyllabusTemplate.objects.create( own_class= new_class)
            new_syllabus_template.save()
            data = {
                "success": True,
                "message": " Template have been created successfully"
            }
            return Response(data)
        else :
            return Response({"success" : False,"message" :"Template was exist"})

@api_view(['GET','POST'])
@permission_classes((IsLecturer,))
def add_template(request):
    class_id = request.data.get('class_id')
    try :
        new_class = Class.objects.get(pk = class_id)
    except Class.DoesNotExist :
        return Response("Class in invalid")
    else:
        delete_all_syllabus = Syllabus.objects.filter(own_class__id = class_id)
        if len(delete_all_syllabus) >0:
            for item in delete_all_syllabus :
                Material.objects.filter(syllabus__id =item.id).delete()
            for item in delete_all_syllabus :
                item.delete()
        template_class_id = request.data.get('template_class_id')
        all_syllabus = Syllabus.objects.filter(own_class__id = template_class_id)
        try :
            for syllabus in all_syllabus :
                new_syllabus =Syllabus.objects.create(own_class =new_class,content = syllabus.content,title = syllabus.title,week = syllabus.week)
                new_syllabus.save()
                all_material = Material.objects.filter(syllabus__id = syllabus.id)
                for material in all_material:
                    new_material = Material.objects.create(name = material.name,material_type = material.material_type,syllabus = new_syllabus,file = material.file)
                    new_material.save()
        except e:
            raise e
        else:
            return Response({"success" : True})
            
@api_view(['GET','POST'])
@permission_classes((IsLecturer,))
def edit_syllabus(request):
    content = request.data.get('content')
    title = request.data.get('title')
    syllabus_id = request.data.get('syllabus_id')
    try :
        syllabus = Syllabus.objects.get(pk = syllabus_id)
    except Syllabus.DoesNotExist :
        return Response("Syllabus is invalid")
    else:
        syllabus.content = content
        syllabus.title = title
        syllabus.save()
        return Response({"success" :True})

@api_view(['GET','POST'])
@permission_classes((IsLecturer,))
def add_material(request):
    file = request.FILES['file']
    name = file.name
    syllabus_id = request.data.get('syllabus_id')
    syllabus = Syllabus.objects.get(id=syllabus_id)
    fs = FileSystemStorage()
    filename = fs.save(name, file)
    new_material = Material.objects.create(syllabus = syllabus, file = file)
    new_material.save()
    return Response({"success" :True})


@api_view(['GET','POST'])
@permission_classes((permissions.IsAuthenticated,))
def delete_syllabus(request):
    syllabus_id = request.data.get('syllabus_id')
    all_material = Material.objects.filter(syllabus__id = syllabus_id).delete()
    Syllabus.objects.filter(syllabus_id).delete()
    return Response({"success" :True,"message" : "Done"})
    
@api_view(["GET", "POST"])
@permission_classes((IsAdminOrLecturer, ))
def remove_material(request):
    if request.method == "POST":
        material_id = request.data.get('material_id')
        try:
            material = Material.objects.get(id=material_id)
        except Material.DoesNotExist:
            return Response({"success": False, "code": "notexist"})
        else:
            material.delete()
            return Response({"success": True, "message": "Material have been removed"})
    errors = {'success': False, 'code': "failed"}
    return Response(errors)

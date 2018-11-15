from rest_framework import serializers
from syllabus.models import Material,Syllabus,SyllabusTemplate

class MaterialSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Material
        fields= '__all__'
        read_only_fields =()

class SyllabusSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Syllabus
        fields= '__all__'
        read_only_fields =()

class SyllabusTemplateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SyllabusTemplate
        fields= '__all__'
        read_only_fields =()

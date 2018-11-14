from rest_framework import serializers

class ClassInfoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    code = serializers.CharField(max_length=250)
    name = serializers.CharField(max_length=255)
    subject = serializers.CharField()
    students = serializers.IntegerField()
    avatar_path = serializers.CharField()
from rest_framework import serializers
from core.models import User


# COURSECATEGORY
class UserSerializerView(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','first_name','last_name','code','avatar','phone_number','gender','unit','birthday','address','group')
        read_only_fields = ()
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        read_only_fields =()


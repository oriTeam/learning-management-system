
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,)
from rest_framework import viewsets, generics, mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import permissions

from syllabus.models import Material,Syllabus,SyllabusTemplate
from syllabus.serializers import MaterialSerializer,SyllabusSerializer,SyllabusTemplateSerializer



class MaterialCreateView(generics.CreateAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer


class MaterialUpdateView(generics.RetrieveUpdateAPIView):
    queryset =Material.objects.all()
    serializer_class = MaterialSerializer
    lookup_field = 'id'


class MaterialDeleteView(generics.DestroyAPIView):
    queryset = Material.objects.all()
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)



class SyllabusCreateView(generics.CreateAPIView):
    queryset = Syllabus.objects.all()
    serializer_class = SyllabusSerializer


class SyllabusUpdateView(generics.RetrieveUpdateAPIView):
    queryset =Syllabus.objects.all()
    serializer_class = SyllabusSerializer
    lookup_field = 'id'


class SyllabusDeleteView(generics.DestroyAPIView):
    queryset = Syllabus.objects.all()
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)



class SyllabusTemplateCreateView(generics.CreateAPIView):
    queryset = SyllabusTemplate.objects.all()
    serializer_class = SyllabusTemplateSerializer


class SyllabusTemplateUpdateView(generics.RetrieveUpdateAPIView):
    queryset =SyllabusTemplate.objects.all()
    serializer_class = SyllabusTemplateSerializer
    lookup_field = 'id'


class SyllabusTemplateDeleteView(generics.DestroyAPIView):
    queryset =SyllabusTemplate.objects.all()
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

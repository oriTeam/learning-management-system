
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

from core.models import User
from core.serializers import UserSerializer



class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserUpdateView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'


class UserDeleteView(generics.DestroyAPIView):
    queryset = User.objects.all()
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)



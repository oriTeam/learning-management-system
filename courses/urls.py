from django.contrib import admin
from django.conf.urls import include, url
from django.views.generic import TemplateView
from django.urls import path, include
from django.conf import settings

from . import views

urlpatterns = [
    path('', views.index, name="hompage"),
]
from django.urls import include, path  # For django versions from 2.0 and up

from django.conf import settings
from . import views

urlpatterns = [
    path('', views.index, name="index"),
]
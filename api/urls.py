from django.urls import include, path
from . import views

app_name = "api"

urlpatterns = [
    path('auth',views.login, name="login"),
]
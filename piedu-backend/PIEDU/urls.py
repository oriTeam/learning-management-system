"""PIEDU URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path  # For django versions from 2.0 and up

from django.conf import settings
from . import views
from django.conf.urls.static import static
from rest_framework_jwt.views import obtain_jwt_token
# from machina.app import board


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include("api.urls")),
    path('account/', include("django.contrib.auth.urls")),
    path('', views.index, name='app'),
    path('login/', views.login, name='login'),
    path('course/my', views.my_course, name='my_course'),
    path('course/all', views.all_course, name='all_course'),
    path('contact/', views.contact, name='contact'),
    path('help/', views.help, name='help'),
    # path('forum/v1/', include(board.urls)),
    path('user',views.user,name = 'user'),
    path('course/1', views.inner_course, name='inner_course'),
    # path('restapi/', include('rest_framework.urls', namespace='rest_framework')),

    path('new/', views.new_class, name='newclass'),
    path('auth/', obtain_jwt_token),
]

# debug_toolbar_URL
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

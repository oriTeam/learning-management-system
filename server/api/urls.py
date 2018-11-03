from django.urls import include, path
from django.conf.urls import  url
from . import views

from rest_framework import routers

from .view.course.views import CourseListCreateAPIView, CourseDetailUpdateAPIView

from .view.course import (
    base_views as course_base_views,
)
from .view.syllabus import (
    base_views as syllabus_base_views,
)
from .view.user import (
    base_views as user_base_views,
)

app_name = "api"

router = routers.SimpleRouter()
router.register(r'courses', CourseListCreateAPIView, base_name="Courses")
router.register(r'courses', CourseDetailUpdateAPIView, base_name="Courses")




course_url_patterns= [
    path('',course_base_views._Course.as_view()),
    path('course_info', course_base_views._Course.as_view()),
    path('class_info',course_base_views._Class.as_view()),
]

syllabus_url_patterns= []

user_url_patterns=[]

urlpatterns = [
    path('auth',views.login, name="login"),
    path('course/',include(course_url_patterns)),
    path('syllabus/',include(syllabus_url_patterns)),
    path('user/',include(user_url_patterns)),
    path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]
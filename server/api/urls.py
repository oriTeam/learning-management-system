from django.urls import include, path
from django.conf.urls import  url
from . import views

from rest_framework import routers

# from .view.course.viewsets import CourseCategoryCreateView, CourseCategoryDetailView, SubjectDetailUpdateAPIView, SubjectListCreateAPIView, ClassDetailUpdateAPIView, ClassListCreateAPIView

from .view.course import (
    base_views as course_base_views,
)
from .view.syllabus import (
    base_views as syllabus_base_views,
)
from .view.user import (
    base_views as user_base_views,
)

# from .view.course import CourseCategoryDeleteView,CourseCayegoryUpdateView,CourseCategoryDetailView,CourseCategoryListView,CourseCategoryCreateView

from .view.course import  viewsets

app_name = "api"

router = routers.SimpleRouter()
# router.register(r'courses', CourseCategoryListCreateAPIView, base_name="Courses")
# router.register(r'courses', CourseCategoryDetailUpdateAPIView, base_name="Courses")
# router.register(r'subjects', SubjectDetailUpdateAPIView, base_name="Subjects")
# router.register(r'subjects', SubjectListCreateAPIView, base_name="Subjects")
# router.register(r'classes', ClassDetailUpdateAPIView, base_name="Subjects")
# router.register(r'classes', ClassListCreateAPIView, base_name="Subjects")

course_category_urlpatterns = [
    path('create', viewsets.CourseCategoryCreateView.as_view(), name="course_category_create"),
    path('list', viewsets.CourseCategoryListView.as_view(), name="course_category_list"),
    path('detail/<int:id>/', viewsets.CourseCategoryDetailView.as_view(), name="course_category_detail"),
    path('update/<int:id>/', viewsets.CourseCayegoryUpdateView.as_view(), name="course_category_update"),
    path('delete/<int:id>/', viewsets.CourseCategoryDeleteView.as_view(), name="course_category_delete"),
]


course_url_patterns= [
    # path('',course_base_views._Course.as_view()),
    path('course_info', course_base_views.GetCourses.as_view()),
    # path('class_info',course_base_views._Class.as_view()),
]

syllabus_url_patterns= []

user_url_patterns=[]

urlpatterns = [
    path('auth',views.login, name="login"),
    path('course/',include(course_url_patterns)),
    path('syllabus/',include(syllabus_url_patterns)),
    path('user/',include(user_url_patterns)),
    path('', include(router.urls)),
    path('course_category/', include(course_category_urlpatterns)),

    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]
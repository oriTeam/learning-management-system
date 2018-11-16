from django.urls import include, path
from django.conf.urls import  url
from . import auth_views
from rest_framework import routers

from .views.course import crud_functions

# from .views.course.viewsets import CourseCategoryCreateView, CourseCategoryDetailView, SubjectDetailUpdateAPIView, SubjectListCreateAPIView, ClassDetailUpdateAPIView, ClassListCreateAPIView

from .views.course import (
    base_views as course_base_views,
)
from .views.syllabus import (
    base_views as syllabus_base_views,
)
from .views.user import (
    base_views as user_base_views,
)

# from .views.course import CourseCategoryDeleteView,CourseCayegoryUpdateView,CourseCategoryDetailView,CourseCategoryListView,CourseCategoryCreateView

from .views.course import  viewsets as course_viewsets
from .views.user import viewsets as user_viewsets
from .views.syllabus import viewsets as syllabus_viewsets

app_name = "api"

router = routers.SimpleRouter()
# router.register(r'courses', CourseCategoryListCreateAPIView, base_name="Courses")
# router.register(r'courses', CourseCategoryDetailUpdateAPIView, base_name="Courses")
# router.register(r'subjects', SubjectDetailUpdateAPIView, base_name="Subjects")
# router.register(r'subjects', SubjectListCreateAPIView, base_name="Subjects")
# router.register(r'classes', ClassDetailUpdateAPIView, base_name="Subjects")
# router.register(r'classes', ClassListCreateAPIView, base_name="Subjects")

course_category_urlpatterns = [
    path('create', course_viewsets.CourseCategoryCreateView.as_view(), name="course_category_create"),
    # path('list', viewsets.CourseCategoryListView.as_view(), name="course_category_list"),
    path('list',course_base_views.course_category_list_view),
    # path('detail/<int:id>/', viewsets.CourseCategoryDetailView.as_view(), name="course_category_detail"),
    path('detail/<int:id>/', course_base_views.course_category_detail),
    path('update/<int:id>/', course_viewsets.CourseCayegoryUpdateView.as_view(), name="course_category_update"),
    path('delete/<int:id>/', course_viewsets.CourseCategoryDeleteView.as_view(), name="course_category_delete"),
    path('<int:id>/get_subject',course_base_views.get_subject),
]

subject_urlpatterns = [
    path('create', course_viewsets.SubjectCreateView.as_view(), name="subject_create"),
    path('list',course_base_views.subject_list_view),
    # path('list', viewsets.SubjectListView.as_view(), name="subject_list"),
    # path('get_subject_from_course_category/<int:id>/', viewsets.SubjectFromCourseListView.as_view(), name="subject_detail_from_course"),
    # path('detail/<int:id>/', viewsets.SubjectDetailView.as_view(), name="subject_detail"),
    path('detail/<int:id>/', course_base_views.subject_detail),
    path('update/<int:id>/', course_viewsets.SubjectUpdateView.as_view(), name="subject_update"),
    path('delete/<int:id>/', course_viewsets.SubjectDeleteView.as_view(), name="subject_delete"),
    path('<int:id>/get_class',course_base_views.get_class),
]

class_urlpatterns = [
    path('create', course_viewsets.ClassCreateView.as_view(), name="class_create"),
    path('list',course_base_views.class_list_view),
    # path('list', viewsets.ClassListView.as_view(), name="class_list"),
    path('detail/<int:id>/', course_base_views.class_detail),
    # path('detail/<int:id>/', viewsets.ClassDetailView.as_view(), name="class_detail"),
    path('update/<int:id>/', course_viewsets.ClassUpdateView.as_view(), name="class_update"),
    path('delete/<int:id>/', course_viewsets.ClassDeleteView.as_view(), name="class_delete"),
    path('a',course_base_views.test),
    path('<int:id>/get_student',course_base_views.get_student),
    path('<int:id>/get_enroll_request',course_base_views.get_enroll_request),
    path('<int:id>/get_current_class',course_base_views.get_current_class),
    path('<int:id>/get_past_class',course_base_views.get_past_class),
    path('all/', crud_functions.get_all_class_info),
    path('info/', crud_functions.get_full_class_info),

]

class_lecturer_urlpatterns = [
    path('create', course_viewsets.ClassLecturerCreateView.as_view(), name="class_lecturer_create"),
    path('update/<int:id>/', course_viewsets.ClassLecturerUpdateView.as_view(), name="class_lecturer_update"),
    path('delete/<int:id>/', course_viewsets.ClassLecturerDeleteView.as_view(), name="class_lecturer_delete"),
]

class_student_urlpatterns = [
    path('create', course_viewsets.ClassStudentCreateView.as_view(), name="class_student_create"),
    path('update/<int:id>/', course_viewsets.ClassStudentUpdateView.as_view(), name="class_student_update"),
    path('delete/<int:id>/', course_viewsets.ClassStudentDeleteView.as_view(), name="class_student_delete"),
]

enroll_request_urlpatterns = [
    path('create', course_viewsets.ClassCreateView.as_view(), name="class_create"),
    path('update/<int:id>/', course_viewsets.ClassUpdateView.as_view(), name="class_update"),
    path('delete/<int:id>/', course_viewsets.ClassDeleteView.as_view(), name="class_delete"),
]

schedule_urlpatterns = [
    path('create', course_viewsets.ScheduleCreateView.as_view(), name="schedule_create"),
    # path('list', viewsets.ScheduleListView.as_view(), name="schedule_list"),
    # path('detail/<int:id>/', viewsets.ScheduleDetailView.as_view(), name="schedule_detail"),
    path('update/<int:id>/', course_viewsets.ScheduleUpdateView.as_view(), name="schedule_update"),
    path('delete/<int:id>/', course_viewsets.ScheduleDeleteView.as_view(), name="schedule_delete"),
]




syllabus_url_patterns= [
    path('create/<int:id>/', syllabus_viewsets.SyllabusCreateView.as_view(), name="syllabus_createl"),
    path('update/<int:id>/', syllabus_viewsets.SyllabusUpdateView.as_view(), name="syllabus_update"),
    path('delete/<int:id>/', syllabus_viewsets.SyllabusDeleteView.as_view(), name="syllabus_delete"),
]
material_url_patterns=[
    path('create/<int:id>/', syllabus_viewsets.MaterialCreateView.as_view(), name="material_create"),
    path('update/<int:id>/', syllabus_viewsets.MaterialUpdateView.as_view(), name="material_update"),
    path('delete/<int:id>/', syllabus_viewsets.MaterialDeleteView.as_view(), name="material_delete"),
]
syllabus_template_url_patterns=[
    path('create/<int:id>/', syllabus_viewsets.SyllabusTemplateCreateView.as_view(), name="syllabus_template_create"),
    path('update/<int:id>/', syllabus_viewsets.SyllabusTemplateUpdateView.as_view(), name="syllabus_template_update"),
    path('delete/<int:id>/', syllabus_viewsets.SyllabusTemplateDeleteView.as_view(), name="syllabus_template_delete"),
]

user_url_patterns=[
    path('detail/<int:id>/',user_base_views.get_user_detail_view),
    # path('create/<int:id>/', user_viewsets.UserCreateView.as_view(), name="user_detail"),
    # path('update/<int:id>/', user_viewsets.UserUpdateView.as_view(), name="user_update"),
    # path('delete/<int:id>/', user_viewsets.UserDeleteView.as_view(), name="user_delete"),
]

urlpatterns = [
    path('auth', auth_views.login, name="login"),
    # path('course/',include(course_url_patterns)),
    path('syllabus/',include(syllabus_url_patterns)),
    path('material/',include(material_url_patterns)), 
    path('syllabus_template/',include(syllabus_template_url_patterns)),
    path('user/',include(user_url_patterns)),
    # path('', include(router.urls)),
    path('course_category/', include(course_category_urlpatterns)),
    path('subject/', include(subject_urlpatterns)),
    path('class/', include(class_urlpatterns)),
    path('class-lecturer/', include(class_lecturer_urlpatterns)),
    path('class-student/', include(class_student_urlpatterns)),
    path('enroll_request/', include(enroll_request_urlpatterns)),
    path('schedule/', include(schedule_urlpatterns)),

]
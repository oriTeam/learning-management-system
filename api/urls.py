from django.urls import include, path
from . import views
from . import view
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

course_url_patterns= [
    path('',course_base_views.Course_.get_courses),
    path('course_info', course_base_views.Course_.as_view()),
]
syllabus_url_patterns= []
user_url_patterns=[]
urlpatterns = [
    path('auth',views.login, name="login"),
    path('course/',include(course_url_patterns)),
    path('syllabus/',include(syllabus_url_patterns)),
    path('user/',include(user_url_patterns)),
]
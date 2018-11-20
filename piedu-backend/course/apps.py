from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class CourseConfig(AppConfig):
    name = 'course'
    verbose_name = _('Course')
    verbose_name_plural = _('Courses')

    def ready(self):
        import course.signals
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class SyllabusConfig(AppConfig):
    name = 'syllabus'
    verbose_name = _('Syllabus')
    verbose_name_plural = _('Syllabuses')

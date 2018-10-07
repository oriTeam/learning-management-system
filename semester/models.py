from django.db import models
from django.utils.translation import gettext as _

# Create your models here.

class Semester(models.Model):
    name = models.CharField(max_length=50, verbose_name=_("Name"))
    semester_code = models.CharField(max_length=20, verbose_name=_("Semester Code"))
    description = models.TextField(blank=True, null=True, verbose_name=_("Description"))

    class Meta:
        db_table = 'semester'
        ordering = ['id']
        verbose_name = _("Semester")
        verbose_name_plural = _("Semesters")

    def __str__(self):
        return self.name


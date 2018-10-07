from django.db import models
from django.utils.translation import gettext as _

# Create your models here.

class Faculty(models.Model):
    name = models.CharField(max_length=50, verbose_name=_("Name"))
    code = models.CharField(max_length=10, null=True, verbose_name=_("Faculty's Code"))

    class Meta:
        db_table = 'faculty'
        ordering = ['id']
        verbose_name = _("Faculty")
        verbose_name_plural = _('Faculties')

    def __str__(self):
        return self.name
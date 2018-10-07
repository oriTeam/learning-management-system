from django.db import models
from django.utils.translation import gettext as _
from django.conf import settings


# Create your models here.

class Document(models.Model):
    name = models.CharField(max_length=50, verbose_name=_("Document's Name"))
    description = models.TextField(null=True, verbose_name=_("Document's Description"))
    type = models.CharField(max_length=10, verbose_name=_("Document's Type"))
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='document_set', null=True, verbose_name=_('Author'))

    class Meta:
        db_table = 'document'
        ordering = ['id']
        verbose_name = _("Document")
        verbose_name_plural = _("Documents")

    def __str__(self):
        return self.name
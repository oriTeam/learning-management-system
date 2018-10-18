from django.db import models
from django.utils.translation import gettext as _
# Create your models here.
class Syllabus(models.Model):
    name = models.TextField(unique = True, verbose_name = _("Syllabus"))
    

    class Meta:
        db_table = "syllabus"
        ordering = ["id"]
        verbose_name = _("Syllabus")
        verbose_name_plural =_("Syllabus")
    def __str__(self):
        return "Syllabus : {}".format(self.name)

class Material(models.Model):
    name = models.TextField(verbose_name = _("Material's Name"))
    syllabus_id = models.ForeignKey(Syllabus,on_delete = models.CASCADE , verbose_name = _("Syllabus"))
    material_type = models.TextField(verbose_name =_("Material's Type")) 
    
    class Meta:
        db_table = "material"
        ordering = ["id"]
        verbose_name = _("Material")
        verbose_name_plural = _("Materials")

    def __str__(self):
        return "Material : {}".format(self.name)



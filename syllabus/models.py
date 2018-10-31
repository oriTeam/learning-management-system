from django.db import models
from django.utils.translation import gettext as _
from course.models import Class


class Syllabus(models.Model):
    title = models.CharField(max_length=100, default="", verbose_name=_("Syllabus's title"))
    content = models.TextField(default="",verbose_name=_("Syllabus's content"))
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE, default="", verbose_name=_('Class'))
    week = models.CharField(max_length=10, default="", verbose_name=_('Week'))

    class Meta:
        db_table = "syllabus"
        ordering = ["id"]
        verbose_name = _("Syllabus")
        verbose_name_plural = _("Syllabus")

    def __str__(self):
        return "Syllabus : {}".format(self.name)

    def parse_data(self):
        data = {
            "id" : self.id,
            "title" : self.title,
            "content" : self.content,
            "class_id" : self.class_id,
            "week" : self.week
            
        }
        return data


class Material(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Material's Name"))
    syllabus_id = models.ForeignKey(Syllabus, on_delete=models.CASCADE, verbose_name=_("Syllabus"))
    material_type = models.CharField(max_length=255, verbose_name=_("Material's Type"))
    file = models.FileField(blank=False, null=True)

    class Meta:
        db_table = "material"
        ordering = ["id"]
        verbose_name = _("Material")
        verbose_name_plural = _("Materials")

    def __str__(self):
        return "Material : {}".format(self.name)

    def parse_data(self):
        data ={
            "id" : self.id,
            "name" : self.name,
            "syllabus_id" : self.syllabus_id,
            "material_type" : self.material_type
        }
        return data

class ClassSyllabus(models.Model):
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE, default="", verbose_name=_("Class"))
    syllabus_id = models.ForeignKey(Syllabus, on_delete=models.CASCADE, verbose_name=_("Syllabus"))

    class Meta:
        db_table = 'class_syllabus'
        ordering = ["id"]
        verbose_name = _("Class - Syllasbus")
        verbose_name_plural = _("Classes - Syllabus")

    def __str__(self):
        return "Class : {} | Syllabus : {}".format(self.class_id.name, self.syllabus_id.name)

class SyllabusTemplate(models.Model):
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE, default="", verbose_name=_('Class'))

    class Meta:
        db_table = 'syllbus_template'
        ordering = ['id']
        verbose_name = _('Syllabus Template')
        verbose_name_plural = _('Syllabus Templates')

    def __str__(self):
        return "Syllabus Template: {}".format(self.class_id.name)

from django.db import models
from django.utils.translation import gettext as _
from course.models import Class
from django.conf import settings

FILE_TYPE_CHOICES = (
    (_('PDF'), _('PDF')),
    (_('DOC/DOCX'), _('DOC/DOCX')),
    (_('IMG/PNG/SVG/GIF'), _('IMG/PNG/SVG/GIF')),
    (_('MP4/AVI'), _('MP4/AVI')),
    (_('MP3'), _('MP3')),
    (_('Other'), _('Other'))
)



class Syllabus(models.Model):
    title = models.CharField(max_length=100, default="", verbose_name=_("Syllabus's title"))
    content = models.TextField(default="",verbose_name=_("Syllabus's content"))
    own_class = models.ForeignKey(Class, on_delete=models.CASCADE, null=True, related_name='syllabuses_set', verbose_name=_('Class'))
    week = models.CharField(max_length=10, default="", verbose_name=_('Week'))

    class Meta:
        db_table = "syllabus"
        ordering = ["id"]
        verbose_name = _("Syllabus")
        verbose_name_plural = _("Syllabus")

    def __str__(self):
        # return "Syllabus : {}".format(self.title + " " + self.own_class.code)
        return "Syllabus : {}".format(self.title)

    def parse_data(self):
        data = {
            "id" : self.id,
            "title" : self.title,
            "content" : self.content,
            "class_id" : self.own_class.id,
            "week" : self.week
            
        }
        return data




class Material(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Material's Name"))
    syllabus = models.ForeignKey(Syllabus, on_delete=models.CASCADE, related_name='materials_set', verbose_name=_("Syllabus"))
    material_type = models.CharField(choices=FILE_TYPE_CHOICES, max_length=255, verbose_name=_("Material's Type"))
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
            "syllabus_id" : self.syllabus.id,
            "material_type" : self.material_type,
            "file" : self.file
        }
        return data

class SyllabusTemplate(models.Model):
    own_class = models.ForeignKey(Class, on_delete=models.CASCADE, null=True, related_name='lecturers_in_template_set', verbose_name=_('Class'))
    # lecturer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, related_name='classes_in_template_set', verbose_name=_('Lecturer'))

    class Meta:
        db_table = 'syllabus_template'
        ordering = ['id']
        verbose_name = _('Syllabus Template')
        verbose_name_plural = _('Syllabus Templates')

    def __str__(self):
        return "Syllabus Template: {}".format(self.own_class.name)


from django.db import models
from .apps import APP_NAME
from django.utils.translation import gettext as _
from utility.models import LinkHelper,ImageHelper
from tinymce.models import HTMLField
from django.shortcuts import reverse
class Page(models.Model,LinkHelper):
    class_name="page"
    app_name=APP_NAME

    title=models.CharField(_("title"), max_length=50)
    short_description=HTMLField(_("short_description"),null=True,blank=True, max_length=5000)
    description=HTMLField(_("description"),null=True,blank=True, max_length=50000)

    class Meta:
        verbose_name = _("Page")
        verbose_name_plural = _("Pages")

    def __str__(self):
        return self.title

    def save(self,*args, **kwargs):
        if self.class_name is None or self.class_name=="":
            self.class_name=class_name
        if self.app_name is None or self.app_name=="":
            self.app_name=app_name
        return super(Page,self).save()



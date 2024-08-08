from django.db import models
from django.utils.translation import gettext as _
from .enums import *
from core.models import LinkHelper
from django.conf import settings
from .apps import APP_NAME


class Process(models.Model,LinkHelper):
    app_name=APP_NAME
    class_name="process"
    priority=models.IntegerField(_("priority"),default=100)
    title=models.CharField(_("title"), max_length=50)
    process_app_name=models.CharField(_("app_name"),choices=AppNameEnum.choices, max_length=50)
    groups=models.ManyToManyField("auth.group",blank=True, verbose_name=_("groups"))
    # group=models.ForeignKey("auth.group", verbose_name=_("group"), on_delete=models.CASCADE)
    class Meta:
        verbose_name = _("Process")
        verbose_name_plural = _("Processs")

    def __str__(self):
        return self.title 

from django.db.models import TextChoices
from django.utils.translation import gettext as _
class AppNameEnum(TextChoices):
    accounting="حسابداری",_("حسابداری")
    projectmanagement="مدیریت پروژه",_("مدیریت پروژه")
from django.db import models
from core.models import LinkHelper
from .apps import APP_NAME
from django.utils.translation import gettext as _


class Customer(models.Model,LinkHelper):

    app_name=APP_NAME
    class_name="customer"

    class Meta:
        verbose_name = _("Customer")
        verbose_name_plural = _("Customers")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Customer_detail", kwargs={"pk": self.pk})

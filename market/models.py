from django.db import models
from core.models import LinkHelper
from .apps import APP_NAME
from django.utils.translation import gettext as _



class Customer(models.Model,LinkHelper):
    account=models.ForeignKey("accounting.account", verbose_name=_("account"), on_delete=models.PROTECT)
    app_name=APP_NAME
    class_name="customer"

    class Meta:
        verbose_name = _("Customer")
        verbose_name_plural = _("Customers")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Customer_detail", kwargs={"pk": self.pk})



class Supplier(models.Model,LinkHelper):
    account=models.ForeignKey("accounting.account", verbose_name=_("account"), on_delete=models.PROTECT)
    app_name=APP_NAME
    class_name="customer"

    class Meta:
        verbose_name = _("Customer")
        verbose_name_plural = _("Customers")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Customer_detail", kwargs={"pk": self.pk})



class ProductSpecification(models.Model,LinkHelper):
    product=models.ForeignKey("accounting.product", verbose_name=_("product"), on_delete=models.CASCADE)
    category=models.CharField(_("category"), max_length=200)
    name=models.CharField(_("name"), max_length=200)
    value=models.CharField(_("value"), max_length=200)
    app_name=APP_NAME
    class_name="productspecification"
    
    class Meta:
        verbose_name = _("ProductSpecification")
        verbose_name_plural = _("ProductSpecifications")

    def __str__(self):
        return f"{self.product.title}:{self.category}:{self.name}:{self.value}"


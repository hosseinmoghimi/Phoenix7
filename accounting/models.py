from django.db import models
from core.models import LinkHelper,Page
from .apps import APP_NAME
from django.utils.translation import gettext as _
from .enums import *
IMAGE_FOLDER=APP_NAME+"/images/"
from phoenix.server_settings import MEDIA_URL
# Create your models here.
class Account(models.Model,LinkHelper):
    title=models.CharField(_("title"), max_length=500)
    profile=models.ForeignKey("authentication.profile",null=True,blank=True, verbose_name=_("profile"), on_delete=models.SET_NULL)
    balance=models.IntegerField("balance",default=0)
    logo_origin=models.ImageField(_("logo"), upload_to=IMAGE_FOLDER+"account", height_field=None, width_field=None, max_length=None)
    class_name="account"
    app_name=APP_NAME
    @property
    def logo(self):
        return f"{MEDIA_URL}{self.logo_origin}"

    class Meta:
        verbose_name = _("Account")
        verbose_name_plural = _("Accounts")

    def __str__(self):
        return self.title
 

 
class TransactionCategory(models.Model,LinkHelper):
    class_name="transactioncategory"
    app_name=APP_NAME
    title=models.CharField(_("title"), max_length=50)
    color_origin=models.CharField(_("color"),choices=ColorEnum.choices,null=True,blank=True, max_length=50)
    @property
    def color(self):
        if self.color_origin:
            return self.color_origin
        if self.title=="هزینه":
            return "danger"
        return 'primary'
    class Meta:
        verbose_name = 'TransactionCategory'
        verbose_name_plural = 'TransactionCategories' 
    def __str__(self):
        return self.title
 
class Transaction(Page):
    class_name="transaction"
    app_name=APP_NAME
    pay_from=models.ForeignKey("account",related_name="transactions_from", verbose_name=_("پرداخت کننده"), on_delete=models.PROTECT)
    pay_to=models.ForeignKey("account", related_name="transactions_to",verbose_name=_("دریافت کننده"), on_delete=models.PROTECT)
    creator=models.ForeignKey("authentication.profile",null=True,blank=True, verbose_name=_("ثبت شده توسط"), on_delete=models.SET_NULL)
    status=models.CharField(_("وضعیت"),choices=TransactionStatusEnum.choices,default=TransactionStatusEnum.DRAFT, max_length=50)
    category=models.ForeignKey("transactioncategory",null=True,blank=True, verbose_name=_("دسته بندی"), on_delete=models.SET_NULL)
    amount=models.IntegerField(_("مبلغ"),default=0)
    payment_method=models.CharField(_("نوع پرداخت"),choices=PaymentMethodEnum.choices,default=PaymentMethodEnum.DRAFT, max_length=50)
    transaction_datetime=models.DateTimeField(_("تاریخ تراکنش"), auto_now=False, auto_now_add=False)
    

    

    class Meta:
        verbose_name = _("Transaction")
        verbose_name_plural = _("Transactions")

    def __str__(self):
        return self.title
 


class TransactionPrint(models.Model):
    transaction=models.ForeignKey("transaction", verbose_name=_("تراکنش"), on_delete=models.CASCADE)
    print_datetime=models.DateTimeField(_("تاریخ چاپ"),null=True,blank=True, auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = _("TransactionPrint")
        verbose_name_plural = _("TransactionPrints")

    def __str__(self):
        print_datetime=PersianCalendar().from_gregorian(self.print_datetime)
        return f"{self.transaction}   @  {print_datetime} "
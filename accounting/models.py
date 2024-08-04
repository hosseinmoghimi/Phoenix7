from django.db import models
from core.models import LinkHelper,Page
from .apps import APP_NAME
from django.utils.translation import gettext as _
from .enums import *
IMAGE_FOLDER=APP_NAME+"/images/"
from phoenix.server_settings import MEDIA_URL,STATIC_URL
# Create your models here.
class Account(models.Model,LinkHelper):
    title=models.CharField(_("title"), max_length=500)
    mobile=models.CharField(_("mobile"),null=True,blank=True, max_length=50)
    tel=models.CharField(_("tel"),null=True,blank=True, max_length=50)
    description=models.CharField(_("description"),null=True,blank=True, max_length=500)
    profile=models.ForeignKey("authentication.profile",null=True,blank=True, verbose_name=_("profile"), on_delete=models.SET_NULL)
    balance=models.IntegerField("balance",default=0)
    logo_origin=models.ImageField(_("logo"), upload_to=IMAGE_FOLDER+"account", height_field=None, width_field=None, max_length=None)
    class_name="account"
    app_name=APP_NAME
    @property
    def logo(self):
        if not self.logo_origin :
            return f"{STATIC_URL}{APP_NAME}/img/pages/thumbnail/account.png"
        return f"{MEDIA_URL}{self.logo_origin}"

        # if self.logo_origin:
        #     return MEDIA_URL+str(self.logo_origin)
        # if self.profile is not None:
        #     return self.profile.image
        # return f"{STATIC_URL}{self.app_name}/img/{self.class_name}.png"
    class Meta:
        verbose_name = _("Account")
        verbose_name_plural = _("Accounts")

    def __str__(self):
        return self.title
 

 
class EventCategory(models.Model,LinkHelper):
    class_name="eventcategory"
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
        verbose_name = 'EventCategory'
        verbose_name_plural = 'EventCategories' 
    def __str__(self):
        return self.title
 
class Event(Page):
    class_name="event"
    app_name=APP_NAME
    pay_from=models.ForeignKey("account",related_name="events_from", verbose_name=_("پرداخت کننده"), on_delete=models.PROTECT)
    pay_to=models.ForeignKey("account", related_name="events_to",verbose_name=_("دریافت کننده"), on_delete=models.PROTECT)
    creator=models.ForeignKey("authentication.profile",null=True,blank=True, verbose_name=_("ثبت شده توسط"), on_delete=models.SET_NULL)
    status=models.CharField(_("وضعیت"),choices=EventStatusEnum.choices,default=EventStatusEnum.DRAFT, max_length=50)
    category=models.ForeignKey("eventcategory",null=True,blank=True, verbose_name=_("دسته بندی"), on_delete=models.SET_NULL)
    amount=models.IntegerField(_("مبلغ"),default=0)
    payment_method=models.CharField(_("نوع پرداخت"),choices=PaymentMethodEnum.choices,default=PaymentMethodEnum.DRAFT, max_length=50)
    event_datetime=models.DateTimeField(_("تاریخ تراکنش"), auto_now=False, auto_now_add=False)
    

    

    class Meta:
        verbose_name = _("Event")
        verbose_name_plural = _("Events")

    def __str__(self):
        return self.title
 


class EventPrint(models.Model):
    event=models.ForeignKey("event", verbose_name=_("تراکنش"), on_delete=models.CASCADE)
    print_datetime=models.DateTimeField(_("تاریخ چاپ"),null=True,blank=True, auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = _("EventPrint")
        verbose_name_plural = _("EventPrints")

    def __str__(self):
        print_datetime=PersianCalendar().from_gregorian(self.print_datetime)
        return f"{self.event}   @  {print_datetime} "

class ProductOrService(Page):
    barcode=models.CharField(_("بارکد"),null=True,blank=True, max_length=100)

    

    class Meta:
        verbose_name = _("ProductOrService")
        verbose_name_plural = _("ProductOrServices")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("ProductOrService_detail", kwargs={"pk": self.pk})



class Product(ProductOrService):

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")
 
        
    def save(self,*args, **kwargs):
        if self.class_name is None or self.class_name=="":
            self.class_name='product'
        if self.app_name is None or self.app_name=="":
            self.app_name=APP_NAME
        return super(Product,self).save(*args, **kwargs)
   
 
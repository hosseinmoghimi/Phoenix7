from django.db import models
from core.models import LinkHelper,Page
from .apps import APP_NAME
from django.utils.translation import gettext as _
from .enums import *
from utility.calendar import PersianCalendar
IMAGE_FOLDER=APP_NAME+"/images/"
from phoenix.server_settings import MEDIA_URL,STATIC_URL 
# Create your models here.
from django.contrib.auth.models import User,Group
class Access(models.Model):

    

    class Meta:
        verbose_name = _("Access")
        verbose_name_plural = _("Accesss")

    def __str__(self):
        return self.name
 
class AccountGroup(models.Model,LinkHelper):
    name=models.CharField(_("name"), max_length=200)
    code=models.CharField(_("code"), max_length=200)
    bedehkar=models.IntegerField(_("bedehkar"),default=0)
    bestankar=models.IntegerField(_("bestankar"),default=0)
    balance=models.IntegerField("balance",default=0)
    
    # basic_accounts=models.ManyToManyField("basicaccount",blank=True, verbose_name=_("حساب های کل"))
    class_name="accountgroup"
    app_name=APP_NAME  
    

    
    def normalize_total(self):
        bedehkar=0
        bestankar=0
        balance=0
        for basic_account in self.basicaccount_set.all(): 
            basic_account.normalize_total()
           

            bedehkar+=basic_account.bedehkar
            bestankar+=basic_account.bestankar
        balance=bestankar-bedehkar
        self.bedehkar=bedehkar
        self.bestankar=bestankar
        self.balance=balance
        self.save() 

  
    @property
    def basic_accounts(self):
        return self.basicaccount_set.all()
    
    @property
    def title(self):
        return self.name
    class Meta:
        verbose_name = _("AccountGroup")
        verbose_name_plural = _("AccountGroups")

    def __str__(self):
        return self.code+" "+self.name
 
class BasicAccount(models.Model,LinkHelper):
    name=models.CharField(_("name"), max_length=200)
    code=models.CharField(_("code"), max_length=200)
    account_group=models.ForeignKey("accountgroup", verbose_name=_("account group"), on_delete=models.CASCADE)
    # moein_accounts=models.ManyToManyField("moeinaccount",blank=True, verbose_name=_("حساب های معین"))
  
    bedehkar=models.IntegerField(_("bedehkar"),default=0)
    bestankar=models.IntegerField(_("bestankar"),default=0)
    balance=models.IntegerField("balance",default=0)
   
    class_name="basicaccount"
    app_name=APP_NAME
 
    @property
    def title(self):
        return self.name
    @property
    def moein_accounts(self):
        return self.moeinaccount_set.all()
   

         
 
    def normalize_total(self):
        bedehkar=0
        bestankar=0
        balance=0
        for moein_account in self.moeinaccount_set.all():
            moein_account.normalize_total()
           
            bedehkar+=moein_account.bedehkar
            bestankar+=moein_account.bestankar
        balance=bestankar-bedehkar
        self.bedehkar=bedehkar
        self.bestankar=bestankar
        self.balance=balance
        self.save() 
    class Meta:
        verbose_name = _("BasicAccount")
        verbose_name_plural = _("BasicAccounts")

    def __str__(self):
        return str(self.account_group)+" " + self.code+" "+self.name
class MoeinAccount(models.Model,LinkHelper):


    class_name="moeinaccount"
    app_name=APP_NAME

    name=models.CharField(_("name"), max_length=200)
    code=models.CharField(_("code"), max_length=200)
    # accounts=models.ManyToManyField("account", verbose_name=_("حساب ها"))
    basic_account=models.ForeignKey("basicaccount", verbose_name=_("basicaccount"), on_delete=models.CASCADE)
    bedehkar=models.IntegerField(_("bedehkar"),default=0)
    bestankar=models.IntegerField(_("bestankar"),default=0)
    balance=models.IntegerField("balance",default=0)
         
    
    def normalize_total(self):
        bedehkar=0
        bestankar=0
        balance=0
        for account in self.account_set.all():
            account.normalize_total()
            
            bedehkar+=account.bedehkar
            bestankar+=account.bestankar
        balance=bestankar-bedehkar
        self.bedehkar=bedehkar
        self.bestankar=bestankar
        self.balance=balance
        self.save() 

 
    @property
    def title(self):
        return self.code+" "+self.name

    @property
    def accounts(self):
        return self.account_set.all()

    def save(self):
        super(MoeinAccount,self).save()
    class Meta:
        verbose_name = _("MoeinAccount")
        verbose_name_plural = _("MoeinAccounts")

    def __str__(self):
        return str(self.basic_account)+" "+self.code+" "+self.name
class Account(models.Model,LinkHelper):
    moein_account=models.ForeignKey("moeinaccount", verbose_name=_("moein account"), on_delete=models.CASCADE)
    code=models.CharField(_("code"), max_length=200)
    
    title=models.CharField(_("title"), max_length=500)
    mobile=models.CharField(_("mobile"),null=True,blank=True, max_length=50)
    tel=models.CharField(_("tel"),null=True,blank=True, max_length=50)
    description=models.CharField(_("description"),null=True,blank=True, max_length=500)
    profile=models.ForeignKey("authentication.profile",null=True,blank=True, verbose_name=_("profile"), on_delete=models.SET_NULL)
    logo_origin=models.ImageField(_("logo"),blank=True,null=True, upload_to=IMAGE_FOLDER+"account", height_field=None, width_field=None, max_length=None)
    bedehkar=models.IntegerField(_("bedehkar"),default=0)
    bestankar=models.IntegerField(_("bestankar"),default=0)
    balance=models.IntegerField("balance",default=0)
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
        return self.moein_account.title+" " +self.title
    def normalize_total(self):
        balance=0
        bestankar=0
        bedehkar=0
        for ac_doc_line in AccountingDocumentLine.objects.filter(account_id=self.id):
            bedehkar+=ac_doc_line.bedehkar
            bestankar+=ac_doc_line.bestankar
        self.balance=bestankar-bedehkar
        self.bedehkar=bedehkar
        self.bestankar=bestankar
        super(Account,self).save()
   
class FinancialDocument(LinkHelper,models.Model):
    account=models.ForeignKey("account", verbose_name=_("account"), on_delete=models.PROTECT)
    event=models.ForeignKey("event", verbose_name=_("event"), on_delete=models.PROTECT)
    
    
    

    class_name="financialdocument"
    app_name=APP_NAME    

    @property
    def amount(self):
        return self.event.amount

    @property
    def event_datetime(self):
        return self.event.event_datetime

    @property
    def status(self):
        return self.event.status
    class Meta:
        verbose_name = _("FinancialDocument")
        verbose_name_plural = _("FinancialDocuments")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("FinancialDocument_detail", kwargs={"pk": self.pk})

class AccountingDocument(models.Model,LinkHelper):
    title=models.CharField(_("title"), max_length=500)
    # lines=models.ManyToManyField("accountingdocumentline",blank=True, verbose_name=_("accounting document lines "))
    # events=models.ManyToManyField("event",blank=True, verbose_name=_("events"))
    
    @property 
    def lines(self):
        return self.accountingdocumentline_set.all()


    def save(self):
        super(AccountingDocument,self).save()


    class_name="accountingdocument"
    app_name=APP_NAME    
    class Meta:
        verbose_name = _("AccountingDocument")
        verbose_name_plural = _("AccountingDocuments")

    def __str__(self):
        return self.title
 
class AccountingDocumentLine(models.Model,LinkHelper):
    accounting_document=models.ForeignKey("accountingdocument", verbose_name=_("accountingdocument"), on_delete=models.CASCADE)
    account=models.ForeignKey("account", verbose_name=_("account"), on_delete=models.PROTECT)
    event=models.ForeignKey("event", verbose_name=_("event"), on_delete=models.PROTECT)
    bedehkar=models.IntegerField(_("بدهکار"),default=0)
    bestankar=models.IntegerField(_("بستانکار"),default=0)
    balance=models.IntegerField(_("بالانس"),default=0)
    def save(self):
        if self.account==self.event.pay_from:
            self.bestankar=self.event.amount
            self.bedehkar=0
            self.balance=self.event.amount
        if self.account==self.event.pay_to:
            self.bestankar=0
            self.bedehkar=self.event.amount
            self.balance=0-self.event.amount
        super(AccountingDocumentLine,self).save()
    @property
    def title(self):
        return self.event.title 
    @property
    def rest(self):
        return 0
    @property
    def amount(self):
        return self.event.amount
    class_name="accountingdocumentline"
    app_name=APP_NAME 

    class Meta:
        verbose_name = _("AccountingDocumentLine")
        verbose_name_plural = _("AccountingDocumentLines")

    def __str__(self):
        return f"{self.account.id} , {self.event.title} , {self.balance}"
 
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
    # accounting_document=models.ForeignKey("accountingdocument",blank=True,null=True, verbose_name=_("سند حسابداری"), on_delete=models.PROTECT)
    pay_from=models.ForeignKey("account",related_name="events_from", verbose_name=_("پرداخت کننده"), on_delete=models.PROTECT)
    pay_to=models.ForeignKey("account", related_name="events_to",verbose_name=_("دریافت کننده"), on_delete=models.PROTECT)
    creator=models.ForeignKey("authentication.profile",null=True,blank=True, verbose_name=_("ثبت شده توسط"), on_delete=models.SET_NULL)
    status=models.CharField(_("وضعیت"),choices=EventStatusEnum.choices,default=EventStatusEnum.DRAFT, max_length=50)
    category=models.ForeignKey("eventcategory",null=True,blank=True, verbose_name=_("دسته بندی"), on_delete=models.SET_NULL)
    amount=models.IntegerField(_("مبلغ"),default=0)
    payment_method=models.CharField(_("نوع پرداخت"),choices=PaymentMethodEnum.choices,default=PaymentMethodEnum.DRAFT, max_length=50)
    event_datetime=models.DateTimeField(_("تاریخ تراکنش"), auto_now=False, auto_now_add=False)
    

    @property 
    def persian_event_datetime(self):
        return PersianCalendar().from_gregorian(self.event_datetime)

    class Meta:
        verbose_name = _("Event")
        verbose_name_plural = _("Events")

    def __str__(self):
        return self.title
 
    def save(self,*args, **kwargs):
        super(Event,self).save()
        if self.accounting_document is not None:
            AccountingDocumentLine.objects.filter(event=self).delete()
            AccountingDocumentLineBestankar=AccountingDocumentLine()
            AccountingDocumentLineBestankar.account=self.pay_from
            AccountingDocumentLineBestankar.accounting_document=self.accounting_document
            AccountingDocumentLineBestankar.event=self
            AccountingDocumentLineBestankar.save()
            AccountingDocumentLineBestankar.account.normalize_balance()

            
            AccountingDocumentLineBedehkar=AccountingDocumentLine()
            AccountingDocumentLineBedehkar.account=self.pay_to
            AccountingDocumentLineBedehkar.accounting_document=self.accounting_document
            AccountingDocumentLineBedehkar.event=self
            AccountingDocumentLineBedehkar.save()
            AccountingDocumentLineBedehkar.account.normalize_balance()

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
   
 
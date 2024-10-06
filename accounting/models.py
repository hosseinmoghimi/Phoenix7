from django.db import models
from core.models import LinkHelper,Page,reverse
from .apps import APP_NAME
from django.utils.translation import gettext as _
from .enums import *
from utility.constants import SUCCEED,FAILED
from utility.currency import to_price_colored,to_price
from utility.calendar import PersianCalendar
from django.contrib.auth.models import User,Group
from phoenix.server_settings import MEDIA_URL,STATIC_URL 
from utility.log import leolog

NO_DUPLICATED_ACCOUNT_NAME=False
NO_DUPLICATED_ACCOUNT_CODE=True

IMAGE_FOLDER=APP_NAME+"/images/"
ACCOUNT_NAME_SEPERATOR=" - "
class Access(models.Model):

    

    class Meta:
        verbose_name = _("Access")
        verbose_name_plural = _("Accesss")

    def __str__(self):
        return self.name
 
class Account(models.Model,LinkHelper): 
    class_name="account"
    app_name=APP_NAME
    color=models.CharField(_("color"),choices=ColorEnum.choices,default=ColorEnum.PRIMARY, max_length=50)
    profile=models.ForeignKey("authentication.profile",null=True,blank=True, verbose_name=_("profile"), on_delete=models.SET_NULL)
    type=models.CharField(_("type"), max_length=200,null=True,blank=True)
    name=models.CharField(_("name"), max_length=200)
    code=models.CharField(_("code"), max_length=200)
    pure_code=models.IntegerField(_("pure_code"), default=0)
    bedehkar=models.IntegerField(_("bedehkar"),default=0)
    bestankar=models.IntegerField(_("bestankar"),default=0)
    balance=models.IntegerField("balance",default=0)
    description=models.CharField(_("description"),null=True,blank=True, max_length=500)
    logo_origin=models.ImageField(_("logo"),blank=True,null=True, upload_to=IMAGE_FOLDER+"account", height_field=None, width_field=None, max_length=None)
    priority=models.IntegerField(default=100)
    # def __init__(self,*args, **kwargs):
    #     if 'name' in kwargs:
    #         self.name=kwargs['name']
            
    #     if 'code' in kwargs:
    #         self.code=kwargs['code']
            
    #     if 'color' in kwargs:
    #         self.color=kwargs['color']
            
    #     if 'type' in kwargs:
    #         self.type=kwargs['type']
    #     if 'description' in kwargs:
    #         self.description=kwargs['description']

            
    #     if 'description' in kwargs:
    #         self.description=kwargs['description']
    #     return super(Account,self).__init__(self)
    def get_full_link(self):
        if self.parent is not None:
            return self.parent.get_full_link()+""+self.get_link()
        return self.get_link()


    def get_link(self):
        return f"""
        <a href="{self.get_absolute_url()}">
                <h6 class="text-f{self.color}">

                    {self.name}
                    <span class="badge badge-{self.color}">
                        {self.type}
                      </span>

                </h6>
              </a>
            """
    def all_sub_accounts_id(self):
        ids=[self.id]
        for child in self.childs:
            for id in child.all_sub_accounts_id():
                ids.append(id)
        return ids

    def all_sub_accounts_lines(self):
        ids=self.all_sub_accounts_id()
        return AccountingDocumentLine.objects.filter(account_id__in=ids)
    def get_absolute_url(self):
        if self.type==AccountTypeEnum.GROUP:
            return reverse("accounting:accountgroup",kwargs={"pk":self.pk})
        elif self.type==AccountTypeEnum.BASIC:
            return reverse("accounting:basicaccount",kwargs={"pk":self.pk})
        elif self.type==AccountTypeEnum.MOEIN:
            return reverse("accounting:moeinaccount",kwargs={"pk":self.pk})
        elif self.type==AccountTypeEnum.MOEIN_2:
            return reverse("accounting:moeinaccount",kwargs={"pk":self.pk})
        elif self.type==AccountTypeEnum.TAFSILI:
            return reverse("accounting:tafsiliaccount",kwargs={"pk":self.pk})
        return reverse("accounting:tafsiliaccount",kwargs={"pk":self.pk})
    @property
    def parent(self):
        if self.type==AccountTypeEnum.GROUP:
            return None

        
        if self.type==AccountTypeEnum.BASIC:
            basic_account=BasicAccount.objects.filter(pk=self.pk).first()
            if basic_account is not None:
                return basic_account.account_group 

        
        if self.type==AccountTypeEnum.MOEIN:
            moein_account=MoeinAccount.objects.filter(pk=self.pk).first()
            if moein_account is not None:
                if moein_account.moein_account is not None:
                    return moein_account.moein_account
                if moein_account.basic_account is not None:
                    return moein_account.basic_account
        
        
        if self.type==AccountTypeEnum.MOEIN_2:
            moein_account=MoeinAccount.objects.filter(pk=self.pk).first()
            if moein_account is not None:
                if moein_account.moein_account is not None:
                    return moein_account.moein_account
                if moein_account.basic_account is not None:
                    return moein_account.basic_account
        

        else :
            tafsili_account=TafsiliAccount.objects.filter(pk=self.pk).first()
            if tafsili_account is not None:
                if tafsili_account.tafsili_account is not None:
                    return tafsili_account.tafsili_account
                if tafsili_account.moein_account is not None:
                    return tafsili_account.moein_account
        return None
    @property
    def full_title(self):

        account_name=self.name
        if self.type==AccountTypeEnum.GROUP:
            account=AccountGroup.objects.filter(pk=self.pk).first()
            if account is None:
                return ""
            return account.name

        
        if self.type==AccountTypeEnum.BASIC:
            account=BasicAccount.objects.filter(pk=self.pk).first()
            if account is None:
                return ""
            return account.account_group.full_title+ACCOUNT_NAME_SEPERATOR+account_name

        
        if self.type==AccountTypeEnum.MOEIN:
            account=MoeinAccount.objects.filter(pk=self.pk).first()
            if account is None:
                return ""
            pass
        
            try:
                if account.parent is not None:
                    return account.parent.full_title+ACCOUNT_NAME_SEPERATOR+account_name
            except:
                pass

            
            try:
                if account.basic_account is not None:
                    return account.basic_account.full_title+ACCOUNT_NAME_SEPERATOR+account_name
            except:
                pass


        
        if self.type==AccountTypeEnum.TAFSILI:
            account=TafsiliAccount.objects.filter(pk=self.pk).first()
            if account is None:
                return ""
        
            try:
                if account.parent is not None:
                    return account.parent.full_title+ACCOUNT_NAME_SEPERATOR+account_name

                else:
                    return account.moein_account.full_title+ACCOUNT_NAME_SEPERATOR+account_name
            except:
                pass

        return self.name
    @property
    def title(self):
        return self.name
   
    def __str__(self):
        return self.name
        f"{self.code} - {self.name}"
   
    def normalize_total(self):
        # print(self.full_title)
        bedehkar=0
        bestankar=0
        balance=0
        for accounting_document_line in AccountingDocumentLine.objects.filter(account_id=self.pk): 
            # basic_account.normalize_total()
            bedehkar+=accounting_document_line.bedehkar
            bestankar+=accounting_document_line.bestankar
        childs=self.childs
        if len(childs)>0:
            for acc in childs:
                bedehkar+=acc.bedehkar
                bestankar+=acc.bestankar
        balance=bestankar-bedehkar
        self.bedehkar=bedehkar
        self.bestankar=bestankar
        self.balance=balance
        self.save() 
        if self.parent is not None:
            self.parent.normalize_total()
    @property
    def logo(self):
        if not self.logo_origin :
            return f"{STATIC_URL}{APP_NAME}/img/pages/thumbnail/account.png"
        return f"{MEDIA_URL}{self.logo_origin}"
   #test
    @property
    def balance_colored(self):
        return to_price_colored(self.balance)
    
    def save(self):
        result=SUCCEED
        message="موفقیت آمیز"
        if NO_DUPLICATED_ACCOUNT_NAME and len(Account.objects.filter(name=self.name).exclude(pk=self.pk))>0:
            result=FAILED
            message="نام تکراری"
        if NO_DUPLICATED_ACCOUNT_CODE and len(Account.objects.filter(code=self.code).exclude(pk=self.pk))>0:
            result=FAILED
            message="کد تکراری"
        if result==SUCCEED:
            from utility.num import filter_number
            self.pure_code=filter_number(self.code)
            super(Account,self).save()
        return self,result,message

    @property
    def childs(self):
        childs=[]
        if self.type==AccountTypeEnum.GROUP:
            childs=BasicAccount.objects.filter(account_group_id=self.pk)
            return childs
        elif self.type==AccountTypeEnum.BASIC:
            childs=MoeinAccount.objects.filter(basic_account_id=self.pk)
            return childs
        elif self.type==AccountTypeEnum.MOEIN:
            childs1=MoeinAccount.objects.filter(moein_account_id=self.pk)
            childs2=TafsiliAccount.objects.filter(moein_account_id=self.pk)
            if len(childs1)>0:
                childs=childs1
            if len(childs2)>0:
                childs=childs2 
        elif self.type==AccountTypeEnum.MOEIN_2:
            childs=TafsiliAccount.objects.filter(moein_account_id=self.pk)
            return childs
        else:
            childs=TafsiliAccount.objects.filter(tafsili_account_id=self.pk)
            return childs
        return childs 

class AccountGroup(Account):
    
    
    # basic_accounts=models.ManyToManyField("basicaccount",blank=True, verbose_name=_("حساب های کل"))
    class_name="accountgroup"
    app_name=APP_NAME  
    
 
  
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
    def save(self):
        self.type=AccountTypeEnum.GROUP
        super(AccountGroup,self).save()

class BasicAccount(Account):
   
    account_group=models.ForeignKey("accountgroup", verbose_name=_("account group"), on_delete=models.CASCADE)
    # moein_accounts=models.ManyToManyField("moeinaccount",blank=True, verbose_name=_("حساب های معین"))
  
   
   
    class_name="basicaccount"
    app_name=APP_NAME
 
    @property
    def moein_accounts(self):
        return self.moeinaccount_set.all()
   

    class Meta:
        verbose_name = _("BasicAccount")
        verbose_name_plural = _("BasicAccounts")

    def __str__(self):
        return str(self.account_group)+" " + self.code+" "+self.name
    def save(self):
        self.type=AccountTypeEnum.BASIC
        return super(BasicAccount,self).save()

class MoeinAccount(Account):


    class_name="moeinaccount"
    app_name=APP_NAME
    moein_account=models.ForeignKey("moeinaccount", verbose_name=_("parent"), on_delete=models.SET_NULL,blank=True,null=True)
   
    # accounts=models.ManyToManyField("account", verbose_name=_("حساب ها"))
    basic_account=models.ForeignKey("basicaccount", verbose_name=_("basicaccount"), on_delete=models.CASCADE,blank=True,null=True)
   
     
    @property
    def title(self):
        return self.code+" "+self.name

    @property
    def accounts(self):
        return self.tafsiliaccount_set.all()

    def save(self):
        self.type=AccountTypeEnum.MOEIN
        if self.moein_account is not None:
            self.type=AccountTypeEnum.MOEIN_2
        return super(MoeinAccount,self).save()
    class Meta:
        verbose_name = _("MoeinAccount")
        verbose_name_plural = _("MoeinAccounts")

    def __str__(self):
        basic_account_name=""
        if self.basic_account is not None:
            basic_account_name=str(self.basic_account)+" "
            
        moein_account_name=""
        if self.parent is not None:
            moein_account_name=str(self.parent)+" "

        return basic_account_name+moein_account_name+self.code+" "+self.name

class TafsiliAccount(Account):
    tafsili_account=models.ForeignKey("tafsiliaccount", verbose_name=_("parent"), on_delete=models.SET_NULL,blank=True,null=True)
    moein_account=models.ForeignKey("moeinaccount", verbose_name=_("moein account"), on_delete=models.CASCADE,blank=True,null=True)
    
    mobile=models.CharField(_("mobile"),null=True,blank=True, max_length=50)
    tel=models.CharField(_("tel"),null=True,blank=True, max_length=50)
     
    class_name="tafsiliaccount"
    app_name=APP_NAME
    

        # if self.logo_origin:
        #     return MEDIA_URL+str(self.logo_origin)
        # if self.profile is not None:
        #     return self.profile.image
        # return f"{STATIC_URL}{self.app_name}/img/{self.class_name}.png"
    class Meta:
        verbose_name = _("حساب تفصیلی")
        verbose_name_plural = _("حساب های تفصیلی")
    def __str__(self):
        return self.moein_account.title+" " +self.title
     

    def save(self):
        if self.moein_account is not None:
            self.type=AccountTypeEnum.TAFSILI
        elif self.tafsili_account.type==AccountTypeEnum.TAFSILI:
            self.type=AccountTypeEnum.TAFSILI_2
        elif self.tafsili_account.type==AccountTypeEnum.TAFSILI_2:
            self.type=AccountTypeEnum.TAFSILI_3
        elif self.tafsili_account.type==AccountTypeEnum.TAFSILI_3:
            self.type=AccountTypeEnum.TAFSILI_4
        elif self.tafsili_account.type==AccountTypeEnum.TAFSILI_4:
            self.type=AccountTypeEnum.TAFSILI_5
        elif self.tafsili_account.type==AccountTypeEnum.TAFSILI_5:
            self.type=AccountTypeEnum.TAFSILI_6 

        return super(TafsiliAccount,self).save()
        
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
    date_added=models.DateTimeField(_("date_added"), auto_now=False, auto_now_add=True)
    date_time=models.DateTimeField(_("date_time"), auto_now=True, auto_now_add=False)
    date_modified=models.DateTimeField(_("date_modified "), auto_now=True, auto_now_add=False)

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
    event=models.ForeignKey("event", null=True,blank=True,verbose_name=_("event"), on_delete=models.PROTECT)
    title=models.CharField(_("title"), max_length=500)
    date_added=models.DateTimeField(_("date_added"), auto_now=False, auto_now_add=True)
    date_time=models.DateTimeField(_("date_time"), auto_now=True, auto_now_add=False)
    date_modified=models.DateTimeField(_("date_modified "),null=True, auto_now=True, auto_now_add=False)
    bedehkar=models.IntegerField(_("بدهکار"),default=0)
    bestankar=models.IntegerField(_("بستانکار"),default=0)
    balance=models.IntegerField(_("بالانس"),default=0)
    @property
    def persian_date_time(self):
        a= PersianCalendar().from_gregorian(self.date_time)    
        return f"""
                    <span>{a[:11]}</span>
                    <small class="text-muted mr-1">{a[11:]}</small>

                """
    def save(self):
        # if self.account==self.event.pay_from:
        #     self.bestankar=self.event.amount
        #     self.bedehkar=0
        #     self.balance=self.event.amount
        # if self.account==self.event.pay_to:
        #     self.bestankar=0
        #     self.bedehkar=self.event.amount
        #     self.balance=0-self.event.amount
        super(AccountingDocumentLine,self).save()
    @property
    def rest(self):
        return 0
    @property
    def amount(self):  
        return self.bedehkar+self.bestankar
    class_name="accountingdocumentline"
    app_name=APP_NAME 

    class Meta:
        verbose_name = _("AccountingDocumentLine")
        verbose_name_plural = _("AccountingDocumentLines")

    def __str__(self):
        event=""
        if self.event is not None :
            event=self.event.title
        return f"{self.account.id} , {event} , {self.account.name} , {self.balance}, {self.bestankar}, {self.bedehkar}"
 
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
        return f"{self.title} , {self.pay_from},  {self.pay_to} , {to_price(self.amount)}"
 
    def save(self,*args, **kwargs):
        super(Event,self).save()
        # if self is not None:
        #     AccountingDocumentLine.objects.filter(event=self).delete()
        #     AccountingDocumentLineBestankar=AccountingDocumentLine()
        #     AccountingDocumentLineBestankar.account=self.pay_from
        #     AccountingDocumentLineBestankar.accounting_document=self.accounting_document
        #     AccountingDocumentLineBestankar.event=self
        #     AccountingDocumentLineBestankar.save()
        #     AccountingDocumentLineBestankar.account.normalize_balance()

            
        #     AccountingDocumentLineBedehkar=AccountingDocumentLine()
        #     AccountingDocumentLineBedehkar.account=self.pay_to
        #     AccountingDocumentLineBedehkar.accounting_document=self.accounting_document
        #     AccountingDocumentLineBedehkar.event=self
        #     AccountingDocumentLineBedehkar.save()
        #     AccountingDocumentLineBedehkar.account.normalize_balance()

class EventPrint(models.Model,LinkHelper):
    event=models.ForeignKey("event", verbose_name=_("تراکنش"), on_delete=models.CASCADE)
    print_datetime=models.DateTimeField(_("تاریخ چاپ"),null=True,blank=True, auto_now=False, auto_now_add=True)

    class_name="eventprint"
    app_name=APP_NAME
    class Meta:
        verbose_name = _("EventPrint")
        verbose_name_plural = _("EventPrints")

    def __str__(self):
        print_datetime=PersianCalendar().from_gregorian(self.print_datetime)
        return f"{self.event}   @  {print_datetime} "
   
class Person(models.Model,LinkHelper):
    code=models.CharField(_("code"), max_length=50)
    profile=models.ForeignKey("authentication.profile", verbose_name=_("profile"), on_delete=models.CASCADE)
    accounts=models.ManyToManyField("account",blank=True, verbose_name=_("accounts"))
    categories=models.ManyToManyField("personcategory",blank=True, verbose_name=_("categories"))
    type=models.CharField(_("ماهیت"),choices=PersonType.choices, max_length=50)
    class_name="person"
    app_name=APP_NAME

    class Meta:
        verbose_name = _("شخص")
        verbose_name_plural = _("اشخاص")

    def __str__(self):
        return self.profile.full_name 
    @property
    def full_name(self):
        return self.profile.full_name

    @property
    def balance(self):
        balance= 0
        for account in self.accounts.all():
            balance+=account.balance
        return balance


    def save(self,*args, **kwargs):
        super(Person,self).save()
        # self.accounts.all().delete()
        # for category in self.categories.all():
        #     account=category.account
        #     moein_account=MoeinAccount.objects.filter(pk=account.pk).first()
        #     if moein_account is not None:
        #         leolog(moein_account=moein_account,code=self.code)
        #         new_account=TafsiliAccount(moein_account=moein_account,name=self.profile.name+ " - "+category.name,code=self.code+category.code)
        #         new_account.save()

        #         leolog(new_account=new_account,step=1)
        #         self.accounts.add(new_account.id) 

                
        #     tafsili_account=TafsiliAccount.objects.filter(pk=account.pk).first()
        #     if tafsili_account is not None:
                
        #         leolog(tafsili_account=tafsili_account,code=self.code)
        #         new_account=TafsiliAccount(tafsili_account=tafsili_account,name=self.profile.name+ " - "+category.name,code=self.code+category.code)
        #         new_account.save()
        #         leolog(new_account=new_account,step=2)
        #         self.accounts.add(new_account.id) 

        # super(Person,self).save()    

class PersonCategory(models.Model):
    code=models.CharField(_("code"), max_length=50)
    name=models.CharField(_("name"), max_length=50)
    account=models.ForeignKey("account", verbose_name=_("account"), on_delete=models.CASCADE)
    class_name="personcategory"
    app_name=APP_NAME
    

    class Meta:
        verbose_name = _("PersonCategory")
        verbose_name_plural = _("PersonCategorys")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("PersonCategory_detail", kwargs={"pk": self.pk})
   
class Thing(Page,LinkHelper):
    
    class Meta:
        verbose_name = _("Thing")
        verbose_name_plural = _("Thingس")
 
class Material(Thing):
    barcode=models.CharField(_("بارکد"),null=True,blank=True, max_length=100)
    class_name="material"
    app_name=APP_NAME

    class Meta:
        verbose_name = _("کالا")
        verbose_name_plural = _("کالا ها")

        
    def save(self,*args, **kwargs):
        if self.class_name is None or self.class_name=="":
            self.class_name='material'
        if self.app_name is None or self.app_name=="":
            self.app_name=APP_NAME
        return super(Service,self).save(*args, **kwargs)

class Service(Thing): 

    class Meta:
        verbose_name = _("خدمت")
        verbose_name_plural = _("خدمات")
 
 
        
    def save(self,*args, **kwargs):
        if self.class_name is None or self.class_name=="":
            self.class_name='service'
        if self.app_name is None or self.app_name=="":
            self.app_name=APP_NAME
        return super(Service,self).save(*args, **kwargs)
from .models import Account,AccountGroup,BasicAccount,BasicAccount,MoeinAccount,AccountingDocument,AccountingDocumentLine
from utility.constants import FAILED,SUCCEED
from authentication.repo import ProfileRepo
from .apps import APP_NAME


def init_all_accounts2():
    account_groups=[
            
        {"name":"دارایی جاری",'code':"1","basic_accounts":[
            {"name":"سرمایه گذاری کوتاه مدت",'code':"102","moein_accounts":[
                {"name":"سرمایه گذاری کوتاه مدت",'code':"102","accounts":[
                    {"name":"سرمایه گذاری کوتاه مدت",'code':"102"}
                ]}
            ]},
            {"name":"موجودی نقد و بانک",'code':"101"},
            ]},
        {"name":"دارایی های غیر جاری",'code':"2","basic_accounts":[
            {"name":"سرمایه گذاری کوتاه مدت",'code':"102"},
            {"name":"موجودی نقد و بانک",'code':"101"},
            ]},
        {"name":"بدهی های جاری	",'code':"3","basic_accounts":[
            {"name":"سرمایه گذاری کوتاه مدت",'code':"102"},
            {"name":"موجودی نقد و بانک",'code':"101"},
            ]},
        {"name":"بدهی های بلند مدت (غیرجاری)",'code':"4","basic_accounts":[
            {"name":"سرمایه گذاری کوتاه مدت",'code':"102"},
            {"name":"موجودی نقد و بانک",'code':"101"},
            ]},
        {"name":"حقوق صاحبان سهام",'code':"5","basic_accounts":[
            {"name":"سرمایه گذاری کوتاه مدت",'code':"102"},
            {"name":"موجودی نقد و بانک",'code':"101"},
            ]},
        {"name":"درآمد ها",'code':"6","basic_accounts":[
            {"name":"سرمایه گذاری کوتاه مدت",'code':"102"},
            {"name":"موجودی نقد و بانک",'code':"101"},
            ]},
        {"name":"بهای تمام شده کالای فروش رفته و خدمات ارائه شده",'code':"7","basic_accounts":[
            {"name":"سرمایه گذاری کوتاه مدت",'code':"102"},
            {"name":"موجودی نقد و بانک",'code':"101"},
            ]},
        {"name":"هزینه ها",'code':"8","basic_accounts":[
            {"name":"سرمایه گذاری کوتاه مدت",'code':"102"},
            {"name":"موجودی نقد و بانک",'code':"101"},
            ]},
        {"name":"سایر حسابها",'code':"9","basic_accounts":[
            {"name":"سرمایه گذاری کوتاه مدت",'code':"102"},
            {"name":"موجودی نقد و بانک",'code':"101"},
            ]},
        
    ]
    for account_group in account_groups:
        new_account_group=AccountGroup.objects.filter(name=account_group["name"]).first()
        if new_account_group is None:
            new_account_group=AccountGroup(name=account_group["name"],code=account_group['code'])
            new_account_group.save()
        if 'basic_accounts' in account_group:
            for basic_account in account_group["basic_accounts"]:
                new_basic_account=BasicAccount.objects.filter(name=basic_account["name"]).first()
                if new_basic_account is None:
                    new_basic_account=BasicAccount(name=basic_account["name"],code=basic_account['code'],account_group=new_account_group)
                    new_basic_account.save()

                if 'moein_accounts' in basic_account:
                        
                    for moein_account in basic_account["moein_accounts"]:
                        new_moein_account=MoeinAccount.objects.filter(name=moein_account["name"]).first()
                        if new_moein_account is None: 
                            new_moein_account=MoeinAccount(name=moein_account["name"],code=moein_account['code'],basic_account=new_basic_account)
                            new_moein_account.save()

                        if 'basic_accounts' in account_group:
                            
                            for account in moein_account["accounts"]:
                                new_account=Account.objects.filter(title=account["name"]).first()
                                if new_moein_account is None: 
                                    new_moein_account=MoeinAccount(title=account["name"],code=account['code'],moein_account=new_moein_account)
                                    new_moein_account.save()
    result=SUCCEED
    message="افزوده شد."
    return (result,message)




def init_all_accounts():
    account_groups=[
            
        {"name":"دارایی جاری",'code':"1","basic_accounts":[
            {"name":"	موجودی نقد و بانک",'code':"11","moein_accounts":[
                {"name":"سرمایه گذاری کوتاه مدت",'code':"102","accounts":[
                    # {"name":"سرمایه گذاری کوتاه مدت",'code':"102"},
                    # {"name":"سرمایه گذاری کوتاه مدت",'code':"102"},
                    # {"name":"سرمایه گذاری کوتاه مدت",'code':"102"},
                ]}
            ]},

            {"name":"سرمایه گذاری کوتاه مدت",'code':"12","moein_accounts":[
                {"name":"سرمایه گذاری کوتاه مدت",'code':"102","accounts":[
                    {"name":"سرمایه گذاری کوتاه مدت",'code':"102"},
                    {"name":"سرمایه گذاری کوتاه مدت",'code':"102"},
                    {"name":"سرمایه گذاری کوتاه مدت",'code':"102"},
                ]}
            ]},

            
            {"name":"حساب ها و اسناد دریافتنی تجاری",'code':"13","moein_accounts":[
                {"name":"سرمایه گذاری کوتاه مدت",'code':"102","accounts":[
                    {"name":"سرمایه گذاری کوتاه مدت",'code':"102"},
                    {"name":"سرمایه گذاری کوتاه مدت",'code':"102"},
                    {"name":"سرمایه گذاری کوتاه مدت",'code':"102"},
                ]}
            ]},

            
            {"name":"سایر حساب های دریافتنی تجاری",'code':"14","moein_accounts":[
                {"name":"سرمایه گذاری کوتاه مدت",'code':"102","accounts":[
                    {"name":"سرمایه گذاری کوتاه مدت",'code':"102"},
                    {"name":"سرمایه گذاری کوتاه مدت",'code':"102"},
                    {"name":"سرمایه گذاری کوتاه مدت",'code':"102"},
                ]}
            ]},

            
            {"name":"جاری شرکا",'code':"15","moein_accounts":[
                {"name":"سرمایه گذاری کوتاه مدت",'code':"102","accounts":[
                    {"name":"سرمایه گذاری کوتاه مدت",'code':"102"},
                    {"name":"سرمایه گذاری کوتاه مدت",'code':"102"},
                    {"name":"سرمایه گذاری کوتاه مدت",'code':"102"},
                ]}
            ]},

            
            {"name":"موجودی مواد و کالا",'code':"16","moein_accounts":[
                {"name":"سرمایه گذاری کوتاه مدت",'code':"102","accounts":[
                    {"name":"سرمایه گذاری کوتاه مدت",'code':"102"},
                    {"name":"سرمایه گذاری کوتاه مدت",'code':"102"},
                    {"name":"سرمایه گذاری کوتاه مدت",'code':"102"},
                ]}
            ]},
            
            {"name":"سفارشات و پیش پرداختها",'code':"17","moein_accounts":[
                {"name":"سرمایه گذاری کوتاه مدت",'code':"102","accounts":[
                    {"name":"سرمایه گذاری کوتاه مدت",'code':"102"},
                    {"name":"سرمایه گذاری کوتاه مدت",'code':"102"},
                    {"name":"سرمایه گذاری کوتاه مدت",'code':"102"},
                ]}
            ]},
            {"name":"سپرده هایمان نزد دیگران",'code':"18"},
 
            ]},
        {"name":"دارایی های غیر جاری",'code':"2","basic_accounts":[
            {"name":"سرمایه گذاری کوتاه مدت",'code':"102"},
            {"name":"موجودی نقد و بانک",'code':"101"},
            ]},
        {"name":"بدهی های جاری	",'code':"3","basic_accounts":[
            {"name":"سرمایه گذاری کوتاه مدت",'code':"102"},
            {"name":"موجودی نقد و بانک",'code':"101"},
            ]},
        {"name":"بدهی های بلند مدت (غیرجاری)",'code':"4","basic_accounts":[
            {"name":"سرمایه گذاری کوتاه مدت",'code':"102"},
            {"name":"موجودی نقد و بانک",'code':"101"},
            ]},
        {"name":"حقوق صاحبان سهام",'code':"5","basic_accounts":[
            {"name":"سرمایه گذاری کوتاه مدت",'code':"102"},
            {"name":"موجودی نقد و بانک",'code':"101"},
            ]},
        {"name":"درآمد ها",'code':"6","basic_accounts":[
            {"name":"سرمایه گذاری کوتاه مدت",'code':"102"},
            {"name":"موجودی نقد و بانک",'code':"101"},
            ]},
        {"name":"بهای تمام شده کالای فروش رفته و خدمات ارائه شده",'code':"7","basic_accounts":[
            {"name":"سرمایه گذاری کوتاه مدت",'code':"102"},
            {"name":"موجودی نقد و بانک",'code':"101"},
            ]},
        {"name":"هزینه ها",'code':"8","basic_accounts":[
            {"name":"سرمایه گذاری کوتاه مدت",'code':"102"},
            {"name":"موجودی نقد و بانک",'code':"101"},
            ]},
        {"name":"سایر حسابها",'code':"9","basic_accounts":[
            {"name":"سرمایه گذاری کوتاه مدت",'code':"102"},
            {"name":"موجودی نقد و بانک",'code':"101"},
            ]},
        
    ]
    AccountGroup.objects.all().delete()
    BasicAccount.objects.all().delete()
    MoeinAccount.objects.all().delete()
    Account.objects.all().delete()
    for account_group in account_groups:
        new_account_group=AccountGroup(name=account_group["name"],code=account_group['code'])
        new_account_group.save()
        if 'basic_accounts' in account_group:
            for basic_account in account_group["basic_accounts"]:
                new_basic_account=BasicAccount(name=basic_account["name"],code=basic_account['code'],account_group=new_account_group)
                new_basic_account.save()
                if 'moein_accounts' in basic_account:
                    for moein_account in basic_account["moein_accounts"]:
                        new_moein_account=MoeinAccount(name=moein_account["name"],code=moein_account['code'],basic_account=new_basic_account)
                        new_moein_account.save()
                        if 'accounts' in moein_account:
                            for account in moein_account["accounts"]:
                                new_account=Account(title=account["name"],code=account['code'],moein_account=new_moein_account)
                                new_account.save()
    result=SUCCEED
    message="افزوده شد."
    return (result,message)



class AccountRepo():
    def __init__(self,request,*args, **kwargs):
        self.request=request
        self.me=None
        profile=ProfileRepo(request=request).me
        self.objects=Account.objects
        if profile is not None:
            self.me=self.objects.filter(profile=profile).first()
    def list(self,*args, **kwargs):
        objects=self.objects
        if "search_for" in kwargs:
            objects=objects.filter(title__contains=kwargs['search_for']) 
        return objects.all()
    def account(self,*args, **kwargs):
        if "pk" in kwargs:
            return self.objects.filter(pk=kwargs['pk']).first() 
        if "id" in kwargs:
            return self.objects.filter(pk=kwargs['id']).first() 

            
    def add_account(self,*args, **kwargs):
        account,message,result=(None,"",FAILED)
        if not self.request.user.has_perm(APP_NAME+".add_account"):
            message="دسترسی غیر مجاز"
            return account,message,result
        if len(Account.objects.filter(title=kwargs['title']))>0:
            message="از قبل حسابی با همین عنوان ثبت شده است."
            return account,message,result

        account=Account()

        if 'title' in kwargs:
            account.title=kwargs['title']
        if 'profile_id' in kwargs:
            account.profile_id=kwargs['profile_id']
        if 'description' in kwargs:
            account.description=kwargs['description']
        if 'address' in kwargs:
            account.address=kwargs['address']
        if 'tel' in kwargs:
            account.tel=kwargs['tel']
        if 'mobile' in kwargs:
            account.mobile=kwargs['mobile']
       
        
        # if 'financial_year_id' in kwargs:
        #     payment.financial_year_id=kwargs['financial_year_id']
        # else:
        #     payment.financial_year_id=FinancialYear.get_by_date(date=payment.transaction_datetime).id

        account.save()
        result=SUCCEED
        message="با موفقیت اضافه گردید."
        
        if 'balance' in kwargs and kwargs['balance'] is not None and not kwargs['balance']==0:
            me_account=self.me
            if me_account is not None:
                balance=kwargs['balance']
                payment=Payment()
                payment.amount=balance if balance>0 else (0-balance)
                payment.title="مانده از قبل"
                payment.creator_id=me_account.profile.id
                payment.status=TransactionStatusEnum.FROM_PAST
                payment.payment_method=PaymentMethodEnum.FROM_PAST
                payment.transaction_datetime=PersianCalendar().date
                if balance>0:
                    payment.pay_to_id=me_account.id
                    payment.pay_from_id=account.id
                if balance<0:
                    payment.pay_from_id=me_account.id
                    payment.pay_to_id=account.id
                payment.save()

        return account,message,result

    def add_account_tag(self,*args, **kwargs):
        result,message,account_tags=FAILED,"",[]
        if not self.request.user.has_perm(APP_NAME+".change_account"):
            return result,message,account_tags
        tag=kwargs['tag']
        account_id=kwargs['account_id']
        account_tags=AccountTag.objects.filter(account_id=account_id).filter(tag=tag)
        
        if len(account_tags)>0:
            account_tags.delete()
            account_tags=AccountTag.objects.filter(account_id=account_id)
            result=SUCCEED
            message="تگ "+tag+" حذف شد."
            return result,message,account_tags
        

        account_tag=AccountTag()
        account_tag.account_id=account_id
        account_tag.tag=tag
        account_tag.save()
        message="تگ "+tag+" اضافه شد."

        account_tags=AccountTag.objects.filter(account_id=account_id)
        result=SUCCEED

        return result,message,account_tags
        
class AccountGroupRepo():
    def __init__(self,request,*args, **kwargs):
        self.request=request
        self.me=None
        profile=ProfileRepo(request=request).me
        self.objects=AccountGroup.objects
        # if profile is not None:
        #     self.me=self.objects.filter(profile=profile).first()
    def list(self,*args, **kwargs):
        objects=self.objects
        if "search_for" in kwargs:
            objects=objects.filter(title__contains=kwargs['search_for']) 
        return objects.all()
    def account_group(self,*args, **kwargs):
        if "pk" in kwargs:
            return self.objects.filter(pk=kwargs['pk']).first() 
        if "id" in kwargs:
            return self.objects.filter(pk=kwargs['id']).first() 

            
    def add_account_group(self,*args, **kwargs):
        account,message,result=(None,"",FAILED)
        if not self.request.user.has_perm(APP_NAME+".add_account"):
            message="دسترسی غیر مجاز"
            return account,message,result
        if len(Account.objects.filter(title=kwargs['title']))>0:
            message="از قبل حسابی با همین عنوان ثبت شده است."
            return account,message,result

        account=Account()

        if 'title' in kwargs:
            account.title=kwargs['title']
        if 'profile_id' in kwargs:
            account.profile_id=kwargs['profile_id']
        if 'description' in kwargs:
            account.description=kwargs['description']
        if 'address' in kwargs:
            account.address=kwargs['address']
        if 'tel' in kwargs:
            account.tel=kwargs['tel']
        if 'mobile' in kwargs:
            account.mobile=kwargs['mobile']
       
        
        # if 'financial_year_id' in kwargs:
        #     payment.financial_year_id=kwargs['financial_year_id']
        # else:
        #     payment.financial_year_id=FinancialYear.get_by_date(date=payment.transaction_datetime).id

        account.save()
        result=SUCCEED
        message="با موفقیت اضافه گردید."
        
        if 'balance' in kwargs and kwargs['balance'] is not None and not kwargs['balance']==0:
            me_account=self.me
            if me_account is not None:
                balance=kwargs['balance']
                payment=Payment()
                payment.amount=balance if balance>0 else (0-balance)
                payment.title="مانده از قبل"
                payment.creator_id=me_account.profile.id
                payment.status=TransactionStatusEnum.FROM_PAST
                payment.payment_method=PaymentMethodEnum.FROM_PAST
                payment.transaction_datetime=PersianCalendar().date
                if balance>0:
                    payment.pay_to_id=me_account.id
                    payment.pay_from_id=account.id
                if balance<0:
                    payment.pay_from_id=me_account.id
                    payment.pay_to_id=account.id
                payment.save()

        return account,message,result

    def add_account_tag(self,*args, **kwargs):
        result,message,account_tags=FAILED,"",[]
        if not self.request.user.has_perm(APP_NAME+".change_account"):
            return result,message,account_tags
        tag=kwargs['tag']
        account_id=kwargs['account_id']
        account_tags=AccountTag.objects.filter(account_id=account_id).filter(tag=tag)
        
        if len(account_tags)>0:
            account_tags.delete()
            account_tags=AccountTag.objects.filter(account_id=account_id)
            result=SUCCEED
            message="تگ "+tag+" حذف شد."
            return result,message,account_tags
        

        account_tag=AccountTag()
        account_tag.account_id=account_id
        account_tag.tag=tag
        account_tag.save()
        message="تگ "+tag+" اضافه شد."

        account_tags=AccountTag.objects.filter(account_id=account_id)
        result=SUCCEED

        return result,message,account_tags
   
class BasicAccountRepo():
    def __init__(self,request,*args, **kwargs):
        self.request=request
        self.me=None
        profile=ProfileRepo(request=request).me
        self.objects=BasicAccount.objects
        # if profile is not None:
        #     self.me=self.objects.filter(profile=profile).first()
    def list(self,*args, **kwargs):
        objects=self.objects
        if "search_for" in kwargs:
            objects=objects.filter(title__contains=kwargs['search_for']) 
        return objects.all()
    def basic_account(self,*args, **kwargs):
        if "pk" in kwargs:
            return self.objects.filter(pk=kwargs['pk']).first() 
        if "id" in kwargs:
            return self.objects.filter(pk=kwargs['id']).first() 

            
    def add_account_group(self,*args, **kwargs):
        account,message,result=(None,"",FAILED)
        if not self.request.user.has_perm(APP_NAME+".add_account"):
            message="دسترسی غیر مجاز"
            return account,message,result
        if len(Account.objects.filter(title=kwargs['title']))>0:
            message="از قبل حسابی با همین عنوان ثبت شده است."
            return account,message,result

        account=Account()

        if 'title' in kwargs:
            account.title=kwargs['title']
        if 'profile_id' in kwargs:
            account.profile_id=kwargs['profile_id']
        if 'description' in kwargs:
            account.description=kwargs['description']
        if 'address' in kwargs:
            account.address=kwargs['address']
        if 'tel' in kwargs:
            account.tel=kwargs['tel']
        if 'mobile' in kwargs:
            account.mobile=kwargs['mobile']
       
        
        # if 'financial_year_id' in kwargs:
        #     payment.financial_year_id=kwargs['financial_year_id']
        # else:
        #     payment.financial_year_id=FinancialYear.get_by_date(date=payment.transaction_datetime).id

        account.save()
        result=SUCCEED
        message="با موفقیت اضافه گردید."
        
        if 'balance' in kwargs and kwargs['balance'] is not None and not kwargs['balance']==0:
            me_account=self.me
            if me_account is not None:
                balance=kwargs['balance']
                payment=Payment()
                payment.amount=balance if balance>0 else (0-balance)
                payment.title="مانده از قبل"
                payment.creator_id=me_account.profile.id
                payment.status=TransactionStatusEnum.FROM_PAST
                payment.payment_method=PaymentMethodEnum.FROM_PAST
                payment.transaction_datetime=PersianCalendar().date
                if balance>0:
                    payment.pay_to_id=me_account.id
                    payment.pay_from_id=account.id
                if balance<0:
                    payment.pay_from_id=me_account.id
                    payment.pay_to_id=account.id
                payment.save()

        return account,message,result

    def add_account_tag(self,*args, **kwargs):
        result,message,account_tags=FAILED,"",[]
        if not self.request.user.has_perm(APP_NAME+".change_account"):
            return result,message,account_tags
        tag=kwargs['tag']
        account_id=kwargs['account_id']
        account_tags=AccountTag.objects.filter(account_id=account_id).filter(tag=tag)
        
        if len(account_tags)>0:
            account_tags.delete()
            account_tags=AccountTag.objects.filter(account_id=account_id)
            result=SUCCEED
            message="تگ "+tag+" حذف شد."
            return result,message,account_tags
        

        account_tag=AccountTag()
        account_tag.account_id=account_id
        account_tag.tag=tag
        account_tag.save()
        message="تگ "+tag+" اضافه شد."

        account_tags=AccountTag.objects.filter(account_id=account_id)
        result=SUCCEED

        return result,message,account_tags
        
class MoeinAccountRepo():
    def __init__(self,request,*args, **kwargs):
        self.request=request
        self.me=None
        profile=ProfileRepo(request=request).me
        self.objects=MoeinAccount.objects
        # if profile is not None:
        #     self.me=self.objects.filter(profile=profile).first()
    def list(self,*args, **kwargs):
        objects=self.objects
        if "search_for" in kwargs:
            objects=objects.filter(title__contains=kwargs['search_for']) 
        return objects.all()
    def moein_account(self,*args, **kwargs):
        if "pk" in kwargs:
            return self.objects.filter(pk=kwargs['pk']).first() 
        if "id" in kwargs:
            return self.objects.filter(pk=kwargs['id']).first() 

            
    def add_account_group(self,*args, **kwargs):
        account,message,result=(None,"",FAILED)
        if not self.request.user.has_perm(APP_NAME+".add_account"):
            message="دسترسی غیر مجاز"
            return account,message,result
        if len(Account.objects.filter(title=kwargs['title']))>0:
            message="از قبل حسابی با همین عنوان ثبت شده است."
            return account,message,result

        account=Account()

        if 'title' in kwargs:
            account.title=kwargs['title']
        if 'profile_id' in kwargs:
            account.profile_id=kwargs['profile_id']
        if 'description' in kwargs:
            account.description=kwargs['description']
        if 'address' in kwargs:
            account.address=kwargs['address']
        if 'tel' in kwargs:
            account.tel=kwargs['tel']
        if 'mobile' in kwargs:
            account.mobile=kwargs['mobile']
       
        
        # if 'financial_year_id' in kwargs:
        #     payment.financial_year_id=kwargs['financial_year_id']
        # else:
        #     payment.financial_year_id=FinancialYear.get_by_date(date=payment.transaction_datetime).id

        account.save()
        result=SUCCEED
        message="با موفقیت اضافه گردید."
        
        if 'balance' in kwargs and kwargs['balance'] is not None and not kwargs['balance']==0:
            me_account=self.me
            if me_account is not None:
                balance=kwargs['balance']
                payment=Payment()
                payment.amount=balance if balance>0 else (0-balance)
                payment.title="مانده از قبل"
                payment.creator_id=me_account.profile.id
                payment.status=TransactionStatusEnum.FROM_PAST
                payment.payment_method=PaymentMethodEnum.FROM_PAST
                payment.transaction_datetime=PersianCalendar().date
                if balance>0:
                    payment.pay_to_id=me_account.id
                    payment.pay_from_id=account.id
                if balance<0:
                    payment.pay_from_id=me_account.id
                    payment.pay_to_id=account.id
                payment.save()

        return account,message,result

    def add_account_tag(self,*args, **kwargs):
        result,message,account_tags=FAILED,"",[]
        if not self.request.user.has_perm(APP_NAME+".change_account"):
            return result,message,account_tags
        tag=kwargs['tag']
        account_id=kwargs['account_id']
        account_tags=AccountTag.objects.filter(account_id=account_id).filter(tag=tag)
        
        if len(account_tags)>0:
            account_tags.delete()
            account_tags=AccountTag.objects.filter(account_id=account_id)
            result=SUCCEED
            message="تگ "+tag+" حذف شد."
            return result,message,account_tags
        

        account_tag=AccountTag()
        account_tag.account_id=account_id
        account_tag.tag=tag
        account_tag.save()
        message="تگ "+tag+" اضافه شد."

        account_tags=AccountTag.objects.filter(account_id=account_id)
        result=SUCCEED

        return result,message,account_tags
       
class AccountingDocumentRepo():
    def __init__(self,request,*args, **kwargs):
        self.request=request
        self.me=None
        profile=ProfileRepo(request=request).me
        self.objects=AccountingDocument.objects
        # if profile is not None:
        #     self.me=self.objects.filter(profile=profile).first()
    def list(self,*args, **kwargs):
        objects=self.objects
        if "search_for" in kwargs:
            objects=objects.filter(title__contains=kwargs['search_for']) 
        return objects.all()
    def accounting_document(self,*args, **kwargs):
        if "pk" in kwargs:
            return self.objects.filter(pk=kwargs['pk']).first() 
        if "id" in kwargs:
            return self.objects.filter(pk=kwargs['id']).first() 

            
    def add_accounting_document(self,*args, **kwargs):
        account,message,result=(None,"",FAILED)
        if not self.request.user.has_perm(APP_NAME+".add_account"):
            message="دسترسی غیر مجاز"
            return account,message,result
        if len(Account.objects.filter(title=kwargs['title']))>0:
            message="از قبل حسابی با همین عنوان ثبت شده است."
            return account,message,result

        account=Account()

        if 'title' in kwargs:
            account.title=kwargs['title']
        if 'profile_id' in kwargs:
            account.profile_id=kwargs['profile_id']
        if 'description' in kwargs:
            account.description=kwargs['description']
        if 'address' in kwargs:
            account.address=kwargs['address']
        if 'tel' in kwargs:
            account.tel=kwargs['tel']
        if 'mobile' in kwargs:
            account.mobile=kwargs['mobile']
       
        
        # if 'financial_year_id' in kwargs:
        #     payment.financial_year_id=kwargs['financial_year_id']
        # else:
        #     payment.financial_year_id=FinancialYear.get_by_date(date=payment.transaction_datetime).id

        account.save()
        result=SUCCEED
        message="با موفقیت اضافه گردید."
        
        if 'balance' in kwargs and kwargs['balance'] is not None and not kwargs['balance']==0:
            me_account=self.me
            if me_account is not None:
                balance=kwargs['balance']
                payment=Payment()
                payment.amount=balance if balance>0 else (0-balance)
                payment.title="مانده از قبل"
                payment.creator_id=me_account.profile.id
                payment.status=TransactionStatusEnum.FROM_PAST
                payment.payment_method=PaymentMethodEnum.FROM_PAST
                payment.transaction_datetime=PersianCalendar().date
                if balance>0:
                    payment.pay_to_id=me_account.id
                    payment.pay_from_id=account.id
                if balance<0:
                    payment.pay_from_id=me_account.id
                    payment.pay_to_id=account.id
                payment.save()

        return account,message,result
 
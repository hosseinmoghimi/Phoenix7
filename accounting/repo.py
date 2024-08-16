from .models import TafsiliAccount,AccountGroup,BasicAccount,BasicAccount,MoeinAccount,AccountingDocument,AccountingDocumentLine
from utility.constants import FAILED,SUCCEED
from authentication.repo import ProfileRepo
from .apps import APP_NAME
from .defaults import init_all_accounts

class TafsiliAccountRepo():
    def __init__(self,request,*args, **kwargs):
        self.request=request
        self.me=None
        profile=ProfileRepo(request=request).me
        self.objects=TafsiliAccount.objects
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

            
    def add_tafsili_account(self,*args, **kwargs):
        tafsili_account,message,result=(None,"",FAILED)
        if not self.request.user.has_perm(APP_NAME+".add_account"):
            message="دسترسی غیر مجاز"
            return tafsili_account,message,result
        if len(TafsiliAccount.objects.filter(name=kwargs['name']))>0:
            message="از قبل حسابی با همین عنوان ثبت شده است."
            return tafsili_account,message,result

        tafsili_account=TafsiliAccount()

        if 'name' in kwargs:
            tafsili_account.name=kwargs['name']
        if 'profile_id' in kwargs:
            account.profile_id=kwargs['profile_id']
        if 'description' in kwargs:
            account.description=kwargs['description']
        if 'moein_account_id' in kwargs and kwargs["moein_account_id"]>0:
            tafsili_account.moein_account_id=kwargs['moein_account_id']
        if 'tel' in kwargs:
            tafsili_account.tel=kwargs['tel']
        if 'parent_id' in kwargs and kwargs["parent_id"]>0:
            tafsili_account.parent_id=kwargs['parent_id']
       
        
        # if 'financial_year_id' in kwargs:
        #     payment.financial_year_id=kwargs['financial_year_id']
        # else:
        #     payment.financial_year_id=FinancialYear.get_by_date(date=payment.transaction_datetime).id

        tafsili_account.save()
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

        return tafsili_account,message,result

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

            
    def add_moein_account(self,*args, **kwargs):
        moein_account,message,result=(None,"",FAILED)
        if not self.request.user.has_perm(APP_NAME+".add_account"):
            message="دسترسی غیر مجاز"
            return account,message,result
        if len(MoeinAccount.objects.filter(name=kwargs['name']))>0:
            message="از قبل حسابی با همین عنوان ثبت شده است."
            return moein_account,message,result

        moein_account=MoeinAccount()

        if 'name' in kwargs:
            moein_account.name=kwargs['name']
        if 'code' in kwargs:
            moein_account.code=kwargs['code']
        if 'profile_id' in kwargs:
            moein_account.profile_id=kwargs['profile_id']
        if 'description' in kwargs:
            moein_account.description=kwargs['description']
        if 'address' in kwargs:
            moein_account.address=kwargs['address']
        if 'tel' in kwargs:
            moein_account.tel=kwargs['tel']
        if 'mobile' in kwargs:
            moein_account.mobile=kwargs['mobile']
        if 'parent_id' in kwargs and kwargs['parent_id']>0 :
            moein_account.parent_id=kwargs['parent_id']
        if 'basic_account_id' in kwargs and kwargs['basic_account_id']>0 :
            moein_account.basic_account_id=kwargs['basic_account_id']
       
        
        # if 'financial_year_id' in kwargs:
        #     payment.financial_year_id=kwargs['financial_year_id']
        # else:
        #     payment.financial_year_id=FinancialYear.get_by_date(date=payment.transaction_datetime).id

        moein_account.save()
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

        return moein_account,message,result
 
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
 
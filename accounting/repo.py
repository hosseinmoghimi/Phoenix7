from .models import Event,TafsiliAccount,AccountGroup,BasicAccount,BasicAccount,MoeinAccount,AccountingDocument,AccountingDocumentLine,Account
from utility.constants import FAILED,SUCCEED
from processmanagement.permission import Permission,OperationEnum
from django.db.models import Q
from utility.log import leolog
from authentication.repo import ProfileRepo
from .apps import APP_NAME
from utility.num import filter_number
from .defaults import init_all_accounts_list,init_all_accounts_list_1
from utility.calendar import PersianCalendar

class EventRepo:
    def __init__(self,request,*args, **kwargs):
        self.request=request
        self.me=None
        profile=ProfileRepo(request=request).me
        self.objects=Event.objects
        # if profile is not None:
        #     self.me=self.objects.filter(profile=profile).first()
    def list(self,*args, **kwargs):
        objects=self.objects
        if "search_for" in kwargs:
            objects=objects.filter(title__contains=kwargs['search_for']) 
        return objects.all()
    def event(self,*args, **kwargs):
        if "event_id" in kwargs:
            return self.objects.filter(pk=kwargs['event_id']).first() 
        if "pk" in kwargs:
            return self.objects.filter(pk=kwargs['pk']).first() 
        if "id" in kwargs:
            return self.objects.filter(pk=kwargs['id']).first() 

                     
    def add_event(self,*args, **kwargs):
        event,message,result=(None,"",FAILED)
        if not Permission(request=self.request).is_permitted(APP_NAME,OperationEnum.ADD,"event"):
        # if not self.request.user.has_perm(APP_NAME+".add_account"):
            message="دسترسی غیر مجاز"
            return account,message,result
        # if len(Account.objects.filter(title=kwargs['title']))>0:
        #     message="از قبل حسابی با همین عنوان ثبت شده است."
        #     return event,message,result

        event=Event()
        if 'event_datetime' in kwargs:
            year=kwargs['event_datetime'][:2]
            if year=="13" or year=="14":
                kwargs['event_datetime']=PersianCalendar().to_gregorian(kwargs["event_datetime"])
            event.event_datetime=kwargs['event_datetime']
        if 'title' in kwargs:
            event.title=kwargs['title']
        if 'bedehkar_id' in kwargs:
            event.pay_to_id=kwargs['bedehkar_id']
        if 'bestankar_id' in kwargs:
            event.pay_from_id=kwargs['bestankar_id']
        if 'amount' in kwargs:
            event.amount=kwargs['amount']
        if 'tel' in kwargs:
            event.tel=kwargs['tel']
        if 'mobile' in kwargs:
            event.mobile=kwargs['mobile']
       
        
        # if 'financial_year_id' in kwargs:
        #     payment.financial_year_id=kwargs['financial_year_id']
        # else:
        #     payment.financial_year_id=FinancialYear.get_by_date(date=payment.transaction_datetime).id
        event.save()
        result=SUCCEED
        message="رویداد مالی جدید با موفقیت اضافه گردید."
         
        return event,message,result



            
    def add_event_to_accounting_document(self,*args, **kwargs):
        event,message,result=(None,"",FAILED)
        if not Permission(request=self.request).is_permitted(APP_NAME,OperationEnum.ADD,"event"):
        # if not self.request.user.has_perm(APP_NAME+".add_account"):
            message="دسترسی غیر مجاز"
            return account,message,result
        # if len(Account.objects.filter(title=kwargs['title']))>0:
        #     message="از قبل حسابی با همین عنوان ثبت شده است."
        #     return event,message,result

        event=self.event(*args,**kwargs)
        accounting_document=AccountingDocumentRepo(request=self.request).accounting_document(*args,**kwargs)
        if event is not None and accounting_document is not None:
            accounting_document_line1,message1,result1=AccountingDocumentLineRepo(request=self.request).add_accounting_document_line(title=event.title,accounting_document_id=accounting_document.id,bestankar=event.amount,account_id=event.pay_from.id,event_id=event.id)
            accounting_document_line2,message2,result2=AccountingDocumentLineRepo(request=self.request).add_accounting_document_line(title=event.title,accounting_document_id=accounting_document.id,bedehkar=event.amount,account_id=event.pay_to.id,event_id=event.id)
            leolog(event=event)
            result=SUCCEED
            return event,message,result
        if 'event_datetime' in kwargs:
            year=kwargs['event_datetime'][:2]
            if year=="13" or year=="14":
                kwargs['event_datetime']=PersianCalendar().to_gregorian(kwargs["event_datetime"])
            event.event_datetime=kwargs['event_datetime']
        if 'title' in kwargs:
            event.title=kwargs['title']
        if 'bedehkar_id' in kwargs:
            event.pay_to_id=kwargs['bedehkar_id']
        if 'bestankar_id' in kwargs:
            event.pay_from_id=kwargs['bestankar_id']
        if 'amount' in kwargs:
            event.amount=kwargs['amount']
        if 'tel' in kwargs:
            event.tel=kwargs['tel']
        if 'mobile' in kwargs:
            event.mobile=kwargs['mobile']
       
        
        # if 'financial_year_id' in kwargs:
        #     payment.financial_year_id=kwargs['financial_year_id']
        # else:
        #     payment.financial_year_id=FinancialYear.get_by_date(date=payment.transaction_datetime).id
        event.save()
        result=SUCCEED
        message="رویداد مالی جدید با موفقیت اضافه گردید."
         
        return event,message,result

class AccountingDocumentLineRepo:
    def __init__(self,request,*args, **kwargs):
        self.request=request
        self.me=None
        profile=ProfileRepo(request=request).me
        self.objects=AccountingDocumentLine.objects
        
    def list(self,*args, **kwargs):
        objects=self.objects
        if "search_for" in kwargs and kwargs["search_for"] is not None and len(kwargs["search_for"])>0 :
            objects=objects.filter(title__contains=kwargs['search_for']) 
        if "amount" in kwargs and kwargs["amount"] is not None and kwargs["amount"]>0 :
            objects=objects.filter(amount=kwargs['amount']) 
        if "account_code" in kwargs:
            account_code=kwargs["account_code"]
            account=AccountRepo(request=self.request).account(code=account_code)
            if account is not None:
                objects=objects.filter(account_id=account.id)
        if "account_id" in kwargs:
            account_id=kwargs["account_id"]
            objects=objects.filter(account_id=account_id)
        if "event_id" in kwargs:
            event_id=kwargs["event_id"]
            objects=objects.filter(event_id=event_id)
        return objects.all()
            

    def accounting_document_line(self,*args, **kwargs):
        if "accounting_document_line_id" in kwargs and kwargs["accounting_document_line_id"] is not None:
            return self.objects.filter(pk=kwargs['accounting_document_line_id']).first() 
        if "pk" in kwargs and kwargs["pk"] is not None:
            return self.objects.filter(pk=kwargs['pk']).first() 
        if "id" in kwargs and kwargs["id"] is not None:
            return self.objects.filter(pk=kwargs['id']).first() 
        
                    

    def add_accounting_document_line(self,*args, **kwargs):
        accounting_document_line,message,result=(None,"",FAILED)
        if not Permission(request=self.request).is_permitted(APP_NAME,OperationEnum.ADD,"accountingdocumentline"):
        # if not self.request.user.has_perm(APP_NAME+".add_accountingdocumentline"):
            message="دسترسی غیر مجاز"
            return accounting_document_line,message,result
        
        accounting_document_line=AccountingDocumentLine()

        if 'title' in kwargs:
            accounting_document_line.title=kwargs['title']
        if 'event_id' in kwargs:
            accounting_document_line.event_id=kwargs['event_id']
        if 'accounting_document_id' in kwargs:
            accounting_document_line.accounting_document_id=kwargs['accounting_document_id']
        if 'description' in kwargs:
            accounting_document_line.description=kwargs['description']
        if 'bestankar' in kwargs  :
            accounting_document_line.bestankar=kwargs['bestankar']
        if 'bedehkar' in kwargs :
            accounting_document_line.bedehkar=kwargs['bedehkar'] 
        if 'account_code' in kwargs and kwargs['account_code'] is not None:
            account=AccountRepo(request=self.request).account(code=kwargs['account_code']) 
            if account is not None:
                accounting_document_line.account=account
        if 'account_id' in kwargs and kwargs['account_id'] is not None:
            accounting_document_line.account_id=kwargs['account_id'] 
        
        
        # if 'financial_year_id' in kwargs:
        #     payment.financial_year_id=kwargs['financial_year_id']
        # else:
        #     payment.financial_year_id=FinancialYear.get_by_date(date=payment.transaction_datetime).id

        accounting_document_line.save()
        accounting_document_line.account.normalize_total()
        result=SUCCEED
        message="با موفقیت اضافه گردید."
         

        return accounting_document_line,message,result

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
            search_for=kwargs["search_for"]
            objects=objects.filter(Q(name__contains=search_for) | Q(code=search_for) | Q(pure_code=search_for ) )
        return objects.all()
    def account(self,*args, **kwargs):
        if "account_id" in kwargs and kwargs["id"] is not None:
            return self.objects.filter(pk=kwargs['account_id']).first() 
        if "pk" in kwargs and kwargs["pk"] is not None:
            return self.objects.filter(pk=kwargs['pk']).first() 
        if "id" in kwargs and kwargs["id"] is not None:
            return self.objects.filter(pk=kwargs['id']).first() 
        if "code" in kwargs and kwargs["code"] is not None:
            a= self.objects.filter(Q(code=kwargs['code'])|Q(pure_code=kwargs['code'])).first()
            if a is not None:
                return a
            else:
                try:
                    pure_code=filter_number(kwargs['code'])
                    a= self.objects.filter(pure_code=pure_coed).first() 
                    if a is not None:
                        return a
                except:
                    pass
        if "account_code" in kwargs and kwargs["account_code"] is not None:
            a= self.objects.filter(code=kwargs['account_code']).first() 
            if a is not None:
                return a
            else:
                try:
                    a= self.objects.filter(pure_code=filter_number(kwargs['account_code'])).first() 
                    if a is not None:
                        return a
                except:
                    pass
                    

    def init_all_accounts_old(self,*args, **kwargs):
        tafsili_accounts_counter=0 
        basic_accounts_counter=0
        moein_accounts_counter=0
        account_group_counter=0
        account_groups,message,result=([],"",FAILED)
        if not self.request.user.has_perm(APP_NAME+".add_account"):
            message="دسترسی غیر مجاز"
            return tafsili_account,message,result
        
        account_groups=init_all_accounts_list()
        for account_group in account_groups:
            new_account_group=AccountGroup(name=account_group["name"],color=account_group["color"],code=account_group['code'])
            new_account_group.save()
            account_group_counter+-1
            if 'basic_accounts' in account_group:
                for basic_account in account_group["basic_accounts"]:
                    new_basic_account=BasicAccount(name=basic_account["name"],color=basic_account["color"],code=basic_account['code'],account_group=new_account_group)
                    new_basic_account.save()
                    if 'moein_accounts' in basic_account:
                        for moein_account in basic_account["moein_accounts"]:
                            new_moein_account=MoeinAccount(name=moein_account["name"],color=moein_account["color"],code=moein_account['code'],basic_account=new_basic_account)
                            # new_moein_account=MoeinAccount(basic_account=new_basic_account,**moein_account)
                            new_moein_account.save()

                            
                            if 'tafsili_accounts' in moein_account:

                                for tafsili_account in moein_account["tafsili_accounts"]:
                                    new_tafsili_account=TafsiliAccount(name=tafsili_account["name"],color=tafsili_account["color"],code=tafsili_account['code'],moein_account=new_moein_account)
                                    new_tafsili_account,result,message=new_tafsili_account.save()
                                    if result==SUCCEED:
                                        tafsili_accounts_counter+=1


                            if 'moein_accounts' in moein_account:
                                for moein_account2 in moein_account["moein_accounts"]:
                                    new_moein_account2=MoeinAccount(name=moein_account2["name"],moein_account=new_moein_account,color=moein_account2["color"],code=moein_account2['code'])
                                    # new_moein_account2=MoeinAccount(parent=new_moein_account,**moein_account2)
                                    new_moein_account2,result,message=new_moein_account2.save()
                                    if result==SUCCEED:
                                        moein_accounts_counter+=1

                                    if 'tafsili_accounts' in moein_account2:
                                        for tafsili_account in moein_account2["tafsili_accounts"]:
                                            new_tafsili_account=TafsiliAccount(name=tafsili_account["name"],color=tafsili_account["color"],code=tafsili_account['code'],moein_account=new_moein_account2)
                                            new_tafsili_account,result,message=new_tafsili_account.save()
                                            if result==SUCCEED:
                                                tafsili_accounts_counter+=1



        result=SUCCEED
        message="با موفقیت اضافه گردید."
        message=f"{tafsili_accounts_counter} تفصیلی {message}" 
        message=f"{tafsili_accounts_counter} تفصیلی {message}" 
        return account_groups,message,result
 
    def init_all_accounts(self,*args, **kwargs):
        tafsili_accounts_counter=0 
        basic_accounts_counter=0
        moein_accounts_counter=0
        moein2_accounts_counter=0
        account_group_counter=0
        result=SUCCEED
        message=""  
        if not self.request.user.has_perm(APP_NAME+".add_account"):
            message="دسترسی غیر مجاز"
            result=FAILED
            return message,result
        
        account_groups,basic_accounts,moein_accounts,moein2_accounts,tafsili_accounts=init_all_accounts_list()
        for account_group in account_groups:
            new_account_group=AccountGroup(name=account_group["name"],color=account_group["color"],code=account_group['code'])
            new_account_group.save()
            account_group_counter+=1
        for basic_account in basic_accounts:
            account_group=AccountGroup.objects.filter(code=basic_account["account_group_code"]).first()
            if account_group is not None:
                new_basic_account=BasicAccount(name=basic_account["name"],color=basic_account["color"],code=basic_account['code'],account_group_id=account_group.id)
                new_basic_account.save()
                basic_accounts_counter+=1
            else:
                message="کد گروه حساب نامعتبر است ."
                result=FAILED    

        for moein_account in moein_accounts:
            basic_account=BasicAccount.objects.filter(code=moein_account["basic_account_code"]).first()
            if basic_account is not None:
                print(moein_account) 
                new_moein_account=MoeinAccount(name=moein_account["name"],color=moein_account["color"],code=moein_account['code'],basic_account_id=basic_account.id)
            # new_moein_account=MoeinAccount(basic_account=new_basic_account,**moein_account)
                new_moein_account.save()
                moein_accounts_counter+=1
            else:
                result=FAILED     
                message="کد حساب کل نامعتبر است ."


        for moein2_account in moein2_accounts:
            moein_account=MoeinAccount.objects.filter(code=moein2_account["moein_account_code"]).first()
            if moein_account is not None: 
                new_moein2_account=MoeinAccount(name=moein2_account["name"],color=moein2_account["color"],code=moein2_account['code'],moein_account_id=moein_account.id)
                # new_moein_account=MoeinAccount(basic_account=new_basic_account,**moein_account)
                new_moein2_account.save()
                moein2_accounts_counter+=1
            else:
                result=FAILED          
                message="کد حساب معین نامعتبر است ."      

        for tafsili_account in tafsili_accounts: 
            moein_account=MoeinAccount.objects.filter(code=tafsili_account["moein_account_code"]).first()
            if moein_account is not None: 
                new_tafsili_account=TafsiliAccount(name=tafsili_account["name"],color=tafsili_account["color"],code=tafsili_account['code'],moein_account_id=moein_account.id)
                new_tafsili_account,result,message=new_tafsili_account.save()
                tafsili_accounts_counter+=1 
            else:
                result=FAILED          
                message="کد حساب معین نامعتبر است ."  

                                  

        account_group_counter=len(AccountGroup.objects.all())
        basic_accounts_counter=len(BasicAccount.objects.all())
        moein_accounts_counter=len(MoeinAccount.objects.all())
        tafsili_accounts_counter=len(TafsiliAccount.objects.all())
        if result==SUCCEED:
            message="با موفقیت اضافه گردید."
        message+=f"<br>{account_group_counter}   گروه حساب" 
        message+=f"<br>{basic_accounts_counter}   حساب  کل " 
        message+=f"<br>{moein_accounts_counter}  حساب معین " 
        message+=f"<br>{tafsili_accounts_counter} حساب تفصیلی " 
        return result,message
 
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
        
    def delete_all_accounts(self,*args, **kwargs):
        if not self.request.user.has_perm(APP_NAME+".delete_account"):
            message="دسترسی غیر مجاز"
            return message,result
        AccountingDocumentLine.objects.all().delete()
        AccountingDocument.objects.all().delete()
        Event.objects.all().delete()
        TafsiliAccount.objects.all().delete()
        MoeinAccount.objects.all().delete()
        BasicAccount.objects.all().delete()
        AccountGroup.objects.all().delete() 
        result=SUCCEED
        message="همه حساب ها حذف شد."
        return result,message
    
    def set_priority(self,*args, **kwargs):
        result,message,priority=FAILED,"",None
        if not self.request.user.has_perm(APP_NAME+".change_account"):
            return result,message,account_tags
        priority=kwargs['priority']
        account_id=kwargs['account_id']
        
         

        account=Account.objects.filter(pk=account_id).first()
        if account is not None:
            account.priority=priority
            account.save()

        result=SUCCEED

        return result,message,priority
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
    def tafsili_account(self,*args, **kwargs):
        if "tafsili_account_id" in kwargs:
            return self.objects.filter(pk=kwargs['tafsili_account_id']).first() 
        if "pk" in kwargs:
            return self.objects.filter(pk=kwargs['pk']).first() 
        if "id" in kwargs:
            return self.objects.filter(pk=kwargs['id']).first() 

            
    def add_tafsili_account(self,*args, **kwargs):
        tafsili_account,message,result=(None,"",FAILED)
        
        if not Permission(request=self.request).is_permitted(APP_NAME,OperationEnum.ADD,"tafsiliaccount"):
        # if not self.request.user.has_perm(APP_NAME+".add_account"):
            message="دسترسی غیر مجاز"
            return tafsili_account,message,result
        if len(TafsiliAccount.objects.filter(name=kwargs['name']))>0:
            message="از قبل حسابی با همین عنوان ثبت شده است."
            return tafsili_account,message,result
        if len(TafsiliAccount.objects.filter(code=kwargs['code']))>0:
            message="از قبل حسابی با همین کد ثبت شده است."
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
            tafsili_account.color=MoeinAccount.objects.filter(pk=kwargs["moein_account_id"]).first().color
        if 'tel' in kwargs:
            tafsili_account.tel=kwargs['tel']
        if 'color' in kwargs:
            tafsili_account.color=kwargs['color']
        if 'code' in kwargs:
            tafsili_account.code=kwargs['code']
        if 'tafsili_account_id' in kwargs and kwargs["tafsili_account_id"]>0:
            tafsili_account.tafsili_account_id=kwargs['tafsili_account_id']
       
        
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
        if "account_group_id" in kwargs:
            return self.objects.filter(pk=kwargs['account_group_id']).first() 
        if "pk" in kwargs:
            return self.objects.filter(pk=kwargs['pk']).first() 
        if "id" in kwargs:
            return self.objects.filter(pk=kwargs['id']).first() 

            
    def add_account_group(self,*args, **kwargs):
        account,message,result=(None,"",FAILED)
        if not Permission(request=self.request).is_permitted(APP_NAME,OperationEnum.ADD,"accountgroup"):
        # if not self.request.user.has_perm(APP_NAME+".add_account"):
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
        if "basic_account_id" in kwargs:
            return self.objects.filter(pk=kwargs['basic_account_id']).first() 
        if "pk" in kwargs:
            return self.objects.filter(pk=kwargs['pk']).first() 
        if "id" in kwargs:
            return self.objects.filter(pk=kwargs['id']).first() 
            
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
            
    def add_basic_account(self,*args, **kwargs):
        basic_account,message,result=(None,"",FAILED)
        if not Permission(request=self.request).is_permitted(APP_NAME,OperationEnum.ADD,"basicaccount"):
        # if not self.request.user.has_perm(APP_NAME+".add_account"):
            message="دسترسی غیر مجاز"
            return account,message,result
        basic_account=Account.objects.filter(name=kwargs['name']).first()
        if basic_account is not None:
            message="از قبل حسابی با همین عنوان ثبت شده است."
            return basic_account,message,result
        basic_account=Account.objects.filter(code=kwargs['code']).first()

        if basic_account is not None:
            message="از قبل حسابی با همین کد ثبت شده است."
            return basic_account,message,result

        basic_account=BasicAccount()

        if 'name' in kwargs:
            basic_account.name=kwargs['name']
        if 'code' in kwargs:
            basic_account.code=kwargs['code']
        if 'profile_id' in kwargs:
            basic_account.profile_id=kwargs['profile_id']
        if 'description' in kwargs:
            basic_account.description=kwargs['description']
        if 'address' in kwargs:
            basic_account.address=kwargs['address']
        if 'tel' in kwargs:
            basic_account.tel=kwargs['tel']
        if 'mobile' in kwargs:
            basic_account.mobile=kwargs['mobile']
        if 'parent_id' in kwargs and kwargs['parent_id']>0 :
            basic_account.parent_id=kwargs['parent_id']
        if 'account_group_id' in kwargs and kwargs['account_group_id']>0 :
            basic_account.color=AccountGroup.objects.filter(pk=kwargs["account_group_id"]).first().color
            basic_account.account_group_id=kwargs['account_group_id']
        if 'color' in kwargs:
            basic_account.color=kwargs['color']
        
        # if 'financial_year_id' in kwargs:
        #     payment.financial_year_id=kwargs['financial_year_id']
        # else:
        #     payment.financial_year_id=FinancialYear.get_by_date(date=payment.transaction_datetime).id

        basic_account.save()
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

        return basic_account,message,result
 
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
        if "moein_account_id" in kwargs:
            return self.objects.filter(pk=kwargs['moein_account_id']).first() 
        if "pk" in kwargs:
            return self.objects.filter(pk=kwargs['pk']).first() 
        if "id" in kwargs:
            return self.objects.filter(pk=kwargs['id']).first() 

            
    def add_moein_account(self,*args, **kwargs):
        moein_account,message,result=(None,"",FAILED)
        if not Permission(request=self.request).is_permitted(APP_NAME,OperationEnum.ADD,"moeinaccount"):
        # if not self.request.user.has_perm(APP_NAME+".add_account"):
            message="دسترسی غیر مجاز"
            return account,message,result

        moein_account=Account.objects.filter(name=kwargs['name']).first()
        if moein_account is not None:
            message="از قبل حسابی با همین عنوان ثبت شده است."
            return moein_account,message,result

            
        moein_account=Account.objects.filter(code=kwargs['code']).first()
        if moein_account is not None:
            message="از قبل حسابی با همین کد ثبت شده است."
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
        if 'moein_account_id' in kwargs and kwargs['moein_account_id']>0 :
            moein_account.moein_account_id=kwargs['moein_account_id']
            
            moein_account.color=MoeinAccount.objects.filter(pk=kwargs["moein_account_id"]).first().color
        if 'basic_account_id' in kwargs and kwargs['basic_account_id']>0 :
            moein_account.basic_account_id=kwargs['basic_account_id']
            moein_account.color=BasicAccount.objects.filter(pk=kwargs["basic_account_id"]).first().color
       
        
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
        if "accounting_document_id" in kwargs:
            return self.objects.filter(pk=kwargs['accounting_document_id']).first() 
        if "pk" in kwargs:
            return self.objects.filter(pk=kwargs['pk']).first() 
        if "id" in kwargs:
            return self.objects.filter(pk=kwargs['id']).first() 

            
    def add_accounting_document(self,*args, **kwargs):
        accounting_document,message,result=(None,"",FAILED)
        if not Permission(request=self.request).is_permitted(APP_NAME,OperationEnum.ADD,"accountingdocument"):
        # if not self.request.user.has_perm(APP_NAME+".add_account"):.
            message="دسترسی غیر مجاز"
            return accounting_document,message,result
        

        accounting_document=AccountingDocument()

        if 'title' in kwargs:
            accounting_document.title=kwargs['title']
        if 'profile_id' in kwargs:
            accounting_document.profile_id=kwargs['profile_id']
        if 'description' in kwargs:
            accounting_document.description=kwargs['description']
        if 'address' in kwargs:
            accounting_document.address=kwargs['address']
        if 'tel' in kwargs:
            accounting_document.tel=kwargs['tel']
        if 'mobile' in kwargs:
            accounting_document.mobile=kwargs['mobile']
       
        
        # if 'financial_year_id' in kwargs:
        #     payment.financial_year_id=kwargs['financial_year_id']
        # else:
        #     payment.financial_year_id=FinancialYear.get_by_date(date=payment.transaction_datetime).id

        accounting_document.save()
        result=SUCCEED
        message="با موفقیت اضافه گردید."
       

        return accounting_document,message,result
 
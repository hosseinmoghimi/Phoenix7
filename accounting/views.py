from django.shortcuts import render,reverse
from .apps import APP_NAME
from django.views import View
from .repo import AccountRepo,AccountGroupRepo,AccountingDocumentRepo,BasicAccountRepo
from .serializers import AccountSerializer,AccountGroupSerializer,BasicAccountSerializer
from .forms import *
from core.views import CoreContext
import json
LAYOUT_PARENT = "phoenix/layout.html"
TEMPLATE_ROOT = "accounting/"


def getContext(request, *args, **kwargs):
    context = CoreContext(request=request, app_name=APP_NAME)
    context['search_form'] = SearchForm()
    context['me_account']=AccountRepo(request=request).me
    context['search_action'] = reverse(APP_NAME+":search")
    context['LAYOUT_PARENT'] = LAYOUT_PARENT
    return context
class IndexView(View):
    def get(self,request,*args, **kwargs):
        context=getContext(request=request)
        return render(request,TEMPLATE_ROOT+"index.html",context)
class AccountsView(View):
    def get(self,request,*args, **kwargs):
        context=getContext(request=request)
        context['expand_accounts']=True
        if 'sv' in kwargs:
            context['SIMPLE_VIEW']=True
        accounts=AccountRepo(request=request).list()
        context['accounts']=accounts
        accounts_s=json.dumps(AccountSerializer(accounts,many=True).data)
        context['accounts_s']=accounts_s
        
        if request.user.has_perm(APP_NAME+".add_account"):
            context['add_account_form']=AddAccountForm()
        return render(request,TEMPLATE_ROOT+"accounts.html",context)
class AccountingDocumentsView(View):
    def get(self,request,*args, **kwargs):
        context=getContext(request=request)
        context['expand_accounts']=True
        if 'sv' in kwargs:
            context['SIMPLE_VIEW']=True
        accounting_documents=AccountingDocumentRepo(request=request).list()
        context['accounting_documents']=accounting_documents
         
        
        if request.user.has_perm(APP_NAME+".add_account"):
            context['add_account_form']=AddAccountingDocumentForm()
        return render(request,TEMPLATE_ROOT+"accounting-documents.html",context)
class AccountingDocumentLineView(View):
    def get(self,requets,*args, **kwargs):
        pass
class AccountingDocumentView(View):
    def get(self,request,*args, **kwargs):
        context=getContext(request=request)
        context['expand_accounts']=True
        if 'sv' in kwargs:
            context['SIMPLE_VIEW']=True
        accounting_document=AccountingDocumentRepo(request=request).accounting_document(*args, **kwargs)
        context['accounting_document']=accounting_document
         
        
        if request.user.has_perm(APP_NAME+".add_account"):
            context['add_account_form']=AddAccountingDocumentForm()
        return render(request,TEMPLATE_ROOT+"accounting-document.html",context)
class AccountView(View):
    def get(self,request,*args, **kwargs):
        context=getContext(request=request)
        account=AccountRepo(request=request).account(*args, **kwargs)
        context['account']=account
        account.normalize_total()
        accounting_document_lines=account.accountingdocumentline_set.all()
        context['accounting_document_lines']=accounting_document_lines

        account_s=json.dumps(AccountSerializer(account).data)
        context['account_s']=account_s
        return render(request,TEMPLATE_ROOT+"account.html",context)

class BasicAccountsView(View):
    def get(self,request,*args, **kwargs):
        context=getContext(request=request)
        basic_accounts=BasicAccountRepo(request=request).list(*args, **kwargs)
        for basic_account in basic_accounts:
            basic_account.normalize_total()
        context['basic_accounts']=basic_accounts
        sum_bed=0
        sum_bes=0
        for basic_account in basic_accounts:
            sum_bed+=basic_account.bedehkar 
            sum_bes+=basic_account.bestankar 
        context['sum_bedehkar']=sum_bed
        context['sum_bestankar']=sum_bes
        balance=sum_bed-sum_bes
        if not balance==0:
            context["balance"]=balance
        basic_accounts_s=json.dumps(BasicAccountSerializer(basic_accounts,many=True).data)
        context['basic_accounts_s']=basic_accounts_s
        return render(request,TEMPLATE_ROOT+"basic-accounts.html",context)

class BalanceView(View):
    def get(self,request,*args, **kwargs):
        context=getContext(request=request)
        basic_accounts=BasicAccountRepo(request=request).list(*args, **kwargs)
        context['basic_accounts']=basic_accounts
         
        basic_accounts_s=json.dumps(BasicAccountSerializer(basic_accounts,many=True).data)
        context['basic_accounts_s']=basic_accounts_s
        return render(request,TEMPLATE_ROOT+"balance.html",context)
class BasicAccountView(View):
    def get(self,request,*args, **kwargs):
        context=getContext(request=request)
        account=AccountRepo(request=request).account(*args, **kwargs)
        context['account']=account
        account_s=json.dumps(AccountSerializer(account).data)
        context['account_s']=account_s
        return render(request,TEMPLATE_ROOT+"basic-account.html",context)
class MoeinAccountView(View):
    def get(self,request,*args, **kwargs):
        context=getContext(request=request)
        account=AccountRepo(request=request).account(*args, **kwargs)
        context['account']=account
        account_s=json.dumps(AccountSerializer(account).data)
        context['account_s']=account_s
        return render(request,TEMPLATE_ROOT+"moein-account.html",context)
class AccountGroupView(View):
    def get(self,request,*args, **kwargs):
        context=getContext(request=request)
        account=AccountRepo(request=request).account(*args, **kwargs)
        context['account']=account
        account_s=json.dumps(AccountSerializer(account).data)
        context['account_s']=account_s
        return render(request,TEMPLATE_ROOT+"account-group.html",context)
class SearchView(View):
    def get(self,request,*args, **kwargs):
        pass
class AccountGroupsView(View):
    def get(self,request,*args, **kwargs):
        context=getContext(request=request)
        account_groups=AccountGroupRepo(request=request).list(*args, **kwargs)
        context['account_groups']=account_groups
        for account_group in account_groups:
            account_group.normalize_total()
        account_groups_s=json.dumps(AccountGroupSerializer(account_groups,many=True).data)
        context['account_groups_s']=account_groups_s
        return render(request,TEMPLATE_ROOT+"account-groups.html",context)
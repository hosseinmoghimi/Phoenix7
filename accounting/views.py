from django.shortcuts import render,reverse
from .apps import APP_NAME
from django.views import View
from .repo import AccountRepo,AccountGroupRepo
from .serializers import AccountSerializer,AccountGroupSerializer
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
class AccountView(View):
    def get(self,request,*args, **kwargs):
        context=getContext(request=request)
        account=AccountRepo(request=request).account(*args, **kwargs)
        context['account']=account
        account_s=json.dumps(AccountSerializer(account).data)
        context['account_s']=account_s
        return render(request,TEMPLATE_ROOT+"account.html",context)
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
        account_groups_s=json.dumps(AccountGroupSerializer(account_groups,many=True).data)
        context['account_groups_s']=account_groups_s
        return render(request,TEMPLATE_ROOT+"account-groups.html",context)
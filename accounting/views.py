from django.shortcuts import render,reverse
from .apps import APP_NAME
from django.views import View
from .repo import TafsiliAccountRepo,AccountGroupRepo,AccountingDocumentRepo,BasicAccountRepo,MoeinAccountRepo
from .serializers import TafsiliAccountSerializer,AccountGroupSerializer,BasicAccountSerializer
from .forms import *
from core.views import CoreContext
import json
from utility.currency import to_price
from utility.templatetags.to_price import to_price_color
from utility.log import leolog
LAYOUT_PARENT = "phoenix/layout.html"
TEMPLATE_ROOT = "accounting/"


def getContext(request, *args, **kwargs):
    context = CoreContext(request=request, app_name=APP_NAME)
    context['search_form'] = SearchForm()
    context['me_account']=TafsiliAccountRepo(request=request).me
    context['search_action'] = reverse(APP_NAME+":search")
    context['LAYOUT_PARENT'] = LAYOUT_PARENT
    return context

def get_account_context(account,*args, **kwargs):
    context={}
    context['account']=account
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

class TafsiliAccountView(View):
    def get(self,request,*args, **kwargs):
        context=getContext(request=request)
        tasili_account=TafsiliAccountRepo(request=request).account(*args, **kwargs)
        context['tasili_account']=tasili_account
        context.update(get_account_context(account=tasili_account))
        account.normalize_total()
        accounting_document_lines=account.accountingdocumentline_set.all()
        context['accounting_document_lines']=accounting_document_lines

        account_s=json.dumps(AccountSerializer(account).data)
        context['account_s']=account_s
        return render(request,TEMPLATE_ROOT+"tafsili-account.html",context)

class AccountView(View):
    def get(self,request,*args, **kwargs):
        context=getContext(request=request)
        tasili_account=TafsiliAccountRepo(request=request).account(*args, **kwargs)
        context['tasili_account']=tasili_account
        context.update(get_account_context(account=tasili_account))
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
        basic_account=BasicAccountRepo(request=request).basic_account(*args, **kwargs)
        context.update(get_account_context(account=basic_account))
        context['basic_account']=basic_account
        # basic_account_s=json.dumps(BasicAccountSerializer(basic_account).data)
        # context['basic_account_s']=basic_account_s
        return render(request,TEMPLATE_ROOT+"basic-account.html",context)

class SettingsView(View):
    def get(self,request,*args, **kwargs):
        context=getContext(request=request)
        basic_account=BasicAccountRepo(request=request).basic_account(*args, **kwargs)
        context['basic_account']=basic_account
        # basic_account_s=json.dumps(BasicAccountSerializer(basic_account).data)
        # context['basic_account_s']=basic_account_s
        return render(request,TEMPLATE_ROOT+"settings.html",context)

class MoeinAccountView(View):   
    def get(self,request,*args, **kwargs):
        context=getContext(request=request)
        moein_account=MoeinAccountRepo(request=request).moein_account(*args, **kwargs)
        context['moein_account']=moein_account 
        context.update(get_account_context(account=moein_account))
        
        # account_s=json.dumps(AccountSerializer(account).data)
        # context['account_s']=account_s
        CAN_ADD_MOEIN_ACCOUNT=True
        CAN_ADD_TAFSILI_ACCOUNT=True
        if CAN_ADD_MOEIN_ACCOUNT :
            context['add_moein_account_form']=AddMoeinAccountForm()
        if CAN_ADD_TAFSILI_ACCOUNT :
            context['add_tafsili_account_form']=AddTafsiliAccountForm()
        return render(request,TEMPLATE_ROOT+"moein-account.html",context)

class MoeinAccountsView(View):   
    def get(self,request,*args, **kwargs):
        context=getContext(request=request)
        moein_accounts=MoeinAccountRepo(request=request).list(*args, **kwargs)
        context['moein_accounts']=moein_accounts 
        
        # account_s=json.dumps(AccountSerializer(account).data)
        # context['account_s']=account_s
        return render(request,TEMPLATE_ROOT+"moein-accounts.html",context)

class AccountGroupView(View):
    def get(self,request,*args, **kwargs):
        context=getContext(request=request)
        account_group=AccountGroupRepo(request=request).account_group(*args, **kwargs)
        context.update(get_account_context(account=account_group))
        context['account_group']=account_group
        # account_s=json.dumps(AccountSerializer(account).data)
        # context['account_s']=account_s
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

class TreeListView(View):
    def get(self,request,*args, **kwargs):
        context=getContext(request=request)
        account_groups=AccountGroupRepo(request=request).list(*args, **kwargs)
        context['account_groups']=account_groups
        return render(request,TEMPLATE_ROOT+"tree-list.html",context)

class AddEventView(View):
    def get(self,request,*args, **kwargs):
        context=getContext(request=request)
        account_groups=AccountGroupRepo(request=request).list(*args, **kwargs)
        context['account_groups']=account_groups
        for account_group in account_groups:
            account_group.normalize_total()
        account_groups_s=json.dumps(AccountGroupSerializer(account_groups,many=True).data)
        context['account_groups_s']=account_groups_s
        return render(request,TEMPLATE_ROOT+"add-event.html",context)

class EditDocumentView(View):
    def get(self,request,*args, **kwargs):
        context=getContext(request=request)
        account_groups=AccountGroupRepo(request=request).list(*args, **kwargs)
        context['account_groups']=account_groups
        for account_group in account_groups:
            account_group.normalize_total()
        # account_groups_s=json.dumps(AccountGroupSerializer(account_groups,many=True).data)
        # context['account_groups_s']=account_groups_s
        
        return render(request,TEMPLATE_ROOT+"edit-document.html",context)

class AddDocumentView(View):
    def get(self,request,*args, **kwargs):
        context=getContext(request=request)
        account_groups=AccountGroupRepo(request=request).list(*args, **kwargs)
        context['account_groups']=account_groups
        for account_group in account_groups:
            account_group.normalize_total()
        account_groups_s=json.dumps(AccountGroupSerializer(account_groups,many=True).data)
        context['account_groups_s']=account_groups_s
        return render(request,TEMPLATE_ROOT+"add-document.html",context)

class TreeChartView(View):
    def get(self,request,*args, **kwargs):
        context=getContext(request=request)
        if 'pk' in kwargs:
            account_groups=[AccountGroupRepo(request=request).account_group(*args, **kwargs)]
        else:
            account_groups=AccountGroupRepo(request=request).list(*args, **kwargs)

        context['account_groups']=account_groups
        pages=[]
        pages.append({
            'title': f"""گروه های حساب""",
            'parent_id': 0,
            'parent': 0,
            'get_absolute_url':reverse("accounting:account_groups"),
            'id': 1,
            'pre_title': "",
            'sub_title': "",
            })
        AG=100
        BA=100000
        MA=100000000
        MA2=10000000000
        for account_group in account_groups:
            page=account_group
            pages.append({
                'title': f"""{page.code}<br>{page.title}""",
                'parent_id': 1,
                'parent': 1,
                'get_absolute_url': page.get_absolute_url(),
                'id': AG+page.id,
                'pre_title': "",
                'sub_title':to_price_color(page.balance),
                })
                
            for basic_account in account_group.basicaccount_set.all():
                page=basic_account
                pages.append({
                    'title': f"""{page.code}<br>{page.title}""",
                    'parent_id': AG+page.account_group.id,
                    'parent': AG+page.account_group.id,
                    'get_absolute_url': page.get_absolute_url(),
                    'id': BA+page.id,
                    'pre_title': "",
                    'sub_title': to_price_color(page.balance),
                    })
                    
                for moein_account in basic_account.moeinaccount_set.all():
                    page=moein_account
                    pages.append({
                        'title': f"""{page.title}""",
                        'parent_id': BA+page.basic_account.id,
                        'parent': BA+page.basic_account.id,
                        'get_absolute_url': page.get_absolute_url(),
                        'id': MA+page.id,
                        'pre_title': "",
                        'sub_title':to_price_color(page.balance),
                        })
                    for moein_account2 in moein_account.moeinaccount_set.all():
                        page=moein_account2
                        pages.append({
                            'title': f"""{page.title}""",
                            'parent_id': MA+page.parent.id,
                            'parent': MA+page.parent.id,
                            'get_absolute_url': page.get_absolute_url(),
                            'id': MA2+page.id,
                            'pre_title': "",
                            'sub_title':to_price_color(page.balance),
                            })

        context['pages_s'] = json.dumps(pages)

        return render(request,TEMPLATE_ROOT+"tree-chart.html",context)
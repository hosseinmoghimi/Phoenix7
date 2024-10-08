from django.shortcuts import render,reverse
from .apps import APP_NAME
from processmanagement.permission import Permission,OperationEnum
from django.views import View
from .repo import PersonRepo,AccountingDocumentLineRepo,TafsiliAccountRepo,AccountGroupRepo,AccountingDocumentRepo,BasicAccountRepo,MoeinAccountRepo,AccountRepo,EventRepo
from .serializers import TafsiliAccountSerializer,AccountGroupSerializer,BasicAccountSerializer,MoeinAccountSerializer,AccountSerializer,EventSerializer,AccountingDocumentSerializer
from .serializers import PersonSerializer,AccountGroupBriefSerializer,BasicAccountBriefSerializer,MoeinAccountBriefSerializer,TafsiliAccountBriefSerializer,AccountingDocumentLineSerializer
from .forms import *
from core.views import CoreContext
from core.enums import ColorEnum
import json
from utility.currency import to_price
from utility.templatetags.to_price import to_price_color
from utility.log import leolog
from phoenix.server_settings import CURRENCY
LAYOUT_PARENT = "phoenix/layout.html"
WIDE_LAYOUT_PARENT = "phoenix/wide-layout.html"
TEMPLATE_ROOT = "accounting/"


def getContext(request,app_name=APP_NAME, *args, **kwargs):
    context = CoreContext(request=request, app_name=APP_NAME)
    context['search_form'] = SearchForm()
    context['me_account']=TafsiliAccountRepo(request=request).me
    context['search_action'] = reverse(APP_NAME+":search")
    context['WIDE_LAYOUT_PARENT'] = WIDE_LAYOUT_PARENT
    context['LAYOUT_PARENT'] = LAYOUT_PARENT
    context['CURRENCY'] = CURRENCY
    return context

def get_account_context(account,*args, **kwargs):

    context={}
    context['account']=account
    
    account.normalize_total()
    account_s=json.dumps(AccountSerializer(account).data)
    context['account_s']=account_s

    
    accounting_document_lines=account.accountingdocumentline_set.all().order_by('-bedehkar')
    context['accounting_document_lines']=accounting_document_lines



    account.normalize_total()
    all_sub_accounts_lines=account.all_sub_accounts_lines().order_by('-bedehkar')
    all_sub_accounts_lines_s=json.dumps(AccountingDocumentLineSerializer(all_sub_accounts_lines,many=True).data)
    context['all_sub_accounts_lines_s']=all_sub_accounts_lines_s
    context['accounting_document_lines']=all_sub_accounts_lines
    context['accounting_document_lines_s']=all_sub_accounts_lines_s
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
    def get(self,request,*args, **kwargs):
        
        context=getContext(request=request)
        context['expand_accounts']=True
        if 'sv' in kwargs:
            context['SIMPLE_VIEW']=True
        accounting_document_line=AccountingDocumentLineRepo(request=request).accounting_document_line()
        context['accounting_document_line']=accounting_document_line
         
         
        return render(request,TEMPLATE_ROOT+"accounting-document-line.html",context)

class AccountingDocumentView(View):
    def get(self,request,*args, **kwargs):
        context=getContext(request=request)
        context['expand_accounts']=True
        if 'sv' in kwargs:
            context['SIMPLE_VIEW']=True
        accounting_document=AccountingDocumentRepo(request=request).accounting_document(*args, **kwargs)
        context['accounting_document']=accounting_document
        accounting_document_lines=accounting_document.accountingdocumentline_set.all().order_by('-bedehkar')
        accounting_document_lines_s=json.dumps(AccountingDocumentLineSerializer(accounting_document_lines,many=True).data)
        context["accounting_document_lines_s"]=accounting_document_lines_s
        
        if request.user.has_perm(APP_NAME+".add_account"):
            context['add_account_form']=AddAccountingDocumentForm()
        
        if request.user.has_perm(APP_NAME+".add_accountingdocumentline"):
            accounts_for_adding_accounting_document_line=AccountRepo(request=request).list().order_by("name")
            context["accounts_for_adding_accounting_document_line"]=accounts_for_adding_accounting_document_line
            context['add_accounting_document_line_form']=AddAccountingDocumentLineForm()
        return render(request,TEMPLATE_ROOT+"accounting-document.html",context)

class TafsiliAccountView(View):
    def get(self,request,*args, **kwargs):
        context=getContext(request=request)
        tafsili_account=TafsiliAccountRepo(request=request).tafsili_account(*args, **kwargs)
        context['tafsili_account']=tafsili_account
        context.update(get_account_context(account=tafsili_account))
        tafsili_account.normalize_total()
        accounting_document_lines=tafsili_account.accountingdocumentline_set.all()
        context['accounting_document_lines']=accounting_document_lines

        tafsili_account_s=json.dumps(TafsiliAccountSerializer(tafsili_account).data)
        context['tafsili_account_s']=tafsili_account_s
        
        CAN_ADD_TAFSILI_ACCOUNT=True
        if CAN_ADD_TAFSILI_ACCOUNT :
            context['add_tafsili_account_form']=AddTafsiliAccountForm()
        return render(request,TEMPLATE_ROOT+"tafsili-account.html",context)

class AccountView(View):
    def get(self,request,*args, **kwargs):
        context=getContext(request=request)
        account=AccountRepo(request=request).account(*args, **kwargs)
        context.update(get_account_context(account=account))
  
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
        account_groups=AccountGroupRepo(request=request).list()
        account_groups_s=json.dumps(AccountGroupBriefSerializer(account_groups,many=True).data)
        context['account_groups_s']=account_groups_s
        context['account_groups']=account_groups
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

        moein_accounts=basic_account.moeinaccount_set.order_by('code')
        moein_accounts_s=json.dumps(MoeinAccountBriefSerializer(moein_accounts,many=True).data)
        context['moein_accounts_s']=moein_accounts_s


        CAN_ADD_MOEIN_ACCOUNT=True
        
        if CAN_ADD_MOEIN_ACCOUNT :
            context['add_moein_account_form']=AddMoeinAccountForm()

        return render(request,TEMPLATE_ROOT+"basic-account.html",context)

class SettingsView(View):
    def get(self,request,*args, **kwargs):
        context=getContext(request=request)
        basic_account=BasicAccountRepo(request=request).basic_account(*args, **kwargs)
        context['basic_account']=basic_account
        # basic_account_s=json.dumps(BasicAccountSerializer(basic_account).data)
        # context['basic_account_s']=basic_account_s
        return render(request,TEMPLATE_ROOT+"settings.html",context)

class SelectionView(View):
    def get(self,request,*args, **kwargs):
        context=getContext(request=request)

        account_groups=AccountGroupRepo(request=request).list(*args, **kwargs)
        context['account_groups']=account_groups
        account_groups_s=json.dumps(AccountGroupBriefSerializer(account_groups,many=True).data)
        context['account_groups_s']=account_groups_s

        

        basic_accounts=BasicAccountRepo(request=request).list(*args, **kwargs)
        context['basic_accounts']=basic_accounts
        basic_accounts_s=json.dumps(BasicAccountBriefSerializer(basic_accounts,many=True).data)
        context['basic_accounts_s']=basic_accounts_s


        moein_accounts=MoeinAccountRepo(request=request).list(*args, **kwargs)
        context['moein_accounts']=moein_accounts
        moein_accounts_s=json.dumps(MoeinAccountBriefSerializer(moein_accounts,many=True).data)
        context['moein_accounts_s']=moein_accounts_s

        
        moein_accounts2=MoeinAccountRepo(request=request).list(*args, **kwargs)
        context['moein_accounts2']=moein_accounts2
        moein_accounts2_s=json.dumps(MoeinAccountBriefSerializer(moein_accounts2,many=True).data)
        context['moein_accounts2_s']=moein_accounts2_s


        return render(request,TEMPLATE_ROOT+"selection.html",context)

class MoeinAccountView(View):   
    def get(self,request,*args, **kwargs):
        context=getContext(request=request)
        moein_account=MoeinAccountRepo(request=request).moein_account(*args, **kwargs)
        context['moein_account']=moein_account 
        context.update(get_account_context(account=moein_account))
        

        moein_accounts=moein_account.moeinaccount_set.order_by('code')
        moein_accounts_s=json.dumps(MoeinAccountBriefSerializer(moein_accounts,many=True).data)
        context['moein_accounts_s']=moein_accounts_s

        # account_s=json.dumps(AccountSerializer(account).data)
        # context['account_s']=account_s

        tafsili_accounts=moein_account.tafsiliaccount_set.order_by('code')
        tafsili_accounts_s=json.dumps(TafsiliAccountBriefSerializer(tafsili_accounts,many=True).data)
        context['tafsili_accounts_s']=tafsili_accounts_s

        CAN_ADD_MOEIN_ACCOUNT=True
        CAN_ADD_TAFSILI_ACCOUNT=True
        if moein_account.basic_account is None:
            CAN_ADD_MOEIN_ACCOUNT=False
        else:
            CAN_ADD_TAFSILI_ACCOUNT=False
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

        basic_accounts=account_group.basicaccount_set.order_by('code')
        context['basic_accounts_s']=json.dumps(BasicAccountBriefSerializer(basic_accounts,many=True).data)

        CAN_ADD_BASIC_ACCOUNT=False
        if Permission(request=self.request).is_permitted(APP_NAME,OperationEnum.ADD,"basicaccount"):
            CAN_ADD_BASIC_ACCOUNT=True
        if CAN_ADD_BASIC_ACCOUNT :
            context['add_basic_account_form']=AddBasicAccountForm()
            context['colors']=(i[0] for i in ColorEnum.choices)
        return render(request,TEMPLATE_ROOT+"account-group.html",context)

class EventsView(View):
    
    def get(self,request,*args, **kwargs):
        context=getContext(request=request)
        events=EventRepo(request=request).list(*args, **kwargs)
        context['events']=events
        events_s=json.dumps(EventSerializer(events,many=True).data)
        context['events_s']=events_s
 
        context['expand_events']=True
        return render(request,TEMPLATE_ROOT+"events.html",context)

class ReportView(View):
    
    def get(self,request,*args, **kwargs):
        context=getContext(request=request)
        events=EventRepo(request=request).list(*args, **kwargs)
        context['events']=events
        events_s=json.dumps(EventSerializer(events,many=True).data)
        context['events_s']=events_s
 
        return render(request,TEMPLATE_ROOT+"report.html",context)
    def post(self,request,*args, **kwargs):
        from .apis import GetReportApi
        return GetReportApi().post(request=request)

class EventView(View):
    def get(self,request,*args, **kwargs):
        context=getContext(request=request)
        event=EventRepo(request=request).event(*args, **kwargs)
        context['event']=event
        event_s=json.dumps(EventSerializer(event).data)
        context['event_s']=event_s


        
        accounting_document_lines=AccountingDocumentLineRepo(request=request).list(event_id=event.id).order_by('-bedehkar')
        accounting_document_lines_s=json.dumps(AccountingDocumentLineSerializer(accounting_document_lines,many=True).data)
        context["accounting_document_lines_s"]=accounting_document_lines_s
        if len(accounting_document_lines)==0:
            context['add_event_to_document_form']=AddEventToAccountingDocumentForm()

        return render(request,TEMPLATE_ROOT+"event.html",context)

class SearchView(View):
    def get(self,request,*args, **kwargs):
        pass
    def post(self,request,*args, **kwargs):
        context=getContext(request=request)
        search_form=SearchForm(request.POST)
        if search_form.is_valid():
            search_for=search_form.cleaned_data['search_for']

            accounts=AccountRepo(request=request).list(search_for=search_for,*args, **kwargs)
            context['accounts']=accounts
            accounts_s=json.dumps(AccountSerializer(accounts,many=True).data)
            context['accounts_s']=accounts_s

            accounting_documents=AccountingDocumentRepo(request=request).list(search_for=search_for,*args, **kwargs)
            context['accounting_documents']=accounting_documents
            accounting_documents_s=json.dumps(AccountingDocumentSerializer(accounting_documents,many=True).data)
            context['accounting_documents_s']=accounting_documents_s


        return render(request,TEMPLATE_ROOT+"search.html",context)

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

class AddAccountingDocumentView(View):
    def post(self,request,*args, **kwargs):
        from .apis import AddAccountingDocumentApi
        return AddAccountingDocumentApi().post(request,*args, **kwargs) 
    def get(self,request,*args, **kwargs):
        context=getContext(request=request)
        account_groups=AccountGroupRepo(request=request).list(*args, **kwargs)
        context['account_groups']=account_groups
        for account_group in account_groups:
            account_group.normalize_total()
        account_groups_s=json.dumps(AccountGroupSerializer(account_groups,many=True).data)
        context['account_groups_s']=account_groups_s
        return render(request,TEMPLATE_ROOT+"add-accounting-document.html",context)

class PersonsView(View):
    def get(self,request,*args, **kwargs):
        context=getContext(request=request)
        persons=PersonRepo(request=request).list(*args, **kwargs)
        context['persons']=persons
        persons_s=json.dumps(PersonSerializer(persons,many=True).data)
        context['persons_s']=persons_s
        return render(request,TEMPLATE_ROOT+"persons.html",context)

class PersonView(View):
    def get(self,request,*args, **kwargs):
        context=getContext(request=request)
        person=PersonRepo(request=request).person(*args, **kwargs)
        context['person']=person
         
        person_s=json.dumps(PersonSerializer(person).data)
        context['person_s']=person_s
        return render(request,TEMPLATE_ROOT+"person.html",context)

class TreeListView(View):
    def get(self,request,*args, **kwargs):
        context=getContext(request=request)
        account_groups=AccountGroupRepo(request=request).list(*args, **kwargs)
        context['account_groups']=account_groups
        return render(request,TEMPLATE_ROOT+"tree-list.html",context)

class AddEventView(View):
    def post(self,request,*args, **kwargs):
        from .apis import AddEventApi
        return AddEventApi().post(request,*args, **kwargs)
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
 
class TreeChartView(View):
    def get(self,request,*args, **kwargs):
        context=getContext(request=request)
        if 'pk' in kwargs:
            account_groups=[AccountGroupRepo(request=request).account_group(*args, **kwargs)]
        else:
            account_groups=AccountGroupRepo(request=request).list(*args, **kwargs)

        context['account_groups']=account_groups
        pages=[]
        # pages.append({
        #     'title': f"""گروه های حساب""",
        #     'parent_id': -1,
        #     'parent': -1,
        #     'get_absolute_url':reverse("accounting:account_groups"),
        #     'id': 1,
        #     'pre_title': "",
        #     'sub_title': "",
        #     })
        AG=100
        BA=100000
        MA=100000000
        MA2=10000000000
        for account_group in account_groups:
            page=account_group
            pages.append({
                'title': f"""{page.code}<br>{page.title}""",
                'parent_id': 0,
                'parent': 0,
                'get_absolute_url': page.get_absolute_url(),
                'id': AG+page.id,
                'pre_title': "",
                'color': page.color,
                'sub_title':to_price_color(page.balance),
                })
                
            for basic_account in account_group.basicaccount_set.all():
                page=basic_account
                pages.append({
                    'title': f"""{page.code}<br>{page.title}""",
                    'parent_id': AG+page.parent.id,
                    'parent': AG+page.parent.id,
                    'get_absolute_url': page.get_absolute_url(),
                    'id': BA+page.id,
                    'pre_title': "",
                    'color': page.color,
                    'sub_title': to_price_color(page.balance),
                    })
                    
                for moein_account in basic_account.moeinaccount_set.all():
                    page=moein_account
                    pages.append({
                        'title': f"""{page.title}""",
                        'parent_id': BA+page.parent.id,
                        'parent': BA+page.parent.id,
                        'get_absolute_url': page.get_absolute_url(),
                        'id': MA+page.id,
                        'pre_title': "",
                        'color': page.color,
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
                            'color': page.color,
                            'sub_title':to_price_color(page.balance),
                            })

        context['pages_s'] = json.dumps(pages)

        return render(request,TEMPLATE_ROOT+"tree-chart.html",context)
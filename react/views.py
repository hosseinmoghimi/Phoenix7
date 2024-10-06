from django.shortcuts import render,reverse
from .apps import APP_NAME
from processmanagement.permission import Permission,OperationEnum
from django.views import View
from accounting.repo import PersonRepo,AccountingDocumentLineRepo,TafsiliAccountRepo,AccountGroupRepo,AccountingDocumentRepo,BasicAccountRepo,MoeinAccountRepo,AccountRepo,EventRepo
from accounting.serializers import TafsiliAccountSerializer,AccountGroupSerializer,BasicAccountSerializer,MoeinAccountSerializer,AccountSerializer,EventSerializer,AccountingDocumentSerializer
from accounting.serializers import PersonSerializer,AccountGroupBriefSerializer,BasicAccountBriefSerializer,MoeinAccountBriefSerializer,TafsiliAccountBriefSerializer,AccountingDocumentLineSerializer
from accounting.forms import *
from core.views import CoreContext
from core.enums import ColorEnum
import json
from utility.currency import to_price
from utility.templatetags.to_price import to_price_color
from utility.log import leolog
from phoenix.server_settings import CURRENCY
LAYOUT_PARENT = "phoenix/layout.html"
WIDE_LAYOUT_PARENT = "phoenix/wide-layout.html"
TEMPLATE_ROOT = "react/"


def getContext(request,app_name=APP_NAME, *args, **kwargs):
    context = CoreContext(request=request, app_name=APP_NAME)
    context['search_form'] = SearchForm()
    context['me_account']=TafsiliAccountRepo(request=request).me
    context['search_action'] = reverse(APP_NAME+":search")
    context['WIDE_LAYOUT_PARENT'] = WIDE_LAYOUT_PARENT
    context['LAYOUT_PARENT'] = LAYOUT_PARENT
    context['CURRENCY'] = CURRENCY
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
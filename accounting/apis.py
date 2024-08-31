
import json
from unicodedata import category
from utility.constants import FAILED,SUCCEED
from rest_framework.views import APIView

from utility.calendar import PersianCalendar
from utility.log import leolog
from .repo import TafsiliAccountRepo,MoeinAccountRepo,BasicAccountRepo,AccountRepo,AccountingDocumentLineRepo
from django.http import JsonResponse
from .forms import *
from .serializers import TafsiliAccountBriefSerializer,MoeinAccountBriefSerializer,BasicAccountBriefSerializer,AccountingDocumentLineSerializer

class SelectAccountGroupApi(APIView):
    def post(self,request,*args, **kwargs):
        context={}
        result=FAILED
        message=""
        log=111
        context['result']=FAILED
        if request.method=='POST':
            log=222
            select_account_group_form=SelectAccountGroupForm(request.POST)
            if add_moein_account_form.is_valid():
                log=333
                cd=add_moein_account_form.cleaned_data
                moein_account,message,result=MoeinAccountRepo(request=request).add_moein_account(**cd)
                if moein_account is not None:
                    context['moein_account']=MoeinAccountSerializer(moein_account).data
        context['message']=message
        context['result']=result
        context['log']=log
        return JsonResponse(context)


class AddMoeinAccountApi(APIView):
    def post(self,request,*args, **kwargs):
        context={}
        result=FAILED
        message=""
        log=111
        context['result']=FAILED
        if request.method=='POST':
            log=222
            add_moein_account_form=AddMoeinAccountForm(request.POST)
            if add_moein_account_form.is_valid():
                log=333
                cd=add_moein_account_form.cleaned_data
                moein_account,message,result=MoeinAccountRepo(request=request).add_moein_account(**cd)
                if moein_account is not None:
                    context['moein_account']=MoeinAccountBriefSerializer(moein_account).data
        context['message']=message
        context['result']=result
        context['log']=log
        return JsonResponse(context)




class AddBasicAccountApi(APIView):
    def post(self,request,*args, **kwargs):
        context={}
        result=FAILED
        message=""
        log=111
        context['result']=FAILED
        if request.method=='POST':
            log=222
            add_basic_account_form=AddBasicAccountForm(request.POST)
            if add_basic_account_form.is_valid():
                log=333
                cd=add_basic_account_form.cleaned_data
                basic_account,message,result=BasicAccountRepo(request=request).add_basic_account(**cd)
                if basic_account is not None:
                    context['basic_account']=BasicAccountBriefSerializer(basic_account).data
        context['message']=message
        context['result']=result
        context['log']=log
        return JsonResponse(context)





class AddTafsiliAccountApi(APIView):
    def post(self,request,*args, **kwargs):
        context={}
        result=FAILED
        message=""
        log=111
        context['result']=FAILED
        if request.method=='POST':
            log=222
            add_tafsili_account_form=AddTafsiliAccountForm(request.POST)
            if add_tafsili_account_form.is_valid():
                log=333
                cd=add_tafsili_account_form.cleaned_data
                tafsili_account,message,result=TafsiliAccountRepo(request=request).add_tafsili_account(**cd)
                if tafsili_account is not None:
                    context['tafsili_account']=TafsiliAccountBriefSerializer(tafsili_account).data
        context['message']=message
        context['result']=result
        context['log']=log
        return JsonResponse(context)




class InitALLAccountsApi(APIView):
    def post(self,request,*args, **kwargs):
        context={}
        result=FAILED
        message=""
        log=111
        context['result']=FAILED
        if request.method=='POST':
            (account_groups,result,message)=AccountRepo(request=request).init_all_accounts() 
        context['message']=message
        context['result']=result
        context['log']=log
        return JsonResponse(context)



class DeleteALLAccountsApi(APIView):
    def post(self,request,*args, **kwargs):
        context={}
        result=FAILED
        message=""
        log=111
        context['result']=FAILED
        if request.method=='POST':
            (result,message)=AccountRepo(request=request).delete_all_accounts() 
        context['message']=message
        context['result']=result
        context['log']=log
        return JsonResponse(context)


class AddAccountingDocumentLineApi(APIView):
    def post(self,request,*args, **kwargs):
        context={}
        result=FAILED
        message=""
        log=111
        context['result']=FAILED
        if request.method=='POST':
            log=222
            message="پارامتر های ورودی صحیح نمی باشند."
            _form=AddAccountingDocumentLineForm(request.POST)
            if _form.is_valid():
                log=333
                cd=_form.cleaned_data
                accounting_document_line,message,result=AccountingDocumentLineRepo(request=request).add_accounting_document_line(**cd)
                if accounting_document_line is not None:
                    context['accounting_document_line']=AccountingDocumentLineSerializer(accounting_document_line).data
        context['message']=message
        context['result']=result
        context['log']=log
        return JsonResponse(context)


class AddAccountApi(APIView):
    def post(self,request,*args, **kwargs):
        context={}
        result=FAILED
        message=""
        log=111
        context['result']=FAILED
        if request.method=='POST':
            log=222
            add_account_form=AddAccountForm(request.POST)
            if add_account_form.is_valid():
                log=333
                cd=add_account_form.cleaned_data
                account,message,result=AccountRepo(request=request).add_account(**cd)
                if account is not None:
                    context['account']=AccountSerializer(account).data
        context['message']=message
        context['result']=result
        context['log']=log
        return JsonResponse(context)

 
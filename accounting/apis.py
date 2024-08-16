
import json
from unicodedata import category
from utility.constants import FAILED,SUCCEED
from rest_framework.views import APIView

from utility.calendar import PersianCalendar
from utility.log import leolog
from .repo import TafsiliAccountRepo,MoeinAccountRepo
from django.http import JsonResponse
from .forms import *
from .serializers import TafsiliAccountSerializer,MoeinAccountSerializer

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
                    context['moein_account']=MoeinAccountSerializer(moein_account).data
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
            from .repo import init_all_accounts
            (result,message)=init_all_accounts() 
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

 
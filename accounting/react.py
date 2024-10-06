
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


class ReactView(View):
    def get(self,request,*args, **kwargs):
        context=getContext(request=request)
        persons=PersonRepo(request=request).list(*args, **kwargs)
        context['persons']=persons
        persons_s=json.dumps(PersonSerializer(persons,many=True).data)
        context['persons_s']=persons_s
        return render(request,TEMPLATE_ROOT+"persons.html",context)

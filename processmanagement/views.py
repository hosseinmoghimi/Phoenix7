from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import render,reverse
from .apps import APP_NAME
from core.views import CoreContext, MessageView, PageContext,SearchForm
# Create your views here.
from .repo import ProcessRepo
from django.views import View 
import json
from phoenix.apps import phoenix_apps
LAYOUT_PARENT = "phoenix/layout.html"
TEMPLATE_ROOT = "processmanagement/"


def getContext(request, *args, **kwargs):
    context = CoreContext(request=request, app_name=APP_NAME)
    context['LAYOUT_PARENT'] = LAYOUT_PARENT
    return context

 
class IndexView(View):
    def get(self,request,*args, **kwargs):
        context=getContext(request=request)
        
        return render(request,TEMPLATE_ROOT+"index.html",context)

class ProcessView(View):
    def get(self,request,*args, **kwargs):
        context=getContext(request=request)
        
        context=getContext(request=request)
        process=ProcessRepo(request=request).process(*args, **kwargs)
        context['process']=process
        return render(request,TEMPLATE_ROOT+"process.html",context)

class ProcessesView(View):
    def get(self,request,*args, **kwargs):
        context=getContext(request=request)
        processes=ProcessRepo(request=request).list().order_by('process_app_name').order_by('-priority')
        context['processes']=processes
        
        return render(request,TEMPLATE_ROOT+"processes.html",context)

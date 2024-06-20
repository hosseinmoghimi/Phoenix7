from django.shortcuts import render,reverse
from django.views import View
from .apps import APP_NAME
from .repo import CustomerRepo
from .forms import *
from phoenix.settings import ADMIN_URL
from django.http import Http404
from core.views import CoreContext


TEMPLATE_ROOT = "market/"
BASE_LAYOUT='phoenix/layout.html'
WIDE_BASE_LAYOUT='phoenix/wide-layout.html'

def getContext(request,*args, **kwargs):
    context=CoreContext(app_name=APP_NAME,request=request)
    context['app_name']=APP_NAME
    context['search_form']=SearchForm()
    context['search_action']=reverse(APP_NAME+":search")
    return context

class HomeView(View):
    def get(self, request, *args, **kwargs):
        context=getContext(request=request)
        return render(request,TEMPLATE_ROOT+"index.html",context) 


class SearchView(View):
    def get(self, request, *args, **kwargs):
        context = getContext(request=request)

        return render(request, TEMPLATE_ROOT+"search.html", context)

    def post(self, request, *args, **kwargs):
        context = getContext(request=request)
        search_form = SearchForm(request.POST)
        if search_form.is_valid():
            cd = search_form.cleaned_data
            search_for = cd['search_for']
            context.update(SearchContext(request=request,search_for=search_for))

        return render(request, TEMPLATE_ROOT+"search.html", context)

class CustomersView(View):
    def get(self, request, *args, **kwargs):
        context=getContext(request=request)
        return render(request,TEMPLATE_ROOT+"customers.html",context) 


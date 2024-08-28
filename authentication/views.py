from django.shortcuts import render
from django.views import View
from .apps import APP_NAME
from core.views import CoreContext

from django.contrib.auth import login, logout, authenticate


from django.http import Http404
TEMPLATE_ROOT = "authentication/"
BASE_LAYOUT='phoenix/layout.html'
WIDE_BASE_LAYOUT='phoenix/wide-layout.html'
 

def getContext(request,*args, **kwargs):
    context=CoreContext(app_name=APP_NAME,request=request)
    return context

class HomeView(View):
    def get(self, request, *args, **kwargs):
        context=getContext(request=request)
        return render(request,TEMPLATE_ROOT+"index.html",context) 

 
class LogoutView(View):
    def get(self, request, *args, **kwargs):
        context=getContext(request=request)
        logout(request=request)
        return render(request,TEMPLATE_ROOT+"index.html",context) 

 
class LoginView(View):
    def get(self, request, *args, **kwargs):
        context=getContext(request=request)
        return render(request,TEMPLATE_ROOT+"index.html",context) 

 
    def post(self, request, *args, **kwargs):
        context=getContext(request=request)
        return render(request,TEMPLATE_ROOT+"index.html",context) 

 
class ProfileView(View):
    def get(self, request, *args, **kwargs):
        context=getContext(request=request)
        return render(request,TEMPLATE_ROOT+"profile.html",context) 

class ChangePasswordView(View):
    def get(self, request, *args, **kwargs):
        context=getContext(request=request)
        return render(request,TEMPLATE_ROOT+"change-password.html",context) 

from django.shortcuts import render,reverse
from django.views import View
from .apps import APP_NAME
from .repo import PageRepo
from .forms import *

from django.http import Http404
TEMPLATE_ROOT = "core/"
BASE_LAYOUT='phoenix/layout.html'
WIDE_BASE_LAYOUT='phoenix/wide-layout.html'


def SearchContext(request,search_for, *args, **kwargs):
    context = {}
    context['search_for'] = search_for
    
    ########################################################
    # tags
    if False:
        tags = TagRepo(request=request).list(
            search_for=search_for)
        if len(tags)>0:
            context['tags'] = tags
            tags_s = json.dumps(
                TagSerializer(tags, many=True).data)
            context['tags_s'] = tags_s


    ########################################################
    # pages
    if False:
        pages = PageRepo(request=request).list(search_for=search_for)
        if len(pages)>0:
            context['pages'] = pages
            pages_s = json.dumps(
                PageSerializer(pages, many=True).data)
            context['pages_s'] = pages_s
    ########################################################
    # links
    if False:
        links = PageLinkRepo(request=request).list(
            search_for=search_for).order_by('priority')
        if len(links)>0:
            context['links'] = links
            links_s = json.dumps(
                PageLinkSerializer(links, many=True).data)
            context['links_s'] = links_s

    ########################################################
    # downloads
    if False:
        downloads = PageDownloadRepo(request=request).list(search_for=search_for).order_by('priority')
        if len(downloads)>0:
            context['downloads'] = downloads
            downloads_s = json.dumps(PageDownloadSerializer(downloads, many=True).data)
            context['page_downloads_s'] = downloads_s
        
    return context

def CoreContext(request, *args, **kwargs):
    context = {}
    context['BASE_LAYOUT'] = BASE_LAYOUT
    context['WIDE_BASE_LAYOUT'] = WIDE_BASE_LAYOUT
    if 'app_name' in kwargs:
        context['app_name']=kwargs['app_name']

    return context

def PageContext(request, *args, **kwargs):
    page=None
    no_detail=True
    
    if 'no_detail' in kwargs:
        no_detail = kwargs['no_detail']
    if 'page' in kwargs:
        page = kwargs['page']
    if 'page_id' in kwargs:
        page = PageRepo(request=request).page(pk=kwargs['page_id'])
    if page is None:
        if not 'no404' in kwargs and not kwargs['no404'] :
            raise Http404
    context = {}
    context['page'] = page
    

    return context

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


class PageView(View):
    def get(self, request, *args, **kwargs):
        context = getContext(request=request)
        page=PageRepo(request=request).page(*args, **kwargs)
        if page is None:
            raise Http404
        context.update(PageContext(page=page,request=request))
        return render(request, TEMPLATE_ROOT+"page.html", context)
 

class PagesView(View):
    def get(self, request, *args, **kwargs):
        context = getContext(request=request)

        return render(request, TEMPLATE_ROOT+"page.html", context)
 

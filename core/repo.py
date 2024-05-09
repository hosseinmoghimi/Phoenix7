from .models import Page

class PageRepo():
    def __init__(self,request,*args, **kwargs):
        self.request=request
        self.objects=Page.objects
    
    def page(self,*args, **kwargs):
        page=None
        if 'page' in kwargs:
            page=self.objects.filter(pk=kwargs['page'].id).first()
        if 'page_id' in kwargs:
            page=self.objects.filter(pk=kwargs['page_id']).first()
        if 'pk' in kwargs:
            page=self.objects.filter(pk=kwargs['pk']).first()
        return page

    def list(self,*args, **kwargs):
        objects=self.objects
        if 'page_id' in kwargs:
            objects=self.objects.filter(pk=kwargs['page_id'])
        return objects

from .models import Account
from authentication.repo import ProfileRepo
class AccountRepo():
    def __init__(self,request,*args, **kwargs):
        self.request=request
        self.me=None
        profile=ProfileRepo(request=request).me
        self.objects=Account.objects
        if profile is not None:
            self.me=self.objects.filter(profile=profile).first()
    def list(self,*args, **kwargs):
        objects=self.objects
        if "search_for" in kwargs:
            objects=objects.filter(title__contains=kwargs['search_for']) 
        return objects.all()
    def account(self,*args, **kwargs):
        if "pk" in kwargs:
            return self.objects.filter(pk=kwargs['pk']).first() 
        if "id" in kwargs:
            return self.objects.filter(pk=kwargs['id']).first() 
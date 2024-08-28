from .models import Profile

class ProfileRepo:
    def __init__(self,request):
        self.request=request
        self.objects=Profile.objects 
        self.me=self.objects.filter(user=request.user).first()

    def get(self,*args, **kwargs):
        if 'user' in kwargs:
            return Profile.objects.filter(user=kwargs['user']).first()
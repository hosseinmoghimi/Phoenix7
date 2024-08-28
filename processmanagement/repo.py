from .models import Process

class ProcessRepo():
    def __init__(self,request,*args, **kwargs):
        self.request=request

        self.objects=Process.objects

    def list(self,*args, **kwargs):
        objects =self.objects
        return objects.all()
    def process(self,*args, **kwargs):
        objects =self.objects
        if 'pk' in kwargs:
            return objects.filter(pk=kwargs['pk']).first()
        if 'id' in kwargs:
            return objects.filter(pk=kwargs['id']).first()
        if 'process_id' in kwargs:
            return objects.filter(pk=kwargs['process_id']).first()
 
from django.contrib import admin
from .models import PersonCategory,Account,Material,Service,Person,TafsiliAccount,Event,EventPrint,EventCategory,AccountGroup,BasicAccount,MoeinAccount,AccountingDocumentLine,AccountingDocument

admin.site.register(Account)
admin.site.register(AccountGroup)
admin.site.register(AccountingDocument) 
admin.site.register(AccountingDocumentLine) 
admin.site.register(BasicAccount)
admin.site.register(Event)
admin.site.register(EventCategory)
admin.site.register(EventPrint)
admin.site.register(MoeinAccount) 
admin.site.register(Material)
admin.site.register(Person)
admin.site.register(PersonCategory)
admin.site.register(Service)
admin.site.register(TafsiliAccount)
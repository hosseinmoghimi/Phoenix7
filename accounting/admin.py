from django.contrib import admin
from .models import TafsiliAccount,Event,EventPrint,EventCategory,AccountGroup,BasicAccount,MoeinAccount,AccountingDocumentLine,AccountingDocument

admin.site.register(AccountGroup)
admin.site.register(TafsiliAccount)
admin.site.register(Event)
admin.site.register(EventPrint)
admin.site.register(EventCategory)
admin.site.register(BasicAccount)
admin.site.register(MoeinAccount) 
admin.site.register(AccountingDocumentLine) 
admin.site.register(AccountingDocument) 
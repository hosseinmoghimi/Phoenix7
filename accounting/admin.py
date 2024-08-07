from django.contrib import admin
from .models import Account,Event,EventPrint,EventCategory,AccountGroup,BasicAccount,MoeinAccount

admin.site.register(AccountGroup)
admin.site.register(Account)
admin.site.register(Event)
admin.site.register(EventPrint)
admin.site.register(EventCategory)
admin.site.register(BasicAccount)
admin.site.register(MoeinAccount) 
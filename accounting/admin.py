from django.contrib import admin
from .models import Account,Transaction,TransactionPrint,TransactionCategory

admin.site.register(Account)
admin.site.register(Transaction)
admin.site.register(TransactionPrint)
admin.site.register(TransactionCategory)
from django.db import models
from core.models import LinkHelper
from .apps import APP_NAME



# Create your models here.
class Account(models.Model):
    
    class_name="account"
    app_name=APP_NAME
    

    class Meta:
        verbose_name = _("Account")
        verbose_name_plural = _("Accounts")

    def __str__(self):
        return self.name
 

 
class Transaction(models.Model):
    class_name="transaction"
    app_name=APP_NAME
    

    class Meta:
        verbose_name = _("Transaction")
        verbose_name_plural = _("Transactions")

    def __str__(self):
        return self.name
 

from .models import Person,TafsiliAccount,AccountingDocumentLine,AccountingDocument,Event,AccountGroup,BasicAccount,MoeinAccount,Account
from rest_framework import serializers



class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id', 'get_absolute_url','full_name','code','balance']


class EventBriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'title','get_absolute_url','get_edit_url','get_delete_url','amount','persian_event_datetime']


class TafsiliAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = TafsiliAccount
        fields = ['id','type','pure_code', 'title','get_absolute_url','get_edit_url','get_delete_url','balance','logo']

class AccountingDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountingDocument
        fields = ['id','title', 'get_absolute_url','get_edit_url','get_delete_url']

 
class MoeinAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoeinAccount
        fields = ['id', 'name','pure_code','type','color','code','basic_account_id','moein_account_id','get_absolute_url','get_edit_url','get_delete_url','balance']
 
class AccountGroupBriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountGroup
        fields = ['id', 'name','pure_code','type','color','code','get_absolute_url','get_edit_url','get_delete_url','balance']



class BasicAccountSerializer(serializers.ModelSerializer):
    moein_accounts=MoeinAccountSerializer(many=True)
    account_group=AccountGroupBriefSerializer()
    class Meta:
        model = BasicAccount
        fields = ['id', 'name','type','color','pure_code','account_group','code','moein_accounts','get_absolute_url','get_edit_url','get_delete_url','balance']

class AccountGroupSerializer(serializers.ModelSerializer):
    basic_accounts=BasicAccountSerializer(many=True)
    class Meta:
        model = AccountGroup
        fields = ['id', 'name','type','pure_code','color','code','basic_accounts','get_absolute_url','get_edit_url','get_delete_url','balance']


 


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'name','pure_code',"full_title",'logo','type','balance_colored','color','code','get_absolute_url','get_edit_url','get_delete_url','balance']



class AccountGroupBriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountGroup
        fields = ['id', 'name','pure_code','color','code','get_absolute_url','get_edit_url','get_delete_url','balance']

class BasicAccountBriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasicAccount
        fields = ['id','balance_colored','pure_code', 'name','color','account_group_id','logo','code','get_absolute_url','get_edit_url','get_delete_url','balance']

class MoeinAccountBriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoeinAccount
        fields = ['id', 'name','color','pure_code','logo','code','basic_account_id','moein_account_id','get_absolute_url','get_edit_url','get_delete_url','balance']


class TafsiliAccountBriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = TafsiliAccount
        fields = ['id', 'name','color','pure_code','code','moein_account_id','get_absolute_url','get_edit_url','get_delete_url','balance']

class AccountingDocumentBriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountingDocument
        fields = ['id', 'title','get_absolute_url']

class AccountingDocumentLineSerializer(serializers.ModelSerializer):
    event=EventBriefSerializer()
    accounting_document=AccountingDocumentBriefSerializer()    
    account=AccountSerializer()
    class Meta:
        model = AccountingDocumentLine
        fields = ['id', 'title','persian_date_time','accounting_document','amount','event','account','bedehkar','bestankar','get_absolute_url','get_edit_url','get_delete_url']

class EventSerializer(serializers.ModelSerializer): 
    pay_to=AccountSerializer()
    pay_from=AccountSerializer()
    class Meta:
        model = Event
        fields = ['id','pay_to','pay_from', 'title','get_absolute_url','get_edit_url','get_delete_url','amount','persian_event_datetime']

        
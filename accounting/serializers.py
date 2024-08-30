from .models import TafsiliAccount,AccountingDocumentLine,AccountingDocument,Event,AccountGroup,BasicAccount,MoeinAccount,Account
from rest_framework import serializers



class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'title','get_absolute_url','get_edit_url','get_delete_url','amount','persian_event_datetime']

class TafsiliAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = TafsiliAccount
        fields = ['id', 'title','get_absolute_url','get_edit_url','get_delete_url','balance','logo']

class AccountingDocumentLineSerializer(serializers.ModelSerializer):
    event=EventSerializer()
    account=TafsiliAccountSerializer()
    class Meta:
        model = AccountingDocumentLine
        fields = ['id', 'title','get_absolute_url','get_edit_url','get_delete_url','balance','logo']

class AccountingDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountingDocument
        fields = ['id', 'name','code','get_absolute_url','get_edit_url','get_delete_url','balance','logo']

 
class MoeinAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoeinAccount
        fields = ['id', 'name','color','code','basic_account_id','get_absolute_url','get_edit_url','get_delete_url','balance']

class BasicAccountSerializer(serializers.ModelSerializer):
    moein_accounts=MoeinAccountSerializer(many=True)
    class Meta:
        model = BasicAccount
        fields = ['id', 'name','color','code','moein_accounts','get_absolute_url','get_edit_url','get_delete_url','balance']

 
class AccountGroupSerializer(serializers.ModelSerializer):
    basic_accounts=BasicAccountSerializer(many=True)
    class Meta:
        model = AccountGroup
        fields = ['id', 'name','color','code','basic_accounts','get_absolute_url','get_edit_url','get_delete_url','balance']



class BasicAccountSerializer(serializers.ModelSerializer):
    moein_accounts=MoeinAccountSerializer(many=True)
    account_group=AccountGroupSerializer()
    class Meta:
        model = BasicAccount
        fields = ['id', 'name','color','account_group','code','moein_accounts','get_absolute_url','get_edit_url','get_delete_url','balance']

class AccountGroupSerializer(serializers.ModelSerializer):
    basic_accounts=BasicAccountSerializer(many=True)
    class Meta:
        model = AccountGroup
        fields = ['id', 'name','color','code','basic_accounts','get_absolute_url','get_edit_url','get_delete_url','balance']





class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'name','type','balance_colored','color','code','get_absolute_url','get_edit_url','get_delete_url','balance']



class AccountGroupBriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountGroup
        fields = ['id', 'name','color','code','get_absolute_url','get_edit_url','get_delete_url','balance']

class BasicAccountBriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasicAccount
        fields = ['id','balance_colored', 'name','color','account_group_id','logo','code','get_absolute_url','get_edit_url','get_delete_url','balance']

class MoeinAccountBriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoeinAccount
        fields = ['id', 'name','color','logo','code','basic_account_id','get_absolute_url','get_edit_url','get_delete_url','balance']


class TafsiliAccountBriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = TafsiliAccount
        fields = ['id', 'name','color','code','moein_account_id','get_absolute_url','get_edit_url','get_delete_url','balance']

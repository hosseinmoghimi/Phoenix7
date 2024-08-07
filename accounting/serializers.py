from .models import Account,AccountingDocumentLine,AccountingDocument,Event,AccountGroup,BasicAccount,MoeinAccount
from rest_framework import serializers



class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'title','get_absolute_url','get_edit_url','get_delete_url','amount','persian_event_datetime']

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'title','get_absolute_url','get_edit_url','get_delete_url','balance','logo']

class AccountingDocumentLineSerializer(serializers.ModelSerializer):
    event=EventSerializer()
    account=AccountSerializer()
    class Meta:
        model = AccountingDocumentLine
        fields = ['id', 'title','get_absolute_url','get_edit_url','get_delete_url','balance','logo']

class AccountingDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountingDocument
        fields = ['id', 'title','get_absolute_url','get_edit_url','get_delete_url','balance','logo']

 
class MoeinAccountSerializer(serializers.ModelSerializer):
    accounts= AccountSerializer(many=True)
    class Meta:
        model = MoeinAccount
        fields = ['id', 'title','accounts','get_absolute_url','get_edit_url','get_delete_url','balance']


class BasicAccountSerializer(serializers.ModelSerializer):
    moein_accounts=MoeinAccountSerializer(many=True)
    class Meta:
        model = BasicAccount
        fields = ['id', 'title','moein_accounts','get_absolute_url','get_edit_url','get_delete_url','balance']
class AccountGroupSerializer(serializers.ModelSerializer):
    basic_accounts=BasicAccountSerializer(many=True)
    class Meta:
        model = AccountGroup
        fields = ['id', 'title','basic_accounts','get_absolute_url','get_edit_url','get_delete_url','balance']

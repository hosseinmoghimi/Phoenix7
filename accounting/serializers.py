from .models import TafsiliAccount,AccountingDocumentLine,AccountingDocument,Event,AccountGroup,BasicAccount,MoeinAccount
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
        fields = ['id', 'title','get_absolute_url','get_edit_url','get_delete_url','balance','logo']

 
class MoeinAccountSerializer(serializers.ModelSerializer):
    accounts= TafsiliAccountSerializer(many=True)
    class Meta:
        model = MoeinAccount
        fields = ['id', 'title','accounts','get_absolute_url','get_edit_url','get_delete_url','balance']


class BasicAccountSerializer(serializers.ModelSerializer):
    moein_accounts=MoeinAccountSerializer(many=True)
    class Meta:
        model = BasicAccount
        fields = ['id', 'name','moein_accounts','get_absolute_url','get_edit_url','get_delete_url','balance']
class AccountGroupSerializer(serializers.ModelSerializer):
    basic_accounts=BasicAccountSerializer(many=True)
    class Meta:
        model = AccountGroup
        fields = ['id', 'name','basic_accounts','get_absolute_url','get_edit_url','get_delete_url','balance']

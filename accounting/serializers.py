from .models import Account
from rest_framework import serializers



class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'title','get_absolute_url','get_edit_url','get_delete_url','balance','logo']

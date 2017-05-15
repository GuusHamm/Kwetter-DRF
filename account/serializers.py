from rest_framework import serializers

from account.models import Account
from kweet.serializers import KweetSerializer


class AccountSerializer(serializers.ModelSerializer):
    kweets = KweetSerializer(many=True, read_only=True)

    class Meta:
        model = Account
        fields = ('username', 'password', 'firstname', 'lastname', 'kweets', 'id')
        extra_kwargs = {'password': {'write_only': True}}
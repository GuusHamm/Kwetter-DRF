from rest_framework import serializers

from kwetter.models import Kweet, Account


class KweetSerializer(serializers.HyperlinkedModelSerializer):
    username = serializers.ReadOnlyField(source='account.username')

    class Meta:
        model = Kweet
        fields = ('message', 'account', 'username', 'timestamp', 'id')


class AccountSerializer(serializers.ModelSerializer):
    kweets = KweetSerializer(many=True, read_only=True)

    class Meta:
        model = Account
        fields = ('username', 'password', 'firstname', 'lastname', 'kweets', 'id')
        extra_kwargs = {'password': {'write_only': True}}


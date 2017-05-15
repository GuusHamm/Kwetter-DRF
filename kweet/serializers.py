from rest_framework import serializers

from kweet.models import Kweet


class KweetSerializer(serializers.HyperlinkedModelSerializer):
    username = serializers.ReadOnlyField(source='account.username')

    class Meta:
        model = Kweet
        fields = ('message', 'account', 'username', 'timestamp', 'id')

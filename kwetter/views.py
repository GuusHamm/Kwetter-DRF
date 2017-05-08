from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from kwetter.models import Account, Kweet
from kwetter.serializers import AccountSerializer, KweetSerializer


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    ordering_fields = ('account', 'timestamp')
    search_fields = ('username',)


class KweetViewSet(viewsets.ModelViewSet):
    queryset = Kweet.objects.order_by('-timestamp')
    serializer_class = KweetSerializer
    filter_fields = ('account',)
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    ordering_fields = ('account', 'timestamp')
    search_fields = ('message', 'account__username')

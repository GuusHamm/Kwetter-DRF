from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets

from kweet.models import Kweet
from kweet.serializers import KweetSerializer


class KweetViewSet(viewsets.ModelViewSet):
    queryset = Kweet.objects.order_by('-timestamp')
    serializer_class = KweetSerializer
    filter_fields = ('account',)
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    ordering_fields = ('account', 'timestamp')
    search_fields = ('message', 'account__username')

from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination
from rest_framework import mixins
from rest_framework import generics
from .serializers import MerchandiseSerializer
from .models import Merchandise
from rest_framework import viewsets
from rest_framework import filters
from .filter import MerchandisesFilter
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.

class MerchandisesPagination(PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    page_query_param = 'page'
    max_page_size = 100


class MerchandisesViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Merchandise.objects.all().order_by('id')
    serializer_class = MerchandiseSerializer
    pagination_class = MerchandisesPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filterset_class = MerchandisesFilter
    ordering_fields = ['price']
    search_fields = ['$name']




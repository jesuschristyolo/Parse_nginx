from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import Log
from .serializers import LogSerializer
from rest_framework.pagination import PageNumberPagination


class NginxLogPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class NginxLogViewSet(viewsets.ModelViewSet):
    queryset = Log.objects.all()
    serializer_class = LogSerializer
    pagination_class = NginxLogPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['ip_address', 'uri', 'http_method']
    ordering_fields = ['timestamp', 'status_code']

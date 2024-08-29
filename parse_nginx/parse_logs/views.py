from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import Log
from .serializers import LogSerializer
from rest_framework.pagination import PageNumberPagination


class NginxLogPagination(PageNumberPagination):
    """
    Пагинация для представления NginxLogViewSet.

    Атрибуты:
        page_size - Количество записей на странице по умолчанию.
        page_size_query_param - Параметр, который можно использовать для указания размера страницы.
        max_page_size - Максимальное количество записей на странице.
    """
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class NginxLogViewSet(viewsets.ModelViewSet):
    """
        ViewSet для модели Log, реализующий CRUD операции через API.

        Атрибуты:
            queryset - Набор данных для обработки.
            serializer_class - Сериализатор, используемый для преобразования данных.
            pagination_class - Класс пагинации.
            search_fields - Поля, по которым можно выполнять поиск.
            ordering_fields - Поля, по которым можно сортировать результаты.
        """

    queryset = Log.objects.all()
    serializer_class = LogSerializer
    pagination_class = NginxLogPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['ip_address', 'uri', 'http_method']
    ordering_fields = ['timestamp', 'status_code']

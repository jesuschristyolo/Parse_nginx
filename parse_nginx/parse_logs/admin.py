from django.contrib import admin
from .models import Log


@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    """
   Конфигурация модели Log для отображения в Django Admin.

   Определяет поля, отображаемые в списке записей, и возможности фильтрации и поиска.

   Атрибуты:
       list_display - Поля, отображаемые в списке записей.
       search_fields - Поля, по которым можно искать.
       list_filter - Поля, по которым можно фильтровать.
   """

    list_display = ('ip_address', 'timestamp', 'http_method', 'uri', 'status_code', 'response_size')
    search_fields = ('ip_address', 'uri', 'http_method')
    list_filter = ('status_code', 'http_method')

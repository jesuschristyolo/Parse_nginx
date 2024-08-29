from django.contrib import admin
from .models import Log


@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display = ('ip_address', 'timestamp', 'http_method', 'uri', 'status_code', 'response_size')
    search_fields = ('ip_address', 'uri', 'http_method')
    list_filter = ('status_code', 'http_method')

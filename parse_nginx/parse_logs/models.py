from django.db import models


class Log(models.Model):
    ip_address = models.GenericIPAddressField()
    timestamp = models.DateTimeField(null=True)
    http_method = models.CharField(max_length=10)
    uri = models.CharField(max_length=255)
    protocol = models.CharField(max_length=10)
    status_code = models.IntegerField()
    response_size = models.IntegerField()
    referrer = models.CharField()
    agent = models.CharField(max_length=255, null=True, blank=True)

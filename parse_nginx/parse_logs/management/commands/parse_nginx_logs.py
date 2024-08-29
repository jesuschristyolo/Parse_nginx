import json
from django.core.management.base import BaseCommand
import re
from datetime import datetime
from parse_logs.models import Log
import requests


class Command(BaseCommand):
    """
    Management command для импорта логов Nginx.

    Эта команда загружает лог-файл с Google Drive по предоставленному URL, парсит каждую строку
    как JSON и сохраняет соответствующие данные в базу данных.

    Атрибуты:
        help (str): Описание команды, отображаемое при вызове `--help`.
    """
    help = 'import nginx logs'

    def add_arguments(self, parser):
        """
        Определяет аргументы для команды.
        """
        parser.add_argument('url', help='logs url', type=str)

    def handle(self, *args, **kwargs):
        """
        Основная логика команды.
        Выполняет загрузку файла по URL, парсит его и сохраняет данные в базу.
        """

        share_url = kwargs['url']
        match = re.search(r'/d/([a-zA-Z0-9_-]+)', share_url)
        if match:
            file_id = match.group(1)
        else:
            raise ValueError("Неверный формат ссылки Google Drive")

        download_url = f"https://drive.google.com/uc?id={file_id}&export=download"

        response = requests.get(download_url, stream=True)

        file_content = response.content.decode('utf-8')

        for line in file_content.splitlines():
            log_entry = json.loads(line)
            timestamp = datetime.strptime(log_entry['time'], '%d/%b/%Y:%H:%M:%S %z')
            method, uri, protocol = log_entry['request'].split()

            Log.objects.create(
                ip_address=log_entry['remote_ip'],
                timestamp=timestamp,
                http_method=method,
                uri=uri,
                protocol=protocol,
                status_code=log_entry['response'],
                response_size=log_entry['bytes'],
                referrer=log_entry.get('referrer', None),
                agent=log_entry.get('agent', None)
            )

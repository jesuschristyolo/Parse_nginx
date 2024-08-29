from django.test import TestCase
from parse_logs.models import Log
from datetime import datetime


class LogModelTest(TestCase):
    def setUp(self):
        self.log = Log.objects.create(
            ip_address='192.168.1.1',
            timestamp=datetime.now(),
            http_method='GET',
            uri='/test',
            protocol='HTTP/1.1',
            status_code=200,
            response_size=1234,
            referrer='https://example.com',
            agent='Mozilla/5.0'
        )

    def test_log_creation(self):
        self.assertIsInstance(self.log, Log)
        self.assertEqual(self.log.ip_address, '192.168.1.1')
        self.assertEqual(self.log.http_method, 'GET')
        self.assertEqual(self.log.uri, '/test')
        self.assertEqual(self.log.status_code, 200)

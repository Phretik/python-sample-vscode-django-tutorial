from django.test import TestCase
from django.utils import timezone
from hello.models import LogMessage
import datetime

class LogMessageTests(TestCase):

    def create_logmessage(self):
        """"
        Create a log message instance
        """""
        return LogMessage.objects.create(
            message="This is a test message.",
            Log_date=timezone.now()
        )

    def test_logmessage_creation(self):
        """"
        Test the creation of the log message instance.
        """""
        log_message = self.create_logmessage()
        self.assertTrue(isinstance(log_message, log_message))
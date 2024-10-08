from django.conf import settings
from django.test import TestCase

# Create your tests here.
class DBTestCase(TestCase):

    def test_db_url(self):
        DATABASE_URL = settings.DATABASE_URL
        self.assertIn("", DATABASE_URL)
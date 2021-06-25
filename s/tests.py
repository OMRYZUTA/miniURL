from django.test import TestCase
from .models import UsedUrlData
from .views import urlShort, urlRedirect

LONG_URL1 = "http://www.google.com/"
SHORT_URL1 = "234djk"


class UsedUrlData(TestCase):
    def setUp(self):
        UsedUrlData.objects.create(
            url=LONG_URL1, short_url=SHORT_URL1)

    def test_url_redirect(self):
        data = UsedUrlData.get(short_url=SHORT_URL1)
        self.assertEqual(data.url, LONG_URL1)

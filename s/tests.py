from django.test import TestCase
from .models import UsedUrlData
from .views import urlShort, urlRedirect
from django.http.response import Http404

LONG_URL1 = "http://www.google.com/"
SHORT_URL1 = "234djk"

LONG_URL2 = "http://www.youtube.com/"
SHORT_URL_LENGTH = 6
RELATIVE_URL = 'http://localhost:8000/s/'

class TestUsedUrlData(TestCase):
    def setUp(self):
        pass

    def test_create_url_data(self):
        new_url_object = UsedUrlData(url=LONG_URL2)
        new_url_object.get_short_url()
        new_url_object.save()
        result = urlRedirect(None, new_url_object.short_url)
        self.assertEqual(result.url, LONG_URL2)

    def test_non_exist_short_url(self):
        new_url_object = UsedUrlData(url=LONG_URL2)
        non_exist_short = new_url_object.generate_short_url()
        self.assertTrue(len(UsedUrlData.objects.filter(
            short_url=non_exist_short)) == 0)

    def test_404_on_non_exist_short_url(self):
        new_url_object = UsedUrlData(url=LONG_URL2)
        non_exist_short = new_url_object.generate_short_url()
        result = urlRedirect(None, non_exist_short)
        self.assertTrue(isinstance(result, Http404))

    def test_short_url_is_short(self):
        new_url_object = UsedUrlData(url=LONG_URL2)
        new_url = new_url_object.get_short_url()
        self.assertEqual(len(new_url),SHORT_URL_LENGTH+ len(RELATIVE_URL))

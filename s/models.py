from django.db import models
import random
import string


SHORT_URL_LENGTH = 6
# 64 possibilities for each character, 64^SHORT_URL_LENGTH
SHORT_URL_CHARACTERS = ''.join(
    string.ascii_letters + string.digits+'+/')
RELATIVE_URL = 'http://localhost:8000/s/'


class UsedUrlData(models.Model):
    url = models.CharField(max_length=255)
    # for 67 bilion possibilities
    short_url = models.CharField(max_length=SHORT_URL_LENGTH, unique=True)

    def get_short_url(self):
        short_url = self.generate_short_url()
        self.set_short_url(short_url)
        return RELATIVE_URL + short_url

    def set_short_url(self, short_url):
        self.short_url = short_url

    def generate_short_url(self):
        short_url = ''.join(random.choice(SHORT_URL_CHARACTERS)
                            for x in range(SHORT_URL_LENGTH))

    # @$ avoid getting 2 identical short urls
        if len(UsedUrlData.objects.filter(short_url=short_url)) == 0:
            return short_url
        else:
            return self.generate_short_url()


def __str__(self):
    return f"Short Url for: {self.url} is {self.short_url}"

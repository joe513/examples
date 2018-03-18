from django.test import SimpleTestCase
from django.shortcuts import reverse


class URLTestCase(SimpleTestCase):

    def test_GET_urls(self):

        urls = [
            # Names
            'first_url',
            'second_one',
            'etc'
        ]

        for url in urls:
            self.assertEqual(200, self.client.get(reverse(url), follow=True).status_code,
                             msg="Unable to open %s, status_code %s" % (reverse(url),
                                                                        self.client.get(reverse(url)).status_code))

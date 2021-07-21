from django.urls import reverse
from rest_framework.test import APITestCase
import re


class APITests(APITestCase):
    def test_get_sentence(self):
        madlib_re = re.compile("It was a \w+ day. I went downstairs to see if I could \w+ dinner. I asked, " 
                               "'Does the stew need fresh \w+\\?'")
        url = reverse('madlib')
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        self.assertIsNotNone(re.search(madlib_re, response.data))

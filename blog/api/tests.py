from django.test import TestCase

import requests
from requests.auth import HTTPBasicAuth

class APITestCase(TestCase):
    base_url= "https://aladdin-heavy-8000.codio.io/api/v1/"


class PostAPIAuthTestCase(APITestCase):
    # Correct URL for current box
    base_url = "https://aladdin-heavy-8000.codio.io/api/v1/"

    def 

    def test_incorrect_auth_info(self):
        """ Input incorrect authentication information, recieve a 403 error response """
        resp = requests.get(self.base_url, auth=HTTPBasicAuth("user@example.com", "badpassword"))
        self.assertEqual(str(resp), '<Response [403]>')
        self.assertEqual(str(resp), '<Response [403]>')
    def test_correct_auth_info(self):
        """ Input correct authentication information, recieve a 200 response """
        resp = requests.get(self.base_url, auth=HTTPBasicAuth("user200@gmail.com", "G00dpassword"))
        self.assertEqual(str(resp), '<Response [200]>') 

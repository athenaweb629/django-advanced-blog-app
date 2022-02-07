from django.test import TestCase

class APITestCase(TestCase):
    base_url= ""
    class APIAuthTestCase(APITestCase):

        def test_incorrect_auth_info(self):
            resp = requests.get(self.base_url, auth=HTTPBasicAuth("user@example.com", "badpassword"))
            self.assertEqual(str(resp), '<Response [403]>')

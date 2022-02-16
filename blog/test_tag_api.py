from django.test import LiveServerTestCase
from requests.auth import HTTPBasicAuth
from rest_framework.test import RequestsClient

from django.contrib.auth import get_user_model
from blog.models import Tag


class TagApiTestCase(LiveServerTestCase):
    def setUp(self):
        get_user_model().objects.create_user(
            email="testuser@example.com", password="password"
        )

        self.tag_values = {"tag1", "tag2", "tag3", "tag4"}
        for t in self.tag_values:
            Tag.objects.create(value=t)
        self.client = RequestsClient()

    def test_tag_list(self):
        resp = self.client.get(self.live_server_url + "/api/v1/tags/")
        self.assertEqual(resp.status_code, 200)
        data = resp.json()["results"]
        self.assertEqual(len(data), 4)
        self.assertEqual(self.tag_values, {t["value"] for t in data})

    def test_tag_create_basic_auth(self):
        self.client.auth = HTTPBasicAuth("testuser@example.com", "password")
        resp = self.client.post(
            self.live_server_url + "/api/v1/tags/", {"value": "tag5"}
        )
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(Tag.objects.all().count(), 5)

    def test_tag_create_token_auth(self):
        token_resp = self.client.post(
            self.live_server_url + "/api/v1/token-auth/",
            {"username": "testuser@example.com", "password": "password"},
        )
        self.client.headers["Authorization"] = "Token " + token_resp.json()["token"]

        resp = self.client.post(
            self.live_server_url + "/api/v1/tags/", {"value": "tag5"}
        )
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(Tag.objects.all().count(), 5)
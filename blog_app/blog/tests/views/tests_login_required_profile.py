from django.test import TestCase
from django.test.client import Client
from django.urls import reverse

client = Client()


class ProfileViewTests(TestCase):
    def test_sholud_return_302_when_profile_is_call(self):
        resp = client.get(reverse("profile"))
        assert resp.status_code == 302

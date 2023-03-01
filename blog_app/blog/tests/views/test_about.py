from django.test import TestCase
from django.test.client import Client
from django.urls import reverse

client = Client()


class AboutViewTests(TestCase):
    def test_sholud_return_200_when_about_is_call(self):
        resp = client.get(reverse('blog-about'))
        assert resp.status_code == 200

from django.test import TestCase
from django.urls import reverse


class CarsURLsTest(TestCase):
    def test_home_url_is_correct(self):
        url = reverse('cars:home')
        self.assertEqual(url, '/')
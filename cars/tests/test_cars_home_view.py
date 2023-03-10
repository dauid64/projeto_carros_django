from django.test import TestCase
from django.urls import resolve, reverse

from cars import views


class HomeViewsTest(TestCase):
    def test_home_view_function_is_correct(self):
        view = resolve(reverse('cars:home'))
        self.assertIs(view.func.view_class, views.HomeView)
from django.test import TestCase
from django.urls import resolve, reverse

from ..models import Board
from ..views import home


class HomeTests(TestCase):
    def setUp(self):
        self.board = Board.objects.create(
            name='Django', description='Django board.')
        url = reverse('home')
        self.response = self.client.get(url)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func, home)

from django.test import TestCase
from django.urls import resolve, reverse

from ..models import Board


class HomeTests(TestCase):
    def setUp(self):
        self.board = Board.objects.create(
            name='Django', description='Forfer.')
        url = reverse('home')
        self.response = self.client.get(url)

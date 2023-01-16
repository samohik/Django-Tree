from django.test import TestCase
from django.urls import reverse

from menu.models import *


class MenuTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        menu = Menu.objects.create(
            title='Main',
            named_url='home'
        )
        menu_item = MenuItem.objects.create(
            menu=menu,
            title='Test',
            named_url='test',
        )
        MenuItem.objects.create(
            parent=menu_item,
            title='Child1',
            named_url='c1',
        )
        MenuItem.objects.create(
            parent=menu_item,
            title='Child2',
            named_url='c2',
        )

    def test_home_page(self):
        url = reverse('home')
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'menu/home.html')

    def test_menu_count(self):
        url = reverse('home')
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.context['menu']) == 1)
        self.assertFalse(len(response.context['menu']) == 2)

    def test_menu_items_count(self):
        url = reverse('detail', kwargs={'named_url': 'test'})
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.context['menu']) == 1)
        self.assertFalse(len(response.context['menu']) == 2)

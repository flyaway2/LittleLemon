from django.test import TestCase
from django.test import Client
from django.urls import reverse
from restaurant.views import MenuItemView
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
import json
class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(Title="omlette",Price=100,Inventory=1)
    def test_getall(self):
        url = 'http://127.0.0.1:8000/restaurant/menu/'
        client=Client()
        response=client.get(path=url,content_type="application/json")
        menu=Menu.objects.all()
        serialized=MenuSerializer(menu,many=True)
        self.assertEqual(serialized.data,response.data)
from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
import json
class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(Title="omlette",Price=100,Inventory=1)
    def test_getall(self):
        menu=Menu.objects.all()
        serialized=MenuSerializer(menu,many=True)
        self.assertEqual(json.dumps(serialized.data),'[{"id": 2, "Title": "omlette", "Price": "100.00", "Inventory": 1}]')
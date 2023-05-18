from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(Title="Fried Chicken",Price=200,Inventory=10)
        Menu.objects.create(Title="omlette",Price=100,Inventory=1)
    def test_getall(self):
        menu=Menu.objects.all
        serialized=MenuSerializer(menu)
        self.assertEqual(serialized,{})
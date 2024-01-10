from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from LittleLemonAPI.models import Menu
from LittleLemonAPI.serializers import MenuItemSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        # Creating test instances of the Menu model
        Menu.objects.create(name='Dish 1', description='Description 1', price=10.99)
        Menu.objects.create(name='Dish 2', description='Description 2', price=8.50)

    def test_getall(self):
        client = APIClient()
        url = reverse('menu-list-create')  # Assuming the URL name is 'menu-list-create'

        # Making a GET request to retrieve all Menu objects
        response = client.get(url)
        menus = Menu.objects.all()
        serializer = MenuItemSerializer(menus, many=True)

        # Assertions to check if the serialized data equals the response data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

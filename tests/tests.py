from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
 
from api.serializers import *
from users.models import *


class TaskApiTest(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(
            username="example", email="example@gmail.com", 
            password="ex@mql3"
        )
        self.client.force_authenticate(self.user)

        Series.objects.create(id=1,
            name='Iron Man',
            description='Billionaire, playboy, philantropist')


    def test_get_series_list(self):
        res = self.client.get(reverse('api:get-series'))
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_get_series_list_fail(self):
        res = self.client.get('api/get-series/')
        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)

    def test_series_detail(self):
        res = self.client.get(reverse('api:series', kwargs={'pk': 1}))
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_series_detail_fail(self):
        res = self.client.get('api/get-series/', kwargs={'pk': 1})
        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_series(self):
        sample_data = {
            'name': 'Iron Man',
            'description': 'Billionaire, playboy, philantropist'
        }
        res = self.client.post(reverse('api:create-series'), sample_data)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_create_series_fail(self):
        sample_data = {
            'name': [],
            'description': []
        }
        res = self.client.get(reverse('api:create-series'), sample_data)
        self.assertEqual(res.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_update_series(self):
        sample_data = {
            'name': 'Black Panther',
            'description': 'King of Wakanda'
        }
        res = self.client.patch(reverse('api:update-series', kwargs={'pk': 1}), sample_data)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_update_series_fail(self):
        sample_data = {
            'name': 'Black Panther',
            'description': 'King of Wakanda'
        }
        res = self.client.post(reverse('api:update-series', kwargs={'pk': 1}), sample_data)
        self.assertEqual(res.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_delete_series(self):
        res = self.client.delete(reverse('api:delete-series', kwargs={'pk': 1}))
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_delete_series_fail(self):
        res = self.client.delete(reverse('api:series', kwargs={'pk': 1}))
        self.assertEqual(res.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)    
        
       
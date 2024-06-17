from django.urls import reverse
from django.test import TestCase, Client

from ..models import Service


class ServiceViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('resolve_path_collision', args=['yandex'])

    def test_create_or_update_with_valid_data(self):
        data = {'password': 'password/yandex'}

        response = self.client.post(self.url, data, content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertTrue(Service.objects.filter(name='yandex').exists())

    def test_create_or_update_without_password(self):
        data = {'service_name': 'yandex'}

        response = self.client.post(self.url, data, content_type='application/json')

        self.assertEqual(response.status_code, 400)

    def test_create_or_update_without_service(self):
        data = {'password': 'password123'}

        response = self.client.post(self.url, data, content_type='application/json')

        self.assertEqual(response.status_code, 400)

    def test_create_or_update_validate_password(self):
        data = {'password': 'short', 'service_name': 'yandex'}

        response = self.client.post(self.url, data, content_type='application/json')

        self.assertEqual(response.status_code, 400)

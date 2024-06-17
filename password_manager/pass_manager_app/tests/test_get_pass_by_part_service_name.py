from django.test import TestCase, Client
from django.urls import reverse

from ..errors.errors import ValidationError
from ..models import Service
from ..repository import repository_service
from ..repository import repository_password
from unittest.mock import patch


class PasswordRetrievalTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.partial_service_name = 'test'
        self.full_service_name = 'test_service'
        self.service_url = reverse('get_password_by_part_of_service_name')
        self.service = Service.objects.create(name=self.full_service_name)
        self.password = 'test_password'

    def test_get_password_success(self):
        with patch.object(repository_service.ServiceManager,
                          'get_service_by_part_of_name', return_value=self.service), \
             patch.object(repository_password.PasswordManager,
                          'get_password_by_service_id', return_value=self.password):

            response = self.client.get(self.service_url, {'service_name': self.partial_service_name})

            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json(), {'password': self.password,
                                               'service_name': self.full_service_name})

    def test_service_not_found(self):
        with patch.object(repository_service.ServiceManager, 'get_service_by_part_of_name', return_value=None):

            response = self.client.get(self.service_url, {'service_name': self.partial_service_name})

            self.assertEqual(response.status_code, 404)
            self.assertIn('Service not found', response.json()['error'])

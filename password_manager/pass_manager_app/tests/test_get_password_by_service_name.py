from django.test import TestCase, Client
from django.urls import reverse
from ..models import Service
from ..repository import repository_password
from ..repository import repository_service
from unittest.mock import patch


class PasswordManagementTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.service_name = 'test_service'
        self.service_url = reverse('resolve_path_collision', kwargs={'service_name': self.service_name})
        self.service = Service.objects.create(name=self.service_name)
        self.password = 'test_password'

    def test_service_not_found(self):
        with patch.object(repository_service.ServiceManager, 'get_service_by_name', return_value=None) as mock_service:
            response = self.client.get(self.service_url)
            self.assertEqual(response.status_code, 400)

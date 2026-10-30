from django.test import TestCase
from django.urls import reverse


class StatusAPITests(TestCase):

    def test_status_endpoint_returns_200(self):
        response = self.client.get(reverse('status'))
        self.assertEqual(response.status_code, 200)

    def test_status_endpoint_returns_correct_data(self):
        response = self.client.get(reverse('status'))

        self.assertEqual(response.data['status'], 'success')
        self.assertEqual(response.data['version'], 1)
        self.assertEqual(
            response.data['message'],
            'CSC 325 CI/CD Pipeline is working!'
        )
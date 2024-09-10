from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse


class ServiceCartTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='tester',
            email='aik@yahoo.com',
            password='secret'
        )
        self.client.force_login(self.user)

    def test_service_cart(self):
        response = self.client.get('/service_cart/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'service_cart/service_cart_summary.html')
        response = self.client.get(reverse('service-cart-summary'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'service_cart/service_cart_summary.html')
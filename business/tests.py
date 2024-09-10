from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Business
from django.contrib.auth.decorators import login_required

class BusinessTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='tester',
            email='aik@yahoo.fr',
            password='secret'
        )
        self.business = Business.objects.create(
            owner=self.user,
            business_name='tester',
            logo='test_logo.png',
            business_description='Busineess description test',
            location='test location',
            email='aik@yahoo.com',
            contact=12345
        )
    def test_business_creation(self):
        self.business.save()
        self.assertEqual(self.business.owner, self.user)
        self.assertEqual(self.business.business_name, 'tester')
        self.assertEqual(self.business.logo, 'test_logo.png')
    def test_business_updating(self):
        self.business.save()
        self.business.email = 'aiknew@yahoo.com'
        self.business.save()
        self.assertEqual(self.business.email, 'aiknew@yahoo.com')

    def test_homepage_view_authenticated(self):
        self.client.login(username='tester', password='secret')
        response = self.client.get(reverse('businesses_list'))
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse('register_biz'))
        self.assertEqual(response.status_code, 200)
    def test_homepage_view_unauthenticated(self):
        response = self.client.get(reverse('businesses_list'))
        self.assertEqual(response.status_code, 302)

    def test_businessdetail_view_authenticated(self):
        self.client.login(username='tester', password='secret')
        self.business.save()
        count = Business.objects.count()
        query_from_business = Business.objects.filter(owner=self.user).first()
        url = reverse('catalogue', kwargs={'pk': query_from_business.pk})
        self.assertEqual(url, '/business/'+str(count))
        url = self.client.get(reverse('catalogue', kwargs={'pk': query_from_business.pk}))
        self.assertEqual(url.status_code, 200)
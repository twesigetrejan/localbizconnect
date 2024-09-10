from django.test import TestCase
from .models import service, booking
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.urls import reverse

class ServiceTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='tester',
            email='aik@yahoo.fr',
            password='secret'
        )
        self.client.force_login(self.user)
        self.service = service.objects.create(
            service_name="test",
            service_description="test description",
            service_prices="100",
            location="test location",
            Contact=256,
            image1="test_image1.png",
            image2="test_image2.png",
            image3="test_image3.png",
            image4="test_image4.png",
            image5="test_image5.png",
            image6="test_image6.png"
        )
        self.booking = booking.objects.create(
            customer=self.user,
            service_booked=self.service,
        )
    def test_service_creation(self):
        self.service.save()
        latest_service = service.objects.latest('id')
        self.assertEqual(latest_service.service_name, "test")
        self.assertEqual(latest_service.service_description, "test description")
    def test_booking_creation(self):
        self.service.save()
        self.booking.save()
        latest_service = service.objects.latest('id')
        latest_booking = booking.objects.latest('id')
        self.assertEqual(latest_booking.service_booked, self.service)

        #Testing two bookings for one service
        # booking2 = booking.objects.create(
        #     customer=self.user,
        #     service_booked=self.service,
        #     date_booked=self.booking.date_booked + timezone.timedelta(days=1)
        # )
        # booking2.save()
        # latest_booking2 = booking.objects.latest('id')
        # self.assertNotEqual(latest_booking2.id, latest_booking.id)
        # self.assertEqual(booking.objects.count(), 2)
    def test_services_home_view(self):
        self.service.save()
        response = self.client.get('/services/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse('services'))
        self.assertEqual(response.status_code, 200)
    def test_services_bookings_view(self):
        self.service.save()
        response = self.client.get('/services/')
        self.assertEqual(response.status_code, 200)

        self.booking.save()
        response = self.client.get(reverse('service-booking', kwargs={'service_id': self.booking.id}))
        self.assertEqual(response.status_code, 200)


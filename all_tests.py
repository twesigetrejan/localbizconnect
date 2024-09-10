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
        booking2 = booking.objects.create(
            customer=self.user,
            service_booked=self.service,
            date_booked=timezone.now() + timezone.timedelta(days=1)
        )
        booking2.save()
        latest_booking2 = booking.objects.latest('id')
        self.assertNotEqual(latest_booking2.id, latest_booking.id)
        self.assertEqual(booking.objects.count(), 2)
    def test_services_home_view(self):
        self.service.save()
        response = self.client.get('/services/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse('services'))
        self.assertEqual(response.status_code, 200)
    def test_services_bookings_view(self):
        self.service.save()
        response = self.client.get('/services/bookings/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse('booking-request'))
        self.assertEqual(response.status_code, 200)






from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import *

class TestStorefront(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='tester',
            email='aik@yahoo.fr',
            password='secret'
        )
        self.client.login(username='tester', password='secret')

        self.item = Item.objects.create(
            title='test item',
            picture='test_picture.png',
            price=100.10,
            category='music',
            label='limited'
        )
        self.item_detail = Item_details.objects.create(
            item=self.item,
            description='test description',
            key_features='test key_features'
        )
        self.order_item = OrderItem.objects.create(item=self.item)

        # self.order = Order.objects.create(
        #     user=self.user,
        #     items=self.item_detail.item,
        #     start_date=timezone.now(),
        #     ordered_date=timezone.now(),
        #     ordered=False
        # )

    def test_item_creation(self):
        self.item.save()
        latest_item = Item.objects.latest('id')
        self.assertEqual(self.item.title, latest_item.title)
        self.assertEqual(self.item.category, latest_item.category)

    def test_item_update(self):
        self.item.save()
        self.item.title = 'New test item'
        self.item.save()
        self.assertEqual(self.item.title, 'New test item')

    def test_item_false_category(self):
        self.item.category = 'not my category'
        latest_item = Item.objects.latest('id')
        self.assertNotEqual(latest_item.category, 'not my category')

    def test_item_detail_creation(self):
        self.item_detail.save()
        latest = Item_details.objects.latest('id')
        self.assertEqual(self.item_detail.description, latest.description)
    def test_item_detail_update(self):
        self.item_detail.save()
        self.item_detail.description = 'new description'
        self.item_detail.save()
        latest = Item_details.objects.latest('id')
        self.assertEqual('new description', latest.description)
    # def test_order_creation(self):
    #     count = Order.objects.count()
    #     order = Order.objects.create(user=self.user, start_date=timezone.now(), ordered_date=timezone.now(),
    #                                  ordered=False)
    #     order.items.add(self.order_item)
    #     self.assertEqual(Order.objects.count(), count + 1)
    def test_view_home(self):
        response = self.client.get(reverse('Item-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "storefront/home.html")
    def test_product_details_view(self):
        response = self.client.get(reverse('item-details'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "storefront/Item_details.html")
    def test_add_to_cart(self):
        self.item.save()
        query = Item.objects.latest('id')
        url = self.client.get(reverse('add-to-cart', kwargs={'item_id': query.id}))
        expected_url = '/cart/'
        self.assertEqual(url.status_code, 302)
        self.assertRedirects(url, expected_url, status_code=302)
    #def test_view_cart(self):
    
    
    
    
    
    from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Profile
from PIL import Image

class ProfileTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='tester',
            email='aik@yahoo.fr',
            password='secret'
        )

        image = Image.new('RGB', (100, 100), (255, 255, 255))
        image_path = 'media/test.png'
        image.save(image_path)

        if not hasattr(self.user, 'profile'):
            self.profile = Profile.objects.create(
                user=self.user,
                image='media/test.png',
                Bio='This is a test bio.'
            )
        else:
            self.profile = self.user.profile
            self.profile.image = 'test.png'
            self.profile.Bio = 'This is a test bio.'
            self.profile.save()

    def test_profile_creation(self):
        self.profile.save()
        self.assertEqual(self.profile.user, self.user)
        self.assertEqual(self.profile.image, 'test.png')
        self.assertEqual(self.profile.Bio, 'This is a test bio.')

    def test_save_profile(self):
        self.profile.save()
        query_from_db = Profile.objects.get(user=self.user)
        self.assertEqual(query_from_db.user, self.profile.user)
        self.assertEqual(query_from_db.image, 'test.png')
        self.assertEqual(query_from_db.Bio, 'This is a test bio.')
    def test_update_profile(self):
        self.profile.save()
        self.profile.Bio = "This is new bio"
        self.profile.save()
        query_from_db = Profile.objects.get(user=self.user)
        self.assertEqual(query_from_db.Bio, 'This is new bio')


    def test_homepage_view(self):
        response = self.client.get(reverse('site-home'))
        self.assertEqual(response.status_code, 200)
    def test_userlogin_page_view(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
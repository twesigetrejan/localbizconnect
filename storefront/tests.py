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
        self.client.force_login(self.user)

        self.item = Item.objects.create(
            title='test item',
            picture='test_picture.png',
            price=100.10,
            category='music',
            label='limited',
            short_description='test description',
        )
        self.item_detail = Item_details.objects.create(
            item=self.item,
            key_features='test key_features'
        )
        #self.order_item = OrderItem.objects.create(item=self.item)


    def test_order_model(self):
        self.order = Order.objects.create(
            user=self.user,
            item=self.item_detail.item,
            total_price=1000,
            location="Kampala",
            order_status='Pending',
            payment_method='Cash On Delivery',
            confirmation_token='Test token',
        )
        self.order.save()
        latest_order = Order.objects.latest('id')
        self.assertEqual(latest_order.location, "Kampala")
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
        self.assertEqual(self.item_detail.key_features, latest.key_features)
    def test_item_detail_update(self):
        self.item_detail.save()
        self.item_detail.key_features = 'new key-feature'
        self.item_detail.save()
        latest = Item_details.objects.latest('id')
        self.assertEqual('new key-feature', latest.key_features)
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
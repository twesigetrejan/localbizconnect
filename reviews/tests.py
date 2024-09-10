from django.test import TestCase
from .models import Item, Review
from django.contrib.auth import get_user_model
class ItemTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='tester',
            email='aik@yahhoo.fr',
            password='secret'
        )
        self.item = Item.objects.create(
            name='Test Item',
            description='test description'
        )
        self.review = Review.objects.create(
            item=self.item,
            user=self.user,
            rating=9,
            comment='test comment',
        )

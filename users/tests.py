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
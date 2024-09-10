from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

class Business(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    business_name = models.CharField(max_length=35, default ='Business name')
    logo = models.ImageField(default='default.jpg', upload_to='business_logos')
    business_description = models.TextField(max_length=200)
    location = models.TextField(max_length = 50)
    email = models.EmailField()
    contact = models.IntegerField()

    def __str__(self):
        return f'{self.owner.username} Business'

    def get_absolute_url(self):
        return reverse('catalogue', args=str(self.pk))

class Catalogue(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name='catalogues', default=None)
    images = models.ImageField(upload_to='business_catalogue', default=None)

    def __str__(self):
        return f'Catalogue for {self.business.business_name}'
    
class Image(models.Model):
    image = models.ImageField(upload_to='business_catalogue_images')
    def __str__(self):
        return f'Image {self.id}'



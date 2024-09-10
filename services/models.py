from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image

class service(models.Model):
    service_name = models.CharField(max_length = 100)
    service_description = models.CharField(default ='service description', max_length=600)
    service_prices = models.CharField(max_length = 100) 
    image1 = models.ImageField(upload_to='service_images', blank=True)
    image2 = models.ImageField(upload_to='service_images', blank=True)
    image3 = models.ImageField(upload_to='service_images', blank=True)
    image4 = models.ImageField(upload_to='service_images', blank=True)
    image5 = models.ImageField(upload_to='service_images', blank=True)
    image6 = models.ImageField(upload_to='service_images', blank=True)
    location = models.CharField(max_length = 100, default = 'Kampala')
    Contact = models.IntegerField(default =+256)
    
    def __str__(self):
        return f'{self.service_name}  {self.service_description}'

STATUS_CHOICE = (
    ('Pending','Pending'),
    ('Booked', 'Booked'),
    ('Cancelled','Cancelled')
)
class booking(models.Model):
    customer = models.ForeignKey(User, on_delete = models.CASCADE)
    service_booked = models.OneToOneField(service, on_delete = models.CASCADE)
    date_booked = models.DateTimeField(default =timezone.now)
    start_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices= STATUS_CHOICE, max_length=18, default = 'Pending')
    
      
def __str__(self):
        return f'Booking of {self.service_booked.service_name} - {self.service_booked.service_description} by {self.customer}'
    

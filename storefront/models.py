from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth import get_user
from PIL import Image


class Customer(models.Model):
    name = models.CharField(max_length=200,null=True,blank=True)
    phone_number = models.CharField(max_length=200,null=True,blank=True)
    email = models.EmailField(max_length=200,null=True,blank=True)
    address = models.CharField(max_length=200,null=True,blank=True)
    city = models.CharField(max_length=200,null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return f'{self.name.username} details' 
    
    
    def __str__(self):
        return f'{self.name}'
    
    
    def __str__(self):
        return f'{self.customer} order' 
    
    
# refresh
CATEGORY_CHOICES = (
    ('food and beverages','food and beverages'),
    ('phones','phones'),
    ('outdoor','outdoor'),
    ('indoor','indoor'),
    ('watches and jewelry','watches and jewelry'),
    ('books and stationery','books and stationery'),
    ('toys','toys'),
    ('games','games'),
    ('shoes','shoes'),
    ('bags', "bags"),
    ('electronics','electronics'),
    ('health and beauty', 'health and beauty'),
    ('sports','sports'),
    ('furniture','furniture'),
    ('music','music'),
    ('baby','baby'),
    ('fitness and gym','fitness and gym'),
    ('kitchen and dining','kitchen and dining')
    )
LABEL_CHOICES = (
    ('new','new'),
    ('flash sale', 'flash sale'),
    ('limited','limited')
)
class Item(models.Model):
    title = models.CharField(max_length =100)
    picture = models.ImageField(default='default.jpg', upload_to = 'item_pics')
    price  = models.FloatField()
    category = models.CharField(choices =CATEGORY_CHOICES, max_length =30, default =None)
    short_description = models.TextField(max_length =70, default ='description')
    label = models.CharField(choices = LABEL_CHOICES, max_length = 15, default =None)
    quantity = models.IntegerField(default = 1)
    
    def __str__(self):
        return self.title
    
class Item_details(Item):
    item = models.OneToOneField(Item, on_delete = models.CASCADE, related_name ='details')
    key_features = models.TextField(max_length= 200) 

    def __str__(self):
        return f'{self.item.title} description'
         



STATUS = (
    ('Pending', 'Pending'),
    ('Delivered','Delivered'),
    ('Cancelled', 'Cancelled')
                )
PAYMENT = (
    ('Cash On Delivery', 'Cash On Delivery'),
)
class Order(models.Model):
    user  = models.ForeignKey(get_user_model(), on_delete= models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null = True)
    total_price = models.DecimalField(max_digits=20, decimal_places=1, default = 0)
    location = models.CharField(max_length= 40, null= False, default= 'enter delivery location')
    order_status = models.CharField(max_length=20, choices= STATUS, default = 'Pending')
    created_at = models.DateTimeField(default= timezone.now)
    payment_method = models.CharField(choices= PAYMENT, default = 'Cash On Delivery', max_length= 30)
    confirmation_token = models.CharField(max_length=255, blank=True, null=True)
    def save(self, *args, **kwargs):
        # Ensure that the user is set before saving the order
        if not self.user:
            raise ValueError("User must be set before saving the order.")
        super().save(*args, **kwargs)
     
    

    def save(self, *args, **kwargs):
        current_user = get_user(kwargs.get('request'))
        if isinstance(current_user, AnonymousUser):
            # If the user is not logged in, handle it accordingly
            # For example, you can set user to None or any default user
            self.user = None
        else:
            self.user = current_user
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Order #{self.pk} by {self.user.username}'
    
    


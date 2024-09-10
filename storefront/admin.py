from django.contrib import admin
from .models import  Item, Order, Item_details

admin.site.register(Item)
admin.site.register(Order)
admin.site.register(Item_details)

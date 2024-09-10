from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from storefront.models import Item

# class Item(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField()
#     def __str__(self):
#         return self.title

class Review(models.Model):
    item = models.ForeignKey(Item, on_delete = models.CASCADE, related_name ='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review for {self.item.title} by {self.user.username}'
from django.urls import path
from . import views

urlpatterns = [
    path('', views.service_cart_summary, name= 'service-cart-summary'),
    path('add/', views.service_cart_add, name= 'service-cart-add'),
    path('delete/', views.service_cart_delete, name= 'service-cart-delete'),
    path('update/', views.service_cart_update, name= 'service-cart-update'),
    
]
#add to cart
# delete
#update
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name ="Item-list"),
    path('item/<int:item_id>/', views.item_detail, name='item_detail'),
    path('add-to-cart/<int:item_id>/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.cart_view, name='cart-view'),
    path('remove-item/<int:item_id>/', views.remove_item, name='remove-item'),
    path('create_order/<total_price>/<str:confirmation_token>/', views.create_order, name='create-order'),
    path('about/', views.about, name = 'about'),
    path('add-item/', views.ItemAdd, name ='add-item'),
    ]


from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name ='site-home'),
    path('logout/', views.logout_view, name='logout'),
]
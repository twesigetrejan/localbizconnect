from django.urls import path
from .views import ReviewCreateView

urlpatterns = [
    path('new/', ReviewCreateView.as_view(), name='reviews'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('new/', views.BusinessCreateView.as_view(), name='register_biz'),
    path('<int:pk>', views.BusinessDetailView.as_view(), name='catalogue'),
    path('', views.BusinessListView.as_view(), name='businesses_list'),
] 
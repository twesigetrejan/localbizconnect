from .models import Review
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
class ReviewCreateView(CreateView):
    model = Review
    template_name = 'reviews/create_review.html'
    fields = '__all__'
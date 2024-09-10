from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Business, Catalogue
from .forms import BusinessForm, CatalogueForm
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView
# from users.urls import


class BusinessCreateView(LoginRequiredMixin, CreateView):
    model = Business
    template_name = 'business/business_create.html'
    fields = '__all__'
    login_url = 'login'

    def get_success_url(self):
        return reverse('catalogue', kwargs={'pk': self.object.pk})

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            self.object = form.save()

            photos = request.FILES.getlist('photos')
            for photo in photos:
                Catalogue.objects.create(business=self.object, images=photo)

            return self.form_valid(form)
        else:
            return self.form_invalid(form)

class BusinessDetailView(LoginRequiredMixin, DetailView):
    model = Business
    template_name = 'business/business_detail.html'

class BusinessListView(LoginRequiredMixin, ListView):
    model = Business
    template_name = 'business/businesses_list.html'
    context_object_name = 'businesses'

    def get_queryset(self):
        return Business.objects.filter(owner=self.request.user)



# @login_required(login_url='/login')
# def register_business(request):
#     if request.method == 'POST':
#         form = BusinessForm(request.POST)
#         if form.is_valid():
#             owner= form.cleaned_data.get('owner')
#             business =form.save()
#             business.owner = request.user
#             business.save()
#             return redirect('catalogue')
#     else:
#         form = BusinessForm()
#     return render(request, 'business/business.html', {'form':form})
#
# def add_catalogue(request):
#     if request.method == 'POST':
#         CartForm= CatalogueForm(request.POST)
#         if CartForm.is_valid():
#             cart = CartForm.save()
#             return redirect('login')
#     else:
#         CartForm =CatalogueForm()
#     return render(request, 'business/catalogue.html', {'CartForm':CartForm})


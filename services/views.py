from django.shortcuts import render, redirect, get_object_or_404
from .models import service, booking
from .forms import BookingForm
from django.contrib import messages
def service_request(request):
    context = {
        'services_provided': service.objects.all()
    }
    return render(request, 'services/service.html', context)

def book_service(request, service_id):
    service_instance = get_object_or_404(service, id=service_id)
    
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():  # Ensure to call is_valid as a method
            booking_instance = form.save(commit=False)
            booking_instance.service_booked = service_instance
            booking_instance.save()
            
            service_booked = booking_instance.service_booked
            customer = booking_instance.customer
            messages.success(request, f"{service_booked} has been booked for {customer}")
            
            return redirect('services')
    else:
        form = BookingForm(initial={'service_booked': service_instance})
    
    return render(request, 'services/booking.html', {'form': form })




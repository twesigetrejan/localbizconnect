from django.shortcuts import render

def service_cart_summary(request):
    return render(request, 'service_cart/service_cart_summary.html')

def service_cart_add(request):
    return render(request, 'service_cart/service_cart_add.html')

def service_cart_delete(request):
    return render(request, 'service_cart/service_cart_delete.html')

def service_cart_update(request):
    return render(request, 'service_cart/service_cart_summary.html')
   


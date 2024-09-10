from django import forms
from .models import booking, service

class BookingForm(forms.ModelForm):
    class Meta:
        model = booking
        fields = ['service_booked', 'date_booked']
        
    def __init__(self, *args, **kwargs):
        service_instance = kwargs.pop('service_instance', None)
        super().__init__(*args, **kwargs)
        
        # Set initial value for service_booked field
        if service_instance:
            self.initial['service_booked'] = service_instance
            
        # Customize the service_booked field widget to display services
        self.fields['service_booked'].widget = ServiceBookedWidget()


class ServiceBookedWidget(forms.widgets.TextInput):
    def render(self, name, value, attrs=None, renderer=None):
        if value:
            if isinstance(value, int):
                # If value is an integer, assume it's a service ID and get the corresponding service instance
                service_instance = service.objects.get(pk=value)
                value = f"{service_instance.service_name} - {service_instance.service_description}"
            elif isinstance(value, str):
                # If value is a string, just display it as it is
                pass
        
        return super().render(name, value, attrs, renderer)

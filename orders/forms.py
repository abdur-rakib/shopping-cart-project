from django import forms
from .models import Order
from django_countries.fields import CountryField


class OrderCreateForm(forms.ModelForm):
    country = CountryField().formfield()
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'country', 'postal_code', 'city', 'address']

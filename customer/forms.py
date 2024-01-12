from django import forms
from .models import Customer


class Customer_form(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['username', 'password', 'first_name', 'last_name', 'phone_number', 'address', 'natural_number']

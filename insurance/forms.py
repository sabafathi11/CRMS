from django import forms
from .models import Insurance


class Insurance_form(forms.ModelForm):
    class Meta:
        model = Insurance
        fields = ['name', 'duration', 'payment_kind']

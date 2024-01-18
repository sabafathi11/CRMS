from django import forms
from .models import Insurance, Use_insurance, Bank_card


class Insurance_form(forms.ModelForm):
    class Meta:
        model = Insurance
        fields = ['name', 'duration', 'payment_kind']

class Use_insurance_form(forms.ModelForm):
    class Meta:
        model = Use_insurance, Bank_card
        fields = ['card_number', 'shaba_number', 'bank_name', 'request_content', 'amount', 'documents']
from django.db import models
from customer.models import Customer
from consultant.models import Consultant


class Insurance(models):
    name = models.CharField(max_length=150, blank=False)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, related_name='Insurance')
    consultant = models.ForeignKey(Consultant, on_delete=models.SET_NULL, related_name='consultant')
#    forms = models.FileField(upload_to='Files/Insurance_Forms', max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    duration = models.IntegerField(max_length=15, choices=[1, 5, 10, 15, 30])  # years
    cost = models.FloatField(max_length=150, blank=False)


    # payment dates , installment payment , consultant contact ,

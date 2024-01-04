from django.db import models
from customer.models import Customer
from consultant.models import Consultant


class Insurance(models):
    name = models.CharField(max_length=150, blank=False)
    cost_per_month = models.FloatField(max_length=150, blank=False)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, related_name='Insurance')
    consultant = models.ForeignKey(Consultant, on_delete=models.SET_NULL, related_name='consultant')
    forms = models.FileField(upload_to='Files/Insurance_Forms',max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    duration = models.IntegerField(max_length=15, choices=[1, 5, 10, 15, 30])  # years
    cost = models.FloatField(max_length=150, blank=False)

    payment_kind = models.CharField(max_length=15, choices=['yearly', 'monthly'])
    if payment_kind == 'yearly':
        payment_count = duration
    else:
        payment_count = duration * 12
    payment_amount = cost / payment_count

    payment_dates = []
    if payment_kind == 'yearly':
        for i in range(payment_count):
            payment_dates.append(created_at.replace(year=created_at.year + i))
    else:
        for i in range(payment_count):
            payment_dates.append(created_at.replace(month=created_at.month + i))

    payment_check = {i: False for i in payment_dates}

    def pay(self, date: models.DateTimeField):
        self.payment_check[date] = True

    def next_payment(self):
        for key in self.payment_check.keys():
            if not self.payment_check[key]:
                return key

    # payment dates , installment payment , consultant contact ,



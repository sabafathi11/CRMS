from django.db import models
from customer.models import Customer
from consultant.models import Consultant


class Insurance(models.Model):
    name = models.CharField(max_length=150, blank=False)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, related_name='Insurance', null=True)
    consultant = models.ForeignKey(Consultant, on_delete=models.SET_NULL, related_name='consultant', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    duration = models.IntegerField(choices=((1, '1 year'),(5, '5 years'),(10, '10 years'),(15, '15 years'),(30, '30 years'),))
    cost = models.FloatField(max_length=150, blank=False)
    payment_kind = models.CharField(max_length=15, choices=(('1','yearly'), ('2','monthly')))

    @property
    def payment_count(self):
        if self.payment_kind == '1':
            return self.duration
        else:
            return self.duration * 12

    @property
    def payment_amount(self):
        return self.cost / self.payment_count

    # payment dates , installment payment , consultant contact ,


class Payment_dates(models.Model):
    date = models.DateTimeField()
    paid = models.BooleanField(default=False)
    insurance = models.ForeignKey(Insurance, on_delete=models.SET_NULL, related_name='payment_dates', null=True)

    def pay(self):
        self.paid = True


class Use_insurance(models.Model):
    date = models.DateTimeField()
    amount = models.FloatField(max_length=150, blank=False)
    insurance = models.ForeignKey(Insurance, on_delete=models.SET_NULL, related_name='use_insurance', null=True)

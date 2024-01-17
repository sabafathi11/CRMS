from django.db import models
from customer.models import Customer
from consultant.models import Consultant


class Insurance(models.Model):
    Choices = (
        (1, 'بدنه ماشین'), (2, 'شخص ثالث'), (3, 'حوادث'), (4, 'درمان'), (5, 'عمر'), (6, 'واحد مسکونی'),
        (7, 'مرکز صنعتی'), (8, 'مرکز غیر صنعتی'), (9, 'حمل و نقل'), (10, 'هواپیما'))
    name = models.IntegerField(blank=False, choices=(Choices))
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, related_name='Insurance', null=True)
    consultant = models.ForeignKey(Consultant, on_delete=models.SET_NULL, related_name='consultant', null=True)
    created_at = models.DateField()
    duration = models.IntegerField(
        choices=((1, '1 year'), (5, '5 years'), (10, '10 years'), (15, '15 years'), (30, '30 years'),))
    cost = models.FloatField(max_length=150, blank=False)
    payment_kind = models.CharField(max_length=15, choices=(('1', 'yearly'), ('2', 'monthly')))

    @property
    def name_value(self):
        for (i, j) in self.Choices:
            if i == self.name:
                return j

    @property
    def payment_count(self):
        if self.payment_kind == '1':
            return int(self.duration)
        else:
            return int(self.duration) * 12

    @property
    def payment_amount(self):
        return self.cost / self.payment_count

    # payment dates , installment payment , consultant contact ,


class Payment_dates(models.Model):
    date = models.DateField()
    paid = models.BooleanField(default=False)
    insurance = models.ForeignKey(Insurance, on_delete=models.SET_NULL, related_name='payment_dates', null=True)

    def pay(self):
        self.paid = True


class Bank_card(models.Model):
    card_number = models.IntegerField(blank=False)
    shaba_number = models.IntegerField(blank=False)
    bank_name = models.CharField(max_length=150, blank=False)
    owner = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='Bank_card', null=True)


class Use_insurance(models.Model):
    request_content = models.CharField(max_length=500, default='')
    request_answer = models.CharField(max_length=500, default='')
    request_date = models.DateField()
    amount = models.FloatField(max_length=150, default=0)
    recieve_card = models.ForeignKey(Bank_card, on_delete=models.SET_NULL, related_name='use_insurance', null=True)
    documents = models.FileField(default='')
    insurance = models.ForeignKey(Insurance, on_delete=models.CASCADE, related_name='use_insurance', null=True)
    paid = models.BooleanField(default=False)
    paid_date = models.DateField()

from django.db import models
from customer.models import Customer
from consultant.models import Consultant


class Insurance(models.Model):
    cost_per_year = {1: 300000,
                     2: 400000,
                     3: 500000,
                     4: 300000,
                     5: 200000,
                     6: 250000,
                     7: 600000,
                     8: 600000,
                     9: 500000,
                     10: 1000000}
    Choices = (
        (1, 'بدنه ماشین'), (2, 'شخص ثالث'), (3, 'حوادث'), (4, 'درمان'), (5, 'عمر'), (6, 'واحد مسکونی'),
        (7, 'مرکز صنعتی'), (8, 'مرکز غیر صنعتی'), (9, 'حمل و نقل'), (10, 'هواپیما'))
    name = models.IntegerField(blank=False, choices=(Choices))
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, related_name='insurance_from_customer', null=True)
    consultant = models.ForeignKey(Consultant, on_delete=models.SET_NULL, related_name='insurance_from_consultant',
                                   null=True, blank=True)
    created_at = models.DateField()
    duration = models.IntegerField(
        choices=((1, 'یک سال'), (5, '5 سال'), (10, '10 سال'), (15, '15 سال'), (30, '30 سال'),))
    cost = models.FloatField(max_length=150, blank=False)
    payment_kind = models.CharField(max_length=15, choices=(('1', 'سالانه'), ('2', 'ماهانه')))

    @property
    def name_value(self):
        for (i, j) in self.Choices:
            if i == self.name:
                return j

    @property
    def payment_kind_value(self):
        if self.payment_kind == '1':
            return 'سالانه'
        return 'ماهانه'

    @property
    def expire_date(self):
        return self.created_at.replace(year=self.created_at.year + self.duration)

    @property
    def payment_count(self):
        if self.payment_kind == '1':
            return int(self.duration)
        else:
            return int(self.duration) * 12

    @property
    def cost_money(self):
        num = int(self.cost)
        return str('{:,}'.format(num))

    @property
    def payment_amount(self):
        num = int(self.cost / self.payment_count)
        return str('{:,}'.format(num))

    @property
    def not_paid_dates(self):
        for i in self.payment_dates_from_insurance.all():
            if not i.paid:
                return True

    @property
    def paid_dates(self):
        for i in self.payment_dates_from_insurance.all():
            if i.paid:
                return True

    def __str__(self):
        return self.name_value + ' ' + self.customer.username


class Payment_dates(models.Model):
    date = models.DateField()
    paid_date = models.DateField(null=True,blank=True)
    paid = models.BooleanField(default=False)
    insurance = models.ForeignKey(Insurance, on_delete=models.SET_NULL, related_name='payment_dates_from_insurance',
                                  null=True)

    def pay(self):
        self.paid = True

    def __str__(self):
        return self.insurance.__str__() + str(self.date)


class Bank_card(models.Model):
    card_number = models.IntegerField(blank=False)
    shaba_number = models.IntegerField(blank=False)
    bank_name = models.CharField(max_length=150, blank=False)
    owner = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='Bank_card_from_user', null=True)

    def __str__(self):
        return self.owner.__str__() + ' ' + self.bank_name


class Use_insurance(models.Model):
    request_content = models.CharField(max_length=500, default='')
    request_answer = models.CharField(max_length=500, default='', blank=True)
    request_date = models.DateField()
    amount = models.FloatField(max_length=150, default=0)
    recieve_card = models.ForeignKey(Bank_card, on_delete=models.SET_NULL, related_name='use_insurance_from_card',
                                     null=True)
    documents = models.FileField(default='')
    insurance = models.ForeignKey(Insurance, on_delete=models.CASCADE, related_name='use_insurance_from_insurance',
                                  null=True)
    paid = models.BooleanField(default=False)
    paid_date = models.DateField(null=True, blank=True)
    show_to_consultant = models.BooleanField(default=True)

    def __str__(self):
        return self.insurance.__str__() + ' ' + str(self.request_date)

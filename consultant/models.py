from django.db import models
from customer.models import Customer


class Consultant(Customer):
    salary = models.FloatField(max_length=250, blank=False)



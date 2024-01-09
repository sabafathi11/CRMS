from django.db import models


class Consultant(models.Model):
    username = models.CharField(max_length=150, blank=False)
    password = models.CharField(max_length=150, blank=False)
    first_name = models.CharField(max_length=150, blank=False)
    last_name = models.CharField(max_length=150, blank=False)
    phone_number = models.CharField(max_length=11, blank=False)
    address = models.CharField(max_length=250, blank=False)
    natural_number = models.CharField(max_length=20, blank=False)
    salary = models.FloatField(max_length=250, blank=False)
    # customer
    # salary data

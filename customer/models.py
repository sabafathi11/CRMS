from django.contrib.auth.models import AbstractUser
from django.db import models


class Customer(AbstractUser):
    # username
    # password
    first_name = models.CharField(max_length=150, blank=False)
    last_name = models.CharField(max_length=150, blank=False)
    phone_number = models.CharField(max_length=11, blank=False)
    address = models.CharField(max_length=250, blank=False)
    natural_number = models.CharField(max_length=20, blank=False)
    # insurances
    # payment datas


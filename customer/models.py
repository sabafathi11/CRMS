from django.contrib.auth.models import AbstractUser
from django.db import models


class Customer(AbstractUser):
    # username inherits from AbstractUser
    # password inherits from AbstractUser
    first_name = models.CharField(max_length=150, blank=False)
    last_name = models.CharField(max_length=150, blank=False)
    phone_number = models.CharField(max_length=11, blank=False)
    address = models.CharField(max_length=250, blank=False)
    natural_number = models.CharField(max_length=20, blank=False)
    kind = models.CharField(max_length=10, choices=(('1', 'customer'),('2', 'consultant')), default='1')

    def __str__(self):
        return self.first_name + ' ' + self.last_name


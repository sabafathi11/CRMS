from django.contrib import admin
from .models import Customer


@admin.register(Customer)
class Customer_admin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'phone_number', 'address', 'natural_number')
    search_fields = ('username', 'first_name', 'last_name', 'phone_number')
    ordering = ('username',)
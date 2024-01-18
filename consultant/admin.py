from django.contrib import admin
from .models import Consultant


@admin.register(Consultant)
class Consultant_admin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'phone_number', 'address', 'natural_number', 'salary')
    search_fields = ('username', 'first_name', 'last_name', 'phone_number')
    ordering = ('username',)

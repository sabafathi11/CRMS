from django.contrib import admin
from .models import Insurance, Use_insurance, Payment_dates, Bank_card


@admin.register(Insurance)
class Insurance_admin(admin.ModelAdmin):
    list_display = ('name', 'customer', 'consultant', 'created_at', 'updated_at', 'duration', 'cost', 'payment_kind')
    search_fields = ('name', 'customer', 'consultant', 'payment_kind')
    ordering = ('created_at',)


@admin.register(Payment_dates)
class Payment_dates_admin(admin.ModelAdmin):
    list_display = ('insurance', 'date', 'paid')
    search_fields = ('insurance', 'date', 'paid')
    ordering = ('date',)


@admin.register(Use_insurance)
class Use_insurance_admin(admin.ModelAdmin):
    list_display = ('insurance', 'request_date', 'paid_date', 'paid', 'documents', 'amount')
    search_fields = ('insurance', 'request_date', 'paid_date', 'amount')
    ordering = ('request_date',)

@admin.register(Bank_card)
class Bank_card_admin(admin.ModelAdmin):
    list_display = ('card_number', 'shaba_number', 'bank_name', 'owner')
    search_fields = ('card_number', 'shaba_number', 'bank_name', 'owner')
from django.contrib import admin

#my model
from django.contrib import admin
from .models import Currency, ExchangeRate

@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ['code']

@admin.register(ExchangeRate)
class ExchangeRateAdmin(admin.ModelAdmin):
    list_display = ['base_currency', 'quote_currency', 'rate', 'timestamp']
    list_filter = ['base_currency', 'quote_currency']
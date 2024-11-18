from django.shortcuts import render

#my view
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Currency, ExchangeRate

@api_view(['GET'])
def currency_list(request):
    currencies = Currency.objects.values('code')
    return Response(currencies)

@api_view(['GET'])
def exchange_rate_detail(request, base_code, quote_code):
    try:
        base_currency = Currency.objects.get(code=base_code)
        quote_currency = Currency.objects.get(code=quote_code)
        exchange_rate = ExchangeRate.objects.filter(
            base_currency=base_currency,
            quote_currency=quote_currency
        ).order_by('-timestamp').first()
        
        if exchange_rate:
            data = {
                "currency_pair": f"{base_code}{quote_code}",
                "exchange_rate": exchange_rate.rate
            }
            return Response(data)
        return Response({"error": "Exchange rate not found."}, status=404)
    except Currency.DoesNotExist:
        return Response({"error": "Currency code not found."}, status=404)

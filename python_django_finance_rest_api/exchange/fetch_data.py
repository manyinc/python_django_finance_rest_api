import yfinance as yf
from .models import Currency, ExchangeRate

def fetch_data():
    currency_pairs = ["EURUSD=X", "USDJPY=X", "PLNUSD=X"]
    for pair in currency_pairs:
        data = yf.Ticker(pair).history(period="1d")
        base, quote = pair[:3], pair[3:6]
        
        base_currency, _ = Currency.objects.get_or_create(code=base)
        quote_currency, _ = Currency.objects.get_or_create(code=quote)

        for _, row in data.iterrows():
            ExchangeRate.objects.create(
                base_currency=base_currency,
                quote_currency=quote_currency,
                rate=row['Close']
            )
    print("Successfully fetched currency data.")

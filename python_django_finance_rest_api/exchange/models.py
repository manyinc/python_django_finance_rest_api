from django.db import models

#my model
class Currency(models.Model):
    code = models.CharField(max_length=3, unique=True)

    def __str__(self):
        return self.code


class ExchangeRate(models.Model):
    base_currency = models.ForeignKey(Currency, related_name="base_currency", on_delete=models.CASCADE)
    quote_currency = models.ForeignKey(Currency, related_name="quote_currency", on_delete=models.CASCADE)
    rate = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('base_currency', 'quote_currency', 'timestamp')
        ordering = ['-timestamp']
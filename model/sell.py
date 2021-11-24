from django.db import models

class Sell(models.Model):
    name = models.CharField(max_length=255)
    stopSellPercentage = models.IntegerField()

    def __str__(self):
        return str(self.name)

    class Meta:
        db_table = 'model_stocksell'
 
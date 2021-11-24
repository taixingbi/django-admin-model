from django.db import models

class stockSell(models.Model):
    name = models.CharField(max_length=255)
    stopSellPercentage = models.IntegerField()

    def __str__(self):
        # return str(self.id)
        return str(self.name)

    class Meta:
        verbose_name = "Sell"

    class Meta:
        db_table = 'model_stocksell'
from django.contrib import admin

from model.models import stockSell

@admin.register(stockSell)
class  StockSellAdmin(admin.ModelAdmin):
    pass
from django.contrib import admin
from .models import Logs, Drug, Sales

@admin.register(Logs)
class LogsAdmin(admin.ModelAdmin):
    list_display = ('period', 'action',)
    list_filter = ('period',)
    search_fields = ('action',)

@admin.register(Drug)
class LogsAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'qty_in_stock')
    search_fields = ('name',)

@admin.register(Sales)
class LogsAdmin(admin.ModelAdmin):
    list_display = ('period', 'drug', 'selling_price', 'seller', 'qty_sold')
    search_fields = ('drug__name',)
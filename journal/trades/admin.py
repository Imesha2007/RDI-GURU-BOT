from django.contrib import admin
from .models import Trade


@admin.register(Trade)
class TradeAdmin(admin.ModelAdmin):
    list_display = ("user", "symbol", "side", "quantity", "entry_price", "exit_price", "entry_time", "exit_time")
    list_filter = ("side", "symbol")
    search_fields = ("symbol", "notes", "user__username")

# Register your models here.

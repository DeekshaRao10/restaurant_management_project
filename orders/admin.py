from django.contrib import admin
from .models import Order, OrderStatus

def mark_orders_processed(modeladmin,request,queryset):
    processed_status,_=OrderStatus.objects.get_or_create(name="processsed")
    queryset.update(status=processed_status)
mark_orders_processed.short_description="mark selected orders as processe"

@admin.register(order)
class OrderAdmin(admin.Admin):
    list_display=("id","created_at","total_price","statsu")
    list_Filter=("status","created_at")
    actions=[mark_orders_processed]
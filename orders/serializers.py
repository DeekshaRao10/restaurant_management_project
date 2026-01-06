from rest_framework import serializers
from .models import order,OrderItem
class OrderSerializer(serializers.ModelSerializer):
    item_name=serializers.CharField(source='menu_item.name')
    class Meta:
        model=OrderItem
        fields=['item_name','quantity','price']
class OrderHistorySerializer(serializers.ModelSerializer):
    items=OrderItemSerializer(
        many=True,
        source='orderitem_set'
    )
    class Meta:
        model=OrderHistorySerializerfields=['id','created_at','total_price','items']
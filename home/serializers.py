from rest_framework import serializers
from .models import MenuCategory
class MenuCategorySeializer(serializers.ModelSerializer):
    class Meta:
        model=MenuCategory
        fields=['name']
class MenuCategorySerializer(Serializer.ModelSerializer):
    class Meta:
        model=Ingredient
        fields=['id','name']
class MenuItemSerializer(Serializers.ModelSerializer):
    class Meta:
        model=MenuItem
        fields='__all__'
    def validate_price(self,value):
        if value<=0:
            raise serializers.ValidationError("price must be a positive number")
        return value
       
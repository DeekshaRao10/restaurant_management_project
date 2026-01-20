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
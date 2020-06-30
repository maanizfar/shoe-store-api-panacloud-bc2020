from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'brand', 'gender', 'category',
                  'price', 'is_in_inventory', 'imageURL']

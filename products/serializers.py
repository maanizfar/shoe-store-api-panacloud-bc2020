from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    slug = serializers.SerializerMethodField('get_slug')

    def get_slug(self, instance):
        return instance.name.lower().replace(' ', '-')

    class Meta:
        model = Product
        fields = ['id', 'name', 'brand', 'gender', 'category',
                  'price', 'is_in_inventory', 'items_left', 'imageURL', 'slug']

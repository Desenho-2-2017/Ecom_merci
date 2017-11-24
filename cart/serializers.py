from rest_framework import serializers
from .models import (
    Cart,
    Item
    )


class CartSerializerDefault(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'


class ItemSerializerDefault(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'quantity', 'object_id', 'unit_price', 'cart',
                  'content_type')

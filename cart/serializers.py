from rest_framework import serializers
from .models import (
    Cart,
    Item
    )


class CartSerializerDefault(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'


class CartSerializerPOST(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ('pk', 'creation_date', 'checked_out')

    def create(self, validated_data):
        cart = Cart(**validated_data)
        return cart


class ItemSerializerDefault(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'quantity', 'object_id', 'unit_price', 'cart',
                  'content_type')

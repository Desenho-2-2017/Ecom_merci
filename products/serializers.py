from rest_framework import serializers
from .models import (
    ProductCategory,
    Product
    )


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

    def create(self, validated_data):
        obj = Product.objects.create(**validated_data)
        return obj


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = "__all__"

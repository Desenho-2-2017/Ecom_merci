from rest_framework import serializers
from .models import (
    ProductCategory,
    Product
    )


class ProductSerializerDefault(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class ProductSerializerPOST(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('pk', 'product_name', 'category_id', 'stock_quantity',
                  'price', 'weight', 'width', 'height', 'PRODUCT_TYPES',
                  'product_type', 'illustration')

    def create(self, validated_data):
        obj = Product.objects.create(**validated_data)
        return obj


class ProductCategorySerializerDefault(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = "__all__"


class ProductCategorySerializerPOST(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ('pk', 'category_name', 'father_category')

    def create(self, validated_data):
        obj = ProductCategory.objects.create(**validated_data)
        return obj

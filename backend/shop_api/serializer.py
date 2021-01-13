from rest_framework import serializers
from .models import *


class ColourSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductColour
        fields = ("colours",
                  "inventory",
                  "price")


class VariantSerializer(serializers.ModelSerializer):
    colours = ColourSerializer()

    class Meta:
        model = ProductVariant
        
        fields = ("cloth_type",
                  "shirt_size",
                  "hat_size",
                  "trouser_size",
                  "colours")


class ProductSerializer(serializers.ModelSerializer):
    variant = VariantSerializer()

    class Meta:
        model = Product
        fields = '__all__'
        lookup = 'slug'
        


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        lookup = 'reference_code'


class OrderedProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderedProduct
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

from rest_framework import serializers
from .models import *


class ColourSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductColour
        fields = '__all__'


class VariantSerializer(serializers.ModelSerializer):
    colour = ColourSerializer(many=True)

    class Meta:
        model = ProductVariant
        fields = ('cloth_type',
                  'cloth_size',
                  'shoe_size',
                  'colour')


class ProductSerializer(serializers.ModelSerializer):
    variant = VariantSerializer(many=True)

    class Meta:
        model = Product
        fields = ('name', 'image', 'description', 'variant')
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

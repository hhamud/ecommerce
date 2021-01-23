from rest_framework import serializers
from .models import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payments
        fields = '__all__'


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    address = AddressSerializer(many=True)
    payment = PaymentSerializer(many=True)

    class Meta:
        model = User
        lookup = 'user'
        fields = ('email', 'first_name', 'last_name',
                  'phone_number', 'address', 'payment')


class VariantSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductVariant
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    variant = VariantSerializer(many=True)

    class Meta:
        model = Product
        fields = ('name', 'image', 'description', 'slug', 'variant')
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


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        token['user_id'] = user.id

        return token

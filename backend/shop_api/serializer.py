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
    address = AddressSerializer(many=True, required=False)
    payment = PaymentSerializer(many=True, required=False)

    def create(self, validated_data):

        if "address" in validated_data and "payment" in validated_data:
            address_data = validated_data.pop('address')
            payment_data = validated_data.pop('payment')
            user = User.objects.create(**validated_data)

            for payment in payment_data:
                Payments.objects.create(user=user, **payment)

            for address in address_data:
                Address.objects.create(user=user, **address)

            return user
        else:
            return User.objects.create(**validated_data)

    class Meta:
        model = User
        lookup = 'user'
        fields = ('id', 'email', 'password', 'first_name', 'last_name',
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

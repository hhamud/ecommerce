from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework import generics, status
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    lookup_field = 'id'
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    lookup_field = 'id'
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]


class OrderListView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]


class OrderedProductListView(generics.ListAPIView):
    queryset = OrderedProduct.objects.all()
    serializer_class = OrderedProduct
    permission_classes = [IsAuthenticated]

class ObtainTokenPairWithColorView(TokenObtainPairView):
    permission_classes = [AllowAny,]
    serializer_class = MyTokenObtainPairSerializer

class UserCreate(APIView):
    permission_classes = [AllowAny,]
    authentication_classes = ()

    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDashboard(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all() 
    serializer_class = UserSerializer
    permission_class = [IsAuthenticated, ]
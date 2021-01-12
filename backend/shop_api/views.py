from django.shortcuts import render
from .models import *
from .serializer import ProductSerializer, OrderedProductsSerializer, OrderSerializer, UserSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated 

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









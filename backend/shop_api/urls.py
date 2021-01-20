from django.conf.urls import url, include
from .views import *
from django.urls import path
from rest_framework_simplejwt import views as jwt_views

accounts_urlpatterns = [
    url('products/', ProductListView.as_view()),
    url('products/<slug:slug>/', ProductDetailView.as_view()),
    url('checkout/', OrderedProductListView.as_view()),
    path('user/create/', UserCreate.as_view(), name="create_user"),
    path('token/obtain/', ObtainTokenPairWithColorView.as_view(), name='token_create'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),


]

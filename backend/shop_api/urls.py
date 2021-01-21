from django.conf.urls import url, include
from .views import *
from django.urls import path
from rest_framework_simplejwt import views as jwt_views

accounts_urlpatterns = [
    path('products/', ProductListView.as_view()),
    path('products/<slug:slug>/', ProductDetailView.as_view()),
    path('checkout/', OrderedProductListView.as_view()),
    path('users/<int:pk>/details/', UserDashboard.as_view()),
    path('users/<int:pk>/orders/', OrderedProductListView.as_view()),
    path('user/create/', UserCreate.as_view(), name="create_user"),
    path('token/obtain/', ObtainTokenPairWithColorView.as_view(), name='token_create'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]

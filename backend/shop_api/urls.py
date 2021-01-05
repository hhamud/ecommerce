from django.conf.urls import url, include
from .views import *

accounts_urlpatterns = [
    url('', include('djoser.urls')),
    url('', include('djoser.urls.authtoken')),
    url('products/', ProductListView.as_view()),
    url('products/<slug:slug>/', ProductDetailView.as_view()),
    url('checkout/', OrderedProductListView.as_view()),

]
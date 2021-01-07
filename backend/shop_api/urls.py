from django.conf.urls import url, include
from .views import *

accounts_urlpatterns = [
    url('api/', include('djoser.urls')),
    url('api/', include('djoser.urls.authtoken')),
    url('products/', ProductListView.as_view()),
    url('products/<slug:slug>/', ProductDetailView.as_view()),
    url('checkout/', OrderedProductListView.as_view()),

]
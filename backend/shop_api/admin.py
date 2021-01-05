from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *


@admin.register(User)
class MainUserAdmin(UserAdmin):
    exclude = ['slug', ]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    list_display = [
        'user',
        'ordered_date',
        'ordered',
        'payment',
        'returns_requested',
        'returns_granted',
        'billing_address',
        'shipping_address'
    ]
    list_display_links = [
        'billing_address',
        'shipping_address',
        'payment',
    ]
    list_filter = [
        'ordered',
        'returns_requested',
        'returns_granted',
    ]
    search_fields = [
        'reference_code'
    ]


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'home_number',
        'street',
        'area',
        'city',
        'post_code',
        'address_type',
    ]
    list_filter = [
        'address_type',
        'city',
        'country'
    ]
    search_fields = [
        'user',
        'home_number',
        'street',
        'area',
        'city',
        'post_code'
    ]


admin.site.register(Product)
admin.site.register(Payments)
admin.site.register(Returns)
admin.site.register(OrderedProduct)

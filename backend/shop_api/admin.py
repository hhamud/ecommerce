from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *


@admin.register(User)
class MainUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (('Personal info'), {'fields': ('first_name', 'last_name')}),
        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)


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


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    exclude = ['slug', ]
    
    def get_form(self, request, obj=None, **kwargs):
        if obj == None:
            pass
        elif obj.variant.cloth_type == 'hats' :
            self.exclude = ('shirt_size', 'trouser_size', )
        elif obj.variant.cloth_type == 'shirts':
            self.exclude = ('hat_size', 'trouser_size', )
        elif obj.variant.cloth_type == 'trousers':
            self.exclude = ('shirt_size', 'hat_size',)
        form = super(ProductAdmin, self).get_form(request, obj, **kwargs)
        return form


admin.site.register(Payments)
admin.site.register(Returns)
admin.site.register(OrderedProduct)
admin.site.register(ProductVariant)
admin.site.register(ProductColour)

import csv
from django.contrib import admin
from .models import *

admin.site.register(Address)
admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(ReturnedOrder)


######################
# Products
######################
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0


class ProductAttributeInline(admin.TabularInline):
    model = ProductAttribute
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'description', 'discount_price', 'sell_price', 'category',
        'created_at', 'updated_at', 'is_active'
    ]

    inlines = [ProductAttributeInline, ProductImageInline]
admin.site.register(Product, ProductAdmin)


######################
# Customer
######################
class AddressInline(admin.TabularInline):
    model = Address
    extra = 0


class CartInline(admin.TabularInline):
    model = Cart
    extra = 0


class OrderInline(admin.TabularInline):
    model = Order
    extra = 0


class CustomerAdmin(admin.ModelAdmin):
    inlines = [AddressInline, CartInline, OrderInline]
    list_display = [
        "id", "customer", "gender", "created_at", "is_active"
    ]

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Customer, CustomerAdmin)


######################
# orders
######################

class OrderAdmin(admin.ModelAdmin):
    # actions = ['download_csv']
    list_display = [
        'id', 'customer', 'product', 'quantity', 'ordered_date', 'order_status',
        'payment_mode', 'transaction_id', 'is_returned', 'is_delivered', 'updated_at'
        ]
admin.site.register(Order, OrderAdmin)

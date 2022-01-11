from django.contrib import admin
from .models import *

admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductAttributeBase)
admin.site.register(ProductAttribute)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(ReturnedOrder)


# Register your models here.

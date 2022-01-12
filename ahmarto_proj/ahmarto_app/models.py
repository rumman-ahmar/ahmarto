from django.contrib.auth.models import User
from django.db import models

GENDER_CHOICE = (
    ("M", "Male"),
    ("F", "Female"),
    ("O", "Others")
)

CATEGORY_CHOICE = (
    ("DE", "Daily Essentials"),
    ("SP", "Soap")
)

ORDER_STATUS_CHOICE = (
    ("Pending", "Pending"),
    ("Accepted", "Accepted"),
    ("Packed", "Packed"),
    ("Out For Delivery", "Out For Delivery"),
    ("Cancel", "Cancel")
)


PAYMENT_MODE_CHOICE = (
    ("COD", "Cash On Delivery"),
    ("UPI", "Unified Payments Interface"),
    ("Card", "Card"),
    ("NB", "Net Banking"),
    ("Wallet", "Wallet")
)


ADDRESS_TYPE_CHOICE = (
    ("H", "Home"),
    ("O", "Office")
)


# Create your models here.
class Customer(models.Model):
    customer = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(choices=GENDER_CHOICE, max_length=1, default=None, blank=True, null=True)
    profile_image = models.ImageField(upload_to="customer_images", blank=True, null=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)


class Address(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    house_number = models.CharField(max_length=50, blank=False, null=False)
    street_area = models.CharField(max_length=100, blank=False, null=False)
    city = models.CharField(max_length=50, blank=False, null=False)
    landmark = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=False, null=False)
    country = models.CharField(max_length=50, blank=False, null=False)
    pincode = models.CharField(max_length=6, blank=False, null=False)
    phone_number = models.CharField(max_length=10, blank=False, null=False)
    address_type = models.CharField(choices=ADDRESS_TYPE_CHOICE, max_length=1, blank=False, null=False)
    is_default = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)


class Category(models.Model):
    category_name = models.CharField(choices=CATEGORY_CHOICE, max_length=2, blank=False, null=False)
    category_image = models.ImageField(upload_to="category_images", blank=True, null=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)


class Product(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    discount_price = models.FloatField()
    sell_price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # product_image = models.ImageField(upload_to="product_images", blank=True, null=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        # data = {"id": self.id, "name": self.name}
        # return str(data)
        return self.name


class ProductAttribute(models.Model):
    attribute_name = models.CharField(max_length=255, blank=True, null=True)
    attribute_value = models.CharField(max_length=255, blank=True, null=True)
    product = models.ForeignKey(Product, related_name='product_attributes', blank=True, null=True,
                                on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)


class ProductImage(models.Model):
    product_image = models.ImageField(upload_to="product_images", blank=True, null=True, default="")
    product = models.ForeignKey(Product, related_name='product_images', blank=True, null=True,
                                on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)


class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    order_status = models.CharField(choices=ORDER_STATUS_CHOICE, max_length=50, default="Pending")
    payment_mode = models.CharField(choices=PAYMENT_MODE_CHOICE, max_length=10)
    transaction_id = models.CharField(max_length=255, default="", blank=True, null=True)
    is_returned = models.BooleanField(default=False)
    is_delivered = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)


class ReturnedOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    is_refunded = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)


# class ProductAttributeBase(models.Model):
#     attribute_name = models.CharField(max_length=255)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     is_active = models.BooleanField(default=False)
#
#     def __str__(self):
#         return str(self.id)


# class ProductAttribute(Attribute):
#     product = models.ForeignKey(Product, related_name='attributes', blank=True, null=True, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return str(self.id)
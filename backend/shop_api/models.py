from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.template.defaultfilters import slugify


class Delivery(models.TextChoices):
    PREPARING = 'preparing'
    ON_ROUTE = 'on_route'
    DELIVERED = 'delivered'


class Size(models.TextChoices):
    EXTRA_SMALL = 'XS'
    SMALL = 'S'
    MEDIUM = 'M'
    LARGE = 'L'
    EXTRA_LARGE = 'XL'


class Addresschoices(models.TextChoices):
    SHIPPING_ADDRESS = 'S'
    BILLING_ADDRESS = 'B'


class User(AbstractUser):
    phone_number = PhoneNumberField(max_length=11)
    email_address = models.EmailField()
    stripe_customer_id = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    home_number = models.CharField(max_length=5)
    street = models.CharField(max_length=20)
    area = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    post_code = models.CharField(max_length=10)
    country = models.CharField(max_length=20)
    address_type = models.CharField(
        max_length=1, choices=Addresschoices.choices)
    default_address = models.BooleanField(default=False)

    def __str__(self):
        return '%s %s %s %s %s %s' % (self.home_number, self.street, self.area, self.city, self.post_code, self.country)

    class Meta:
        verbose_name_plural = 'Addresses'


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='images')
    description = models.TextField()
    shirt_size = models.CharField(
        max_length=2, choices=Size.choices, default=Size.MEDIUM)
    hat_size = models.CharField(
        max_length=2, choices=Size.choices, default=Size.MEDIUM)
    trouser_size = models.CharField(
        max_length=2, choices=Size.choices, default=Size.MEDIUM)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)


    def __str__(self):
        return '%s %s' % (self.name, self.price)


class OrderedProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField(default=1)

    def __str__(self):
        return '%s of %s' % (self.amount, self.Product.name)

    def total_product_price(self):
        return self.amount * self.Product.price


class Payments(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True)
    amount = models.FloatField()
    time_stamp = models.DateTimeField(auto_now_add=True)
    stripe_api_charge = models.CharField(max_length=50)

    def __str__(self):
        return self.User.username

    class Meta:
        verbose_name_plural = 'Payments'


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(OrderedProduct)
    reference_code = models.CharField(max_length=50, blank=True, null=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    status = models.CharField(
        max_length=9, choices=Delivery.choices, default=Delivery.PREPARING)
    payment = models.ForeignKey(Payments, on_delete=models.CASCADE)
    returns_requested = models.BooleanField(default=False)
    returns_granted = models.BooleanField(default=False)
    shipping_address = models.ForeignKey(Address, related_name="shipping_address", on_delete=models.SET_NULL, blank=True, null=True)
    billing_address = models.ForeignKey(Address, related_name="billing_address", on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.reference_code

    def total_order_amount(self):
        total = 0
        return [total := total + i for i in self.products.all()][-1]


class Returns(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    reason_return = models.TextField()
    email = models.EmailField(max_length=254)
    
    def __str__(self):
        return "%s" % (self.pk)
    
    class Meta:
        verbose_name_plural = 'Returns'

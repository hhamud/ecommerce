from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
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


class Catagory(models.TextChoices):
    HATS = 'hats'
    TROUSERS = 'trousers'
    SHIRTS = 'shirts'
    SHOES = 'shoes'


class Colour(models.TextChoices):
    BLACK = 'black'
    WHITE = 'white'
    BLUE = 'blue'
    YELLOW = 'yellow'


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None
    phone_number = PhoneNumberField(max_length=11, null=True, blank=True)
    email = models.EmailField(unique=True)
    stripe_customer_id = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password', ]

    objects = UserManager()

    def __str__(self):
        return self.email


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='address')
    home_number = models.CharField(max_length=5,  null=True, blank=True)
    street = models.CharField(max_length=20,  null=True, blank=True)
    area = models.CharField(max_length=20,  null=True, blank=True)
    city = models.CharField(max_length=20,  null=True, blank=True)
    post_code = models.CharField(max_length=10,  null=True, blank=True)
    country = models.CharField(max_length=20,  null=True, blank=True)
    address_type = models.CharField(
        max_length=1, choices=Addresschoices.choices,  null=True, blank=True)
    default_address = models.BooleanField(default=False)

    def __str__(self):
        return '%s, %s, %s, %s, %s, %s' % (self.home_number, self.street, self.area, self.city, self.post_code, self.country)

    class Meta:
        verbose_name_plural = 'Addresses'


class ProductVariant(models.Model):
    cloth_type = models.CharField(
        max_length=8, choices=Catagory.choices, default=Catagory.SHIRTS)
    cloth_size = models.CharField(
        max_length=2, choices=Size.choices, null=True, blank=True)
    shoe_size = models.IntegerField(choices=[
        (x, x) for x in range(0, 13)],  null=True, blank=True)
    colours = models.CharField(
        max_length=8, choices=Colour.choices, default=Colour.WHITE)
    inventory = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return "%s %s %s %s %s" % (self.cloth_type, self.colours, self.inventory, self.shoe_size, self.cloth_size)


class Product(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images')
    slug = models.SlugField(unique=True)
    description = models.TextField()
    variant = models.ManyToManyField(ProductVariant)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class OrderedProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField(default=1)

    def __str__(self):
        return '%s of %s' % (self.amount, self.Product.name)

    def total_product_price(self):
        return self.amount * self.Product.price

    def inventory_update(self):
        return self.Product.inventory - self.amount


class Payments(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True, related_name='payment')
    amount = models.FloatField( null=True, blank=True)
    time_stamp = models.DateTimeField(auto_now_add=True,  null=True, blank=True)
    stripe_api_charge = models.CharField(max_length=50,  null=True, blank=True)

    def __str__(self):
        return self.stripe_api_charge

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
    shipping_address = models.ForeignKey(
        Address, related_name="shipping_address", on_delete=models.SET_NULL, blank=True, null=True)
    billing_address = models.ForeignKey(
        Address, related_name="billing_address", on_delete=models.SET_NULL, blank=True, null=True)

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

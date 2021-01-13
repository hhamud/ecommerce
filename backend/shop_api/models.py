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
    phone_number = PhoneNumberField(max_length=11)
    email = models.EmailField(unique=True)
    stripe_customer_id = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email


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
        return '%s, %s, %s, %s, %s, %s' % (self.home_number, self.street, self.area, self.city, self.post_code, self.country)

    class Meta:
        verbose_name_plural = 'Addresses'


class ProductColour(models.Model):
    colours = models.CharField(
        max_length=8, choices=Colour.choices, default=Colour.WHITE)
    inventory = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return '%s %s' % (self.colours, self.inventory)


class ProductVariant(models.Model):
    cloth_type = models.CharField(
        max_length=8, choices=Catagory.choices, default=Catagory.SHIRTS)
    shirt_size = models.CharField(
        max_length=2, choices=Size.choices, default=Size.MEDIUM)
    hat_size = models.CharField(
        max_length=2, choices=Size.choices, default=Size.MEDIUM)
    trouser_size = models.CharField(
        max_length=2, choices=Size.choices, default=Size.MEDIUM)
    colour = models.ManyToManyField(ProductColour)

   

    def __str__(self):
        if self.cloth_type == 'hats':
            return '%s ' % (self.hat_size)
        elif self.cloth_type == 'shirts':
            return '%s ' % (self.shirt_size)
        elif self.cloth_type == 'trousers':
            return '%s ' % (self.trouser_size)


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

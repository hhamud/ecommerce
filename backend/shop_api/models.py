from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=11)
    email_address = models.EmailField()
 

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

    def __str__(self):
        return '%s %s %s %s %s %s' % (self.home_number, self.street, self.area, self.city, self.post_code, self.country)


class Size(models.TextChoices):
    EXTRA_SMALL = 'XS'
    SMALL = 'S'
    MEDIUM = 'M'
    LARGE = 'L'
    EXTRA_LARGE = 'XL'


class Catagory(models.TextChoices):
    SHOE = 'shoe'
    SHIRT = 'shirt'
    TROUSER = 'trouser'
    HAT = 'HAT'


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='images')
    description = models.TextField()
    shirt_size = models.CharField(
        max_length=2, choices=Size.choices, default=Size.MEDIUM)
    shoe_size = models.CharField(
        max_length=1, choices=[(x, x) for x in range(1, 13)], default=2)
    cloth_type = models.CharField(max_length=10, choices=Catagory.choices)

    def __str__(self):
        return '%s %s' % (self.name, self.price)

from django.db import models


class Size(models.Textchoices):
    EXTRA_SMALL = 'XS'
    SMALL = 'S'
    MEDIUM = 'M'
    LARGE = 'L'
    EXTRA_LARGE = 'XL'

class Catagory(models.Textchoices):
    SHOE = 'shoe'
    SHIRT = 'shirt'
    TROUSER = 'trouser'
    HAT = 'HAT'
    
class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(uploaded_to='images')
    description = models.TextField()
    shirt_size = models.CharField(
        max_length=2, choices=Size.choices, default=Size.MEDIUM)
    shoe_size = models.CharField(
        max_length=1, choices=[x for x in range(1,13)], default=2)
    cloth_type = models.CharField(max_length=10, choices=Catagory.choices)
    def __str__(self):
        return self.name

class User(models.Model):

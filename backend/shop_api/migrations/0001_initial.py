# Generated by Django 3.1.5 on 2021-01-14 22:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import phonenumber_field.modelfields
import shop_api.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=11, region=None)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('stripe_customer_id', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', shop_api.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home_number', models.CharField(max_length=5)),
                ('street', models.CharField(max_length=20)),
                ('area', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('post_code', models.CharField(max_length=10)),
                ('country', models.CharField(max_length=20)),
                ('address_type', models.CharField(choices=[('S', 'Shipping Address'), ('B', 'Billing Address')], max_length=1)),
                ('default_address', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Addresses',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference_code', models.CharField(blank=True, max_length=50, null=True)),
                ('ordered_date', models.DateTimeField()),
                ('ordered', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('preparing', 'Preparing'), ('on_route', 'On Route'), ('delivered', 'Delivered')], default='preparing', max_length=9)),
                ('returns_requested', models.BooleanField(default=False)),
                ('returns_granted', models.BooleanField(default=False)),
                ('billing_address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='billing_address', to='shop_api.address')),
            ],
        ),
        migrations.CreateModel(
            name='ProductColour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('colours', models.CharField(choices=[('black', 'Black'), ('white', 'White'), ('blue', 'Blue'), ('yellow', 'Yellow')], default='white', max_length=8)),
                ('inventory', models.IntegerField(default=1)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
        migrations.CreateModel(
            name='Returns',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason_return', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop_api.order')),
            ],
            options={
                'verbose_name_plural': 'Returns',
            },
        ),
        migrations.CreateModel(
            name='ProductVariant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cloth_type', models.CharField(choices=[('hats', 'Hats'), ('trousers', 'Trousers'), ('shirts', 'Shirts'), ('shoes', 'Shoes')], default='shirts', max_length=8)),
                ('cloth_size', models.CharField(choices=[('XS', 'Extra Small'), ('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'Extra Large')], default='M', max_length=2)),
                ('shoe_size', models.CharField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12)], default=1, max_length=5)),
                ('colour', models.ManyToManyField(to='shop_api.ProductColour')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='images')),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField()),
                ('variant', models.ManyToManyField(to='shop_api.ProductVariant')),
            ],
        ),
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
                ('stripe_api_charge', models.CharField(max_length=50)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Payments',
            },
        ),
        migrations.CreateModel(
            name='OrderedProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered', models.BooleanField(default=False)),
                ('amount', models.IntegerField(default=1)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop_api.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='payment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop_api.payments'),
        ),
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(to='shop_api.OrderedProduct'),
        ),
        migrations.AddField(
            model_name='order',
            name='shipping_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='shipping_address', to='shop_api.address'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

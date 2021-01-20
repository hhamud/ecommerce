# Generated by Django 3.1.5 on 2021-01-15 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_api', '0004_auto_20210114_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productvariant',
            name='cloth_size',
            field=models.CharField(blank=True, choices=[('XS', 'Extra Small'), ('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'Extra Large')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='productvariant',
            name='shoe_size',
            field=models.IntegerField(blank=True, choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12)], null=True),
        ),
    ]

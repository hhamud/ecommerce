# Generated by Django 3.1.5 on 2021-01-05 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_api', '0004_auto_20210105_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='cloth_type',
            field=models.CharField(choices=[('hats', 'Hat'), ('trousers', 'Trousers'), ('shirts', 'Shirts')], default='shirts', max_length=8),
        ),
    ]

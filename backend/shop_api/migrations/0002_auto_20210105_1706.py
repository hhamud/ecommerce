# Generated by Django 3.1.5 on 2021-01-05 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name_plural': 'Addresses'},
        ),
        migrations.AlterModelOptions(
            name='payments',
            options={'verbose_name_plural': 'Payments'},
        ),
        migrations.AlterModelOptions(
            name='returns',
            options={'verbose_name_plural': 'Returns'},
        ),
    ]
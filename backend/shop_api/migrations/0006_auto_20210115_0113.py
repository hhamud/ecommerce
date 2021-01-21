# Generated by Django 3.1.5 on 2021-01-15 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_api', '0005_auto_20210115_0012'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productvariant',
            name='colour',
        ),
        migrations.AddField(
            model_name='productvariant',
            name='colours',
            field=models.CharField(choices=[('black', 'Black'), ('white', 'White'), ('blue', 'Blue'), ('yellow', 'Yellow')], default='white', max_length=8),
        ),
        migrations.AddField(
            model_name='productvariant',
            name='inventory',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='productvariant',
            name='price',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=8),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='ProductColour',
        ),
    ]
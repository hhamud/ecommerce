# Generated by Django 3.1.5 on 2021-01-12 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductVariant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cloth_type', models.CharField(choices=[('hats', 'Hats'), ('trousers', 'Trousers'), ('shirts', 'Shirts')], default='shirts', max_length=8)),
                ('shirt_size', models.CharField(choices=[('XS', 'Extra Small'), ('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'Extra Large')], default='M', max_length=2)),
                ('hat_size', models.CharField(choices=[('XS', 'Extra Small'), ('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'Extra Large')], default='M', max_length=2)),
                ('trouser_size', models.CharField(choices=[('XS', 'Extra Small'), ('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'Extra Large')], default='M', max_length=2)),
                ('inventory', models.IntegerField(default=1)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('colours', models.ManyToManyField(to='shop_api.ProductColour')),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='colours',
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default=1, unique=True),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='ProductSize',
        ),
        migrations.AlterField(
            model_name='product',
            name='sizes',
            field=models.ManyToManyField(to='shop_api.ProductVariant'),
        ),
    ]
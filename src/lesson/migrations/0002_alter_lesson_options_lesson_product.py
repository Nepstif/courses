# Generated by Django 4.0.10 on 2023-09-23 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_product_options_product_user'),
        ('lesson', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lesson',
            options={'ordering': ['name'], 'verbose_name': 'Продукт', 'verbose_name_plural': 'Продукты'},
        ),
        migrations.AddField(
            model_name='lesson',
            name='product',
            field=models.ManyToManyField(related_name='products', to='product.product'),
        ),
    ]
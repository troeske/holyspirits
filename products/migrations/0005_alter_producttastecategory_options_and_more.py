# Generated by Django 5.1.2 on 2024-10-23 19:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_bottler_description_alter_bottler_link_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='producttastecategory',
            options={'verbose_name_plural': 'Product Taste Categories'},
        ),
        migrations.AlterField(
            model_name='productimage',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_image', to='products.product'),
        ),
    ]

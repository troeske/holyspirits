# Generated by Django 5.1.2 on 2024-10-24 05:07

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_producttastecategory_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='list_image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
    ]

# Generated by Django 5.1.2 on 2024-10-24 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_currency_alter_product_product_category_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='currency',
        ),
        migrations.DeleteModel(
            name='Currency',
        ),
    ]
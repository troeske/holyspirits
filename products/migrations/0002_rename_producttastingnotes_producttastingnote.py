# Generated by Django 5.1.2 on 2024-10-23 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProductTastingNotes',
            new_name='ProductTastingNote',
        ),
    ]
# Generated by Django 4.0.7 on 2022-11-25 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_product_product_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_picture',
        ),
    ]
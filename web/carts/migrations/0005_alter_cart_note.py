# Generated by Django 4.0.7 on 2023-01-28 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0004_cart_merchant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='note',
            field=models.TextField(blank=True, default=None),
        ),
    ]
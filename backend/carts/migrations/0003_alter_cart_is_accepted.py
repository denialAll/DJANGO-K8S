# Generated by Django 4.0.7 on 2022-12-04 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0002_alter_cart_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='is_accepted',
            field=models.BooleanField(default=None, null=True),
        ),
    ]

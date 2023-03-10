# Generated by Django 4.0.9 on 2023-02-20 05:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('merchantinfo', '0010_alter_merchantinfo_display_picture'),
        ('carts', '0008_cart_merchant_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='merchant_info',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='merchant_info', to='merchantinfo.merchantinfo'),
        ),
    ]

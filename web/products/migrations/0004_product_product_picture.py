# Generated by Django 4.0.7 on 2022-11-19 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_rename_serving_product_servings'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_picture',
            field=models.ImageField(blank=True, upload_to='product_picture'),
        ),
    ]

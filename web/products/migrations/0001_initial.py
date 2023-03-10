# Generated by Django 4.0.7 on 2022-11-06 14:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(default='Desi', max_length=120)),
                ('title', models.CharField(default='', max_length=200)),
                ('description', models.CharField(default='', max_length=200)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('is_available', models.BooleanField(default=True)),
                ('serving', models.IntegerField(default=0)),
                ('merchant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

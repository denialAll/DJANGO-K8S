from django.db import models

# Create your models here.

class Product(models.Model):
    merchant = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    category = models.CharField(max_length=120, default="Miscellaneous")
    category_order = models.IntegerField(default=1) # this paired with the category how it should be displayed in the frondend
    title = models.CharField(max_length=200, default="")
    description = models.CharField(max_length=200, default="")
    price = models.DecimalField(max_digits=6,decimal_places=2, default=0)
    is_available = models.BooleanField(default=True)
    servings = models.IntegerField(default=0)
    product_picture = models.ImageField(upload_to="product_picture", blank=True, null=True)


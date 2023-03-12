from django.db import models

# Create your models here.

class MerchantInfo(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=155) # name of the restaurant
    phone_number = models.CharField(max_length=11)
    display_picture = models.ImageField(upload_to="display_picture", blank=True, null=True)
    is_open = models.BooleanField(default=False) # whether the restaurant is open or closed by the restaurant owner
    is_verified = models.BooleanField(default=False) # will be set by the verification team
    delivery_charges = models.DecimalField(default=0.0, max_digits=5, decimal_places=1)
    delivery_free_cutoff = models.DecimalField(default=1000000, max_digits=12, decimal_places=1)
    min_order = models.DecimalField(default=0.0, max_digits=5, decimal_places=1)
    delivery_radius = models.DecimalField(default=0.0, max_digits=3, decimal_places=1)
    

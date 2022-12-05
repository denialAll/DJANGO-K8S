from django.db import models

# Create your models here.

class MerchantInfo(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=155) # name of the restaurant
    phone_number = models.CharField(max_length=11)
    display_picture = models.ImageField(upload_to="display_picture", blank=True)
    is_open = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False) # will be set by the verification team
    

from django.db import models

# Create your models here.

class Address(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    city = models.CharField(max_length=255)
    address = models.TextField()
    longitude = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    latitude = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    isMerchant = models.BooleanField(default=False)
    isCustomer = models.BooleanField(default=False)





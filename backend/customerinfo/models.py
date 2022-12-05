from django.db import models
from addresses import Address 

# Create your models here.

class CustomerInfo(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=11)
    current_address = models.ForeignKey(Address, on_delete=models.CASCADE)
    
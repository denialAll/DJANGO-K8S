from django.db import models
from useraddresses.models import Address
from merchantinfo.models import MerchantInfo

# Create your models here.

class Cart(models.Model):
    customer = models.ForeignKey('auth.User', related_name='cart_owner', on_delete=models.CASCADE, null = True)
    merchant = models.ForeignKey('auth.User', related_name='cart_merchant', on_delete=models.CASCADE, null = True)
    merchant_info = models.ForeignKey(MerchantInfo, related_name='merchant_info', on_delete=models.CASCADE, null = True, blank = True)
    address = models.ForeignKey(Address, related_name='cart_address',on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=11)
    created = models.DateTimeField(db_index=True, auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    note = models.TextField(default=None, blank = True)
    is_accepted = models.BooleanField(default=None, null = True)
    is_sent = models.BooleanField(default=False)
    is_rated = models.BooleanField(default=False)
    delivery_cost = models.DecimalField(max_digits=5, decimal_places=1, null=True, blank = True, default=0.0)
    total_price = models.DecimalField(max_digits=8, decimal_places=1, null=True, blank = True, default=0.0)

    
    # @property
    # def total_price(self):
    #     total_price = 0
    #     for item in self.cart_item:
    #         total_price += item.total_price
    #     return "%.1f" %(total_price)

 
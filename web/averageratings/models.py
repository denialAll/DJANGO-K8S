from django.db import models
from carts.models import Cart

# Create your models here.

class AverageRating(models.Model):
    merchant = models.OneToOneField("auth.User", on_delete=models.CASCADE, null = True, blank = True, related_name="merchant_user_id")
    customer = models.ForeignKey("auth.User", blank = True, null = True, on_delete=models.CASCADE, related_name="customer_user_id")
    taste = models.DecimalField(max_digits=3, decimal_places=1)
    speed = models.DecimalField(max_digits=3, decimal_places=1)
    service = models.DecimalField(max_digits=3, decimal_places=1)
    orders = models.IntegerField()

    @property
    def avg_rating(self):
        return ( self.taste + self.speed + self.service )/ 3
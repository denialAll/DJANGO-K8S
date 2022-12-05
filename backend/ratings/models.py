from django.db import models
from carts.models import Cart

# Create your models here.

class Rating(models.Model):
    cart = models.ForeignKey(Cart, related_name='cart-rating')
    taste = models.DecimalField(max_digits=3, decimal_places=1)
    speed = models.DecimalField(max_digits=3, decimal_places=1)
    service = models.DecimalField(max_digits=3, decimal_places=1)
    comment = models.TextField(null=True)

    @property
    def avg_rating(self):
        return ( self.taste + self.speed + self.service )/ 3
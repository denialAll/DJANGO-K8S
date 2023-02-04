from django.db import models
from carts.models import Cart

# Create your models here.

class AverageRating(models.Model):
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE)
    taste = models.DecimalField(max_digits=3, decimal_places=1)
    speed = models.DecimalField(max_digits=3, decimal_places=1)
    service = models.DecimalField(max_digits=3, decimal_places=1)
    orders = models.IntegerField()

    @property
    def avg_rating(self):
        return ( self.taste + self.speed + self.service )/ 3
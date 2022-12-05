from django.db import models
from products.models import Product
from carts.models import Cart

# Create your models here.

class CartItem(models.Model):
    product = models.ForeignKey(
        Product, related_name='cart_product', on_delete=models.CASCADE
    )
    quantity = models.IntegerField(default=1)
    cart = models.ForeignKey(Cart, related_name='cartitem_cart', on_delete=models.CASCADE, null=True)
    
    @property
    def total_price(self):
        return "%.1f" %(self.product.price * self.quantity)
   

    def __repr__(self):
        return f'owner={self.owner}, product_title={self.Product.title}, created={self.created}'

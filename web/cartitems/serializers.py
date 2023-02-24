from rest_framework import serializers
from .models import CartItem


class CartItemSerializer(serializers.ModelSerializer):
    title = serializers.ReadOnlyField(source='product.title')
    price = serializers.ReadOnlyField(source='product.price')
    merchant = serializers.ReadOnlyField(source='product.merchant.username')
    merchant_id = serializers.ReadOnlyField(source='product.merchant.id')
    customer = serializers.ReadOnlyField(source='cart.customer.id')
    first_name = serializers.ReadOnlyField(source='cart.customer.first_name')
    last_name = serializers.ReadOnlyField(source='cart.customer.last_name')
    address = serializers.ReadOnlyField(source='cart.address.id')
    address_name = serializers.ReadOnlyField(source='cart.address.address')
    latitude = serializers.ReadOnlyField(source='cart.address.latitude')
    longitude = serializers.ReadOnlyField(source='cart.address.longitude')
    phone_number = serializers.ReadOnlyField(source='cart.phone_number')
    created = serializers.ReadOnlyField(source='cart.created')
    modified =  serializers.ReadOnlyField(source='cart.modified')
    note = serializers.ReadOnlyField(source='cart.note')
    is_accepted = serializers.ReadOnlyField(source='cart.is_accepted')
    is_sent = serializers.ReadOnlyField(source='cart.is_sent')
    is_rated = serializers.ReadOnlyField(source='cart.is_rated')
    restaurant_name = serializers.ReadOnlyField(source='cart.merchant_info.name')
    restaurant_phone = serializers.ReadOnlyField(source='cart.merchant_info.phone_number')
    delivery_cost = serializers.ReadOnlyField(source='cart.delivery_cost')
    total_price = serializers.ReadOnlyField(source='cart.total_price') # calculated when the order was created
    


    class Meta:
        model = CartItem
        fields = '__all__'
        
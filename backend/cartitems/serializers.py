from rest_framework import serializers
from .models import CartItem


class CartItemSerializer(serializers.ModelSerializer):
    title = serializers.ReadOnlyField(source='product.title')
    price = serializers.ReadOnlyField(source='product.price')
    merchant = serializers.ReadOnlyField(source='product.merchant.username')
    first_name = serializers.ReadOnlyField(source='cart.customer.first_name')
    last_name = serializers.ReadOnlyField(source='cart.customer.last_name')
    address = serializers.ReadOnlyField(source='cart.address.id')
    phone_number = serializers.ReadOnlyField(source='cart.phone_number')
    created = serializers.ReadOnlyField(source='cart.created')
    modified =  serializers.ReadOnlyField(source='cart.modified')
    note = serializers.ReadOnlyField(source='cart.note')
    is_accepted = serializers.ReadOnlyField(source='cart.is_accepted')
    is_sent = serializers.ReadOnlyField(source='cart.is_sent')


    class Meta:
        model = CartItem
        fields = '__all__'
        
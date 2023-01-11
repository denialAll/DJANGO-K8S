from rest_framework import serializers
from .models import Cart


class CartSerializer(serializers.ModelSerializer):
    first_name = serializers.ReadOnlyField(source='customer.first_name')
    last_name = serializers.ReadOnlyField(source='customer.last_name')
    class Meta:
        model = Cart
        fields = '__all__'
        
    
    
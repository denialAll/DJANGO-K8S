from rest_framework import serializers
from .models import Rating


class RatingSerializer(serializers.ModelSerializer):
    customer = serializers.ReadOnlyField(source = 'cart.customer.id')
    merchant = serializers.ReadOnlyField(source = 'cart.merchant.id')
    class Meta:
        model = Rating
        fields = '__all__'
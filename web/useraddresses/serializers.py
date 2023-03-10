from rest_framework import serializers
from .models import Address

class AddressSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="auth.User")

    class Meta:
        model = Address
        fields = '__all__'




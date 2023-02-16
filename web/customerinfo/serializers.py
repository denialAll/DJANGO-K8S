from rest_framework import serializers
from .models import CustomerInfo


class CustomerInfoSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')
    first_name = serializers.ReadOnlyField(source='user.first_name')
    last_name = serializers.ReadOnlyField(source='user.last_name')
   
    class Meta:
        model = CustomerInfo
        fields = '__all__'
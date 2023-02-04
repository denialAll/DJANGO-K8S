from rest_framework import serializers
from .models import MerchantInfo

class MerchantInfoSerializer(serializers.ModelSerializer):
    display_picture = serializers.ImageField()
    first_name = serializers.ReadOnlyField(source = 'user.first_name')
    last_name = serializers.ReadOnlyField(source = 'user.last_name')

    class Meta:
        model = MerchantInfo
        fields = '__all__'
from rest_framework import serializers
from .models import MerchantInfo

class MerchantInfoSerializer(serializers.ModelSerializer):
    display_picture = serializers.ImageField()

    class Meta:
        model = MerchantInfo
        fields = '__all__'
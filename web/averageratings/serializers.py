from rest_framework import serializers
from .models import AverageRating

class AverageRatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = AverageRating
        fields = '__all__'
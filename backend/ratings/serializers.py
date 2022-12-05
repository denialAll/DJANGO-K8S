from rest_framework import serializers


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
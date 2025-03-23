from rest_framework import serializers
from .models import aboutUS

class aboutUSSerializer(serializers.ModelSerializer):
    class Meta:
        model = aboutUS
        fields = '__all__'

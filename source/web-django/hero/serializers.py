from rest_framework import serializers
from .models import hero

class heroSerializer(serializers.ModelSerializer):
    class Meta:
        model = hero
        fields = '__all__'

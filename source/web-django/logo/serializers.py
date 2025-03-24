from rest_framework import serializers
from .models import logo

class logoSerializer(serializers.ModelSerializer):
    class Meta:
        model = logo
        fields = '__all__'

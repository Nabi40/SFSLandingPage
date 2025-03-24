from rest_framework import serializers
from .models import aboutUss

class aboutUssSerializer(serializers.ModelSerializer):
    class Meta:
        model = aboutUss
        fields = '__all__'

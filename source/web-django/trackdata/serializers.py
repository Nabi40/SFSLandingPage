from rest_framework import serializers
from .models import Reference, AnotherModel

class ReferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reference
        fields = ['id', 'source', 'specifics']
        read_only_fields = ['id']  # since it's auto-generated


class AnotherModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnotherModel
        fields = '__all__'  # or specify fields explicitly like ['id', 'name'] if needed

from rest_framework import serializers

class VisitTrackSerializer(serializers.Serializer):
    ref = serializers.CharField(max_length=16)

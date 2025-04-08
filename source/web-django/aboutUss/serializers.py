from rest_framework import serializers
from .models import aboutUss, SlideImage, MissionVision, Value, ValueDetail, ExecutiveTeam


class SlideImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SlideImage
        fields = '__all__'


class aboutUssSerializer(serializers.ModelSerializer):
    slide_images = SlideImageSerializer(many=True, read_only=True)

    class Meta:
        model = aboutUss
        fields = '__all__'


class MissionVisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MissionVision
        fields = '__all__'


class ValueDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ValueDetail
        fields = '__all__'


class ValueSerializer(serializers.ModelSerializer):
    value_details = ValueDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Value
        fields = ('value_description', 'value_details')

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        # Reorder the dict so "value_description" comes first
        reordered = {
            'value_description': rep['value_description'],
            'value_details': rep['value_details'],
        }
        return reordered



class ExecutiveTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExecutiveTeam
        fields = '__all__'

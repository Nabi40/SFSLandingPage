from rest_framework import serializers
from .models import aboutUss, SlideImage, MissionVision, Value, ExecutiveTeam

class SlideImageSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = SlideImage
        fields = ["id", "image", "image_url"]

    def get_image_url(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.image.url) if obj.image else None


class MissionVisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MissionVision
        fields = ["our_mission", "our_vision"]


class ValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Value
        fields = ["id", "title", "description"]


class ExecutiveTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExecutiveTeam
        fields = ["id", "name", "position"]


class aboutUssSerializer(serializers.ModelSerializer):  
    banner = serializers.SerializerMethodField()
    mission = MissionVisionSerializer(many=True)  # Use the exact related_name
    values = ValueSerializer(many=True)  
    executive_team = ExecutiveTeamSerializer(many=True)

    class Meta:
        model = aboutUss
        fields = ["id", "banner", "mission", "values", "executive_team"]

    def get_banner(self, obj):
        return {
            "description": obj.about_description,
            "slide_images": SlideImageSerializer(obj.slide_images.all(), many=True, context=self.context).data
        }

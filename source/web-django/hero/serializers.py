from rest_framework import serializers
from .models import hero, SlideImage, SlideLogos, StableLogos, OurService, WorkDescription, CustomerReview, FAQ

class SlideImageSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = SlideImage
        fields = ["id", "slide_image", "image_url"]

    def get_image_url(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.slide_image.url) if obj.slide_image else None


class SlideLogosSerializer(serializers.ModelSerializer):
    slide_logo_url = serializers.SerializerMethodField()

    class Meta:
        model = SlideLogos
        fields = ["id", "slide_logo", "slide_logo_url"]

    def get_slide_logo_url(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.slide_logo.url) if obj.slide_logo else None


class StableLogosSerializer(serializers.ModelSerializer):
    stable_logo_url = serializers.SerializerMethodField()

    class Meta:
        model = StableLogos
        fields = ["id", "hero_title", "stable_logo", "sort_title", "sort_description", "stable_logo_url"]

    def get_stable_logo_url(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.stable_logo.url) if obj.stable_logo else None


class OurServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurService
        fields = ["id", "ourservice_description", "service_logo", "title", "description"]


class WorkDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkDescription
        fields = ["id", "work_description", "work_logo", "title", "description"]


class CustomerReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerReview
        fields = ["id", "name", "customer_images", "description", "rating"]



class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ["id", "question", "answer"]


class heroSerializer(serializers.ModelSerializer):
    slide_logos = SlideLogosSerializer(many=True, read_only=True)
    stable_logos = StableLogosSerializer(many=True, read_only=True)
    our_service = OurServiceSerializer(many=True, read_only=True)
    work_description = WorkDescriptionSerializer(many=True, read_only=True)
    customer_review = CustomerReviewSerializer(many=True, read_only=True)
    faq = FAQSerializer(many=True, read_only=True)

    class Meta:
        model = hero
        fields = "__all__"






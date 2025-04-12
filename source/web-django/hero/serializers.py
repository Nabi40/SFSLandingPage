from rest_framework import serializers
from .models import (hero, Logos, SlideLogo, OurService,
                      WorkDescription, CustomerReview, FAQ, Service,
                     Inquiry, Office, Subscribe
)

class heroSerializer(serializers.ModelSerializer):
    class Meta:
        model = hero
        fields = "__all__"

class SlideLogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SlideLogo
        fields = "__all__"

class LogosSerializer(serializers.ModelSerializer):
    slide_logos = SlideLogoSerializer(many=True, read_only=True)  # Read-only nested list

    class Meta:
        model = Logos
        fields = "__all__"


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"


class OurServiceSerializer(serializers.ModelSerializer):
    service = ServiceSerializer(many=True, read_only=True)
    class Meta:
        model = OurService
        fields = "__all__"

class WorkDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkDescription
        fields = "__all__"

class CustomerReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerReview
        fields = "__all__"

class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = "__all__"


class InquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inquiry
        fields = '__all__'


class OfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Office
        fields = '__all__'


class SubscribeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscribe
        fields = '__all__'


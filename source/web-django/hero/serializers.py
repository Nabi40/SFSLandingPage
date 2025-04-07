from rest_framework import serializers
from .models import hero, SlideImage, Logos, SlideLogo, OurService, WorkDescription, CustomerReview, FAQ, Service

class SlideImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SlideImage
        fields = "__all__"

class heroSerializer(serializers.ModelSerializer):
    slide_images = SlideImageSerializer(many=True, read_only=True)

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




























# from rest_framework import serializers
# from .models import hero, Logos, OurService, WorkDescription, CustomerReview, FAQ, SlideImage, slide_logo


# # serializers.py
# class SlideImageSerializer(serializers.ModelSerializer):
#     image_url = serializers.SerializerMethodField()

#     class Meta:
#         model = SlideImage
#         fields = ['id', 'image', 'image_url', 'hero']


#     def get_image_url(self, obj):
#         request = self.context.get('request')
#         return request.build_absolute_uri(obj.image.url) if obj.image else None

# class heroSerializer(serializers.ModelSerializer):
#     slide_images = SlideImageSerializer(many=True, required=False)

#     class Meta:
#         model = hero
#         fields = ["id", "cover_image", "hero_title", "hero_description", "slide_images"]

#     def create(self, validated_data):
#         slide_images_data = self.initial_data.getlist('slide_images')  # from request.FILES
#         hero_instance = hero.objects.create(
#             cover_image=validated_data.get('cover_image'),
#             hero_title=validated_data.get('hero_title'),
#             hero_description=validated_data.get('hero_description')
#         )

#         for image in slide_images_data:
#             slide_instance = SlideImage.objects.create(image=image)
#             hero_instance.slide_images.add(slide_instance)

#         return hero_instance



# class slide_logoSerializer(serializers.ModelSerializer):
#     logo_url = serializers.SerializerMethodField()

#     class Meta:
#         model = slide_logo
#         fields = ['id', 'logo', 'logo_url', 'hero']


#     def get_logo_url(self, obj):
#         request = self.context.get('request')
#         return request.build_absolute_uri(obj.logo.url) if obj.logo else None



# class LogosSerializer(serializers.ModelSerializer):
#     slide_logo_url = serializers.SerializerMethodField()
#     stable_logo_url = serializers.SerializerMethodField()

#     class Meta:
#         model = Logos
#         fields = ["id", "slide_logo", "slide_logo_url", "stable_logo", "stable_logo_url", "sort_title", "sort_description"]

#     def get_slide_logo_url(self, obj):
#         request = self.context.get('request')
#         return request.build_absolute_uri(obj.slide_logo.url) if obj.slide_logo else None

#     def get_stable_logo_url(self, obj):
#         request = self.context.get('request')
#         return request.build_absolute_uri(obj.stable_logo.url) if obj.stable_logo else None


# class OurServiceSerializer(serializers.ModelSerializer):
#     service_logo_url = serializers.SerializerMethodField()

#     class Meta:
#         model = OurService
#         fields = ["id", "ourservice_description", "service_logo", "service_logo_url", "title", "description"]

#     def get_service_logo_url(self, obj):
#         request = self.context.get('request')
#         return request.build_absolute_uri(obj.service_logo.url) if obj.service_logo else None


# class WorkDescriptionSerializer(serializers.ModelSerializer):
#     work_logo_url = serializers.SerializerMethodField()

#     class Meta:
#         model = WorkDescription
#         fields = ["id", "work_description", "work_logo", "work_logo_url", "title", "description"]

#     def get_work_logo_url(self, obj):
#         request = self.context.get('request')
#         return request.build_absolute_uri(obj.work_logo.url) if obj.work_logo else None


# class CustomerReviewSerializer(serializers.ModelSerializer):
#     customer_image_url = serializers.SerializerMethodField()

#     class Meta:
#         model = CustomerReview
#         fields = ["id", "name", "customer_images", "customer_image_url", "description", "rating"]

#     def get_customer_image_url(self, obj):
#         request = self.context.get('request')
#         return request.build_absolute_uri(obj.customer_images.url) if obj.customer_images else None


# class FAQSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = FAQ
#         fields = ["id", "question", "answer"]


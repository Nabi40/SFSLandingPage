from rest_framework import viewsets
from rest_framework.response import Response
from .models import hero, Logos, OurService, WorkDescription, CustomerReview, FAQ, SlideImage, SlideLogo, Service
from .serializers import (
    heroSerializer,
    LogosSerializer,
    OurServiceSerializer,
    WorkDescriptionSerializer,
    CustomerReviewSerializer,
    FAQSerializer,
    SlideImageSerializer,
    SlideLogoSerializer,
    ServiceSerializer
)

class heroViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = hero.objects.all()
    serializer_class = heroSerializer

    def get_object(self):
        return self.queryset.first()

    def list(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

class SlideImageListView(viewsets.ReadOnlyModelViewSet):
    queryset = SlideImage.objects.all()
    serializer_class = SlideImageSerializer

class LogosViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Logos.objects.all()
    serializer_class = LogosSerializer

class SlideLogoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SlideLogo.objects.all()
    serializer_class = SlideLogoSerializer


class ServiceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class OurServiceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = OurService.objects.all()
    serializer_class = OurServiceSerializer

    def get_object(self):
        return self.queryset.first()

    def list(self, request, *args, **kwargs):
        instance = self.get_object()
        response_data = {
            "ourservice_description": instance.ourservice_description,
            "service": ServiceSerializer(instance.service.all(), many=True).data  # Fetch related service objects
        }
        return Response(response_data)


class WorkDescriptionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = WorkDescription.objects.all()
    serializer_class = WorkDescriptionSerializer

class CustomerReviewViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CustomerReview.objects.all()
    serializer_class = CustomerReviewSerializer

class FAQViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

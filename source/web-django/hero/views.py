from rest_framework import viewsets
from rest_framework.response import Response
from .models import (hero, Logos, OurService, WorkDescription,
                      CustomerReview, FAQ, SlideLogo,
                        Service, Inquiry, Office, Subscribe)
from .serializers import (
    heroSerializer,
    LogosSerializer,
    OurServiceSerializer,
    WorkDescriptionSerializer,
    CustomerReviewSerializer,
    FAQSerializer,
    SlideLogoSerializer,
    ServiceSerializer,
    InquirySerializer,
    OfficeSerializer,
    SubscribeSerializer
)

class heroViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = hero.objects.all()
    serializer_class = heroSerializer

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



class InquiryViewSet(viewsets.ModelViewSet):
    queryset = Inquiry.objects.all()
    serializer_class = InquirySerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        inquiry = serializer.save()

        # Send email to office
        send_mail(
            subject="New Inquiry from {}".format(inquiry.full_name),
            message=f"""
            Email: {inquiry.email}
            Name: {inquiry.full_name}
            Company: {inquiry.company_name}
            Phone: {inquiry.phone_number}
            message: {inquiry.message}
            Phone: {inquiry.phone_number}
            """,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=["mahamudun.nabi@smartfieldservice.com"],  # replace with your office mail
            fail_silently=False,
        )

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

class OfficeViewSet(viewsets.ModelViewSet):
    queryset = Office.objects.all()
    serializer_class = OfficeSerializer

class SubscribeViewSet(viewsets.ModelViewSet):
    queryset = Subscribe.objects.all()
    serializer_class = SubscribeSerializer

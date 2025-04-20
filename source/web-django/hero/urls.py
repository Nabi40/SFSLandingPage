from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    heroViewSet,
    LogosViewSet,
    SlideLogoViewSet,
    OurServiceViewSet,
    WorkDescriptionViewSet,
    CustomerReviewViewSet,
    FAQViewSet,
    InquiryViewSet,
    OfficeViewSet,
    SubscribeViewSet,
    WorkDescriptionGroupViewSet,
)

router = DefaultRouter()
router.register(r'hero', heroViewSet, basename='hero')
router.register(r'SlideLogo', SlideLogoViewSet, basename='SlideLogo')
router.register(r'logos', LogosViewSet, basename='logos')
router.register(r'ourservice', OurServiceViewSet, basename='ourservice')
router.register(r'workdescription', WorkDescriptionViewSet, basename='workdescription')
router.register(r'WorkDescriptionGroup', WorkDescriptionGroupViewSet, basename='SWorkDescriptionGroup')
router.register(r'customerreview', CustomerReviewViewSet, basename='customerreview')
router.register(r'faq', FAQViewSet, basename='faq')
router.register(r'inquiry', InquiryViewSet, basename='inquiry')
router.register(r'Office', OfficeViewSet, basename='Office')
router.register(r'Subscribe', SubscribeViewSet, basename='Subscribe')




urlpatterns = [
    path('', include(router.urls)),  
]
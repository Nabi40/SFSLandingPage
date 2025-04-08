from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    aboutUssViewSet,
    SlideImageViewSet,
    MissionVisionViewSet,
    ValueViewSet,
    ValueDetailViewSet,
    ExecutiveTeamViewSet,
)

router = DefaultRouter()
router.register(r'about-us', aboutUssViewSet, basename='about-us')
router.register(r'slide-images', SlideImageViewSet, basename='slide-image')
router.register(r'mission-vision', MissionVisionViewSet, basename='mission-vision')
router.register(r'values', ValueViewSet, basename='value')
router.register(r'value-details', ValueDetailViewSet, basename='value-detail')
router.register(r'executive-team', ExecutiveTeamViewSet, basename='executive-team')

urlpatterns = [
    path('', include(router.urls)),
]

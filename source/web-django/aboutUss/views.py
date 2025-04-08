from rest_framework import viewsets
from .models import aboutUss, SlideImage, MissionVision, Value, ValueDetail, ExecutiveTeam
from .serializers import (
    aboutUssSerializer,
    SlideImageSerializer,
    MissionVisionSerializer,
    ValueSerializer,
    ValueDetailSerializer,
    ExecutiveTeamSerializer,
)


class aboutUssViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = aboutUss.objects.all()
    serializer_class = aboutUssSerializer


class SlideImageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SlideImage.objects.all()
    serializer_class = SlideImageSerializer


class MissionVisionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MissionVision.objects.all()
    serializer_class = MissionVisionSerializer


class ValueViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Value.objects.all()
    serializer_class = ValueSerializer


class ValueDetailViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ValueDetail.objects.all()
    serializer_class = ValueDetailSerializer


class ExecutiveTeamViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ExecutiveTeam.objects.all()
    serializer_class = ExecutiveTeamSerializer

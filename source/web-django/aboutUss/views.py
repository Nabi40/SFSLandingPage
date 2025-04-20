from rest_framework.response import Response
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

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if queryset.exists():
            serializer = self.get_serializer(queryset.first())
            return Response(serializer.data)
        return Response({})


class SlideImageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SlideImage.objects.all()
    serializer_class = SlideImageSerializer


class MissionVisionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MissionVision.objects.all()
    serializer_class = MissionVisionSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if queryset.exists():
            serializer = self.get_serializer(queryset.first())
            return Response(serializer.data)
        return Response({})



class ValueViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Value.objects.all()
    serializer_class = ValueSerializer


    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if queryset.exists():
            serializer = self.get_serializer(queryset.first())
            return Response(serializer.data)
        return Response({})


class ValueDetailViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ValueDetail.objects.all()
    serializer_class = ValueDetailSerializer


class ExecutiveTeamViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ExecutiveTeam.objects.all()
    serializer_class = ExecutiveTeamSerializer

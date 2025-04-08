from rest_framework import viewsets
from .models import OurTeam, Head, HeadTeam, AllTeamDescrip, AllTeam
from .serializers import (
    OurTeamSerializer,
    HeadSerializer,
    HeadTeamSerializer,
    AllTeamDescripSerializer,
    AllTeamSerializer
)

class OurTeamViewSet(viewsets.ModelViewSet):
    queryset = OurTeam.objects.all()
    serializer_class = OurTeamSerializer


class HeadViewSet(viewsets.ModelViewSet):
    queryset = Head.objects.all()
    serializer_class = HeadSerializer


class HeadTeamViewSet(viewsets.ModelViewSet):
    queryset = HeadTeam.objects.all()
    serializer_class = HeadTeamSerializer


class AllTeamDescripViewSet(viewsets.ModelViewSet):
    queryset = AllTeamDescrip.objects.all()
    serializer_class = AllTeamDescripSerializer


class AllTeamViewSet(viewsets.ModelViewSet):
    queryset = AllTeam.objects.all()
    serializer_class = AllTeamSerializer

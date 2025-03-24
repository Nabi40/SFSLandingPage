from rest_framework import viewsets
from .models import aboutUss
from .serializers import aboutUssSerializer

class aboutUssViewSet(viewsets.ModelViewSet):
    queryset = aboutUss.objects.all()
    serializer_class = aboutUssSerializer

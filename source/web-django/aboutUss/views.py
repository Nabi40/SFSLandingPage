from rest_framework import viewsets
from rest_framework.response import Response
from .models import aboutUss
from .serializers import aboutUssSerializer

class aboutUssViewSet(viewsets.ModelViewSet):
    queryset = aboutUss.objects.all()
    serializer_class = aboutUssSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if queryset.exists():
            serializer = self.get_serializer(queryset.first())
            return Response(serializer.data)
        return Response({})

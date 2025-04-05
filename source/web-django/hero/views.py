from rest_framework import viewsets
from rest_framework.response import Response
from .models import hero
from .serializers import heroSerializer

class heroViewSet(viewsets.ModelViewSet):
    queryset = hero.objects.all()
    serializer_class = heroSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if queryset.exists():
            serializer = self.get_serializer(queryset.first())
            return Response(serializer.data)
        return Response({})

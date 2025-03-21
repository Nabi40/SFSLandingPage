from rest_framework import viewsets
from .models import hero
from .serializers import heroSerializer

class heroViewSet(viewsets.ModelViewSet):
    queryset = hero.objects.all()
    serializer_class = heroSerializer

    def partial_update(self, request, *args, **kwargs):
            """Handle PATCH requests for partial updates."""
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=True)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

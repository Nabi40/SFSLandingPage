from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import SiteVisitReferences, ReferenceVisitLogs
from .serializers import VisitTrackSerializer

@api_view(['GET', 'POST'])
def track_visit_api(request):
    if request.method == 'GET':
        return Response({"message": "Tracking endpoint ready"}, status=status.HTTP_200_OK)

    serializer = VisitTrackSerializer(data=request.data)
    if serializer.is_valid():
        ref_id = serializer.validated_data['ref']
        try:
            ref = SiteVisitReferences.objects.get(id=ref_id)
            ReferenceVisitLogs.objects.create(visit_ref=ref)
            return Response({"message": "Visit logged successfully"}, status=status.HTTP_201_CREATED)
        except SiteVisitReferences.DoesNotExist:
            return Response({"error": "Invalid ref"}, status=status.HTTP_404_NOT_FOUND)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

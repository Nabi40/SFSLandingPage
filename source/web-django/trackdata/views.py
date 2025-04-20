from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Reference, AnotherModel
from .serializers import ReferenceSerializer, AnotherModelSerializer


@api_view(['POST'])
def reference_create_api(request):
    serializer = ReferenceSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def reference_list_api(request):
    references = Reference.objects.all()
    serializer = ReferenceSerializer(references, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def another_model_create_api(request):
    serializer = AnotherModelSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def another_model_list_api(request):
    models = AnotherModel.objects.all()
    serializer = AnotherModelSerializer(models, many=True)
    return Response(serializer.data)

from django.shortcuts import render

# For MongoDB REST API
from rest_framework_mongoengine import viewsets as myviewsets
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from Test.serializers import DriverSerializer
from Test.models import Driver

# Create your views here.

class DriverViewSet(myviewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer

class DriverAPI(APIView):

    def get(self, request):
        serializer = DriverSerializer(Driver.objects.all(), many=True)
        response = {"Drivers": serializer.data}
        return Response(response, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        data = request.data
        serializer = DriverSerializer(data=data)
        if serializer.is_valid():
            driver = Driver(**data)
            driver.save()
            response = serializer.data
            return Response(response, status=status.HTTP_200_OK)
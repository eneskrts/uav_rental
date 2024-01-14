from rest_framework import viewsets
from rental.models import Rental, UAV
from rental.api.serializers import UAVSerializer, RentalSerializer


class RentalViewSet(viewsets.ModelViewSet):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer


class UAVViewSet(viewsets.ModelViewSet):
    queryset = UAV.objects.all()
    serializer_class = UAVSerializer

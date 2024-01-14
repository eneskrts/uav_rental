
from rest_framework import serializers, viewsets

from rental.models import UAV, Rental


class UAVSerializer(serializers.ModelSerializer):
    class Meta:
        model = UAV
        fields = ['brand', 'model', 'weight', 'category']


class RentalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rental
        fields = ['id', 'uav', 'start_date', 'end_date', 'renting_member']
        depth = 1

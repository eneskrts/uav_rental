from django.db import models
from django.contrib.auth.models import User

from utils.models import StarterModel


class UAV(StarterModel):
    brand = models.CharField(max_length=255)  # it can be enum or choice field model instance
    model = models.CharField(max_length=255)  # it can be enum or choice field model instance
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)  # it can be enum or choice field model instance

    def __str__(self):
        return f"{self.brand} - {self.model}"


class Rental(StarterModel):
    uav = models.ForeignKey(UAV, on_delete=models.CASCADE)
    renting_member = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return f"{self.uav} rented by {self.renting_member.username} ({self.start_date} - {self.end_date})"


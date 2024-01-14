from django.urls import path
# api imports
from rental.api.views import *
# add routers
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'rentals', RentalViewSet)
router.register(r'uavs', UAVViewSet)


urlpatterns = [
    ]

urlpatterns += router.urls

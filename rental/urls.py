from django.urls import path

from rental.views import GetTokenView, RentalView


urlpatterns = [
    path('get-token/', GetTokenView.as_view(), name='get-token'),
    path('rental/', RentalView.as_view(), name='rental'),
    ]
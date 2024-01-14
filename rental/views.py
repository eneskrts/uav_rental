from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse


class GetTokenView(View):
    def get(self, request):
        return JsonResponse({'token': request.session.get('token', None)})



class RentalView(View):
    def get(self, request):
        return render(request, 'rental/rental.html')

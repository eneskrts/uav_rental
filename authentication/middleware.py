from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.utils.deprecation import MiddlewareMixin
from rest_framework.authtoken.models import Token

class LoginMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        super().__init__(get_response)

    def process_request(self, request):
        session = request.session
        if request.user.is_authenticated and session: #and not getattr(session.first(), 'token', None):
            token, _ = Token.objects.get_or_create(user=request.user)
            request.session['token'] = token.key
            request.session.save()

    def process_response(self, request, response):
        return response

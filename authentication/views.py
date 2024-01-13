from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView


class CustomLoginView(LoginView):
    template_name = 'authentication/login.html'
    # TODO: index page
    # success_url = reverse_lazy('index')


class RegisterView(CreateView):
    template_name = 'authentication/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')



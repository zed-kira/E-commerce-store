from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, TemplateView

from django.views.generic import CreateView
from .forms import CustomUserCreationForm , CustomAuthenticationForm


# Create your views here.

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class CustomLoginView(LoginView):
    form_class = CustomAuthenticationForm


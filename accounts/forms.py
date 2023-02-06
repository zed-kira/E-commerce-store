from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm , AuthenticationForm , UsernameField
from .models import CustomUser

class CustomAuthenticationForm(AuthenticationForm): #Costomizing login form
    pass

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email', 'age')
    
class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'age')

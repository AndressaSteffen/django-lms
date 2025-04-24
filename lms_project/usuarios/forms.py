from django import forms 
from django.contrib.auth.forms import UserCreationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'tipo', 'password1', 'password2')
        widgets = {
            'tipo': forms.Select(attrs={'class': 'form-control'}),
        }
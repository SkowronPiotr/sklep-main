from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'login',
        'style': 'width: 300px; background-color: white; color: #666; border: 2px solid #ddd; border-radius: 15px; font-size: 20px; padding: 10px;',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Hasło',
        'style': 'width: 300px; background-color: white; color: #666; border: 2px solid #ddd; border-radius: 15px; font-size: 20px; padding: 10px;',
    }))

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'login',
        'style': 'width: 300px; background-color: white; color: #666; border: 2px solid #ddd; border-radius: 15px; font-size: 20px; padding: 10px;',
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'example@sklep.pl',
        'style': 'width: 300px; background-color: white; color: #666; border: 2px solid #ddd; border-radius: 15px; font-size: 20px; padding: 10px;',
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Password 1',
        'style': 'width: 300px; background-color: white; color: #666; border: 2px solid #ddd; border-radius: 15px; font-size: 20px; padding: 10px;',
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Repeat Password',
        'style': 'width: 300px; background-color: white; color: #666; border: 2px solid #ddd; border-radius: 15px; font-size: 20px; padding: 10px;',
    }))
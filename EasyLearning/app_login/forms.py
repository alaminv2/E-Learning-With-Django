from django import forms
from app_login.models import User
from django .contrib.auth.forms import UserCreationForm, AuthenticationForm


class signUpForm(UserCreationForm):
    username = forms.CharField(label="", widget=forms.TextInput(attrs={
        'placeholder': 'Username',
        'style': 'border:2px solid green; border-radius:25px;',
    }))
    password1 = forms.CharField(label="", widget=forms.PasswordInput(attrs={
        'placeholder': 'Password',
        'style': 'border:2px solid green; border-radius:25px;',
    }))
    password2 = forms.CharField(label="", widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm Password',
        'style': 'border:2px solid green; border-radius:25px;',
    }))

    class Meta:
        model = User
        fields = ('username',)


class loginForm(AuthenticationForm):
    username = forms.CharField(label="", widget=forms.TextInput(attrs={
        'placeholder': 'Username',
        'style': 'border:2px solid green; border-radius:25px;',
    }))
    password = forms.CharField(label="", widget=forms.PasswordInput(attrs={
        'placeholder': 'Password',
        'style': 'border:2px solid green; border-radius:25px;',
    }))

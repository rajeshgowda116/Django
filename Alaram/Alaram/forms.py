from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

def RegistrationForm(UserCreationForm):
    username=forms.CharFild(max_length=100,
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    email=forms.EmailField(max_length=100,
                            widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1=forms.CharFild(max_length=100,
                            widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharFild( max_length=100,
                             widget=forms.PasswordInput(attrs={'class':'form-controls'}))
    class Meta:
        model=User
        filds=['username','email','password1','password2']
        
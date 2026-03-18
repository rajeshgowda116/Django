from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):

  name=forms.CharField(max_length=100,
                       widget=forms.TextInput(attrs={'class':'form-control'}))
  username=forms.CharField(max_length=100,
                           widget=forms.TextInput(attrs={'class':'form-control'}))
  password1=forms.CharField(max_length=100,
                           widget=forms.TextInput(attrs={'class':'form-control'}))
  password2=forms.CharField(max_length=100,
                           widget=forms.TextInput(attrs={'class':'form-control'}))
  class Meta:
    model=User
    fields=['name','username','password1','password2']
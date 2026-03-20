from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth 


def register(request):
  if request.method == 'POST':
    form=RegistrationForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('home')
  else:
    form=RegistrationForm()
  return render(request,'register.html',{'form':form})

def login(request):
  if request.method == 'POST':
    form=AuthenticationForm(request=request,data=request.POST)
    if form.is_valid():
      username=form.cleaned_data.get('username')
      password=form.cleaned_data.get('password')
      user=auth.authenticate(username=username,password=password)
      if user is not None:
        login(request,user)   
      return redirect('home')
  else:
    form=AuthenticationForm()
  return render(request, 'login.html',{'form':form})


def home(request):
  return HttpResponse("Hi this is home page")

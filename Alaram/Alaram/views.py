from django.shortcuts import redirect,render,HttpResponse 
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from Task.models import Task
# Create your views here.   

def register(request):
  if request.method=='POST':
    form=RegistrationForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('home')
    else:
      print(form.errors)
  else:
    form=RegistrationForm()
  return render(request,'register.html',{'form':form})

def login(request):
  if request.method=='POST':
    form=AuthenticationForm(request,data=request.POST)
    if form.is_valid():
      user=form.get_user()
      auth.login(request,user)
      return redirect('home')
  else:
    form=AuthenticationForm()
  return render(request,'login.html',{'form':form})

def logout(request):
  auth.logout(request)
  return redirect('login')

@login_required
def home(request):
  tasks=Task.objects.filter(user=request.user,completed=False).order_by('-created_at')
  return render(request,'dashboard.html',{'tasks':tasks})
  

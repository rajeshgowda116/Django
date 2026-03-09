from django.shortcuts import redirect,render,HttpResponse 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm

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

def home(request):
  return HttpResponse("Hi Rajesh")
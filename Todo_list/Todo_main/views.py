from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.http import HttpResponse
from todos.models import Task
from django.contrib.auth.decorators import login_required 
from django.contrib import auth      


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            print(form.errors)
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
            return redirect('home')
  
    form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})
    
@login_required(login_url='login')
def home(request):
  if not request.user.is_authenticated:
    return redirect('login')

  task = Task.objects.filter(user=request.user, is_completed=False).order_by('-created_at')
  completed_tasks = Task.objects.filter(user=request.user, is_completed=True).order_by('-created_at')
  context = {
    'task': task,
    'completed_tasks': completed_tasks
  }

  return render(request, 'home.html', context)


def logout_view(request):
    logout(request)
    return redirect('login')




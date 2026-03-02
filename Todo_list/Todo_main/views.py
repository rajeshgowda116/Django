from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.http import HttpResponse
from todos.models import Task
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
        else:
            print(form.errors)
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})
    
@login_required
def home(request):
  task = Task.objects.filter(is_completed=False).order_by('-created_at')
  completed_tasks = Task.objects.filter(is_completed=True).order_by('-created_at')
  context = {
    'task': task,
    'completed_tasks': completed_tasks
  }

  return render(request, 'home.html', context)


def logout_view(request):
    logout(request)
    return redirect('login')




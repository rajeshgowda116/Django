from django.shortcuts import render,redirect
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth  

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    else:
        form = RegistrationForm()
        
    return render(request, 'register.html',{'form':form})

def login(request):
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

def home(request):
    
    return render(request, 'home.html')

def logout(request):
    auth.logout(request)
    return redirect('home')

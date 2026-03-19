from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import RegistrationForm


def register(request):
  if request.method == 'POST':
    form=RegistrationForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('home')
  else:
    form=RegistrationForm()
  return render(request,'register.html',{'form':form})
def home(request):
  return HttpResponse("Hi this is home page")

from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Task


# Create your views here.
def add_task(request):
  if request.method == 'POST':
    task =request.POST.get('task')
    if task:
      Task.objects.create(task=task)
  return redirect('home')

def mark_as_done(requst,pk):
  task = Task.objects.get(pk=pk)
  task.is_completed = True
  task.save()
  return redirect('home')

def mark_as_undone(request,pk):
  task= Task.objects.get(pk=pk)
  task.is_completed = False
  task.save()
  return redirect('home')
 
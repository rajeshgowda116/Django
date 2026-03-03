from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Task
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def add_task(request):
  if request.method == 'POST':
    task =request.POST.get('task')
    if task:
      Task.objects.create(user=request.user, task=task)
  return redirect('home')

@login_required
def mark_as_done(request,pk):
  task = get_object_or_404(Task, pk=pk, user=request.user)
  task.is_completed = True
  task.save()
  return redirect('home')

@login_required
def mark_as_undone(request,pk):
  task= get_object_or_404(Task, pk=pk, user=request.user)
  task.is_completed = False
  task.save()
  return redirect('home')

@login_required
def task_task(request,pk):
  tasks=get_object_or_404(Task, pk=pk, user=request.user)
  if request.method=="POST":
    new_task=request.POST.get('task')
    tasks.task=new_task
    tasks.save()
    return redirect('home')
  else:
    context={'tasks':tasks}
    return render(request,'edit.html',context)

@login_required
def delete_task(request,pk):
  task=get_object_or_404(Task, pk=pk, user=request.user)
  task.delete()
  return redirect('home')
 

from datetime import datetime
from django.shortcuts import get_object_or_404, redirect, render
from .models import Task
from django.contrib.auth.decorators import login_required

@login_required
def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        reminder_hour = request.POST.get('reminder_hour')
        reminder_minute = request.POST.get('reminder_minute')
        reminder_period = request.POST.get('reminder_period')
        reminder_time = None
        if reminder_hour and reminder_minute and reminder_period:
            reminder_time = datetime.strptime(
                f'{reminder_hour}:{reminder_minute} {reminder_period}',
                '%I:%M %p',
            ).time()
        completed = request.POST.get('completed') == 'on'
        task = Task(
            user=request.user,
            title=title,
            description=description,
            reminder_time=reminder_time,
            completed=completed,
        )
        task.save()
        return redirect('home')
    context = {
        'hours': [f'{hour:02d}' for hour in range(1, 13)],
        'minutes': [f'{minute:02d}' for minute in range(60)],
    }
    return render(request, 'add_task.html', context)

@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)

    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        reminder_hour = request.POST.get('reminder_hour')
        reminder_minute = request.POST.get('reminder_minute')
        reminder_period = request.POST.get('reminder_period')

        if reminder_hour and reminder_minute and reminder_period:
            task.reminder_time = datetime.strptime(
                f'{reminder_hour}:{reminder_minute} {reminder_period}',
                '%I:%M %p',
            ).time()
        else:
            task.reminder_time = None

        task.completed = request.POST.get('completed') == 'on'
        task.save()
        return redirect('home')

    reminder_hour = ''
    reminder_minute = ''
    reminder_period = 'AM'
    if task.reminder_time:
        reminder_hour = task.reminder_time.strftime('%I')
        reminder_minute = task.reminder_time.strftime('%M')
        reminder_period = task.reminder_time.strftime('%p')

    context = {
        'task': task,
        'hours': [f'{hour:02d}' for hour in range(1, 13)],
        'minutes': [f'{minute:02d}' for minute in range(60)],
        'task_reminder_hour': reminder_hour,
        'task_reminder_minute': reminder_minute,
        'task_reminder_period': reminder_period,
    }
    return render(request, 'edit_task.html', context)

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)

    if request.method == 'POST':
        task.delete()
        return redirect('home')

    return render(request, 'delete_task.html', {'task': task})


# Create your views here.

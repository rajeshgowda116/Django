from datetime import datetime

from django.shortcuts import redirect, render
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

def edit_task(request, task_id):
    return render(request, 'edit_task.html')







# Create your views here.

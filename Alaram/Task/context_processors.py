import json

from .models import Task


def reminder_tasks(request):
    if not request.user.is_authenticated:
        return {'tasks_json': '[]'}

    tasks = Task.objects.filter(user=request.user, completed=False).exclude(reminder_time__isnull=True)
    serialized_tasks = [
        {
            'id': task.pk,
            'title': task.title,
            'description': task.description,
            'reminder_time': task.reminder_time.strftime('%H:%M') if task.reminder_time else '',
        }
        for task in tasks
    ]
    return {'tasks_json': json.dumps(serialized_tasks)}

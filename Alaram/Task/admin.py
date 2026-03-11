from django.contrib import admin
from .models import Task

# Register your models here.

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'completed', 'created_at','reminder_time')
    list_filter = ('completed', 'created_at', 'user')
    search_fields = ('title', 'user__username')


# Register your models here.

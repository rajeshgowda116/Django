from django.contrib import admin
from .models import IdCard

class Taskadmin(admin.ModelAdmin):
    list_display = ['fullname', 'college_name', 'branch', 'year', 'created_at', 'updated_at']
    search_fields = ['fullname', 'college_name', 'branch', 'year']

admin.site.register(IdCard, Taskadmin)

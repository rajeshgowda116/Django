from django.contrib import admin
from .models import Result
# Register your models here.
@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
  list_display=['user','s1_name','s1_marks','s2_name','s2_marks','s3_name','s3_marks','s4_name','s4_marks','percentage']

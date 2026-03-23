from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Result(models.Model):
  user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
  s1_name=models.CharField(max_length=50)
  s1_marks=models.IntegerField()
  s2_name=models.CharField(max_length=50)
  s2_marks=models.IntegerField()
  s3_name=models.CharField(max_length=50)
  s3_marks=models.IntegerField()
  s4_name=models.CharField(max_length=50)
  s4_marks=models.IntegerField()
  percentage=models.IntegerField(default=0)

  
  


from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class IdCard(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    fullname=models.CharField(max_length=100)
    college_name=models.CharField(max_length=100)
    branch=models.CharField(max_length=100)
    year=models.CharField(max_length=100)
    photo=models.ImageField(upload_to='uploads/%Y/%m/%d')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self) :
       return self.fullname
    


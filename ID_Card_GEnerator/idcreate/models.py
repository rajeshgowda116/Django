from django.db import models

# Create your models here.
class IdCard(models.Model):
    name=models.CharField(max_length=100)
    surname=models.CharField(max_length=100)
    father_name=models.CharField(max_length=100)
    mother_name=models.CharField(max_length=100)
    date_of_birth=models.DateField()
    nationality=models.CharField(max_length=100)
    gender=models.CharField(max_length=10)
    phno=models.CharField(max_length=10)
    address=models.CharField(max_length=100)
    blood_group=models.CharField(max_length=10)
    photo=models.ImageField(upload_to='photos')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self) :
       return self.name
    


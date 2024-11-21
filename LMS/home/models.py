from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class department(models.Model):
    department = models.CharField(max_length=30,null= True,blank=True)

    def __str__(self):
        return self.department


class student_id(models.Model):
    student_id = models.CharField(max_length=30,unique=True)

    def __str__(self):
        return self.student_id

class Student(models.Model):
    d = models.ForeignKey(department,related_name="dept", on_delete=models.SET_NULL,null= True,blank= True)
    student_id = models.OneToOneField( student_id ,  related_name="std_id", on_delete=models.CASCADE,null=True,blank=True)
    full_name = models.CharField(null=True,blank=True,max_length=20)
    age = models.DateField(null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    address = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.full_name
    


class user(models.Model):
    user = models.ForeignKey(User, null= True,blank= True, on_delete=models.SET_NULL)

    
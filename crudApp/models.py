from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=25)
    age=models.IntegerField()
    email=models.EmailField()
    phone_number=models.CharField(max_length=13)
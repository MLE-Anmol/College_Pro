from django.db import models

# Create your models here.
class Student(models.Model):
    stu_fname = models.CharField(max_length=20)
    stu_lname = models.CharField(max_length=20)
    stu_id = models.CharField(max_length=10)
    program = models.CharField(max_length=15)
    
